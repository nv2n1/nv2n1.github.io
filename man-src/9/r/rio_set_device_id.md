---
title: "rio_set_device_id(9)"
name: "rio_set_device_id"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_set_device_id/"
description: "rio_set_device_id – Set the base/extended device id for a device"
---

<p>rio_set_device_id &#8211; Set the base/extended device id for a device</p>
<h2>Synopsis</h2>
<pre><code>void rio_set_device_id(struct rio_mport *port, u16 destid, u8 hopcount, u16 did);</code></pre>
<h2>Arguments</h2>
<p><i>port</i></p>
<dl>
<dd>
<dd>RIO master port</dl>
<p> <i>destid</i></p>
<dl>
<dd>Destination ID of device</dl>
<p> <i>hopcount</i></p>
<dl>
<dd>Hopcount to device</dl>
<p> <i>did</i></p>
<dl>
<dd>Device ID value to be written</dl>
<h2>Description</h2>
<p>Writes the base/extended device id from a device.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
