from rest_framework import serializers
from task.models import Students

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Students
		fields= ['Name', 'College', 'Email', 'id']