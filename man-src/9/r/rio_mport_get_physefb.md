---
title: "rio_mport_get_physefb(9)"
name: "rio_mport_get_physefb"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_mport_get_physefb/"
description: "rio_mport_get_physefb – Helper function that returns register offset for Physical Layer Extended Features Block."
---

<p>rio_mport_get_physefb &#8211; Helper function that returns register offset for Physical Layer Extended Features Block.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>u32 rio_mport_get_physefb(struct rio_mport&nbsp;<wbr>*&nbsp;<wbr></code><i>port</i><code>, int&nbsp;<wbr></code><i>local</i><code>, u16&nbsp;<wbr></code><i>destid</i><code>, u8&nbsp;<wbr></code><i>hopcount</i><code>, u32&nbsp;<wbr>*&nbsp;<wbr></code><i>rmap</i><code>);</code></dl>
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
<p> <i>rmap</i></p>
<dl>
<dd>pointer to location to store register map type info</dl>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
