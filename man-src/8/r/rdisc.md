---
title: "rdisc(8)"
name: "rdisc"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rdisc/"
description: "rdisc – network router discovery daemon"
---

<p>rdisc &#8211; network router discovery daemon</p>
<h2>Synopsis</h2>
<p><code>rdisc</code> [<code>-abdfrstvV</code>] [<code>-p </code><i>preference</i>] [<code>-T </code><i>max_interval</i>] [<i>send_address</i>] [<i>receive_address</i>] </p>
<h2>Description</h2>
<p><code>rdisc</code> implements client side of the ICMP router discover protocol. <code>rdisc</code> is invoked at boot time to populate the network routing tables with default routes. </p>
<p> <code>rdisc</code> listens on the ALL_HOSTS (224.0.0.1) multicast address (or <i>receive_address</i> provided it is given) for ROUTER_ADVERTISE messages from routers. The received messages are handled by first ignoring those listed router addresses with which the host does not share a network. Among the remaining addresses the ones with the highest preference are selected as default routers and a default route is entered in the kernel routing table for each one of them. </p>
<p> Optionally, <code>rdisc</code> can avoid waiting for routers to announce themselves by sending out a few ROUTER_SOLICITATION messages to the ALL_ROUTERS (224.0.0.2) multicast address (or <i>send_address</i> provided it is given) when it is started. </p>
<p> A timer is associated with each router address and the address will no longer be considered for inclusion in the the routing tables if the timer expires before a new <code>advertise</code> message is received from the router. The address will also be excluded from consideration if the host receives an <code>advertise</code> message with the preference being maximally negative. </p>
<p> Server side of router discovery protocol is supported by Cisco IOS and by any more or less complete UNIX routing daemon, f.e <code>gated</code>. Or, <code>rdisc</code> can act as responder, if compiled with -DRDISC_SERVER.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code></p>
<dd>Accept all routers independently of the preference they have in their <code>advertise</code> messages. Normally <code>rdisc</code> only accepts (and enters in the kernel routing tables) the router or routers with the highest preference.</p>
<dt><code>-b</code></p>
<dd>Opposite to <code>-a</code>, i.e. install only router with the best preference value. It is default behaviour.</p>
<dt><code>-d</code></p>
<dd>Send debugging messages to syslog.</p>
<dt><code>-f</code></p>
<dd>Run <code>rdisc</code> forever even if no routers are found. Normally <code>rdisc</code> gives up if it has not received any <code>advertise</code> message after after soliciting three times, in which case it exits with a non-zero exit code. If <code>-f</code> is not specified in the first form then <code>-s</code> must be specified.</p>
<dt><code>-r</code></p>
<dd>Responder mode, available only if compiled with -DRDISC_SERVER.</p>
<dt><code>-s</code></p>
<dd>Send three <code>solicitation</code> messages initially to quickly discover the routers when the system is booted. When <code>-s</code> is specified <code>rdisc</code> exits with a non-zero exit code if it can not find any routers. This can be overridden with the <code>-f</code> option.</p>
<dt><code>-p </code><i>preference</i></p>
<dd>Set preference in advertisement. Available only with -r option.</p>
<dt><code>-T </code><i>max_interval</i></p>
<dd>Set maximum advertisement interval in seconds. Default is 600 secs. Available only with -r option.</p>
<dt><code>-t</code></p>
<dd>Test mode. Do not go to background.</p>
<dt><code>-v</code></p>
<dd>Be verbose i.e. send lots of debugging messages to syslog.</p>
<dt><code>-V</code></p>
<dd>Print version and exit.</dl>
<h2>History</h2>
<p>This program was developed by Sun Microsystems (see copyright notice in source file). It was ported to Linux by Alexey Kuznetsov &lt;kuznet [at] ms2.inr.ac.ru&gt;. It is now maintained by YOSHIFUJI Hideaki &lt;yoshfuji [at] skbuff.net&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-icmp/">icmp</a></code>(7), <code><a href="/docs/linux/man/7-inet/">inet</a></code>(7), <code><a href="/docs/linux/man/8-ping/">ping</a></code>(8).</p>
<h2>References</h2>
<p>Deering, S.E.,ed &quot;ICMP Router Discovery Messages&quot;, RFC1256, Network Information Center, SRI International, Menlo Park, Calif., September 1991.</p>
<h2>Security</h2>
<p><code>rdisc</code> requires CAP_NET_RAW to listen and send ICMP messages and capability CAP_NET_ADMIN to update routing tables.</p>
<h2>Availability</h2>
<p><code>rdisc</code> is part of <i>iputils</i> package and the latest versions are available in source form at <a rel="nofollow" href="http://www.skbuff.net/iputils/iputils-current.tar.bz2.">http://www.skbuff.net/iputils/iputils-current.tar.bz2.</a></p>
