raspi-brew-www
==============

_RaSPi Web client_ for Brewing service

Web site runs on Lighttpd  FastCGI. The main thing that it is simple.
It also runs Python. Just to keep to one language all the code.

get ssh configured

apt-get install lighttpd
apt-get install python-flup
lighttpd configuration for FastCGI looks like this:


fastcgi.server = ( ".py" => ( "python-fcgi" => ( "socket" => "/tmp/fastcgi.python.socket", "bin-path" => "/var/www/cgi-bin/fcgiPipe.py", "check-local" => "disable", "max-procs" => 1) ) )

