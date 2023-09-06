from django.urls import path
from .views import ServicesView,contactView, TechnologyView, ExperienceView, ProjectView, TestimonialsView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

urlpatterns = [
    path('services/', ServicesView.as_view(), name="Services"),
    path('technology/', TechnologyView.as_view(), name="Technology"),
    path('testimonials/', TestimonialsView.as_view(), name="Testimonials"),
    path('experience/', ExperienceView.as_view(), name="experiences"),
    path('projects/', ProjectView.as_view(), name="Projects"),
    path('contact/', contactView, name="Contact")
] + router.urls