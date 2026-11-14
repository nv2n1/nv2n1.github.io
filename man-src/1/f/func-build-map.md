---
title: "func-build-map(1)"
name: "func-build-map"
section: "1"
letter: "f"
url: "/docs/linux/man/1-func-build-map/"
---

<h2>NAME</h2>

 func-build-map -- Builds/augments delegation map of all available func minions

<h2>SYNOPSIS</h2>

 func-build-map [-a|--append] [-o|--onlyalive] [-v|--verbose]

<h2>DESCRIPTION</h2>

 Func's delegation feature allows an overlord to execute commands through proxies (minions which also run as overlords) to reduce <font SIZE="-1">XMLRPC</font> overhead and the amount of time required to execute commands over large Func networks. 

 To accomplish this task, Func needs to know where each proxy and minion sits in the Func network, and for the sake of expediency, this data is stored within a map file on the overlord. 

 func-build-map, when run on an overlord, recursively probes through one's Func network, discovering its topology. When complete, it stores a mapfile, encoded in <font SIZE="-1">YAML</font>, in /var/lib/func/map. 

 If you utilize delegation frequently, we recommend running this tool as a cron job to ensure that your mapfile remains up to date with changes in your Func network topology.

<h2>DELEGATION</h2>

 Run without arguments, func-build-map will rewrite any mapfile currently sitting in /var/lib/func. 

 To delegate commands, this mapfile must be created and kept updated. It is hence recommended to run this as a daily cron job on the highest overlord. 

 Note: Minions not yet in the map file will not be reached by delegation calls.

<h2>-a, --append</h2>

 Combines new Func network topology data with data from the old map file, performing a tree merge. If this merge fails, it replaces the old mapfile with a fresh version.

<h2>-o, --onlyalive</h2>

 Pings all minions and proxies and returns a map containing those which return those pings. Useful for Func network diagnostics and for those who maintain networks where minions are frequently switched on and off.

<h2>-v, --verbose</h2>

 Gives additional information as to what func-build-map is doing

<h2>DELEGATES</h2>

 To get started with delegation via the Python <font SIZE="-1">API</font>, try the following code: 

 <pre>
  import func.overlord.client as fc
  my_overlord = fc.Overlord(&quot;&lt;your glob&gt;&quot;, delegate=True)
</pre> 

 If you want to use an alternative delegation map file, you can add the argument mapfile=&lt;your mapfile location&gt; to the Overlord constructor to tell it to pull the mapping data out of it instead. 

 From this point, you can treat your delegating overlord object in the same manner as a non-delegating overlord. Minions that exist under multiple layers of overlords will appear as if they existed directly beneath your master overlord, so make some function calls and play around with it!

<h2>ADDITIONAL RESOURCES</h2>

 See <a rel="nofollow" HREF="https://fedorahosted.org/func/">https://fedorahosted.org/func/</a> for more information. 

 For feature-specific info, visit <a rel="nofollow" HREF="https://fedorahosted.org/func/wiki/DelegationModule.">https://fedorahosted.org/func/wiki/DelegationModule.</a>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-func-create-module/">func-create-module</a></i>(1), <i><a HREF="/docs/linux/man/1-func-transmit/">func-transmit</a></i>(1), <i><a HREF="/docs/linux/man/1-func-inventory/">func-inventory</a></i>(1), <i><a HREF="/docs/linux/man/1-func/">func</a></i>(1), <i><a HREF="/docs/linux/man/1-funcd/">funcd</a></i>(1).

<h2>AUTHOR</h2>

 Steve Salevan &lt;ssalevan [at] redhat.com&gt;, Nima Talebi &lt;nima [at] it.net.au&gt; 

<h2>Index</h2>


