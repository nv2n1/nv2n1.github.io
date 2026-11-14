---
title: "dhcp_release(1)"
name: "dhcp_release"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dhcp_release/"
description: "dhcp_release – Release a DHCP lease on a the local dnsmasq DHCP server."
---

<h2>NAME</h2>
<p> dhcp_release &#8211; Release a DHCP lease on a the local dnsmasq DHCP server.</p>
<h2>SYNOPSIS</h2>
<p> <code>dhcp_release &lt;interface&gt; &lt;address&gt; &lt;MAC address&gt; &lt;client_id&gt;</code></p>
<h2>DESCRIPTION</h2>
<p> A utility which forces the DHCP server running on this machine to release a DHCP lease. </p>
<p> Send a DHCPRELEASE message via the specified interface to tell the local DHCP server to delete a particular lease. </p>
<p> The interface argument is the interface in which a DHCP request _would_ be received if it was coming from the client, rather than being faked up here.<br />
 The address argument is a dotted-quad IP addresses and mandatory.<br />
 The MAC address is colon separated hex, and is mandatory. It may be prefixed by an address-type byte followed by -, eg </p>
<p> 10-11:22:33:44:55:66 </p>
<p> but if the address-type byte is missing it is assumed to be 1, the type for ethernet. This encoding is the one used in dnsmasq lease files. </p>
<p> The client-id is optional. If it is &quot;*&quot; then it treated as being missing.</p>
<h2>NOTES</h2>
<p> MUST be run as root &#8211; will fail otherwise.</p>
<h2>LIMITATIONS</h2>
<p> Only usable on IPv4 DHCP leases.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-dnsmasq/">dnsmasq</a></code>(8)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Simon Kelley &lt;simon [at] thekelleys.org.uk&gt;. </p>
<h2>Index</h2>
