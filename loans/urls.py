from django.conf.urls import url

from .views import (LoanPetitionCreate, LoanPetitionDelete,
                    LoanPetitionList, LoanPetitionUpdate)


urlpatterns = [
    url(r'^$', LoanPetitionList.as_view(), name='loan-list'),
    url(r'^(?P<pk>\d+)/', LoanPetitionUpdate.as_view(), name='loan-update'),
    url(r'^delete/(?P<pk>\d+)/', LoanPetitionDelete.as_view(), name='loan-delete'),
    url(r'^petition/', LoanPetitionCreate.as_view(), name='loan-petition'),
]
