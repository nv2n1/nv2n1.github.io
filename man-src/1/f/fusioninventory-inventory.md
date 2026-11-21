---

title: "fusioninventory-inventory(1)"
name: "fusioninventory-inventory"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fusioninventory-inventory/"
---

fusioninventory-inventory - Standalone inventory 

fusioninventory-inventory [options] 

 <pre><code>
  Options:
    --scan-homedirs                scan use home directories (false)
    --scan-profiles                scan user profiles (false)
    --html                         save the inventory as HTML (false)
    --no-category=CATEGORY         do not list given category items
    -t --tag=TAG                   mark the machine with given tag
    --backend-collect-timeout=TIME timeout for inventory modules
                                     execution (30)
    --additional-content=FILE      additional inventory content file
    --verbose                      verbose output (control messages)
    --debug                        debug output (execution traces)
    -h --help                      print this message and exit
    --version                      print the task version and exit
</code></pre>

<i>fusioninventory-inventory</i> allows to run an inventory task without a <font SIZE="-1">GLPI</font> server.
