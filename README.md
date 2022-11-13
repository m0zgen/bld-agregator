# BLD Agregator

![today](https://raw.githubusercontent.com/m0zgen/bld-agregator/data/badge_date.svg) ![total](https://raw.githubusercontent.com/m0zgen/bld-agregator/data/badge_total.svg) ![total](https://raw.githubusercontent.com/m0zgen/bld-agregator/data/badge_total_allow.svg)

Block and Allow lists periodically updated from different sources, you cand download it's lists from links bellow.

## Lists for download

Block lists:
* [hosts.txt](https://raw.githubusercontent.com/m0zgen/bld-agregator/data/hosts.txt)
* [blocklist.txt](https://raw.githubusercontent.com/m0zgen/bld-agregator/data/blocklist.txt)
* [blocklist.cdb](https://raw.githubusercontent.com/m0zgen/bld-agregator/data/blocklist.cdb)

Allow (White) lists:
* [allowlist.txt](https://raw.githubusercontent.com/m0zgen/bld-agregator/data/allowlist.txt)
* [allowlist.cdb](https://raw.githubusercontent.com/m0zgen/bld-agregator/data/allowlist.cdb)

# Sources
Block lists sources:
* Aggregate many blacklists to one blacklist from different sources, for block lists see `blocking.yml`

Allow lists sources:
* https://raw.githubusercontent.com/m0zgen/dns-hole/master/whitelist.txt
* https://raw.githubusercontent.com/m0zgen/dns-hole/master/vendors-wl/google.txt
* https://raw.githubusercontent.com/m0zgen/dns-hole/master/vendors-wl/microsoft.txt
* https://raw.githubusercontent.com/m0zgen/dns-hole/master/vendors-wl/yandex.txt
* https://raw.githubusercontent.com/m0zgen/dns-hole/master/regex/common-wl.txt

# Credits
* https://github.com/dmachard/python-blocklist-aggregator
* https://github.com/dmachard/blocklist-domains
* https://wazuh.com/blog/using-osint-to-create-cdb-lists/
* https://iplists.firehol.org
* https://github.com/m0zgen/dns-hole
