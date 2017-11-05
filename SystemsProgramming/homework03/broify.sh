#!/bin/sh
#Eugene Choi

DELIM="#" #stores comment delimiter; default is #
WFLAG=0 #determines whether -W flag is called 

usage() {
	echo "Usage: broify.sh"
	echo "-d DELIM Use this as the comment delimiter"
	echo "-W       Don't strip empty lines"

	exit 1
}



while [[ "$#" -gt "0" ]]; do
	case $1 in
		-W) WFLAG=1 ;;
		-d) DELIM=$2 shift;;
		-h) usage
	esac
	shift
done

if [[ "$WFLAG" -eq "0" ]]; then
	sed -e "s|$DELIM.*||" -e 's/\s*$//' -e '/^$/d'
else
	sed -e "s|$DELIM.*||" -e 's/\s*$//'

fi
