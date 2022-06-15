#!/usr/local/bin/bash
PASSWORD=$1
USERPID=$2
/bin/kill -9 $USERPID
echo "Send signal!"
