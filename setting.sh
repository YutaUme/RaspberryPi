#!/bin/bash
if [ $# -ne 1 ]; then
	echo "The Num of args is $#" 1>&2
	echo "You set one arg to to Exec. this script" 1>&2
	exit 1
fi

var=$1
echo $var
echo $var >> setting.txt
$1

exit 0

