---
title: "corosync-cfgtool(8)"
name: "corosync-cfgtool"
section: "8"
letter: "c"
url: "/docs/linux/man/8-corosync-cfgtool/"
description: "corosync-cfgtool – An administrative tool for corosync."
---

<p>corosync-cfgtool &#8211; An administrative tool for corosync.</p>
<h2>Synopsis</h2>
<p><code>corosync-cfgtool [-i] [IP_address] [-s] [-r] [-l] [-u] [-H] [service_name] [-v] [version] [-k] [nodeid] [-a] [nodeid]</code></p>
<h2>Description</h2>
<p><code>corosync-cfgtool</code> A tool for displaying and configuring active parameters within corosync.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Print basic usage.</p>
<dt><code>-i</code></p>
<dd>Finds only information about the specified interface IP address.</p>
<dt><code>-s</code></p>
<dd>Displays the status of the current rings on this node. If any interfaces are faulty, 1 is returned by the binary. If all interfaces are active 0 is returned to the shell.</p>
<dt><code>-r</code></p>
<dd>Reset redundant ring state cluster wide after a fault to re-enable redundant ring operation.</p>
<dt><code>-l</code></p>
<dd>Load a service identified by &quot;service_name&quot;.</p>
<dt><code>-u</code></p>
<dd>Unload a service identified by &quot;service_name&quot;.</p>
<dt><code>-a</code></p>
<dd>Display the IP address(es) of a node.</p>
<dt><code>-k</code></p>
<dd>Kill a node identified by node id.</p>
<dt><code>-R</code></p>
<dd>Tell all instances of corosync in this cluster to reload corosync.conf</p>
<dt><code>-H</code></p>
<dd>Shutdown corosync cleanly on this node.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync_overview/">corosync_overview</a></code>(8),</p>
<h2>Author</h2>
<p>Angus Salkeld</p>
