#!/bin/bash
if [ -f visited ]; then
   if grep -Fxq $1 visited; then
      echo "Already visited" >> log
      exit 0
   fi
fi
wget -q -O - $1 | grep -oP ".{0,10}$2.{0,10}"
#echo $found
#if [ ! $found ]; then
#   echo "Nothing found" >> log
#   exit 0
#fi
#for str in $found; do
#   echo "$1;$str"
#done
echo $1 >> visited
links=$(wget -q -O - $1 | grep -oP '(?<=<a).*(?=(<\/a>))' | grep -oP '(?<=href=").*(?=>)' | cut -d ' ' -f1 | cut -d '"' -f1 | sed 's/^\/\/\(.*\)/\1/')
for link in $links; do
  if [[ ${link:0:1} != \# ]]; then
     ./script.sh $link $2
  fi
done
