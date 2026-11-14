---
title: "avahi-autoipd-action(8)"
name: "avahi-autoipd-action"
section: "8"
letter: "a"
url: "/docs/linux/man/8-avahi-autoipd-action/"
description: "avahi-autoipd.action – avahi-autoipd action script"
---

<p>avahi-autoipd.action &#8211; avahi-autoipd action script</p>
<h2>Synopsis</h2>
<p><code>/etc/avahi/avahi-autoipd.action </code></p>
<h2>Description</h2>
<p><i>avahi-autoipd.action</i> is the action script that is called whenever an IP address has been acquired by avahi-autoipd or when it detected an IP address conflict. The script should add or remove the specified address from the specified network interface.</p>
<h2>Parameters</h2>
<dl>
<dt><code>argv[1]</code> An event string: one of BIND, CONFLICT, UNBIND or STOP. If BIND is passed an IP address has been successfully acquired and the script shall add it to the network interface. If CONFLICT is passed avahi-autopid detected a IP address on the local network, the action script should remove the configured IP address. If UNBIND is passed the IP address should be removed from the interface, too, because a routable address has been configured to the interface by some other program. If STOP is passed the avahi-autoipd is being shutdown and the action script should remove the IP address. In short: on BIND the address should be added to the interface, on CONFLICT, UNBIND or STOP it should be removed.</p>
<dd>
<dt><code>argv[2]</code> The network interface name.</p>
<dd>
<dt><code>argv[3]</code> An IP address from the IPv4LL range.</p>
<dd></dl>
<h2>Authors</h2>
<p>The Avahi Developers &lt;avahi (at) lists (dot) freedesktop (dot) org&gt;; Avahi is available from <code><a rel="nofollow" href="http://avahi.org/">http://avahi.org/</a></code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-avahi-autoipd/">avahi-autoipd</a>(8)</code>, <code><a href="/docs/linux/man/8-dhclient-script/">dhclient-script</a>(8)</code>, <code><a href="/docs/linux/man/8-ip/">ip</a>(8)</code>, <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a>(8)</code></p>
<h2>Comments</h2>
<p>This man page was written using <code><a href="/docs/linux/man/1-xml2man/">xml2man</a>(1)</code> by Oliver Kurth.</p>
