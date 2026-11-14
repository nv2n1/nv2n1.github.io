---
title: "avahi-dnsconfd-action(8)"
name: "avahi-dnsconfd-action"
section: "8"
letter: "a"
url: "/docs/linux/man/8-avahi-dnsconfd-action/"
description: "avahi-dnsconfd.action – avahi-dnsconfd action script"
---

<p>avahi-dnsconfd.action &#8211; avahi-dnsconfd action script</p>
<h2>Synopsis</h2>
<p><code>/etc/avahi/avahi-dnsconfd.action </code></p>
<h2>Description</h2>
<p><i>avahi-dnsconfd.action</i> is the action script that is called whenever a new unicast DNS server is found or removed by avahi-dnsconfd. The default script as shipped with avahi patches <i>/etc/resolv.conf</i> to reflect the changed unicast DNS server configuration.</p>
<h2>Parameters</h2>
<dl>
<dt><code>argv[1]</code> Contains the character &quot;+&quot; if the DNS server is new, &quot;-&quot; when it shall be removed from the DNS server list.</p>
<dd>
<dt><code>argv[2]</code> The IP address of the DNS server.</p>
<dd>
<dt><code>argv[3]</code> Numerical network interface number this DNS server was found on.</p>
<dd>
<dt><code>argv[4]</code> Numerical protocol number this DNS server was found on. (usually 2 for IPv4 and 10 for IPv6)</p>
<dd></dl>
<h2>Environment</h2>
<dl>
<dt><code>AVAHI_INTERFACE</code> Contains the textual interface name the corresponds with argv[3]. (e.g. &quot;eth0&quot;)</p>
<dd>
<dt><code>AVAHI_INTERFACE_DNS_SERVERS</code> Contains a list of all DNS servers that avahi-dnsconfd found on the interface <code>$AVAHI_INTERFACE</code>, separated by spaces.</p>
<dd>
<dt><code>AVAHI_DNS_SERVERS</code> Contains a list of all DNS server that avahi-dnsconfd found on all interfaces, separated by spaces.</p>
<dd></dl>
<h2>Authors</h2>
<p>The Avahi Developers &lt;avahi (at) lists (dot) freedesktop (dot) org&gt;; Avahi is available from <code><a rel="nofollow" href="http://avahi.org/">http://avahi.org/</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-avahi-dnsconfd/">avahi-dnsconfd</a>(8)</code>, <code><a href="/docs/linux/man/8-avahi-daemon/">avahi-daemon</a>(8)</code></p>
<h2>Comments</h2>
<p>This man page was written using <code><a href="/docs/linux/man/1-xml2man/">xml2man</a>(1)</code> by Oliver Kurth.</p>
