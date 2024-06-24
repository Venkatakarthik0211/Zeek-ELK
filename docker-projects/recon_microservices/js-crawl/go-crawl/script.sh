#!/bin/sh

# Check if domain argument is provided
if [ -z "$1" ]; then
  echo "Please provide a domain name as an argument."
  exit 1
fi

# Domain name passed as argument
DOMAIN="$1"

# using waybackurls
waybackurls "$DOMAIN" | sort -u | grep '\.js$' > waybackurls-js.txt
cat waybackurls-js.txt

# temporary conversion
new_domain=$(echo "$DOMAIN" | sed 's/\./_/g')

# using gospider
gospider -u "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148" -c 30 -d 1 -s "https://$DOMAIN" -o gospider && mv gospider/"$new_domain" gospider.txt && rm -r gospider/

echo https://"$DOMAIN" | hakrawler -subs
