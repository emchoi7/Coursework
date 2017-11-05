#!/bin/sh
#Eugene Choi

#Need to take care of the no argument thing

LOWER=abcdefghijklmnopqrstuvwxyz
UPPER=ABCDEFGHIJKLMNOPQRSTUVWXYZ



if [[ "$1" == "-h" ]]; then

	echo "Usage: caesar.sh [rotation]"

elif [[ "$#" -eq "0" ]]; then
	ROTATE=13
	sed "y/${LOWER}/${LOWER:$ROTATE}${LOWER::$ROTATE}/" | sed "y/${UPPER}/${UPPER:$ROTATE}${UPPER::$ROTATE}/"

elif [[ "$#" -gt "0" ]]; then
	#Also account for uppercase chars???
	ROTATE=$1 #stores number to rotate the letters
	if [[ "$ROTATE" -gt "26" ]]; then #accounts for when given number is bigger than number of alphabets
		ROTATE=$ROTATE%26
		sed "y/${LOWER}/${LOWER:$ROTATE}${LOWER::$ROTATE}/" | sed "y/${UPPER}/${UPPER:$ROTATE}${UPPER::$ROTATE}/"
	else
		sed "y/${LOWER}/${LOWER:$ROTATE}${LOWER::$ROTATE}/" | sed "y/${UPPER}/${UPPER:$ROTATE}${UPPER::$ROTATE}/"
	fi

fi