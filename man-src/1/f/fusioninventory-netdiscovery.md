---

title: "fusioninventory-netdiscovery(1)"
name: "fusioninventory-netdiscovery"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fusioninventory-netdiscovery/"
---

fusioninventory-netdiscovery - Standalone network discovery 

fusioninventory-netdiscovery [options] --first &lt;start&gt; --last &lt;stop&gt; 

 <pre><code>
Options : --first address IP range first address-- last address IP range last address-- credential SNMP credential(default:version : 1, community
                                                                                                                   : public)-- entity GLPI entity
          -- threads nb number of discovery threads(default : 1)-- timeout val SNMP timeout(default : 1s)-- control output control messages
          -- debug debug output(execution traces) -
          h-- help print this message and exit
          -- version print the task version and exit
</code></pre>

<i>fusioninventory-netdiscovery</i> allows to run a network discovery task without a <font SIZE="-1">GLPI</font> server.
