# Modify /etc/default/nginx to be able to close more requests
# restart nginx after file has been changed
exec { "restart nginx":
     command   => "/bin/sed -i 's|-n 15|-n 4096|g' /etc/default/nginx ; /etc/init.d/nginx restart"
}
