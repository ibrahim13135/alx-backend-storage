# Install MySQL and start the service
sudo apt-get update
sudo apt-get install mysql-server -y
sudo service mysql start

# Create the SQL script to list databases
echo "SHOW DATABASES;" > 0-list_databases.sql

# List databases
cat 0-list_databases.sql | mysql -uroot -p
# (Enter 'root' as the password when prompted)

# Create a new database
echo "CREATE DATABASE holberton;" | mysql -uroot -p
# (Enter 'root' as the password when prompted)

# Import the SQL dump
# curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/holberton.sql" -s | mysql -uroot -p holberton
# (Enter 'root' as the password when prompted)

# Verify the import
echo "SELECT * FROM tv_genres;" | mysql -uroot -p holberton
# (Enter 'root' as the password when prompted)
