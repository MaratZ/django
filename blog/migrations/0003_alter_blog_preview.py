from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_blog_publication_attribute"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="preview",
            field=models.ImageField(
                blank=True, null=True, upload_to="blogs/photo", verbose_name="Фото"
            ),
        ),
    ]