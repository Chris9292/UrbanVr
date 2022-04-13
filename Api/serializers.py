#src/gis_rest_project/nairobi_hospitals_api/serializers.py
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import  Building, Block


class BuildingSerializer(GeoFeatureModelSerializer):

	class Meta:
		model = Building
		fields = '__all__'
		geo_field = 'geom'


class BlockSerializer(GeoFeatureModelSerializer):

	class Meta:
		model = Block
		fields = '__all__'
		geo_field = 'geom'