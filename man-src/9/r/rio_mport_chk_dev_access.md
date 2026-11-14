---
title: "rio_mport_chk_dev_access(9)"
name: "rio_mport_chk_dev_access"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_mport_chk_dev_access/"
description: "rio_mport_chk_dev_access – Validate access to the specified device."
---

<p>rio_mport_chk_dev_access &#8211; Validate access to the specified device.</p>
<h2>Synopsis</h2>
<pre><code>int rio_mport_chk_dev_access(struct rio_mport *mport, u16 destid, u8 hopcount);</code></pre>
<h2>Arguments</h2>
<p><i>mport</i></p>
<dl>
<dd>
<dd>Master port to send transactions</dl>
<p> <i>destid</i></p>
<dl>
<dd>Device destination ID in network</dl>
<p> <i>hopcount</i></p>
<dl>
<dd>Number of hops into the network</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
