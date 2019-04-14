from django.db import migrations

class Migration(migrations.Migration)
  initial = True

  dependencies = []

  operations = [
    migrations.RunSQL(
      sql="""
        CREATE TABLE `Account` (
          `userid` bigint(20) unsigned NOT NULL AUTO_INCREMENT
        );
      """,
      reverse_sql="""
        DROP TABLE `Account`;
      """
    )
  ]
