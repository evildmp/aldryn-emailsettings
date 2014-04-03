from aldryn_client.forms import BaseForm, CharField, NumberField, CheckboxField


class Form(BaseForm):

    email_host = CharField(default='localhost')
    email_host_password = CharField(default='')
    email_host_user = CharField(default='')
    email_port = NumberField(default=25)
    email_use_tls = CheckboxField()

    def to_settings(self, data, settings):
        email_settings = {
            'EMAIL_HOST': data.get('email_host'),
            'EMAIL_HOST_PASSWORD': data.get('email_host_password'),
            'EMAIL_HOST_USER': data.get('email_host_user'),
            'EMAIL_PORT': data.get('email_port'),
            'EMAIL_USE_TLS': data.get('email_use_tls'),
        }
        settings.update(email_settings)
        return settings
