---

title: "fusioninventory-injector(1)"
name: "fusioninventory-injector"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fusioninventory-injector/"
---

fusioninventory-injector - A tool to push inventory in an OCS Inventory or compatible server. 

fusioninventory-injector [options] [--file &lt;file&gt;|--directory &lt;directory&gt;|--stdin|--useragent &lt;user-agent&gt;] 

 <pre><code>
  Options:
    -h --help      this menu
    -d --directory load every .ocs files from a directory
    -R --recursive recursively load .ocs files from &lt;directory&gt;
    -f --file      load a speficic file
    -u --url       server URL
    -r --remove    remove succesfuly injected files
    -v --verbose   verbose mode
    --stdin        read data from STDIN
    --useragent    set used HTTP User-Agent for POST
    -x --xml-ua    use Client version found in XML as User-Agent for POST
  Examples:
    fusioninventory-injector -v -f /tmp/toto-2010-09-10-11-42-22.ocs --url https://login:pw@server/ocsinventory
    fusioninventory-injector -v -R -d /srv/ftp/fusion --url https://login:pw@glpi-server/plugins/fusioninventory/
</code></pre>

This tool can be used to test your server, do benchmark or push inventory from off-line machine.
