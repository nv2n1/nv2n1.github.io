---
title: "pingd(8)"
name: "pingd"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pingd/"
description: "pingd – node up/down monitoring daemon"
---

<p>pingd &#8211; node up/down monitoring daemon</p>
<h2>Synopsis</h2>
<p><code>pingd [OPTIONS]</code></p>
<h2>Description</h2>
<p>The <code>pingd</code> daemon regularly sends out ICMP pings to determine if nodes are still up or down. The <code>pingd</code> daemon can be configured using the pingd configuration file. Nodes which should be pinged may also be configured via loadable modules. See the <code><a href="/docs/linux/man/5-pingd-conf/">pingd.conf</a>(5)</code> manpage for additional information. </p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Output help</p>
<dt><code>-v, &#8211;version</code></p>
<dd>Output version </p>
</dl>
<h2>Clusterlist Modules</h2>
<p>The <code>pingd </code> daemon nodes to ping can also be configured with a clusterlist module. The clusterlist module can obtain a list of all cluster nodes. There are several possible clusterlist formats that can be parsed. By default, the following clusterlist modules are searched for by <code>pingd</code> in the following order: </p>
<p> genders &#8211; Uses a genders database and the genders library to determine all nodes in the cluster. See <a rel="nofollow" href="http://genders.sourceforge.net.">http://genders.sourceforge.net.</a> </p>
<p> hostsfile &#8211; Uses a file that lists the hostname of every node in the cluster on a separate line. The default hostsfile is /etc/hostsfile. </p>
<p> If none of the above are found, nodes must be configured via the pingd configuration file.</p>
<h2>Files</h2>
<p>/etc/pingd.conf </p>
<p> /usr/lib64/pingd</p>
<h2>Origin</h2>
<p>Developed by Albert Chu &lt;chu11 [at] llnl.gov&gt; on LLNL&#8217;s Linux clusters.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-pingd-conf/">pingd.conf</a>(5) </p>
