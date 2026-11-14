---
title: "rio_local_get_device_id(9)"
name: "rio_local_get_device_id"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_local_get_device_id/"
description: "rio_local_get_device_id – Get the base/extended device id for a port"
---

<p>rio_local_get_device_id &#8211; Get the base/extended device id for a port</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u16 rio_local_get_device_id(struct rio_mport&nbsp;<wbr>*&nbsp;<wbr></code><i>port</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>port</i></p>
<dl>
<dd>
<dd>RIO master port from which to get the deviceid</dl>
<h2>Description</h2>
<p>Reads the base/extended device id from the local device implementing the master port. Returns the 8/16-bit device id.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
