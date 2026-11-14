---
title: "rio_get_device_id(9)"
name: "rio_get_device_id"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_get_device_id/"
description: "rio_get_device_id – Get the base/extended device id for a device"
---

<p>rio_get_device_id &#8211; Get the base/extended device id for a device</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u16 rio_get_device_id(struct rio_mport&nbsp;<wbr>*&nbsp;<wbr></code><i>port</i><code>, u16&nbsp;<wbr></code><i>destid</i><code>, u8&nbsp;<wbr></code><i>hopcount</i><code>);</code></dl>
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
<h2>Description</h2>
<p>Reads the base/extended device id from a device. Returns the 8/16-bit device ID.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
