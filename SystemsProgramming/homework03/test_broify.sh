#!/bin/sh

SCRIPT=broify.sh
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

cat > $WORKSPACE/input0 <<EOF
# Super useful comment describing a tricky configuration option
SETUP_THE_BOMB="no" # Hide the evidence

# Another super userful comment
BASE_OWNERSHIP="us" # All your base are belong to...
EOF

cat > $WORKSPACE/output0 <<EOF
SETUP_THE_BOMB="no"
BASE_OWNERSHIP="us"
EOF

cat > $WORKSPACE/output0W <<EOF

SETUP_THE_BOMB="no"


BASE_OWNERSHIP="us"
EOF

cat > $WORKSPACE/input1 <<EOF
// C++ is so cool
int main() {
    // Totes
    return 0;	// YESSS
}
EOF

cat > $WORKSPACE/output1 <<EOF
int main() {
    return 0;
}
EOF

cat > $WORKSPACE/output1W <<EOF

int main() {

    return 0;
}
EOF

./$SCRIPT -h 2>&1 | grep -i usage 2>&1 > /dev/null
if [ $? -ne 0 ]; then
    error "Failed Usage Test"
fi

./$SCRIPT < $WORKSPACE/input0 | diff -y - $WORKSPACE/output0 > $WORKSPACE/test
if [ $? -ne 0 ]; then
    error "Failed BASE Test"
fi

./$SCRIPT -W < $WORKSPACE/input0 | diff -y - $WORKSPACE/output0W > $WORKSPACE/test
if [ $? -ne 0 ]; then
    error "Failed BASE Test (-W)"
fi

./$SCRIPT -d '//' < $WORKSPACE/input1 | diff -y - $WORKSPACE/output1 > $WORKSPACE/test
if [ $? -ne 0 ]; then
    error "Failed C++ Test"
fi

./$SCRIPT -d '//' -W < $WORKSPACE/input1 | diff -y - $WORKSPACE/output1W > $WORKSPACE/test
if [ $? -ne 0 ]; then
    error "Failed C++ Test (-W)"
fi

echo "$SCRIPT test succesful!"
exit 0
