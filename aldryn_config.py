# -*- coding: utf-8 -*-
from aldryn_client.forms import BaseForm, CharField, NumberField, CheckboxField


class Form(BaseForm):

    email_host = CharField('SMTP Host', initial='localhost')
    email_port = NumberField('SMTP Port', initial=25)
    email_host_user = CharField('SMTP User', initial='')
    email_host_password = CharField('SMTP Password', initial='')
    email_use_tls = CheckboxField('Use TLS', required=False, initial=False)

    default_from_email = CharField('Default from email', initial='', required=False)

    def to_settings(self, data, settings):
        email_settings = {
            'EMAIL_HOST': data.get('email_host'),
            'EMAIL_HOST_PASSWORD': data.get('email_host_password'),
            'EMAIL_HOST_USER': data.get('email_host_user'),
            'EMAIL_PORT': data.get('email_port'),
            'EMAIL_USE_TLS': data.get('email_use_tls'),
        }
        if data.get('default_from_email', False):
            email_settings['DEFAULT_FROM_EMAIL'] = data.get('default_from_email')
            email_settings['SERVER_EMAIL'] = data.get('default_from_email')
        settings.update(email_settings)
        return settings
