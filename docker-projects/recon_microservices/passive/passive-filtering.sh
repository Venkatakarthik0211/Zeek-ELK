# use dsieve for further filtration of parent domains
echo "Extracting parent domains............."
mkdir -p filtered-parent-domains

# Run dsieve to filter parent domains and append the output to respective files
docker run -v $(pwd)/output-passive.txt:/root/output-passive.txt quay.io/trickest/dsieve -if /root/output-passive.txt -f 3 >> filtered-parent-domains/filter3.txt
docker run -v $(pwd)/output-passive.txt:/root/output-passive.txt quay.io/trickest/dsieve -if /root/output-passive.txt -f 4 >> filtered-parent-domains/filter4.txt

# Copy domains.txt to filtered-parent-domains directory
cp domains.txt filtered-parent-domains/

# Concatenate all files in filtered-parent-domains directory and save the result to output-filtered.txt
find filtered-parent-domains -type f -exec cat {} + | tee output-filtered.txt
