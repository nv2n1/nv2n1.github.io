---
title: "rio_unregister_scan(9)"
name: "rio_unregister_scan"
section: "9"
letter: "r"
url: "/docs/linux/man/9-rio_unregister_scan/"
description: "rio_unregister_scan – removes enumeration/discovery method from mport"
---

<p>rio_unregister_scan &#8211; removes enumeration/discovery method from mport</p>
<h2>Synopsis</h2>
<pre><code>int rio_unregister_scan(int mport_id, struct rio_scan *scan_ops);</code></pre>
<h2>Arguments</h2>
<p><i>mport_id</i></p>
<dl>
<dd>
<dd>mport device ID for which fabric scan routine has to be unregistered (RIO_MPORT_ANY = apply to all mports that use the specified scan_ops)</dl>
<p> <i>scan_ops</i></p>
<dl>
<dd>enumeration/discovery operations structure</dl>
<h2>Description</h2>
<p>Removes enumeration or discovery method assigned to the specified mport device. If RIO_MPORT_ANY is specified, removes the specified operations from all mports that have them attached.</p>
<h2>Author</h2>
<p><code>Matt Porter</code> &lt;mporter [at] kernel.crashing.org&gt;, &lt;mporter [at] mvista.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
