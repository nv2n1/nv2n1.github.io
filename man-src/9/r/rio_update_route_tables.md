---
title: "rio_update_route_tables(9)"
name: "rio_update_route_tables"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_update_route_tables/"
description: "rio_update_route_tables – Updates route tables in switches"
---

<p>rio_update_route_tables &#8211; Updates route tables in switches</p>
<h2>Synopsis</h2>
<pre><code>void rio_update_route_tables(struct rio_net *net);</code></pre>
<h2>Arguments</h2>
<p><i>net</i></p>
<dl>
<dd>
<dd>RIO network to run update on</dl>
<h2>Description</h2>
<p>For each enumerated device, ensure that each switch in a system has correct routing entries. Add routes for devices that where unknown dirung the first enumeration pass through the switch.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
