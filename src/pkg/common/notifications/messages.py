from django.conf import settings
from django.contrib.sites.models import Site
from django.template.loader import render_to_string


class MessageNotification:
    template_name = NotImplemented
    subject = NotImplemented

    def __init__(self, **context_data):
        self.context_data = context_data

    def _get_context(self):
        data = self.get_context_data()
        data.update(self.context_data)
        return data

    def get_content(self):
        return render_to_string(self.template_name, self._get_context())

    def get_subject(self):
        try:
            return self.subject.format(**self._get_context())
        except (KeyError, IndexError):
            return self.subject

    def get_context_data(self):
        site = Site.objects.get_current()

        return {
            'domain': site.domain,
            'site_name': site.name,
            'site_url': '{0}://{1}'.format(settings.SITE_PROTOCOL, site.name)
        }
