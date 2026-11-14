---
title: "rio_device_has_destid(9)"
name: "rio_device_has_destid"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_device_has_destid/"
description: "rio_device_has_destid – Test if a device contains a destination ID register"
---

<p>rio_device_has_destid &#8211; Test if a device contains a destination ID register</p>
<h2>Synopsis</h2>
<pre><code>int rio_device_has_destid(struct rio_mport *port, int src_ops, int dst_ops);</code></pre>
<h2>Arguments</h2>
<p><i>port</i></p>
<dl>
<dd>
<dd>Master port to issue transaction</dl>
<p> <i>src_ops</i></p>
<dl>
<dd>RIO device source operations</dl>
<p> <i>dst_ops</i></p>
<dl>
<dd>RIO device destination operations</dl>
<h2>Description</h2>
<p>Checks the provided <i>src_ops</i> and <i>dst_ops</i> for the necessary transaction capabilities that indicate whether or not a device will implement a destination ID register. Returns 1 if true or 0 if false.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
