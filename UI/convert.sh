#!/bin/sh

for uiFile in ./*.ui
do 
    fileName=$(basename $uiFile .ui)
    pyuic5 -x $uiFile -o ../$fileName.py
done