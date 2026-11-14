---
title: "esi(8)"
name: "esi"
section: "8"
letter: "e"
url: "/docs/linux/man/8-esi/"
description: "esi – get or set the end system identifier (ESI)"
---

<p>esi &#8211; get or set the end system identifier (ESI)</p>
<h2>Synopsis</h2>
<p><code>esi </code> [<i>itf</i>]<br />
 <code>esi</code> [<code>-f</code>]&nbsp;<wbr><i>esi</i>&nbsp;<wbr>[<i>itf</i>]<br />
 <code>esi</code> <code>-V</code></p>
<h2>Description</h2>
<p><code>esi</code> is used to show or set the end system identifier (ESI, a unique six-byte number corresponding to the MAC address of LAN technologies like Ethernet) of an ATM interface. If the interface number <i>itf</i> is omitted, interface 0 is used by default. The <i>esi</i> argument is a string of twelve hex digits. </p>
<p> Only the ESI stored in the kernel is accessed; <code>esi</code> does not change the ESI stored on the NIC. If a non-zero ESI is already set on an interface, the <code>-f</code> option has to be used to overwrite it. </p>
<p> Note that ESI changes are not automatically propagated throughout the system, e.g. to <code>ilmid</code>. <code>esi</code> should therefore be used early during system initialization.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>force overwriting an existing ESI.</p>
<dt><code>-V</code></p>
<dd>print version number of <code>esi</code> on standard output and exit.</dl>
<h2>Author</h2>
<p>Werner Almesberger, EPFL ICA &lt;Werner.Almesberger [at] epfl.ch&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-ilmid/">ilmid</a>(8) </p>
