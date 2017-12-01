from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import LoanPetitionForm
from .models import LoanPetition


class LoanPetitionCreate(SuccessMessageMixin, CreateView):
    form_class = LoanPetitionForm
    http_method_names = [u'get', u'post']
    template_name = 'loans/loanpetition_create.html'
    success_url = '.'
    success_message = 'Loan petition was not approved'

    def form_valid(self, form):
        approved, error = form.check_status()

        if error:
            self.success_message = 'There was an error with your submission :('
            return HttpResponseRedirect(self.get_success_url())

        if approved:
            self.success_message = 'Loan petition was approved! :)'
            form.instance.approved = True
        return super(LoanPetitionCreate, self).form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class LoanPetitionDelete(DeleteView):
    model = LoanPetition
    success_url = reverse_lazy('loan-list')


@method_decorator(staff_member_required, name='dispatch')
class LoanPetitionList(ListView):
    model = LoanPetition
    http_method_names = [u'get']


@method_decorator(staff_member_required, name='dispatch')
class LoanPetitionUpdate(UpdateView):
    model = LoanPetition
    form_class = LoanPetitionForm
    http_method_names = [u'get', u'post']
    template_name = 'loans/loanpetition_update.html'
    success_url = reverse_lazy('loan-list')
    success_message = 'Loan petition was not updated'

    def form_valid(self, form):
        # En caso de que se quiera tambien volver a consultar y
        # actualizar el estado de la petition usando el endpoint
        # de scoring se podria usar la misma logica de
        # LoanPetitionCreate.form_valid pero habria que moverla
        # a otro lado para no repetir.  Por falta no tiempo no
        # lo hago.
        return super(LoanPetitionCreate, self).form_valid(form)
