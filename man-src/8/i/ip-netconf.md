---
title: "ip-netconf(8)"
name: "ip-netconf"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-netconf/"
description: "ip-netconf – network configuration monitoring"
---

<p>ip-netconf &#8211; network configuration monitoring</p>
<h2>Synopsis</h2>
<p><code>ip </code> [ ip-OPTIONS ] <code>netconf show</code> [ <code>dev</code> <i>NAME</i> ] </p>
<h2>Description</h2>
<p>The <code>ip netconf</code> utility can monitor IPv4 and IPv6 parameters (see <code>/proc/sys/net/ipv[4|6]/conf/[all|DEV]/</code>) like forwarding, rp_filter, proxy_neigh, ignore_routes_with_linkdown or mc_forwarding status. If no interface is specified, the entry <code>all</code> is displayed.</p>
<h3>ip netconf show &#8211; display network parameters</h3>
<dl>
<dt><code>dev</code><i> NAME</i></p>
<dd>the name of the device to display network parameters for. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) </p>
<h2>Author</h2>
<p>Original Manpage by Nicolas Dichtel &lt;nicolas.dichtel [at] 6wind.com&gt;</p>
