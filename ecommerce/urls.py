"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static

from store.views import StripeCheckoutSession, SuccessView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.userProfile, name='profile'),
    path('', views.instruments, name='instruments'),
    path('shoppingCart/', views.shoppingCart, name='shoppingCart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add_instrument/', views.add_instrument, name='add_instrument'),
    path('edit_instrument/<str:pk>/', views.edit_instrument, name='edit_instrument'),
    path('delete_instrument/<str:pk>/', views.delete_instrument, name='delete_instrument'),
    path('view_instrument/<str:pk>/', views.view_instrument, name='view_instrument'),
    path('add_to_cart/<str:pk>/', views.add_to_cart, name='add_to_cart'),
    path('delete_from_cart/<str:pk>/', views.delete_from_cart, name='delete_from_cart'),
    path('increase_quantity/<str:pk>', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<str:pk>', views.decrease_quantity, name='decrease_quantity'),
    path(
        "create-checkout-session/<int:pk>/",
        StripeCheckoutSession.as_view(),
        name="create-checkout-session",
    ),
    path("success/", SuccessView.as_view(), name="success"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
