import blocklist_aggregator

ext_cfg = """
"""

# unified = blocklist_aggregator.fetch(cfg_update=ext_cfg)
unified = blocklist_aggregator.fetch(cfg_filename="config.cfg")

with open("whitelist.yml") as f:
    ext_cfg += "\n" + f.read()
    
with open("blacklist.yml") as f:
    ext_cfg += "\n" + f.read()

blocklist_aggregator.save_raw(filename="blocklist.txt", cfg_update=ext_cfg)
blocklist_aggregator.save_hosts(filename="hosts.txt", cfg_update=ext_cfg) 
blocklist_aggregator.save_cdb(filename="blocklist.cdb", cfg_update=ext_cfg)

