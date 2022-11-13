import blocklist_aggregator
from pathlib import Path

ext_cfg = """
"""
# unified = blocklist_aggregator.fetch(cfg_update=ext_cfg)
unified = blocklist_aggregator.fetch(cfg_filename="blocking.yml")

# Functions
# Sort txt files
def sort_file(path):
    file = Path(path)
    file.write_text(
        "\n".join(
            sorted(
                file.read_text().split("\n")
            )
        )
    )
    with open(path, 'r') as original: data = original.read()
    with open(path, 'w') as modified: modified.write("# BLD Agregator sorted file" + data)

# Stage 1
with open("whitelist.yml") as f:
    ext_cfg += "\n" + f.read()

with open("blacklist.yml") as f:
    ext_cfg += "\n" + f.read()

blocklist_aggregator.save_raw(filename="blocklist.txt", cfg_update=ext_cfg)
blocklist_aggregator.save_hosts(filename="hosts.txt", cfg_update=ext_cfg)
blocklist_aggregator.save_cdb(filename="blocklist.cdb", cfg_update=ext_cfg)

# Stage 2
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

# Sorting
sort_file("blocklist.txt")
sort_file("allowlist.txt")