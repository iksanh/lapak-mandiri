from rest_framework import serializers
from koordinator_substansi.models import KoordinatorSubstansi
from unit_kerja.models import SubUnitKerja
from unit_kerja.api.serializers import SubUnitKerjaSerializer

class KoordinatorSubstansiSerializer(serializers.ModelSerializer):
    sub_unit_kerja = serializers.PrimaryKeyRelatedField(queryset=SubUnitKerja.objects.all())

    class Meta:
        model = KoordinatorSubstansi
        fields = ['koorsub_id', 'nama', 'sub_unit_kerja']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['sub_unit_kerja'] = SubUnitKerjaSerializer(instance.sub_unit_kerja).data
        return representation

    def create(self, validated_data):
        return KoordinatorSubstansi.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nama = validated_data.get('nama', instance.nama)
        instance.sub_unit_kerja = validated_data.get('sub_unit_kerja', instance.sub_unit_kerja)
        instance.save()
        return instance
