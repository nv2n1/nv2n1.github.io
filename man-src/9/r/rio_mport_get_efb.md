---
title: "rio_mport_get_efb(9)"
name: "rio_mport_get_efb"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_mport_get_efb/"
description: "rio_mport_get_efb – get pointer to next extended features block"
---

<p>rio_mport_get_efb &#8211; get pointer to next extended features block</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u32 rio_mport_get_efb(struct rio_mport&nbsp;<wbr>*&nbsp;<wbr></code><i>port</i><code>, int&nbsp;<wbr></code><i>local</i><code>, u16&nbsp;<wbr></code><i>destid</i><code>, u8&nbsp;<wbr></code><i>hopcount</i><code>, u32&nbsp;<wbr></code><i>from</i><code>);</code></dl>
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
<p> <i>from</i></p>
<dl>
<dd>Offset of current Extended Feature block header (if 0 starts from ExtFeaturePtr)</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
