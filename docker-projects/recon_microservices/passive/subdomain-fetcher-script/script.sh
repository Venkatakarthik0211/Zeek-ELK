#!/bin/sh

# Function to fetch subdomains using Certspotter API
certspotter_subdomains() {
    curl -s "https://api.certspotter.com/v1/issuances?domain=$1&include_subdomains=true&expand=dns_names" | jq -r '.[].dns_names | @tsv' |  tr '\t' '\n'
}

# Function to fetch subdomains from web.archive.org
web_archive_subdomains() {
    curl -s "http://web.archive.org/cdx/search/cdx?url=*.ap.gov.in/*&output=text&fl=original&collapse=urlkey" | sed -e 's_https*://__' -e "s/\/.*//" | sed -e 's/:.*//' | sort -u
}

# Function to fetch subdomains using jldc.me/anubis
anubis_subdomains() {
    curl -s "https://jldc.me/anubis/subdomains/$1" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | sort -u
}

# Function to fetch subdomains from crt.sh
crtsh_subdomains() {
    curl -s "https://crt.sh/?q=%25.$1&output=json" | jq -r '.[].name_value' | sort -u
}

# Function to fetch subdomains from Alienvault OTX
alienvault_subdomains() {
    curl -s "https://otx.alienvault.com/api/v1/indicators/domain/$1/url_list?limit=100&page=1" | grep -o '"hostname": *"[^"]*' | sed 's/"hostname": "//' | sort -u
}

# Main script
if [ $# -eq 0 ]; then
    echo "Usage: ./script.sh <domain>"
    exit 1
fi

domain="$1"
echo "Domain: $domain"
certspotter_subdomains "$domain"
web_archive_subdomains "$domain"
anubis_subdomains "$domain"
crtsh_subdomains "$domain"
alienvault_subdomains "$domain"
echo "--------------------------------------"
