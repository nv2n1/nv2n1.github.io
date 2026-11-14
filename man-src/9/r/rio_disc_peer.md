---
title: "rio_disc_peer(9)"
name: "rio_disc_peer"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_disc_peer/"
description: "rio_disc_peer – Recursively discovers a RIO network through a master port"
---

<p>rio_disc_peer &#8211; Recursively discovers a RIO network through a master port</p>
<h2>Synopsis</h2>
<pre><code>int rio_disc_peer(struct rio_net *net, struct rio_mport *port, u16 destid, u8 hopcount, struct rio_dev *prev, int prev_port);</code></pre>
<h2>Arguments</h2>
<p><i>net</i></p>
<dl>
<dd>
<dd>RIO network being discovered</dl>
<p> <i>port</i></p>
<dl>
<dd>Master port to send transactions</dl>
<p> <i>destid</i></p>
<dl>
<dd>Current destination ID in network</dl>
<p> <i>hopcount</i></p>
<dl>
<dd>Number of hops into the network</dl>
<p> <i>prev</i></p>
<dl>
<dd>previous rio_dev</dl>
<p> <i>prev_port</i></p>
<dl>
<dd>previous port number</dl>
<h2>Description</h2>
<p>Recursively discovers a RIO network. Transactions are sent via the master port passed in <i>port</i>.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
