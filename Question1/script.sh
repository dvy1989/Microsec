#!/bin/bash
wget -q -O - $1 | grep -oP ".{0,10}$2.{0,10}"
links=$(wget -q -O - $1 | grep -oP '(?<=<a).*(?=(<\/a>))' | grep -oP '(?<=href=").*(?=>)' | cut -d ' ' -f1 | cut -d '"' -f1 | sed 's/^\/\/\(.*\)/\1/')
for link in $links; do
  if [[ ${link:0:1} != \# ]]; then
     if [[ $link != $1 ]]; then
        ./script.sh $link $2
     fi
  fi
done
