sudo -u postgres psql -c 'CREATE DATABASE %(db_name)s;'
sudo -u postgres psql -c "CREATE USER %(db_user)s WITH PASSWORD '%(db_password)';"
sudo -u postgres psql -c "ALTER USER %(db_user)s superuser createrole createdb replication;"
sudo -u postgres psql -c "ALTER ROLE %(db_user)s SET client_encoding TO 'utf8';"
sudo -u postgres psql -c "ALTER ROLE %(db_user)s SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE %(db_user)s SET timezone TO 'UTC';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE %(db_name)s TO %(db_user)s;"