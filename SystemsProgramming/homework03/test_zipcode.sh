#!/bin/sh

SCRIPT=zipcode.sh
WORKSPACE=/tmp/$SCRIPT.$(id -u)

error() {
    echo 1>&2 "ERROR: $@"
    [ -r $WORKSPACE/test ] && cat $WORKSPACE/test
    exit 1
}

cleanup() {
    rm -fr $WORKSPACE
    exit $1
}

mkdir $WORKSPACE

trap "cleanup 0" EXIT
trap "cleanup 1" INT TERM

./$SCRIPT -h 2>&1 | grep -i usage 2>&1 > /dev/null
if [ $? -ne 0 ]; then
    error "Failed Usage Test"
fi

if [ $(./$SCRIPT | wc -l) -ne 988 ]; then
    error "Failed Default Test"
fi

if [ $(./$SCRIPT -s Indiana | wc -l) -ne 988 ]; then
    error "Failed Indiana Test"
fi

if [ $(./$SCRIPT -s Indiana -c "Notre Dame" | wc -l) -ne 1 ]; then
    error "Failed Notre Dame, Indiana Test"
fi

if [ $(./$SCRIPT -s Indiana -c "South Bend" | wc -l) -ne 18 ]; then
    error "Failed South Bend, Indiana Test"
fi

if [ $(./$SCRIPT -s California | wc -l) -ne 2657 ]; then
    error "Failed California Test"
fi

if [ $(./$SCRIPT -s California -c "Orange" | wc -l) -ne 11 ]; then
    error "Failed Orange, California Test"
fi

if [ $(./$SCRIPT -s "New York" | wc -l) -ne 2205 ]; then
    error "Failed New York Test"
fi

if [ $(./$SCRIPT -s "New York" -c "New York" | wc -l) -ne 162 ]; then
    error "Failed New York, New York Test"
fi

echo "$SCRIPT test succesful!"
exit 0
