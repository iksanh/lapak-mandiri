# Generated by Django 4.2 on 2024-06-23 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit_kerja', '0002_remove_subunitkerja_unitkerjaid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subunitkerja',
            old_name='NamaSubUnitKerja',
            new_name='nama_sub_unit_kerja',
        ),
        migrations.RenameField(
            model_name='subunitkerja',
            old_name='SubUnitKerjaID',
            new_name='sub_unit_kerja_id',
        ),
        migrations.RenameField(
            model_name='unitkerja',
            old_name='NamaUnitKerja',
            new_name='nama_unit_kerja',
        ),
        migrations.RenameField(
            model_name='unitkerja',
            old_name='UnitKerjaID',
            new_name='unit_kerja_id',
        ),
        migrations.RenameField(
            model_name='unitkerja_subunitkerja',
            old_name='SubUnitKerjaID',
            new_name='sub_unit_kerja',
        ),
        migrations.RenameField(
            model_name='unitkerja_subunitkerja',
            old_name='UnitKerjaID',
            new_name='unit_kerja',
        ),
        migrations.AlterUniqueTogether(
            name='unitkerja_subunitkerja',
            unique_together={('unit_kerja', 'sub_unit_kerja')},
        ),
    ]
