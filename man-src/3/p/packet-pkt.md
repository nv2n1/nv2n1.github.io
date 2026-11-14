---
title: "packet-pkt(3)"
name: "packet-pkt"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-pkt/"
description: "packet.pkt – Pkt module"
---

<p>packet.pkt &#8211; Pkt module</p>
<h2>Description</h2>
<p>Provides the object for a packet and the string representation of the packet. This object has an attribute for each of the layers in the packet so each layer can be accessed directly instead of going through each layer. To access the nfs layer object you can use &#8216;x.nfs&#8217; instead of using &#8216;x.ethernet.ip.tcp.rpc.nfs&#8217; which would be very cumbersome to use. Also, since NFS can be used with either TCP or UDP it would be harder to access the nfs object independently of the protocol. </p>
<p> Packet object attributes:<br />
&nbsp;<wbr>Pkt(<br />
&nbsp;<wbr>&nbsp;<wbr>record&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>Record information&nbsp;<wbr>(frame number, etc.)<br />
&nbsp;<wbr>&nbsp;<wbr>ethernet&nbsp;<wbr>=&nbsp;<wbr>ETHERNET II&nbsp;<wbr>(RFC 894)&nbsp;<wbr>object<br />
&nbsp;<wbr>&nbsp;<wbr>ip&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>IPv4 object<br />
&nbsp;<wbr>&nbsp;<wbr>tcp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>TCP object<br />
&nbsp;<wbr>&nbsp;<wbr>rpc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>RPC object<br />
&nbsp;<wbr>&nbsp;<wbr>nfs&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>NFS object<br />
&nbsp;<wbr>)</p>
<h2>Classes</h2>
<h3>class Pkt(baseobj.BaseObj)</h3>
<pre>Packet object
Usage:
 from packet.pkt import Pkt
 x = Pkt()
 # Check if this is an NFS packet
 if x == 'nfs':
 print x.nfs
<code>Methods defined here:</code>
---------------------
<code>__eq__(self, other)</code>
Comparison method used to determine if object has a given layer
<code>__init__(self)</code>
 Do not use BaseObj constructor to have a little bit of
 performance improvement
<code>__ne__(self, other)</code>
Comparison method used to determine if object does not have a given layer
<code>__str__(self)</code>
String representation of object
The representation depends on the verbose level set by debug_repr().
If set to 0 the generic object representation is returned.
If set to 1 the representation of is condensed into a single line.
It contains, the frame number, IP source and destination and/or the
last layer:
 '1 0.386615 192.168.0.62 -&gt; 192.168.0.17 TCP 2049 -&gt; 708, seq: 3395733180, ack: 3294169773, ACK,SYN'
 '5 0.530957 00:0c:29:54:09:ef -&gt; ff:ff:ff:ff:ff:ff, type: 0x806'
 '19 0.434370 192.168.0.17 -&gt; 192.168.0.62 NFS v4 COMPOUND4 call SEQUENCE;PUTFH;GETATTR'
If set to 2 the representation of the object is a line for each layer:
 'Pkt(
 RECORD: frame 19 @ 0.434370 secs, 238 bytes on wire, 238 bytes captured
 ETHERNET: 00:0c:29:54:09:ef -&gt; e4:ce:8f:58:9f:f4, type: 0x800(IPv4)
 IP: 192.168.0.17 -&gt; 192.168.0.62, protocol: 6(TCP), len: 224
 TCP: src port 708 -&gt; dst port 2049, seq: 3294170673, ack: 3395734137, len: 172, flags: ACK,PSH
 RPC: CALL(0), program: 100003, version: 4, procedure: 1, xid: 0x1437d3d5
 NFS: COMPOUND4args(tag='', minorversion=1, argarray=[nfs_argop4(argop=OP_SEQUENCE, ...), ...])
 )'</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
