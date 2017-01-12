#!/bin/bash
#echo "now we are here "$1" "
case "$1" in
	1)
	cp /home/files/00.hosts /etc/hosts
	echo "Using the experiment with HTTP and 0% loss"
	;;
	2)
	cp /home/files/01.hosts /etc/hosts
	echo "Using the experiment with HTTP and 1% loss"
	;;
	3)
	cp /home/files/02.hosts /etc/hosts
	echo "Using the experiment with HTTP and 2% loss"
	;;
	4)
	cp /home/files/10.hosts /etc/hosts
	echo "Using the experiment with HTTP2 and 0% loss"
	;;
	5)
	cp /home/files/11.hosts /etc/hosts
	echo "Using the experiment with HTTP2 and 1% loss"
	;;
	6)
	cp /home/files/12.hosts /etc/hosts
	echo "Using the experiment with HTTP2 and 2% loss"
	;;
	*)
	echo "Experiment from 1 to 6"
	;;
esac