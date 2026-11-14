---
title: "rio_device(9)"
name: "rio_device"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_device/"
description: "RIO_DEVICE – macro used to describe a specific RIO device"
---

<p>RIO_DEVICE &#8211; macro used to describe a specific RIO device</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>RIO_DEVICE(</code><i>dev</i><code>, </code><i>ven</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>the 16 bit RIO device ID</dl>
<p> <i>ven</i></p>
<dl>
<dd>the 16 bit RIO vendor ID</dl>
<h2>Description</h2>
<p>This macro is used to create a struct rio_device_id that matches a specific device. The assembly vendor and assembly device fields will be set to <code>RIO_ANY_ID</code>.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
