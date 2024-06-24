if [ ! -d "SecLists-master" ]; then
      wget -c https://github.com/danielmiessler/SecLists/archive/master.zip -O SecList.zip \
      && unzip SecList.zip \
      && rm -f SecList.zip
fi

cat output-passive.txt | tr . '\n' | sort -n | uniq > chars-newline.txt
cat output-passive.txt | sed 's/[.]/-/g' | awk -F '-' '{for(i=1;i<=(NF-2);i++) print $i}' | sort -n | uniq > dots-dash.txt
cat dots-dash.txt chars-newline.txt  >> /tmp/out.txt
cat /tmp/out.txt "$PWD/SecLists-master/Discovery/DNS/namelist.txt" | sort -n | uniq > wordlists.txt

echo "Prepare wordlists with custom wordlists....."

# Mount output-passive.txt and wordlists.txt into the Docker container
docker run -v "$(pwd)/output-passive.txt:/input/output-passive.txt" \
           -v "$(pwd)/wordlists.txt:/input/wordlists.txt" \
           quay.io/trickest/mksub -df /input/output-passive.txt -w /input/wordlists.txt > output-wordlists.txt
