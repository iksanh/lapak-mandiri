from rest_framework import serializers
from unit_kerja.models import UnitKerja, SubUnitKerja, UnitKerja_SubUnitKerja

class UnitKerjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitKerja
        fields = '__all__'

class SubUnitKerjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubUnitKerja
        fields = '__all__'

class UnitKerja_SubUnitKerjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitKerja_SubUnitKerja
        fields = '__all__'
        depth = 1


class UnitKerjaSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitKerja
        fields = ['nama_unit_kerja']  # Specify the field you want to include

class SubUnitKerjaSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubUnitKerja
        fields = ['nama_sub_unit_kerja']  # Specify the field you want to include