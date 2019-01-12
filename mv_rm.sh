#!/bin/bash
#cleaner to remove movie files

if [ -d "$1" ]; then
	rm -r "$1"
	echo "movie directory successfully deleted"
else
	echo "movie directory not found"
fi
sleep 1
