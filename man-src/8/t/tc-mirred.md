---
title: "tc-mirred(8)"
name: "tc-mirred"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-mirred/"
description: "mirred – mirror/redirect action"
---

<p>mirred &#8211; mirror/redirect action</p>
<h2>Synopsis</h2>
<p><code>tc</code> &#8230; <code>action mirred</code> <i>DIRECTION ACTION</i> [ <code>index</code> <i>INDEX</i> ] <code>dev</code><i> DEVICENAME</i> </p>
<pre><code>DIRECTION := {

    ingress | egress }
ACTION := {

    mirror | redirect }</code></pre>
<h2>Description</h2>
<p>The <code>mirred</code> action allows packet mirroring (copying) or redirecting (stealing) the packet it receives. Mirroring is what is sometimes referred to as Switch Port Analyzer (SPAN) and is commonly used to analyze and/or debug flows.</p>
<h2>Options</h2>
<dl>
<dt><code>ingress</code></p>
<dd><code>egress</code> Specify the direction in which the packet shall appear on the destination interface.</p>
<dt><code>mirror</code></p>
<dd><code>redirect</code> Define whether the packet should be copied (<code>mirror</code>) or moved (<code>redirect</code>) to the destination interface.</p>
<dt><code>index</code><i> INDEX</i></p>
<dd>Assign a unique ID to this action instead of letting the kernel choose one automatically. <i>INDEX</i> is a 32bit unsigned integer greater than zero.</p>
<dt><code>dev</code><i> DEVICENAME</i></p>
<dd>Specify the network interface to redirect or mirror to.</dl>
<h2>Examples</h2>
<p>Limit ingress bandwidth on eth0 to 1mbit/s, redirect exceeding traffic to lo for debugging purposes:</p>
<dl>
<dd># tc qdisc add dev eth0 handle ffff: ingress # tc filter add dev eth0 parent ffff: u32 \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>match u32 0 0 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action police rate 1mbit burst 100k conform-exceed pipe \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action mirred egress redirect dev lo
</dl>
<p> Mirror all incoming ICMP packets on eth0 to a dummy interface for examination with e.g. tcpdump:</p>
<dl>
<dd># ip link add dummy0 type dummy # ip link set dummy0 up # tc qdisc add dev eth0 handle ffff: ingress # tc filter add dev eth0 parent ffff: protocol ip \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>u32 match ip protocol 1 0xff \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action mirred egress mirror dev dummy0
</dl>
<p> Using an <code>ifb</code> interface, it is possible to send ingress traffic through an instance of <code>sfq</code>:</p>
<dl>
<dd># modprobe ifb # ip link set ifb0 up # tc qdisc add dev ifb0 root sfq # tc qdisc add dev eth0 handle ffff: ingress # tc filter add dev eth0 parent ffff: u32 \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>match u32 0 0 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action mirred egress redirect dev ifb0
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-u32/">tc-u32</a></code>(8) </p>
