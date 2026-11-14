---
title: "traceroute6-iputils(8)"
name: "traceroute6-iputils"
section: "8"
letter: "t"
url: "/docs/linux/man/8-traceroute6-iputils/"
description: "traceroute6 – traces path to a network host"
---

<p>traceroute6 &#8211; traces path to a network host</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>traceroute6</code> [<code>-dnrvV</code>] [<code>-i&nbsp;</code><i>interface</i>] [<code>-m&nbsp;</code><i>max_ttl</i>] [<code>-p&nbsp;</code><i>port</i>] [<code>-q&nbsp;</code><i>max_probes</i>] [<code>-s&nbsp;</code><i>source</i>] [<code>-w&nbsp;</code><i>wait time</i>] {destination} [size]</dl>
<h2>Description</h2>
<dd>Description can be found in <code><a href="/docs/linux/man/8-traceroute/">traceroute</a></code>(8), all the references to IP replaced to IPv6. It is needless to copy the description from there.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-traceroute/">traceroute</a></code>(8), <code><a href="/docs/linux/man/8-tracepath/">tracepath</a></code>(8), <code><a href="/docs/linux/man/8-ping/">ping</a></code>(8).</p>
<h2>History</h2>
<p>This program has long history. Author of <code>traceroute</code> is Van Jacobson and it first appeared in 1988. This clone is based on a port of <code>traceroute</code> to IPv6 published in NRL IPv6 distribution in 1996. In turn, it was ported to Linux by Pedro Roque. After this it was kept in sync by Alexey Kuznetsov &lt;kuznet [at] ms2.inr.ac.ru&gt;. And eventually entered <code>iputils</code> package.</p>
<h2>Security</h2>
<p><code>traceroute6</code> requires CAP_NET_RAW capability to be executed. It is safe to be used as set-uid root.</p>
<h2>Availability</h2>
<p><code>traceroute6</code> is part of <i>iputils</i> package.</p>
