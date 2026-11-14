---
title: "ifenslave(8)"
name: "ifenslave"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ifenslave/"
description: "ifenslave – Attach and detach slave network devices to a bonding device."
---

<p><code>ifenslave</code> &#8211; Attach and detach slave network devices to a bonding device.</p>
<h2>Synopsis</h2>
<p>[-<code>acdfhuvV</code> ] [-<code>-all-interfaces</code> ] [-<code>-change-active</code> ] [-<code>-detach</code> ] [-<code>-force</code> ] [-<code>-help</code> ] [-<code>-usage</code> ] [-<code>-verbose</code> ] [-<code>-version</code> ] <i>master</i> <i>slave</i> <code>&#8230;</code></p>
<h2>Description</h2>
<p>is a tool to attach and detach slave network devices to a bonding device. A bonding device will act like a normal Ethernet network device to the kernel, but will send out the packets via the slave devices using a simple round-robin scheduler. This allows for simple load-balancing, identical to &quot;channel bonding&quot; or &quot;trunking&quot; techniques used in switches. </p>
<p> The kernel must have support for bonding devices for to be useful.</p>
<h2>Options</h2>
<dl>
<dt><code>-a, -all-interfaces</code></p>
<dd>Show information about all interfaces.</p>
<dt><code>-c, -change-active</code></p>
<dd>Change active slave.</p>
<dt><code>-d, -detach</code></p>
<dd>Removes slave interfaces from the bonding device.</p>
<dt><code>-f, -force</code></p>
<dd>Force actions to be taken if one of the specified interfaces appears not to belong to an Ethernet device.</p>
<dt><code>-h, -help</code></p>
<dd>Display a help message and exit.</p>
<dt><code>-u, -usage</code></p>
<dd>Show usage information and exit.</p>
<dt><code>-v, -verbose</code></p>
<dd>Print warning and debug messages.</p>
<dt><code>-V, -version</code></p>
<dd>Show version information and exit.</dl>
<p> If not options are given, the default action will be to enslave interfaces.</p>
<h2>Example</h2>
<p>The following example shows how to setup a bonding device and enslave two real Ethernet devices to it: </p>
<pre># modprobe bonding
# ifconfig bond0 192.168.0.1 netmask 255.255.0.0
# ifenslave bond0 eth0 eth1</pre>
<h2>Author</h2>
<p>was originally written by An Donald Becker Aq becker [at] cesdis.gsfc.nasa.gov , and has since been updated by various kernel developers. </p>
<p> This manual page was written by An Guus Sliepen Aq guus [at] debian.org for the Debian GNU/Linux system.</p>
