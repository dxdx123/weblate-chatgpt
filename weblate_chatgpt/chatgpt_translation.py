# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from django.conf import settings
from requests.exceptions import RequestException

from .base import MachineTranslation, MachineTranslationError
from .forms import KeyMachineryForm

CHATGPT_API_ROOT = "https://api.openai.com/v1/engines/davinci-codex/completions"


class ChatGPTBaseTranslation(MachineTranslation):
    # Map codes used by ChatGPT to the ones used by Weblate
    language_map = {
        "nb_NO": "no",
        "fil": "tl",
        "zh_Hant": "zh-TW",
        "zh_Hans": "zh-CN",
    }
    language_aliases = ({"zh-CN", "zh"},)

    def map_language_code(self, code):
        """Convert language to service specific code."""
        return super().map_language_code(code).replace("_", "-").split("@")[0]

    def is_supported(self, source, language):
        # Avoid translation between aliases
        return super().is_supported(source, language) and not any(
            {source, language} == item for item in self.language_aliases
        )


class ChatGPTTranslation(ChatGPTBaseTranslation):
    """ChatGPT machine translation support."""

    name = "ChatGPT Translate"
    max_score = 90
    settings_form = KeyMachineryForm

    @staticmethod
    def migrate_settings():
        return {
            "key": settings.MT_CHATGPT_KEY,
        }

    def download_languages(self):
        """List of supported languages."""
        # Replace this list with the actual list of supported languages by ChatGPT
        return ['en', 'es', 'fr', 'de', 'zh']

    def download_translations(
        self,
        source,
        language,
        text: str,
        unit,
        user,
        threshold: int = 75,
    ):
        """Download list of possible translations from a service."""
        prompt = f"Translate the following text from {source} to {language}: {text}"
        response = self.request(
            "post",
            CHATGPT_API_ROOT,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.settings['key']}",
            },
            json={
                "prompt": prompt,
                "max_tokens": 100,
                "n": 1,
                "stop": None,
                "temperature": 0.8,
            },
        )
        payload = response.json()

        if "error" in payload:
            raise MachineTranslationError(payload["error"]["message"])

        translation = payload["choices"][0]["text"].strip()

        yield {
            "text": translation,
            "quality": self.max_score,
            "service": self.name,
            "source": text,
        }

    def get_error_message(self, exc):
        if isinstance(exc, RequestException) and exc.response is not None:
            data = exc.response.json()
            try:
                return data["error"]["message"]
            except KeyError:
                pass

        return super().get_error_message(exc)