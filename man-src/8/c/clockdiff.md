---
title: "clockdiff(8)"
name: "clockdiff"
section: "8"
letter: "c"
url: "/docs/linux/man/8-clockdiff/"
description: "clockdiff – measure clock difference between hosts"
---

<p>clockdiff &#8211; measure clock difference between hosts</p>
<h2>Synopsis</h2>
<p><code>clockdiff</code> [<code>-o</code>] [<code>-o1</code>] <i>destination</i> </p>
<h2>Description</h2>
<p><code>clockdiff</code> Measures clock difference between us and <i>destination</i> with 1 msec resolution using ICMP TIMESTAMP [2] packets or, optionally, IP TIMESTAMP option [3] option added to ICMP ECHO. [1]</p>
<h2>Options</h2>
<dl>
<dt><code>-o</code></p>
<dd>Use IP TIMESTAMP with ICMP ECHO instead of ICMP TIMESTAMP messages. It is useful with some destinations, which do not support ICMP TIMESTAMP (f.e. Solaris &lt;2.4).</p>
<dt><code>-o1</code></p>
<dd>Slightly different form of <code>-o</code>, namely it uses three-term IP TIMESTAMP with prespecified hop addresses instead of four term one. What flavor works better depends on target host. Particularly, <code>-o</code> is better for Linux.</dl>
<h2>Warnings</h2>
<dl>
<dt>&bull;</p>
<dd>Some nodes (Cisco) use non-standard timestamps, which is allowed by RFC, but makes timestamps mostly useless.</p>
<dt>&bull;</p>
<dd>Some nodes generate messed timestamps (Solaris&gt;2.4), when run <code>xntpd</code>. Seems, its IP stack uses a corrupted clock source, which is synchronized to time-of-day clock periodically and jumps randomly making timestamps mostly useless. Good news is that you can use NTP in this case, which is even better.</p>
<dt>&bull;</p>
<dd><code>clockdiff</code> shows difference in time modulo 24 days.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ping/">ping</a></code>(8), <code><a href="/docs/linux/man/8-arping/">arping</a></code>(8), <code><a href="/docs/linux/man/8-tracepath/">tracepath</a></code>(8).</p>
<h2>References</h2>
<p>[1] ICMP ECHO, RFC0792, page 14. </p>
<p> [2] ICMP TIMESTAMP, RFC0792, page 16. </p>
<p> [3] IP TIMESTAMP option, RFC0791, 3.1, page 16.</p>
<h2>Author</h2>
<p><code>clockdiff</code> was compiled by Alexey Kuznetsov &lt;kuznet [at] ms2.inr.ac.ru&gt;. It was based on code borrowed from BSD <code>timed</code> daemon. It is now maintained by YOSHIFUJI Hideaki &lt;yoshfuji [at] skbuff.net&gt;.</p>
<h2>Security</h2>
<p><code>clockdiff</code> requires CAP_NET_RAW capability to be executed. It is safe to be used as set-uid root.</p>
<h2>Availability</h2>
<p><code>clockdiff</code> is part of <i>iputils</i> package and the latest versions are available in source form at <a rel="nofollow" href="http://www.skbuff.net/iputils/iputils-current.tar.bz2.">http://www.skbuff.net/iputils/iputils-current.tar.bz2.</a></p>
