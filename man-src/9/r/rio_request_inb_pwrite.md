---
title: "rio_request_inb_pwrite(9)"
name: "rio_request_inb_pwrite"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_request_inb_pwrite/"
description: "rio_request_inb_pwrite – request inbound port-write message service for specific RapidIO device"
---

<p>rio_request_inb_pwrite &#8211; request inbound port-write message service for specific RapidIO device</p>
<h2>Synopsis</h2>
<pre><code>int rio_request_inb_pwrite(struct rio_dev *rdev, int (*pwcback)(struct rio_dev *rdev, union rio_pw_msg *msg, int step));</code></pre>
<h2>Arguments</h2>
<p><i>rdev</i></p>
<dl>
<dd>
<dd>RIO device to which register inbound port-write callback routine</dl>
<p> <i>pwcback</i></p>
<dl>
<dd>Callback routine to execute when port-write is received</dl>
<h2>Description</h2>
<p>Binds a port-write callback function to the RapidIO device. Returns 0 if the request has been satisfied.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
