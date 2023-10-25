from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from django.urls import path
from .views.members import MemberViewSet

router = DefaultRouter()
router.register('members', MemberViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html')),
    *router.urls
]
