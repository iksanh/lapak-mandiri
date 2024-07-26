from rest_framework import serializers
from pegawai.models import PangkatGolongan, Pegawai, PegawaiKoordinatorSubstansi
from unit_kerja.models import UnitKerja, SubUnitKerja, UnitKerja_SubUnitKerja
from unit_kerja.api.serializers import UnitKerjaSerializer, SubUnitKerjaSerializer, UnitKerjaSimpleSerializer, SubUnitKerjaSimpleSerializer
from koordinator_substansi.models import KoordinatorSubstansi
from koordinator_substansi.api.serializers import KoordinatorSubstansiSerializer

class PangkatGolonganSerializer(serializers.ModelSerializer):
    class Meta:
        model = PangkatGolongan
        fields = '__all__'

class PegawaiSelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pegawai
        fields = ['id', 'nama', 'unit_kerja', 'jabatan']

class PegawaiSerializer(serializers.ModelSerializer):
    unit_kerja = serializers.PrimaryKeyRelatedField(queryset=UnitKerja.objects.all())
    sub_unit_kerja = serializers.PrimaryKeyRelatedField(queryset=SubUnitKerja.objects.all())
    class Meta:
        model = Pegawai
        fields = ['id','nama','jabatan', 'unit_kerja', 'sub_unit_kerja']
        depth = 1

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['unit_kerja']= UnitKerjaSerializer(instance.unit_kerja).data
        representation['sub_unit_kerja']= SubUnitKerjaSerializer(instance.sub_unit_kerja).data
        return representation

    def create(self, validated_data):
        return Pegawai.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.nama = validated_data.get('nama', instance.nama)
        instance.jabatan = validated_data.get('jabatan', instance.jabatan)
        instance.status = validated_data.get('status', instance.status)
        instance.pangkat_golongan = validated_data.get('pangkat_golongan', instance.pangkat_golongan)
        instance.unit_kerja = validated_data.get('unit_kerja', instance.unit_kerja)
        instance.sub_unit_kerja = validated_data.get('sub_unit_kerja', instance.sub_unit_kerja)
        instance.save()


        return instance


class PegawaiDetailSerializer(serializers.ModelSerializer):
    unit_kerja = serializers.PrimaryKeyRelatedField(queryset=UnitKerja.objects.all())
    sub_unit_kerja = serializers.PrimaryKeyRelatedField(queryset=SubUnitKerja.objects.all())
    pangkat_golongan = serializers.PrimaryKeyRelatedField(queryset=PangkatGolongan.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Pegawai
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['unit_kerja'] = UnitKerjaSerializer(instance.unit_kerja).data if instance.unit_kerja else None
        representation['sub_unit_kerja'] = SubUnitKerjaSerializer(instance.sub_unit_kerja).data if instance.sub_unit_kerja else None
        representation['pangkat_golongan'] = PangkatGolonganSerializer(instance.pangkat_golongan).data if instance.pangkat_golongan else None
        return representation



class PegawaiKoordinatorSubstansiSerializer(serializers.ModelSerializer):
    pegawai = serializers.PrimaryKeyRelatedField(queryset=Pegawai.objects.all(), allow_null=False, required=True)
    koordinator_substansi = serializers.PrimaryKeyRelatedField(queryset=KoordinatorSubstansi.objects.all(), allow_null=False, required=True)
    unit_kerja = serializers.PrimaryKeyRelatedField(queryset=UnitKerja.objects.all(), allow_null = False, required = True)

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['pegawai'] = PegawaiSelectSerializer(instance.pegawai).data if instance.pegawai else None
        representation['koordinator_substansi'] = KoordinatorSubstansiSerializer(instance.koordinator_substansi).data if instance.koordinator_substansi else None
        representation['unit_kerja'] = UnitKerjaSerializer(instance.unit_kerja).data if instance.unit_kerja else None

        return representation
    
    def create(self, validated_data):
        return PegawaiKoordinatorSubstansi.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.pegawai = validated_data.get('pegawai', instance.pegawai)
        instance.koordinator_substansi = validated_data.get('koordinator_substansi', instance.koordinator_substansi)
        instance.tmt = validated_data.get('tmt', instance.tmt)
        # instance.akhir = validated_data.get('akhir', instance.akhir)
        instance.status = validated_data.get('status', instance.status)

        instance.save()

        return instance

        

    class Meta:
        model = PegawaiKoordinatorSubstansi
        fields = '__all__'
        depth = 1
