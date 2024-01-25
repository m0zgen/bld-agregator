import blocklist_aggregator
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

conf = os.getenv("SCRIPT_BL_CONFIG")
bl_list = os.getenv("BLOCK_LIST")
wl_list = os.getenv("ALLOW_LIST")

ext_cfg = """
"""
# unified = blocklist_aggregator.fetch(cfg_update=ext_cfg)
unified = blocklist_aggregator.fetch(cfg_filename=conf)

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
with open(wl_list) as f:
    ext_cfg += "\n" + f.read()

with open(bl_list) as f:
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
# Export domain names data
  - urls:
      - https://raw.githubusercontent.com/m0zgen/dns-hole/master/whitelist.txt
      - https://raw.githubusercontent.com/m0zgen/dns-hole/master/vendors-wl/google.txt
      - https://raw.githubusercontent.com/m0zgen/dns-hole/master/vendors-wl/microsoft.txt
      - https://raw.githubusercontent.com/m0zgen/dns-hole/master/vendors-wl/yandex.txt
    pattern: ^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]$

# "Export regex data
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