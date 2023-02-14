#!/usr/bin/bash

echo "All args: $*"
echo "Nb args: $#"
echo "Arg 1: $1"

if [ "$#" -ne 2 ]
then
    echo "Wrong number of arguments"
    echo "Usage: photo_move.sh srcdir destdir"
    exit 1
fi

if [ ! -d "$1" ]
then
    echo "$1 is not a directory"
    exit 2
fi

if [ ! -d "$2" ]
then
    echo "$2 is not a directory"
    exit 2
fi

SRC_DIR="$1"
DEST_DIR="$2"

for PHOTO in $SRC_DIR/*.jpg
do
    # echo "Photo to move: $PHOTO"
    # TODO: check filename format
    START=${#SRC_DIR}
    ((START += 5))
    DATE_TAG=${PHOTO:$START:8}
    # echo $DATE_TAG
    PHOTO_FOLDER="$DEST_DIR/$DATE_TAG"
    mkdir -p "$PHOTO_FOLDER"
    echo "Will move $PHOTO in $PHOTO_FOLDER"
    mv "$PHOTO" "$PHOTO_FOLDER/"
done 

