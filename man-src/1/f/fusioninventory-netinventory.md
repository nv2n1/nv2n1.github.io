---

title: "fusioninventory-netinventory(1)"
name: "fusioninventory-netinventory"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fusioninventory-netinventory/"
---

fusioninventory-netinventory - Standalone network inventory 

fusioninventory-netinventory [options] [--host &lt;host&gt;|--file &lt;file&gt;] 

 <pre><code>
Options : --host host host to inventorize(use multiple time to inventorize more hosts)-- file snmpwalk output file
          -- community community string(default
                                        : public)-- credentials SNMP credentials
          -- timeout val SNMP timeout(default : 15s)-- threads nb number of invenroty threads(default : 1)-- control output control messages
          -- debug debug output(execution traces) -
          h-- help print this message and exit
          -- version print the task version and exit
</code></pre>

<i>fusioninventory-netinventory</i> allows to run a network inventory task without a <font SIZE="-1">GLPI</font> server.
