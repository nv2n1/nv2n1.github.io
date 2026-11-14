---
title: "tc-ets(8)"
name: "tc-ets"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-ets/"
description: "ETS – Enhanced Transmission Selection scheduler"
---

<p>ETS &#8211; Enhanced Transmission Selection scheduler</p>
<h2>Synopsis</h2>
<p><code>tc qdisc &#8230; ets [ bands</code> number <code>] [ strict</code> number <code>] [ quanta</code> bytes bytes bytes&#8230; <code>] [ priomap</code> band band band&#8230; <code>]</code> <code>tc class &#8230; ets [ quantum</code> bytes <code>]</code> </p>
<h2>Description</h2>
<p>The Enhanced Transmission Selection scheduler is a classful queuing discipline that merges functionality of PRIO and DRR qdiscs in one scheduler. ETS makes it easy to configure a set of strict and bandwidth-sharing bands to implement the transmission selection described in 802.1Qaz. On creation with &#8216;tc qdisc add&#8217;, a fixed number of bands is created. Each band is a class, although it is not possible to directly add and remove bands with &#8216;tc class&#8217; commands. The number of bands to be created must instead be specified on the command line as the qdisc is added. The minor number of classid to use when referring to a band is the band number increased by one. Thus band 0 will have classid of major:1, band 1 that of major:2, etc. ETS bands are of two types: some number may be in strict mode, the remaining ones are in bandwidth-sharing mode. </p>
<h2>Algorithm</h2>
<p>When dequeuing, strict bands are tried first, if there are any. Band 0 is tried first. If it did not deliver a packet, band 1 is tried next, and so on until one of the bands delivers a packet, or the strict bands are exhausted. </p>
<p> If no packet has been dequeued from any of the strict bands, if there are any bandwidth-sharing bands, the dequeuing proceeds according to the DRR algorithm. Each bandwidth-sharing band is assigned a deficit counter, initialized to quantum assigned by a <code>quanta</code> element. ETS maintains an (internal) &#8221;active&#8221; list of bandwidth-sharing bands whose qdiscs are non-empty. This list is used for dequeuing. A packet is dequeued from the band at the head of the list if the packet size is smaller or equal to the deficit counter. If the counter is too small, it is increased by <code>quantum</code> and the scheduler moves on to the next band in the active list. </p>
<p> Only qdiscs that own their queue should be added below the bandwidth-sharing bands. Attaching to them non-work-conserving qdiscs like TBF does not make sense &#8212; other qdiscs in the active list will be skipped until the dequeue operation succeeds. This limitation does not exist with the strict bands.</p>
<h2>Classification</h2>
<p>The ETS qdisc allows three ways to decide which band to enqueue a packet to: </p>
<p> &#8211; Packet priority can be directly set to a class handle, in which case that<br />
&nbsp;<wbr>&nbsp;is the queue where the packet will be put. For example, band number 2 of<br />
&nbsp;<wbr>&nbsp;a qdisc with handle of 11: will have classid 11:3. To mark a packet for<br />
&nbsp;<wbr>&nbsp;queuing to this band, the packet priority should be set to 0x110003. </p>
<p> &#8211; A tc filter attached to the qdisc can put the packet to a band by using<br />
&nbsp;<wbr>&nbsp;the&nbsp;<code>flowid</code>&nbsp;keyword. </p>
<p> &#8211; As a last resort, the ETS qdisc consults its priomap (see below), which<br />
&nbsp;<wbr>&nbsp;maps packets to bands based on packet priority.</p>
<h2>Parameters</h2>
<dl>
<dt>strict</p>
<dd>The number of bands that should be created in strict mode. If not given, this value is 0. </p>
<dt>quanta</p>
<dd>Each bandwidth-sharing band needs to know its quantum, which is the amount of bytes a band is allowed to dequeue before the scheduler moves to the next bandwidth-sharing band. The <code>quanta</code> argument lists quanta for the individual bandwidth-sharing bands. The minimum value of each quantum is 1. If <code>quanta</code> is not given, the default is no bandwidth-sharing bands, but note that when specifying a large number of <code>bands,</code> the extra ones are in bandwidth-sharing mode by default. </p>
<dt>bands</p>
<dd>Number of bands given explicitly. This value has to be at least large enough to cover the strict bands specified through the <code>strict</code> keyword and bandwidth-sharing bands specified in <code>quanta.</code> If a larger value is given, any extra bands are in bandwidth-sharing mode, and their quanta are deduced from the interface MTU. If no value is given, as many bands are created as necessary to cover all bands implied by the <code>strict</code> and <code>quanta</code> keywords. </p>
<dt>priomap</p>
<dd>The priomap maps the priority of a packet to a band. The argument is a list of numbers. The first number indicates which band the packets with priority 0 should be put to, the second is for priority 1, and so on. </p>
<p> There can be up to 16 numbers in the list. If there are fewer, the default band that traffic with one of the unmentioned priorities goes to is the last one. </p>
</dl>
<h2>EXAMPLE &amp; USAGE</h2>
<p>Add a qdisc with 8 bandwidth-sharing bands, using the interface MTU as their quanta. Since all quanta are the same, this will lead to equal distribution of bandwidth between the bands, each will get about 12.5% of the link. The low 8 priorities go to individual bands in a reverse 1:1 fashion (such that the highest priority goes to the first band). </p>
<p> # tc qdisc add dev eth0 root handle 1: ets bands 8 priomap 7 6 5 4 3 2 1 0<br />
 # tc qdisc show dev eth0<br />
 qdisc ets 1: root refcnt 2 bands 8 quanta 1514 1514 1514 1514 1514 1514 1514 1514 priomap 7 6 5 4 3 2 1 0 7 7 7 7 7 7 7 7 </p>
<p> Tweak the first band of the above qdisc to give it a quantum of 2650, which will give it about 20% of the link (and about 11.5% to the remaining bands): </p>
<p> # tc class change dev eth0 classid 1:1 ets quantum 2650<br />
 # tc qdisc show dev eth0<br />
 qdisc ets 1: root refcnt 2 bands 8 quanta 2650 1514 1514 1514 1514 1514 1514 1514 priomap 7 6 5 4 3 2 1 0 7 7 7 7 7 7 7 7 </p>
<p> Create a purely strict Qdisc with reverse 1:1 mapping between priorities and bands: </p>
<p> # tc qdisc add dev eth0 root handle 1: ets strict 8 priomap 7 6 5 4 3 2 1 0<br />
 # tc qdisc sh dev eth0<br />
 qdisc ets 1: root refcnt 2 bands 8 strict 8 priomap 7 6 5 4 3 2 1 0 7 7 7 7 7 7 7 7 </p>
<p> Add a Qdisc with 6 bands, 3 strict and 3 ETS with 35%-30%-25% weights: </p>
<p> # tc qdisc add dev eth0 root handle 1: ets strict 3 quanta 3500 3000 2500 priomap 0 1 1 1 2 3 4 5<br />
 # tc qdisc sh dev eth0<br />
 qdisc ets 1: root refcnt 2 bands 6 strict 3 quanta 3500 3000 2500 priomap 0 1 1 1 2 3 4 5 5 5 5 5 5 5 5 5 </p>
<p> Create a Qdisc such that traffic with priorities 2, 3 and 4 are strictly prioritized over other traffic, and the rest goes into bandwidth-sharing classes with equal weights: </p>
<p> # tc qdisc add dev eth0 root handle 1: ets bands 8 strict 3 priomap 3 4 0 1 2 5 6 7<br />
 # tc qdisc sh dev eth0<br />
 qdisc ets 1: root refcnt 2 bands 8 strict 3 quanta 1514 1514 1514 1514 1514 priomap 3 4 0 1 2 5 6 7 7 7 7 7 7 7 7 7</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-prio/">tc-prio</a></code>(8), <code><a href="/docs/linux/man/8-tc-drr/">tc-drr</a></code>(8) </p>
<h2>Author</h2>
<p>Parts of both this manual page and the code itself are taken from PRIO and DRR qdiscs.<br />
 ETS qdisc itself was written by Petr Machata.</p>
