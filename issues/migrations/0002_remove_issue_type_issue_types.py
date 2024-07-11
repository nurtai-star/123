from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='type',
        ),
        migrations.AddField(
            model_name='issue',
            name='types',
            field=models.ManyToManyField(to='issues.type'),
        ),
    ]
