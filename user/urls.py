from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path("",views.Index.as_view(),name='index'),
    path("addcustomer",views.AddCustomer.as_view(),name='addcustomer'),
    path("editcustomer/<uuid:customer_id>/",views.EditCustomer.as_view(),name='editcustomer'),
    path("viewcustomer/<uuid:customer_id>/",views.ViewCustomer.as_view(),name='viewcustomer'),
    path("deletecustomer/<uuid:customer_id>/",views.DeleteCustomer.as_view(),name='deletecustomer'),

]