import blocklist_aggregator

ext_cfg = """
"""

# unified = blocklist_aggregator.fetch(cfg_update=ext_cfg)
unified = blocklist_aggregator.fetch(cfg_filename="blocking.yml")

with open("whitelist.yml") as f:
    ext_cfg += "\n" + f.read()
    
with open("blacklist.yml") as f:
    ext_cfg += "\n" + f.read()

blocklist_aggregator.save_raw(filename="blocklist.txt", cfg_update=ext_cfg)
blocklist_aggregator.save_hosts(filename="hosts.txt", cfg_update=ext_cfg) 
blocklist_aggregator.save_cdb(filename="blocklist.cdb", cfg_update=ext_cfg)

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
blocklist_aggregator.save_raw(filename="allowlist.txt", cfg_update=allow_yaml)
blocklist_aggregator.save_cdb(filename="allowlist.cdb", cfg_update=allow_yaml)