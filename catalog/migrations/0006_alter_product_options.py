from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_alter_product_price"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "purchase_price", "created_at"],
                "permissions": [
                    ("can_unpublish_product", "Can unpublish product"),
                    ("can_delete_product", "Can delete product"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]