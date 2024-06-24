# Poison: JavaScript and Subdomain Enumeration Suite

**Unleash the Power of Passive Enumeration and JavaScript Crawling**
```sh

 ________  ________  ___  ________  ________  ________      
|\   __  \|\   __  \|\  \|\   ____\|\   __  \|\   ___  \    
\ \  \|\  \ \  \|\  \ \  \ \  \___|\ \  \|\  \ \  \\ \  \   
 \ \   ____\ \  \\\  \ \  \ \_____  \ \  \\\  \ \  \\ \  \  
  \ \  \___|\ \  \\\  \ \  \|____|\  \ \  \\\  \ \  \\ \  \ 
   \ \__\    \ \_______\ \__\____\_\  \ \_______\ \__\\ \__\
    \|__|     \|_______|\|__|\_________\|_______|\|__| \|__|
                            \|_________|                    
                                                                                                                      
```

This comprehensive suite empowers you to delve into the realms of passive subdomain enumeration and JavaScript crawling, unearthing hidden secrets and valuable insights within their confines. Buckle up, security sleuths, and prepare to embark on a captivating exploration!

**Directory Structure and Functionalities:**

**Passive Enumeration (passive directory):**

- `all.sh`: Orchestrates the entire passive enumeration process, streamlining your workflow.
- `passive-filtering.sh`: Refines the subdomain list, ensuring a focused and efficient active enumeration phase.
- `prepare-subdomain-wordlist.sh`: Generates a comprehensive wordlist to fuel your active subdomain enumeration endeavors.
- `exec.sh`: Executes the passive enumeration scripts in a defined sequence.
- `subdomain-fetcher-script` (directory):
    - `script.sh`: The engine that drives subdomain discovery through various channels.
    - `Dockerfile`: Defines the containerization specifications for the subdomain fetcher script.
    - `domains.txt`: (Optional) Seed file containing initial domains to kickstart the enumeration process.
- `passive/domains.txt`: (Optional) Serves as a catch-all for passively discovered domains.
- `passive-subdomains.sh`: Tailored script for passive subdomain enumeration, ideal for targeted operations.
- `test` (directory): (Optional) Houses test files (e.g., `active-js.txt`) to validate the functionality of the passive enumeration scripts.

**Active Crawling and JavaScript Analysis (js-crawl directory):**

- `js-crawl.sh`: The master script that orchestrates the JavaScript crawling process, meticulously extracting secrets and valuable content from unearthed JavaScript files.
- `exit.sh`: Gracefully exits the crawling process, ensuring a clean termination.
- `extract.sh`: Dedicated script focused on extracting secrets and content from JavaScript files.
- `active-urls.sh`: Meticulously gathers active URLs encountered during the crawling process.
- `python-crawl` (directory):
    - `script.sh`: Python-based crawling script, offering an alternative approach.
    - `Dockerfile`: Defines the Docker containerization specifications for the Python crawling script.
    - `config.yml`: Configuration file for the Python crawling script, allowing you to tailor its behavior.
- `python-crawl-support.sh`: Provides auxiliary support functions for the Python crawling script.
- `go-crawl` (directory):
    - `script.sh`: Go-based crawling script, providing a versatile option.
    - `Dockerfile`: Defines the Docker containerization specifications for the Go crawling script.
- `domains.txt`: (Optional) Seed file containing starting domains for active crawling.
- `js-finder` (directory):
    - `entrypoint.sh`: Script that sets the stage for JavaScript file discovery.
    - `Dockerfile`: Defines the Docker containerization specifications for the JavaScript finder.
- `go-filter` (directory):
    - `script.sh`: Script responsible for filtering out irrelevant or noisy data.
    - `Dockerfile`: Defines the Docker containerization specifications for the Go filter.

**How to Use:**

1. **Passive Enumeration:**
   - Navigate to the `passive` directory.
   - Execute `./all.sh` to initiate the comprehensive passive enumeration process.

2. **Active Crawling and JavaScript Analysis:**
   - Ensure you have the necessary dependencies installed (refer to the script comments or documentation for specific requirements).
   - Customize the configuration files (`config.yml` for Python, potentially others for other languages) as needed.
   - Navigate to the `js-crawl` directory.
   - Execute `./js-crawl.sh` to commence the crawling and JavaScript analysis.

**Customization and Advanced Usage:**

- The scripts provide a solid foundation, but you can delve deeper by studying the script comments and potentially modifying them to align with your specific
