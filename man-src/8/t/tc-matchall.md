---
title: "tc-matchall(8)"
name: "tc-matchall"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-matchall/"
description: "matchall – traffic control filter that matches every packet"
---

<p>matchall &#8211; traffic control filter that matches every packet</p>
<h2>Synopsis</h2>
<p><code>tc</code> <code>filter</code> &#8230; <code>matchall</code> [ <code>skip_sw</code> | <code>skip_hw</code> ] [ <code>action</code> <i>ACTION_SPEC</i> ] [ <code>classid</code> <i>CLASSID</i> ]</p>
<h2>Description</h2>
<p>The <code>matchall</code> filter allows to classify every packet that flows on the port and run a action on it.</p>
<h2>Options</h2>
<dl>
<dt><code>action</code><i> ACTION_SPEC</i></p>
<dd>Apply an action from the generic actions framework on matching packets.</p>
<dt><code>classid</code><i> CLASSID</i></p>
<dd>Push matching packets into the class identified by <i>CLASSID</i>.</p>
<dt><code>skip_sw</code></p>
<dd>Do not process filter by software. If hardware has no offload support for this filter, or TC offload is not enabled for the interface, operation will fail.</p>
<dt><code>skip_hw</code></p>
<dd>Do not process filter by hardware.</dl>
<h2>Examples</h2>
<p>To create ingress mirroring from port eth1 to port eth2:</p>
<dl>
<dd>tc qdisc add dev eth1 handle ffff: ingress tc filter add dev eth1 parent ffff: \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;matchall skip_sw&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;action mirred egress mirror&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dev eth2</dl>
<p> The first command creates an ingress qdisc with handle <code>ffff:</code> on device <code>eth1</code> where the second command attaches a matchall filters on it that mirrors the packets to device eth2. To create egress mirroring from port eth1 to port eth2:</p>
<dl>
<dd>tc qdisc add dev eth1 handle 1: root prio tc filter add dev eth1 parent 1: \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;matchall skip_sw&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;action mirred egress mirror&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dev eth2</dl>
<p> The first command creates an egress qdisc with handle <code>1:</code> that replaces the root qdisc on device <code>eth1</code> where the second command attaches a matchall filters on it that mirrors the packets to device eth2. To sample one of every 100 packets flowing into interface eth0 to psample group 12:</p>
<dl>
<dd>tc qdisc add dev eth0 handle ffff: ingress tc filter add dev eth0 parent ffff: matchall \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;action sample rate 100 group 12</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), </p>
