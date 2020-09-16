#!/bin/bash

#***************************************************************************#
#                                                                           #
# Script that takes three arguments(filename, hostname and new IP address.  #
# If the hostname is found in the file the IP address will be changed.      #
#                                                                           #
# Robert Sundh Student 2020-03-19                                           #
#                                                                           #
#***************************************************************************#

REG='([0-9]{1,3}[\.]){3}[0-9]{1,3}'

set -o nounset

DIR="tmp/"

#Check if 3 arguments are given
if [ $# -ne 3 ]; then
	echo "Give three arguments #1 filename #2 hostmame #3 new IP address"
	exit
fi

#Check if file exists, if not program exits
if [ -f $1 ]; then
    echo -e "File found\n"
else
    echo "File not found"
    exit
fi

#Check that the provided IP address is in correct format
if [[ $3 =~ $REG ]] ; then
    echo -e "Correct IP address\n"
else
    echo "Wrong IP address"
    exit
fi

#I removed the for loop from exercise 1 because its not needed if the file to search is specified.

MATCHED_LINE=$(grep -E "\<$2\>" $DIR$1)

#If the above command return 0 the program will enter the if statement and change IP address($3) on the matched line.
if [ "$?" -eq "0" ]; then
    cat $1 | sed 's/^\([0-9]\+\).\([0-9]\+\).\([0-9\+\).\([0-9]\+\)\(\s\+\)\'"$2\b"'\(.*\)/'$3'\4'$2'\5/g' > $DIR$1.upd2
    echo -e "$MATCHED_LINE, changed to $3    $2\n"
    echo -e "Match found in : $DIR$1\n"
    echo -e "New filed saved to $DIR$1.upd2\n"
fi
