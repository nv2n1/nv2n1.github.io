---
title: "rio_enum_peer(9)"
name: "rio_enum_peer"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_enum_peer/"
description: "rio_enum_peer – Recursively enumerate a RIO network through a master port"
---

<p>rio_enum_peer &#8211; Recursively enumerate a RIO network through a master port</p>
<h2>Synopsis</h2>
<pre><code>int rio_enum_peer(struct rio_net *net, struct rio_mport *port, u8 hopcount, struct rio_dev *prev, int prev_port);</code></pre>
<h2>Arguments</h2>
<p><i>net</i></p>
<dl>
<dd>
<dd>RIO network being enumerated</dl>
<p> <i>port</i></p>
<dl>
<dd>Master port to send transactions</dl>
<p> <i>hopcount</i></p>
<dl>
<dd>Number of hops into the network</dl>
<p> <i>prev</i></p>
<dl>
<dd>Previous RIO device connected to the enumerated one</dl>
<p> <i>prev_port</i></p>
<dl>
<dd>Port on previous RIO device</dl>
<h2>Description</h2>
<p>Recursively enumerates a RIO network. Transactions are sent via the master port passed in <i>port</i>.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
