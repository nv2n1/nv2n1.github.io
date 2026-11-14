---
title: "rio_lock_device(9)"
name: "rio_lock_device"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_lock_device/"
description: "rio_lock_device – Acquires host device lock for specified device"
---

<p>rio_lock_device &#8211; Acquires host device lock for specified device</p>
<h2>Synopsis</h2>
<pre><code>int rio_lock_device(struct rio_mport *port, u16 destid, u8 hopcount, int wait_ms);</code></pre>
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
<p> <i>wait_ms</i></p>
<dl>
<dd>Max wait time in msec (0 = no timeout)</dl>
<h2>Description</h2>
<p>Attepts to acquire host device lock for specified device Returns 0 if device lock acquired or EINVAL if timeout expires.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
