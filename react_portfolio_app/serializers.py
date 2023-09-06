from rest_framework import serializers
from .models import Services,Technology,Experience,Projects,Testimonials

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    points = serializers.StringRelatedField(many=True)
    class Meta:
        model = Experience
        fields = '__all__'


class ProjectsSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    class Meta:
        model = Projects
        fields = '__all__'
