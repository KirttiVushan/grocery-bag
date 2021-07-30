from bag.models import Groceries
from rest_framework import serializers

class Groceries_serializers(serializers.ModelSerializer):

	class Meta:
		model=Groceries
		fields=['name','quantity','status','date','user']