from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (
    IndividualForm,
)

class MyPageView(generic.TemplateView):
    template_name = 'accountsDetail/my_page.html'

class IndividualView(generic.CreateView, LoginRequiredMixin):
    template_name = 'accountsDetail/individual.html'
    form_class = IndividualForm
    success_url = reverse_lazy('')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)