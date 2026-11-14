---
title: "dhcp_lease_time(1)"
name: "dhcp_lease_time"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dhcp_lease_time/"
description: "dhcp_lease_time – Query remaining time of a lease on a the local dnsmasq DHCP server."
---

<h2>NAME</h2>
<p> dhcp_lease_time &#8211; Query remaining time of a lease on a the local dnsmasq DHCP server.</p>
<h2>SYNOPSIS</h2>
<p> <code>dhcp_lease_time &lt;address&gt;</code></p>
<h2>DESCRIPTION</h2>
<p> Send a DHCPINFORM message to a dnsmasq server running on the local host and print (to stdout) the time remaining in any lease for the given address. The time is given as string printed to stdout. </p>
<p> If an error occurs or no lease exists for the given address, nothing is sent to stdout a message is sent to stderr and a non-zero error code is returned. </p>
<p> Requires dnsmasq 2.66 or later and may not work with other DHCP servers. </p>
<p> The address argument is a dotted-quad IP addresses and mandatory.</p>
<h2>LIMITATIONS</h2>
<p> Only works with IPv4 addresses and DHCP leases.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-dnsmasq/">dnsmasq</a></code>(8)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Simon Kelley &lt;simon [at] thekelleys.org.uk&gt;. </p>
<h2>Index</h2>
