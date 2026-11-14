---
title: "tc-ct(8)"
name: "tc-ct"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-ct/"
description: "ct – tc connection tracking action"
---

<p>ct &#8211; tc connection tracking action</p>
<h2>Synopsis</h2>
<p><code>tc &#8230; action ct commit [ force ] [ zone </code> <i>ZONE</i> <code>] [ mark </code> <i>MASKED_MARK</i> <code>] [ label </code> <i>MASKED_LABEL</i> <code>] [ nat </code> <i>NAT_SPEC</i> <code>]</code><br />
 <code>tc &#8230; action ct [ nat ] [ zone </code> <i>ZONE</i> <code>]</code><br />
 <code>tc &#8230; action ct clear</code> </p>
<h2>Description</h2>
<p>The ct action is a tc action for sending packets and interacting with the netfilter conntrack module. It can (as shown in the synopsis, in order): Send the packet to conntrack, and commit the connection, while configuring a 32bit mark, 128bit label, and src/dst nat. Send the packet to conntrack, which will mark the packet with the connection&#8217;s state and configured metadata (mark/label), and execute previous configured nat. Clear the packet&#8217;s of previous connection tracking state. </p>
<h2>Options</h2>
<dl>
<dt><code>zone</code><i> ZONE</i></p>
<dd>Specify a conntrack zone number on which to send the packet to conntrack.</p>
<dt><code>mark</code><i> MASKED_MARK</i></p>
<dd>Specify a masked 32bit mark to set for the connection (only valid with commit).</p>
<dt><code>label</code><i> MASKED_LABEL</i></p>
<dd>Specify a masked 128bit label to set for the connection (only valid with commit).</p>
<dt><code>nat</code><i> NAT_SPEC</i></p>
<dd><code>Where</code><i> NAT_SPEC </i><code>:= {src|dst} addr</code><i> addr1</i><code>[-</code><i>addr2</i><code>] [port </code><i>port1</i><code>[-</code><i>port2</i><code>]]</code> </p>
<p> Specify src/dst and range of nat to configure for the connection (only valid with commit).</p>
<dl>
<dd>
<dl>
<dt>src/dst &#8211; configure src or dst nat</p>
<dd>
<dt><i>addr1</i><code>/</code><i>addr2</i><code> &#8211; IPv4/IPv6 addresses</code></p>
<dd>
<dt><i>port1</i><code>/</code><i>port2</i><code> &#8211; Port numbers</code></p>
<dd></dl>
</dl>
<dt><code>nat</code></p>
<dd>Restore any previous configured nat.</p>
<dt><code>clear</code></p>
<dd>Remove any conntrack state and metadata (mark/label) from the packet (must only option specified).</p>
<dt><code>force</code></p>
<dd>Forces conntrack direction for a previously committed connections, so that current direction will become the original direction (only valid with commit). </p>
</dl>
<h2>Examples</h2>
<p>Example showing natted firewall in conntrack zone 2, and conntrack mark usage: #Add ingress qdisc on eth0 and eth1 interfaces </p>
<pre>$ tc qdisc add dev eth0 handle ingress
$ tc qdisc add dev eth1 handle ingress
#Setup filters on eth0, allowing opening new connections in zone 2, and doing src nat + mark for each new connection
$ tc filter add dev eth0 ingress prio 1 chain 0 proto ip flower ip_proto tcp ct_state -trk \
action ct zone 2 pipe action goto chain 2
$ tc filter add dev eth0 ingress prio 1 chain 2 proto ip flower ct_state +trk+new \
action ct zone 2 commit mark 0xbb nat src addr 5.5.5.7 pipe action mirred egress redirect dev eth1
$ tc filter add dev eth0 ingress prio 1 chain 2 proto ip flower ct_zone 2 ct_mark 0xbb ct_state +trk+est \
action ct nat pipe action mirred egress redirect dev eth1
#Setup filters on eth1, allowing only established connections of zone 2 through, and reverse nat (dst nat in this case)
$ tc filter add dev eth1 ingress prio 1 chain 0 proto ip flower ip_proto tcp ct_state -trk \
action ct zone 2 pipe action goto chain 1
$ tc filter add dev eth1 ingress prio 1 chain 1 proto ip flower ct_zone 2 ct_mark 0xbb ct_state +trk+est \
action ct nat pipe action mirred egress redirect dev eth0</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-flower/">tc-flower</a></code>(8) <code><a href="/docs/linux/man/8-tc-mirred/">tc-mirred</a></code>(8)</p>
<h2>Authors</h2>
<p>Paul Blakey &lt;paulb [at] mellanox.com&gt; </p>
<p> Marcelo Ricardo Leitner &lt;marcelo.leitner [at] gmail.com&gt; </p>
<p> Yossi Kuperman &lt;yossiku [at] mellanox.com&gt;</p>
