---
title: "rio_send_doorbell(9)"
name: "rio_send_doorbell"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_send_doorbell/"
description: "rio_send_doorbell – Send a doorbell message to a device"
---

<p>rio_send_doorbell &#8211; Send a doorbell message to a device</p>
<h2>Synopsis</h2>
<pre><code>int rio_send_doorbell(struct rio_dev *rdev, u16 data);</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO device</dl>
<p> <i>data</i></p>
<dl>
<dd>Doorbell message data</dl>
<h2>Description</h2>
<p>Send a doorbell message to a RIO device. The doorbell message has a 16-bit info field provided by the <i>data</i> argument.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
