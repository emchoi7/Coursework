#!/bin/sh
#Eugene Choi

STATE="Indiana" #stores state name; default is Indiana
FORMAT="text" #stores format type; default is text
CITY=0 #stores city name; default is 0 to determine if -c flag is called

usage() {
	echo "Usage: zipcode.sh"
	echo "-c   CITY    Which city to search"
	echo "-f   FORMAT  Which format (text, csv)"
	echo "-s   STATE   Which state to search (Indiana)"
	echo "If no CITY is specified, then all the zip codes for the STATE are displayed"
	exit $1
}

while [[ "$#" -gt "0" ]]; do

	case $1 in
		-c) CITY="$2" shift;;
		-s) STATE="$2" shift;;
		-f) FORMAT="$2" shift;;
		-h) usage 0;;
	esac
	shift

done

if [[ "$CITY" == 0 ]]; then #if CITY was not given

	if [[ "$FORMAT" == "text" ]]; then #text format: list each zipcode in new line
		curl -s http://www.zipcodestogo.com/"$STATE"/ | grep 'zip' | grep -Eo '[0-9]{5}' | sort | uniq

	elif [[ "$FORMAT" == "csv" ]]; then #csv format: list each zipcode separated by a comma
		curl -s http://www.zipcodestogo.com/"$STATE"/ | grep 'zip' | grep -Eo '[0-9]{5}' | sort | uniq | tr '\n' ', '

	fi
else #if CITY was given

	if [[ "$FORMAT" == "text" ]]; then #text format: list each zipcode in new line
		curl -s http://www.zipcodestogo.com/"$STATE"/ | grep "/$CITY/" | grep 'zip' | grep -Eo '[0-9]{5}' | sort | uniq

	elif [[ "$FORMAT" == "csv" ]]; then #csv format: list each zipcode separated by a comma
		curl -s http://www.zipcodestogo.com/"$STATE"/ | grep "/$CITY/" | grep 'zip' | grep -Eo '[0-9]{5}' | sort | uniq | tr '\n' ', '

	fi

fi






















