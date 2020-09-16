#!/bin/bash

#***************************************************************************#
#                                                                           #
# Script that takes one argument -s(search) -b(change) -r(delete).          #
#                                                                           #
# -s search for IP address or hostname                                      #
#                                                                           #
# -r search for IP address or hostname and remove the line with #           #
#                                                                           #
# -b runs another script that takes three arguments-                        # 
# filename, hostname and new IP address.                                    #
# If the hostname is found in the file the IP address will be changed.      #
#                                                                           #
# Robert Sundh Student 2020-03-19                                           #
#                                                                           #
#***************************************************************************#

REG='([0-9]{1,3}[\.]){3}[0-9]{1,3}'
DIR="tmp/"

set -o nounset

USERINPUT=" "

#Function to search for a matching IP address or hostname from userinput and remove the line with a #.
remove_line() {
    for file in $DIR*; do
        MATCHED_LINE=$(grep -E "\<$USERINPUT\>" $file)
 
        if [ "$?" -eq "0" ]; then
            cat $file | sed "/\<$USERINPUT\>/c\#$MATCHED_LINE" > $file.upd3
            echo $MATCHED_LINE
            echo -e "Match found in : $file\n"
            echo -e "New filed saved to $file.upd3\n"
        fi
    done
}

#Function to search for a matching IP address or hostname from userinput.
search_ip_or_host() {
    for file in $DIR*; do
        grep -Eq "\<$USERINPUT\>" $file

        #If the above command return 0 the program will enter the if statement and print the matching line.
        if [ "$?" -eq "0" ]; then
            cat $file | grep -E "\<$USERINPUT\>"
            echo -e "Match found in : $file\n"
        fi
    done
}

#Check if one argument is given.
if [ $# -ne 1 ]; then
    echo "Give one argument -s(search) -b(change) -r(delete)"
    exit
fi

#
if [ $1 = '-s' ]; then
    echo "Search for IP address or hostname : "
    read USERINPUT
fi

#
if [ $1 = '-r' ]; then
    echo "Search for IP address or hostname to delete : "
    read USERINPUT
fi

#The program enters the function with matching argument -s , -r or -b
if [ -n $USERINPUT ] && [[ $1 = '-s' ]]; then
    echo -e "\nValid ip address or hostname\n"
    search_ip_or_host

elif [ -n $USERINPUT ] && [[ $1 = '-r' ]]; then
    echo -e "\nValid ip address or hostname\n"
    remove_line

#Give three arguments to use with "skript2.sh"
elif [ $1 = '-b' ]; then
    echo "Give filename"
    read FILE
    echo "Give hostname"
    read HOST
    echo "Give NEW ip address"
    read IP
    ./skript2.sh $FILE $HOST $IP
    exit

else
    echo "Not valid input"
    exit
fi
