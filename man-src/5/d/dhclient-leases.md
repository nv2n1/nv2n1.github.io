---
title: "dhclient-leases(5)"
name: "dhclient-leases"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dhclient-leases/"
description: "dhclient.leases – DHCP client lease database"
---

<p>dhclient.leases &#8211; DHCP client lease database</p>
<h2>Description</h2>
<p>The Internet Systems Consortium DHCP client keeps a persistent database of leases that it has acquired that are still valid. The database is a free-form ASCII file containing one valid declaration per lease. If more than one declaration appears for a given lease, the last one in the file is used. The file is written as a log, so this is not an unusual occurrence. </p>
<p> The format of the lease declarations is described in <code><a href="/docs/linux/man/5-dhclient-conf/">dhclient.conf</a>(5).</code></p>
<h2>Files</h2>
<p><code>/var/lib/dhcp/dhclient.leases</code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-dhclient/">dhclient</a>(8), <a href="/docs/linux/man/5-dhcp-options/">dhcp-options</a>(5), <a href="/docs/linux/man/5-dhclient-conf/">dhclient.conf</a>(5), <a href="/docs/linux/man/8-dhcpd/">dhcpd</a>(8), <a href="/docs/linux/man/5-dhcpd-conf/">dhcpd.conf</a>(5), RFC2132, RFC2131.</p>
<h2>Author</h2>
<p><code><a href="/docs/linux/man/8-dhclient/">dhclient</a>(8)</code> Information about Internet Systems Consortium can be found at <code><a rel="nofollow" href="https://www.isc.org.">https://www.isc.org.</a></code></p>
