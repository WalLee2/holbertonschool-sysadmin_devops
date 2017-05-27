exec { 'modify_file':
  path    => '/bin:',
  command => "sed -i 's|-n 15|-n 4096|g' /etc/default/nginx"
}
exec { 'restart nginx':
  command   => '/etc/init.d/nginx restart'
}
