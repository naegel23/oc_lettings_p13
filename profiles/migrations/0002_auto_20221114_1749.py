# Generated by Django 3.0 on 2022-11-14 16:49
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
                INSERT INTO profiles_profile(
                    user_id,
                    favorite_city
                )
                SELECT
                    user_id,
                    favorite_city
                FROM
                    oc_lettings_site_profile;
            """, reverse_sql="""
                INSERT INTO oc_lettings_site_profile(
                    user_id,
                    favorite_city 
                )
                SELECT
                    user_id,
                    favorite_city 
                FROM
                    profiles_profile;
            """)
    ]
