---
title: "rio_register_scan(9)"
name: "rio_register_scan"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_register_scan/"
description: "rio_register_scan – enumeration/discovery method registration interface"
---

<p>rio_register_scan &#8211; enumeration/discovery method registration interface</p>
<h2>Synopsis</h2>
<pre><code>int rio_register_scan(int mport_id, struct rio_scan *scan_ops);</code></pre>
<h2>Arguments</h2>
<p><i>mport_id</i></p>
<dl>
<dd>
<dd>mport device ID for which fabric scan routine has to be set (RIO_MPORT_ANY = set for all available mports)</dl>
<p> <i>scan_ops</i></p>
<dl>
<dd>enumeration/discovery operations structure</dl>
<h2>Description</h2>
<p>Registers enumeration/discovery operations with RapidIO subsystem and attaches it to the specified mport device (or all available mports if RIO_MPORT_ANY is specified). </p>
<p> Returns error if the mport already has an enumerator attached to it. In case of RIO_MPORT_ANY skips mports with valid scan routines (no error).</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
