#!/bin/bash                                                                 

#***************************************************************************#
#                                                                           #
# Script to change the third octet in and IP address matching "10" to "20". #
#                                                                           #
# Robert Sundh Student 2020-03-19                                           #
#                                                                           #
#***************************************************************************#

REG="192.168.10.(25[0-5]|2[0-4][0-4]|1[0-9][0-9]|[0-9][0-9]|[0-9])"

DIR="tmp/"

set -o nounset

#For loop goes throu all files inside the directory tmp
for file in $DIR*; do
    grep -Eq $REG $file
    
    #If the above command return 0 the program will enter the if statement and change 10 to 20.
    if [ "$?" -eq "0" ]; then
        cat $file | sed 's/\.10\./.20./g' > $file.upd
    fi
done

