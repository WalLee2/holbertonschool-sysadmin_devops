# debugging wordpress
exec { 'Fix Wordpress':
  path    => '/sbin:/bin:/usr/sbin:/usr/bin',
  command => "sed -i 's/phpp/php/'  /var/www/html/class-wp-locale.php"
}
