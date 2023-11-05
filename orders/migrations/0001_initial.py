# Generated by Django 4.2.5 on 2023-10-25 18:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bills",
            fields=[
                ("order_id", models.AutoField(primary_key=True, serialize=False)),
                ("table_id", models.IntegerField(default=0)),
                ("amount", models.IntegerField(default=0)),
                ("status", models.BooleanField(default=False)),
                ("date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("cust_id", models.AutoField(primary_key=True, serialize=False)),
                ("phone_no", models.CharField(max_length=15, unique=True)),
                ("name", models.CharField(max_length=100)),
                ("membership_applied", models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="tables",
            fields=[
                ("tid", models.AutoField(primary_key=True, serialize=False)),
                ("status", models.BooleanField()),
                (
                    "last_selected_time",
                    models.DateTimeField(default=datetime.datetime.now),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Orders",
            fields=[
                ("serial", models.AutoField(primary_key=True, serialize=False)),
                ("Qty", models.IntegerField(default=1)),
                ("status", models.BooleanField(default=False)),
                (
                    "order_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="orders.bills"
                    ),
                ),
                (
                    "product_id",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="menu.product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="bills",
            name="userId",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="orders.customer"
            ),
        ),
    ]
