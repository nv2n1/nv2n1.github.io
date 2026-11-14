---
title: "ifcfg(8)"
name: "ifcfg"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ifcfg/"
description: "ifcfg – simplistic script which replaces ifconfig IP management"
---

<p>ifcfg &#8211; simplistic script which replaces ifconfig IP management</p>
<h2>Synopsis</h2>
<p><code>ifcfg</code> [ <i>DEVICE</i> ] [ <i>command</i> ] <i>ADDRESS</i> [ <i>PEER</i> ] </p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>ifcfg</code> command. This is a simplistic script replacing one option of <code>ifconfig</code> , namely, IP address management. It not only adds addresses, but also carries out Duplicate Address Detection RFC-DHCP, sends unsolicited ARP to update the caches of other hosts sharing the interface, adds some control routes and restarts Router Discovery when it is necessary. </p>
<h2>Ifconfig &#8211; Command Syntax</h2>
<h3>
<dt><code>DEVICE</code></p>
<dd></h3>
<p>&#8211; it may have alias, suffix, separated by colon. </p>
<dt><code>command</code></p>
<dd>&#8211; add, delete or stop. </p>
<dt><code>ADDRESS</code></p>
<dd>&#8211; optionally followed by prefix length. </p>
<dt><code>peer</code></p>
<dd>&#8211; optional peer address for pointpoint interfaces. </p>
</dl>
<h2>Notes</h2>
<p>This script is not suitable for use with IPv6. </p>
<h2>See Also</h2>
<p>IP Command reference <code>ip-cref.ps</code> </p>
