from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib import admin
from myapp import views as myapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('item-list', myapp_views.item_list, name='item_list'),
    path('create/', myapp_views.item_create, name='item_create'),
    path('item/<int:pk>/edit/', myapp_views.item_update, name='item_update'),
    path('delete/<int:pk>/', myapp_views.item_delete, name='item_delete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('confirm_delete/<int:pk>/', myapp_views.item_delete, name='item_confirm_delete'),
]
