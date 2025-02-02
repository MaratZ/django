from django.urls import path
from catalog.apps import CatalogConfig
from django.conf import settings
from django.conf.urls.static import static
from . import views

from catalog.views import (
    CategoryListView,
    ProductDetailView,
    HomeView,
    ContactsView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductsByCategoryListView
)
app_name = CatalogConfig.name

urlpatterns = ([
                   path("", HomeView.as_view(), name="home"),
                   path("contacts/", ContactsView.as_view(), name="contacts"),
                   path('products/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
                   path('products/create/', ProductCreateView.as_view(), name='products_create'),
                   path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='products_update'),
                   path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='products_delete'),
                   path(
                       "category/<str:category_name>/",
                       ProductsByCategoryListView.as_view(),
                       name="products_by_category",
                   )
               ]
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))