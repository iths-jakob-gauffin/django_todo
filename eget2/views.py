from django.views import generic


class LoggedInView(generic.TemplateView):
  template_name = "accounts/logged_in.html"

class LoggedOutView(generic.TemplateView):
  template_name = "accounts/logged_out.html"