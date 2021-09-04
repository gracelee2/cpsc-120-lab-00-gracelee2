#!/bin/sh
#
# This is based off of compile_check.sh.
# Run clang-tidy and clang-format against all the .cc files in
# a given directory tree
#
# This script should be removed and replaced with something more 
# generic.
#

TIDY="clang-tidy"
FORMAT="clang-format"
TIDYFLAGS="-checks=-*,google-*,modernize-*,readability-*,\
cppcoreguidelines-*,-google-build-using-namespace,\
-modernize-use-trailing-return-type,\
-cppcoreguidelines-avoid-magic-numbers,\
-readability-magic-numbers,\
-cppcoreguidelines-pro-type-union-access,\
-cppcoreguidelines-pro-bounds-constant-array-index"
FORMATFLAGS="-style=Google --Werror"

echo "Hello, Hello! Let's see if you're sticking to the Google C++ Style Guide!"
PARTS=`ls -1 part-* 2>/dev/null`
CCSRC=`ls -1 *.cc 2>/dev/null`

if [ "${PARTS}X" != "X" ]; then
  for p in ${PARTS}; do
    if [ -r $p/Makefile ]; then
      pushd $p >& /dev/null
      make tidy
      if [ $? -ne 0 ]; then
        echo "Look over your code very carefully. There may be errors."
      fi
      make format
      if [ $? -ne 0 ]; then
        echo "Look over your code very carefully. There may be errors."
      fi
      popd >& /dev/null      
    elif [ -r $p/*.cc ]; then
      for f in $p/*.cc; do
        set -x
        ${TIDY} $f ${TIDYFLAGS} 2>/dev/null
        set +x
        if [ $? -ne 0 ]; then
          echo "Whoa! Make sure your code in $p is nice and tidy."
          break
        fi
        $(eval FORMATOUT := $(shell mktemp))
        set -x
        $(FORMAT) $(FORMATFLAGS) $$i > $(FORMATOUT)
        set +x
        diff $$i $(FORMATOUT) || \
        echo "\nYour file does not conform to the Google C++ Style."
        echo "Please edit your code until this message is removed."
        rm $(FORMATOUT)
      done
    fi
  done
elif [ "${CCSRC}X" != "X" ]; then
  for f in ${CCSRC}; do
    set -x
    ${TIDY} $f ${TIDYFLAGS} 2>/dev/null
    set +x
    if [ $? -ne 0 ]; then
      echo "Whoa! Make sure your code in $p is nice and tidy."
      break
    fi
    FORMATOUT=`mktemp`
    set -x
    ${FORMAT} ${FORMATFLAGS} $f > ${FORMATOUT}
    set +x
    diff $f ${FORMATOUT}
    if [ $? -ne 0 ]; then
      echo "Error: Your file does not conform to the Google C++ Style."
      echo "Please edit your code until this message is removed."
    fi
    rm ${FORMATOUT}
  done
fi
echo "If you don't see any errors or warnings then you're on the right track!"
echo "Did you test your programs thoroughly? Make sure they don't break otherwise you won't get the score you want."
