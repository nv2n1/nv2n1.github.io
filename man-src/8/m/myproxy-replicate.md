---
title: "myproxy-replicate(8)"
name: "myproxy-replicate"
section: "8"
letter: "m"
url: "/docs/linux/man/8-myproxy-replicate/"
description: "myproxy-replicate – Stores data from the MyProxy master repository to all the slave servers."
---

<p><code>myproxy-replicate</code> &#8211; Stores data from the MyProxy master repository to all the slave servers.</p>
<h2>Synopsis</h2>
<p><code>myproxy-replicate</code> [options] &#8230; </p>
<pre> Options:
 [-verbose|-v] Print copious output
 [-help|-h] Print usage
 [-storage|-r]=&lt;path to repository&gt; Directory of the MyProxy repository.
 [-config|-c]=&lt;path to config file&gt; Directory of the MyProxy Server
 configuration file.
 [-debug|-d] Run in debug mode</pre>
<h2>Description</h2>
<p><code>myproxy-replicate</code> Replicates data. </p>
<p> This utility will read a specified MyProxy repository and send any new or changed data to a slave MyProxy server. The slave servers are specified in the <a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a><code>(5)</code> file. </p>
<p> This utility will need to run at some specified interval in order to keep the slave repositories semi current with the Master repository. This can best be accomplished using cron, or some similar mechanism.</p>
<h2>Options</h2>
<dl>
<dt><code>-v</code>, <code>-verbose</code></p>
<dd>Enables verbose debugging output to the terminal.</p>
<dt><code>-h</code>, <code>-help</code></p>
<dd>Displays command usage text and exits.</p>
<dt><code>-u</code>, <code>-usage</code></p>
<dd>Displays command usage text and exits.</p>
<dt><code>-r</code> <i>dir</i>, <code>-storage</code> <i>dir</i></p>
<dd>Specifies the location of the credential storage directory. The directory must be accessible only by the user running the <code>myproxy-server</code> process for security reasons. Default: /var/lib/myproxy or /var/myproxy or <tt>$GLOBUS_LOCATION</tt>/var/myproxyA</p>
<dt><code>-c</code> <i>file</i>, <code>-config</code> <i>file</i></p>
<dd>Specifies the location of the myproxy-server configuration file. Default: /etc/myproxy-server.config or<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><tt>$GLOBUS_LOCA</tt>-TION/etc/myproxy-server.config</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-myproxy-init/">myproxy-init</a></i>(1) <i><a href="/docs/linux/man/1-myproxy-store/">myproxy-store</a></i>(1) <i><a href="/docs/linux/man/1-myproxy-retrieve/">myproxy-retrieve</a></i>(1) <i><a href="/docs/linux/man/1-myproxy-delegate/">myproxy-delegate</a></i>(1) <i><a href="/docs/linux/man/8-myproxy-server/">myproxy-server</a></i>(8) <i><a href="/docs/linux/man/5-myproxy-server-config/">myproxy-server.config</a></i>(5)</p>
<h2>Author</h2>
