# Puppet script to debug error

exec { 'sed -i s/phpp/php/g /var/www/html/wp-settings.php':
  path => '/usr/local/bin/:/bin/'
}
