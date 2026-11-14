---
title: "rio_release_inb_pwrite(9)"
name: "rio_release_inb_pwrite"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_release_inb_pwrite/"
description: "rio_release_inb_pwrite – release inbound port-write message service associated with specific RapidIO device"
---

<p>rio_release_inb_pwrite &#8211; release inbound port-write message service associated with specific RapidIO device</p>
<h2>Synopsis</h2>
<pre><code>int rio_release_inb_pwrite(struct rio_dev *rdev);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO device which registered for inbound port-write callback</dl>
<h2>Description</h2>
<p>Removes callback from the rio_dev structure. Returns 0 if the request has been satisfied.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
