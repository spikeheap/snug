### BEGIN INIT INFO
# Provides:          snug
# Required-Start:    $local_fs $network
# Required-Stop:     $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: snug
# Description:       snug heating controller
### END INIT INFO

# Init script courtesy of http://blog.rueedlinger.ch/2013/03/raspberry-pi-and-nodejs-basic-setup/
#
# Add this file to your startup directory using the following command:
#
#   $ ln -s /usr/local/snug/scripts/snug.init.d /etc/init.d/snug
#
# and ensure it is executable with
#
#   $ chmod +x /usr/local/snug/scripts/snug.init.d
#

NODE=/opt/node/bin/node
SERVER_JS_FILE=/usr/local/snug/app/server.js
USER=snug
OUT=/dev/null #If you're not using IPE and want to log, just set your log file path here.

case "$1" in

start)
	echo "starting node: $NODE $SERVER_JS_FILE"
	sudo -u $USER $NODE $SERVER_JS_FILE > $OUT 2>$OUT &
	;;

stop)
	killall $NODE
	;;

*)
	echo "usage: $0 (start|stop)"
esac

exit 0
