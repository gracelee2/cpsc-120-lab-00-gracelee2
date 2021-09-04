#!/bin/sh
#
# Makes a half decent guess as to what it should compile.
# If there are part-? directories with Makefiles, then it will use
# Makefiles
# If there are just a bunch of loose .cc files then it will try to
# compile a binary for each .cc file.
#
# This script should be removed and replaced with something more 
# generic
#
echo "Hello, Hello! Let's see if your programs compile. If they don't you won't get any credit!"
echo "Compiling..."
PARTS=`ls -1 part-* 2>/dev/null`
CCSRC=`ls -1 *.cc 2>/dev/null`
if [ "${PARTS}X" != "X" ]; then
  c=1
  for p in ${PARTS}; do
    # Makefile first, then files
    if [ -r $p/Makefile ]; then
      pushd $p >& /dev/null
      make spotless > /dev/null 2>&1
      make
      if [ $? -ne 0 ]; then
        echo "There appears to be an error."
      fi
      popd >& /dev/null      
    elif [ -r $p/*.cc ]; then
      set -x
      clang++ -Wall -std=c++14 $p/*.cc -o p$c
      set +x
      if [ $? -ne 0 ]; then
        echo "Whoa! There was an error compiling $p. Stopping the check. Fix it ASAP!"
        break
      fi
    fi
    (( c++ ))
  done
elif [ "${CCSRC}X" != "X" ]; then
  for f in ${CCSRC}; do
      set -x
      clang++ -Wall -std=c++14 $f -o p$c
      set +x
      if [ $? -ne 0 ]; then
        echo "Whoa! There was an error compiling $f. Stopping the check. Fix it ASAP!"
        break
      fi
  done
fi
echo "If you don't see any errors or warnings then you're on the right track!"
echo "Did you test your programs thoroughly? Make sure they don't break otherwise you won't get the score you want."
