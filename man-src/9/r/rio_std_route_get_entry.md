---
title: "rio_std_route_get_entry(9)"
name: "rio_std_route_get_entry"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_std_route_get_entry/"
description: "rio_std_route_get_entry – Read switch route table entry (port number) associated with specified destID using standard registers defined in RIO specification rev.1.3"
---

<p>rio_std_route_get_entry &#8211; Read switch route table entry (port number) associated with specified destID using standard registers defined in RIO specification rev.1.3</p>
<h2>Synopsis</h2>
<pre><code>int rio_std_route_get_entry(struct rio_mport *mport, u16 destid, u8 hopcount, u16 table, u16 route_destid, u8 *route_port);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>Master port to issue transaction</dl>
<p> <i>destid</i></p>
<dl>
<dd>Destination ID of the device</dl>
<p> <i>hopcount</i></p>
<dl>
<dd>Number of switch hops to the device</dl>
<p> <i>table</i></p>
<dl>
<dd>routing table ID (global or port-specific)</dl>
<p> <i>route_destid</i></p>
<dl>
<dd>destID entry in the RT</dl>
<p> <i>route_port</i></p>
<dl>
<dd>returned destination port for specified destID</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
