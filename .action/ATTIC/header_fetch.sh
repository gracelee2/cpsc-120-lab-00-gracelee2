#!/bin/sh
#
# This is based off of compile_check.sh.
#
# Run .action/header_check.py with a keyword against the .cc files
# in a given tree.
#
# This script should be removed and replaced with something more 
# generic.
#

PARTS=`ls -1 part-* 2>/dev/null`
CCSRC=`ls -1 *.cc 2>/dev/null`
if [ "${PARTS}X" != "X" ]; then
  for p in ${PARTS}; do
    for f in $p/*.cc; do
      python3 .action/header_fetch.py $f $1
      if [ $? -ne 0 ]; then
        echo "Whoa! $f seems to be missing a header! Stopping the check. Please fix."
        break
      fi
    done
  done
elif [ "${CCSRC}X" != "X" ]; then
  for f in ${CCSRC}; do
    python3 .action/header_fetch.py $f $1
    if [ $? -ne 0 ]; then
      echo "Error! $f seems to be missing a header! Stopping the check. Please fix."
      break
    fi
  done
fi

