# get word occurencies
wget -q -O - $1 | grep -oP ".{0,10}$2.{0,10}"
# Get hyperlinks
wget -q -O - $1 | grep -oP '(?<=<a).*(?=(<\/a>)) | grep -oP '(?<=href=").*(?=">)' | cut -d ' ' -f1 | grep -oP '.*(?=")'