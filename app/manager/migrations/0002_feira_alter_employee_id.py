from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longi', models.CharField(blank=True, default='', max_length=15)),
                ('lat', models.CharField(blank=True, default='', max_length=15)),
                ('setcens', models.CharField(blank=True, default='', max_length=20)),
                ('areap', models.CharField(blank=True, default='', max_length=20)),
                ('coddist', models.IntegerField(blank=True, null=True)),
                ('distrito', models.CharField(blank=True, default='', max_length=20)),
                ('codsubpref', models.IntegerField(blank=True, null=True)),
                ('subprefe', models.CharField(blank=True, default='', max_length=40)),
                ('regiao5', models.CharField(blank=True, default='', max_length=20)),
                ('regiao8', models.CharField(blank=True, default='', max_length=20)),
                ('nome_feira', models.CharField(blank=True, default='', max_length=40)),
                ('registro', models.CharField(blank=True, default='', max_length=10)),
                ('logradouro', models.CharField(blank=True, default='', max_length=40)),
                ('numero', models.CharField(blank=True, default='', max_length=15)),
                ('bairro', models.CharField(blank=True, default='', max_length=40)),
                ('referencia', models.CharField(blank=True, default='', max_length=40)),
            ],
            options={
                'verbose_name': 'Feira',
                'verbose_name_plural': 'Feiras',
            },
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
