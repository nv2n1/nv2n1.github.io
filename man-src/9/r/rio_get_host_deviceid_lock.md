---
title: "rio_get_host_deviceid_lock(9)"
name: "rio_get_host_deviceid_lock"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_get_host_deviceid_lock/"
description: "rio_get_host_deviceid_lock – Reads the Host Device ID Lock CSR on a device"
---

<p>rio_get_host_deviceid_lock &#8211; Reads the Host Device ID Lock CSR on a device</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u16 rio_get_host_deviceid_lock(struct rio_mport&nbsp;<wbr>*&nbsp;<wbr></code><i>port</i><code>, u8&nbsp;<wbr></code><i>hopcount</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>port</i></p>
<dl>
<dd>
<dd>Master port to send transaction</dl>
<p> <i>hopcount</i></p>
<dl>
<dd>Number of hops to the device</dl>
<h2>Description</h2>
<p>Used during enumeration to read the Host Device ID Lock CSR on a RIO device. Returns the value of the lock register.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
