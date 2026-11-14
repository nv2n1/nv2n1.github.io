---
title: "ether-wake(8)"
name: "ether-wake"
section: "8"
letter: "e"
url: "/docs/linux/man/8-ether-wake/"
description: "ether-wake – A tool to send a Wake-On-LAN \"Magic Packet\""
---

<p>ether-wake &#8211; A tool to send a Wake-On-LAN &quot;Magic Packet&quot;</p>
<h2>Synopsis</h2>
<p><code>ether-wake</code> [<i>options</i>]<i> Host-ID</i></p>
<h2>Description</h2>
<p>This manual page documents the usage of the <code>ether-wake</code> command. </p>
<p> <code>ether-wake</code> is a program that generates and transmits a Wake-On-LAN (WOL) &quot;Magic Packet&quot;, used for restarting machines that have been soft-powered-down (ACPI D3-warm state). It generates the standard AMD Magic Packet format, optionally with a password included. The single required parameter is a station (MAC) address or a host ID that can be translated to a MAC address by an <code><a href="/docs/linux/man/5-ethers/">ethers</a></code>(5) database specified in <code><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></code>(5)</p>
<h2>Options</h2>
<p><code>ether-wake</code> needs a single dash (´-´) in front of options. A summary of options is included below.</p>
<dl>
<dt><code>-b</code></p>
<dd>Send the wake-up packet to the broadcast address.</p>
<dt><code>-D</code></p>
<dd>Increase the Debug Level.</p>
<dt><code>-i ifname</code></p>
<dd>Use interface ifname instead of sending a wake packet to all interfaces.</p>
<dt><code>-p passwd</code></p>
<dd>Append a four or six byte password to the packet. Only a few adapters need or support this. A six byte password may be specified in Ethernet hex format (00:22:44:66:88:aa) or four byte dotted decimal (192.168.1.1) format. A four byte password must use the dotted decimal format. </p>
<dt><code>-V</code></p>
<dd>Show the program version information. </p>
</dl>
<h2>Exit Status</h2>
<p>This program returns 0 on success. A permission failures (e.g. run as a non-root user) results in an exit status of 2. Unrecognized or invalid parameters result in an exit status of 3. Failure to retrieve network interface information or send a packet will result in an exit status of 1.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-arp/">arp</a></code>(8).</p>
<h2>Security</h2>
<p>On some non-Linux systems dropping root capability allows the process to be dumped, traced or debugged. If someone traces this program, they get control of a raw socket. Linux handles this safely, but beware when porting this program.</p>
<h2>Author</h2>
<p>The ether-wake program was written by Donald Becker at Scyld Computing Corporation for use with the Scyld() Beowulf System.</p>
