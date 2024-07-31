from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('image', models.ImageField(upload_to='authors/images/', null=True, blank=True)),
                ('bdate', models.DateField(null=True, blank=True, default='1990-01-01')),
            ],
        ),
    ]
