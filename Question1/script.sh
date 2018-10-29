#!/bin/bash
# Reads all appearances of a certain word
# Text is outputed to stdout for future usage
wget -q -O - $1 | grep -oP ".{0,10}$2.{0,10}"
# Read all links (only links in <a> tag are counted)
links=$(wget -q -O - $1 | grep -oP '(?<=<a).*(?=(<\/a>))' | grep -oP '(?<=href=").*(?=>)' | cut -d ' ' -f1 | cut -d '"' -f1 | sed 's/^\/\/\(.*\)/\1/')
for link in $links; do
# There might be anchors
  if [[ ${link:0:1} != \# ]]; then
     # There might a link to page on the page
     # TODO Avoid cycles in further recursive calls (page1 -> page2 -> page1)
     if [[ $link != $1 ]]; then
        ./script.sh $link $2
     fi
  fi
done
