# Killing a specific process called killmenow
exec { 'killmenow':
  path    => '/usr/bin:/sbin:/bin:/usr/sbin',
  command => 'pkill -f killmenow'
}
