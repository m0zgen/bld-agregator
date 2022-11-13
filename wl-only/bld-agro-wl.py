import blocklist_aggregator

allow_yaml = """
verbose: true
whitelist: []
blacklist: []
sources:
  - urls:
      - https://raw.githubusercontent.com/m0zgen/dns-hole/master/whitelist.txt
      - https://raw.githubusercontent.com/m0zgen/dns-hole/master/vendors-wl/google.txt
      - https://raw.githubusercontent.com/m0zgen/dns-hole/master/vendors-wl/microsoft.txt
      - https://raw.githubusercontent.com/m0zgen/dns-hole/master/vendors-wl/yandex.txt
      - https://raw.githubusercontent.com/m0zgen/dns-hole/master/regex/common-wl.txt
    pattern: ^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]$
    
  - urls:
      - https://raw.githubusercontent.com/m0zgen/dns-hole/master/regex/common-wl.txt
    pattern: ^(\/.*\/)$
"""

unified = blocklist_aggregator.fetch(cfg_update=allow_yaml)
blocklist_aggregator.save_raw(filename="../allowlist.txt", cfg_update=allow_yaml)
blocklist_aggregator.save_cdb(filename="../allowlist.cdb", cfg_update=allow_yaml)