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
<dt><code>-h</code></dt>
<dd>Print basic usage.</dd>
<dt><code>-i</code></dt>
<dd>Finds only information about the specified interface IP address.</dd>
<dt><code>-s</code></dt>
<dd>Displays the status of the current rings on this node. If any interfaces are faulty, 1 is returned by the binary. If all interfaces are active 0 is returned to the shell.</dd>
<dt><code>-r</code></dt>
<dd>Reset redundant ring state cluster wide after a fault to re-enable redundant ring operation.</dd>
<dt><code>-l</code></dt>
<dd>Load a service identified by &quot;service_name&quot;.</dd>
<dt><code>-u</code></dt>
<dd>Unload a service identified by &quot;service_name&quot;.</dd>
<dt><code>-a</code></dt>
<dd>Display the IP address(es) of a node.</dd>
<dt><code>-k</code></dt>
<dd>Kill a node identified by node id.</dd>
<dt><code>-R</code></dt>
<dd>Tell all instances of corosync in this cluster to reload corosync.conf</dd>
<dt><code>-H</code></dt>
<dd>Shutdown corosync cleanly on this node.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-corosync_overview/">corosync_overview</a></code>(8),</p>
<h2>Author</h2>
<p>Angus Salkeld</p>
