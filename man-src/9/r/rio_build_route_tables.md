---
title: "rio_build_route_tables(9)"
name: "rio_build_route_tables"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_build_route_tables/"
description: "rio_build_route_tables – Generate route tables from switch route entries"
---

<p>rio_build_route_tables &#8211; Generate route tables from switch route entries</p>
<h2>Synopsis</h2>
<pre><code>void rio_build_route_tables(struct rio_net *net);</code></pre>
<h2>Arguments</h2>
<p><i>net</i></p>
<dl>
<dd>
<dd>RIO network to run route tables scan on</dl>
<h2>Description</h2>
<p>For each switch device, generate a route table by copying existing route entries from the switch.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
