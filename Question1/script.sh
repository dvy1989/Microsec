if [ -f visited ]; then
   if grep -Fxq $1 visited; then
      exit 0
   fi
fi
found=$(wget -q -O - $1 | grep -oP ".{0,10}$2.{0,10}")
if [ ! found ]; then
   exit 0
fi
for str in $found; do
   echo "$1;$str"
done
echo $1 >> visited
links=$(wget -q -O - $1 | grep -oP '(?<=<a).*(?=(<\/a>))' | grep -oP '(?<=href=").*(?=>)' | cut -d ' ' -f1 | cut -d '"' -f1 | sed 's/^\/\/\(.*\)/\1/')
for link in $links; do
  if [[ ${link:0:1} != \# ]]; then
     ./script1.sh $link $2
  fi
done
