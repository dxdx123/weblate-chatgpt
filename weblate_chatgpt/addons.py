# Copyright © 2023 ChatGPT Developer <developer@example.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from .forms import ChatGPTSettingsForm
from weblate.machinery.base import MachineTranslation, MachineTranslationError


class ChatGPTTranslation(MachineTranslation):
    # This addon can be installed multiple times per component
    #multiple = True
    #icon = "language.svg"

    #@classmethod
    #def can_install(cls, component, user):
    #    return True

    name = "ChatGPT"
    max_score = 100
    settings_form = ChatGPTSettingsForm

    def download_languages(self):
        """List of supported languages."""
        # Replace the following list with the actual list of supported languages by ChatGPT
        return ["en", "fr", "de", "es", "zh"]

    def download_translations(
            self,
            source,
            language,
            text,
            unit,
            user,
            search: bool,
            threshold=75
    ):
        """Download list of possible translations from a service."""
        import openai

        openai.api_key = self.settings_form["api_key"]
        model = "text-davinci-002"  # You can use other GPT models here

        try:
            response = openai.Completion.create(
                engine=model,
                prompt=text,
                max_tokens=100,
                n=1,
                stop=None,
                temperature=self.settings_form["temperature"],
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
        except Exception as e:
            raise MachineTranslationError(str(e))

        translation = response.choices[0].text.strip()

        yield {
            "text": translation,
            "quality": self.max_score,
            "service": self.name,
            "source": text,
        }
