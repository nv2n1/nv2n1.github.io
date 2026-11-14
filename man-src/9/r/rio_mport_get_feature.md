---
title: "rio_mport_get_feature(9)"
name: "rio_mport_get_feature"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_mport_get_feature/"
description: "rio_mport_get_feature – query for devices’ extended features"
---

<p>rio_mport_get_feature &#8211; query for devices&#8217; extended features</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u32 rio_mport_get_feature(struct rio_mport&nbsp;<wbr>*&nbsp;<wbr></code><i>port</i><code>, int&nbsp;<wbr></code><i>local</i><code>, u16&nbsp;<wbr></code><i>destid</i><code>, u8&nbsp;<wbr></code><i>hopcount</i><code>, int&nbsp;<wbr></code><i>ftr</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>port</i></p>
<dl>
<dd>
<dd>Master port to issue transaction</dl>
<p> <i>local</i></p>
<dl>
<dd>Indicate a local master port or remote device access</dl>
<p> <i>destid</i></p>
<dl>
<dd>Destination ID of the device</dl>
<p> <i>hopcount</i></p>
<dl>
<dd>Number of switch hops to the device</dl>
<p> <i>ftr</i></p>
<dl>
<dd>Extended feature code</dl>
<h2>Description</h2>
<p>Tell if a device supports a given RapidIO capability. Returns the offset of the requested extended feature block within the device&#8217;s RIO configuration space or 0 in case the device does not support it.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
