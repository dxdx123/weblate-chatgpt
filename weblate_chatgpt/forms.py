# Copyright © 2023 ChatGPT Developer <developer@example.com>
#
# SPDX-License-Identifier: GPL-3.0-or-later

from django import forms
from django.utils.translation import gettext_lazy as _


class ChatGPTSettingsForm(forms.Form):
    api_key = forms.CharField(
        label=_("API Key"),
        help_text=_("ChatGPT API Key."),
        required=True,
    )
    temperature = forms.FloatField(
        label=_("Temperature"),
        help_text=_("The temperature to be used for generating translations."),
        required=True,
        min_value=0.0,
        max_value=1.0,
        initial=0.8
    )


def clean(self):
    cleaned_data = super().clean()

    api_key = cleaned_data.get("api_key")
    temperature = cleaned_data.get("temperature")

    if not api_key:
        self.add_error("api_key", _("API Key is required."))

    if temperature is None:
        self.add_error("temperature", _("Temperature is required."))

    return cleaned_data
