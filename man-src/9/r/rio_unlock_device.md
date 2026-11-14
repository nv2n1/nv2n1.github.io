---
title: "rio_unlock_device(9)"
name: "rio_unlock_device"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_unlock_device/"
description: "rio_unlock_device – Releases host device lock for specified device"
---

<p>rio_unlock_device &#8211; Releases host device lock for specified device</p>
<h2>Synopsis</h2>
<pre><code>int rio_unlock_device(struct rio_mport *port, u16 destid, u8 hopcount);</code></pre>
<h2>Arguments</h2>
<p><i>port</i></p>
<dl>
<dd>
<dd>Master port to send transaction</dl>
<p> <i>destid</i></p>
<dl>
<dd>Destination ID for device/switch</dl>
<p> <i>hopcount</i></p>
<dl>
<dd>Hopcount to reach switch</dl>
<h2>Description</h2>
<p>Returns 0 if device lock released or EINVAL if fails.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
