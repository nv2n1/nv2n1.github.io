---
title: "rio_route_get_entry(9)"
name: "rio_route_get_entry"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_route_get_entry/"
description: "rio_route_get_entry – Read an entry from a switch routing table"
---

<p>rio_route_get_entry &#8211; Read an entry from a switch routing table</p>
<h2>Synopsis</h2>
<pre><code>int rio_route_get_entry(struct rio_dev *rdev, u16 table, u16 route_destid, u8 *route_port, int lock);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO device</dl>
<p> <i>table</i></p>
<dl>
<dd>Routing table ID</dl>
<p> <i>route_destid</i></p>
<dl>
<dd>Destination ID to be routed</dl>
<p> <i>route_port</i></p>
<dl>
<dd>Pointer to read port number into</dl>
<p> <i>lock</i></p>
<dl>
<dd>apply a hardware lock on switch device flag (1=lock, 0=no_lock)</dl>
<h2>Description</h2>
<p>If available calls the switch specific <code>get_entry</code> method to fetch a route entry from a switch routing table. Otherwise uses standard RT read method as defined by RapidIO specification. A specific routing table can be selected using the <i>table</i> argument if a switch has per port routing tables or the standard (or global) table may be used by passing <code>RIO_GLOBAL_TABLE</code> in <i>table</i>. </p>
<p> Returns <code>0</code> on success or <code>-EINVAL</code> on failure.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
