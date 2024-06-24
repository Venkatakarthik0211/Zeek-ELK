#!/bin/bash

# create files with read permissions
touch waymore.txt output-urls.txt output-wordlists.txt output-parameters.txt output-oos.txt

# Run xnLinkFinder with the provided domain argument
waymore -i "$1" -mode U > waymore.txt
xnLinkFinder -i "$1" \
    -sp "$1" \
    -sf "$1" \
    -spo \
    -inc \
    -vv \
    -H 'Authorization: Bearer XXXXXXXXXXXXXX' \
    -H 'Cookie: SessionId=MYSESSIONID' \
    -u desktop mobile \
    -d 10 \
    -o output-urls.txt \
    -owl output-wordlists.txt \
    -op output-parameters.txt \
    -oo output-oos.txt




