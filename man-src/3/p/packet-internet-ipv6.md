---
title: "packet-internet-ipv6(3)"
name: "packet-internet-ipv6"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-internet-ipv6/"
description: "packet.internet.ipv6 – IPv6 module"
---

<p>packet.internet.ipv6 &#8211; IPv6 module</p>
<h2>Description</h2>
<p>Decode IP version 6 layer. Extension headers are not supported.</p>
<h2>Classes</h2>
<h3>class IPv6(packet.internet.ipv4.IPv4)</h3>
<pre>IPv6 object
Usage:
 from packet.internet.ipv6 import IPv6
 x = IPv6(pktt)
Object definition:
IPv6(
 version = int,
 traffic_class = int,
 flow_label = int,
 total_size = int,
 protocol = int,
 hop_limit = int,
 src = IPv6Addr(),
 dst = IPv6Addr(),
 data = string, # raw data of payload if protocol
 # is not supported
)
<code>Methods defined here:</code>
---------------------
<code>__init__(self, pktt)</code>
Constructor
Initialize object's private data.
<dl><dt><dd><dl><dt><code>pktt:</code>
<dd>Packet trace object (packet.pktt.Pktt) so this layer has
access to the parent layers.
</dl></dl></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3),</code> <code><a href="/docs/linux/man/3-packet-internet-ipv4/">packet.internet.ipv4</a>(3),</code> <code><a href="/docs/linux/man/3-packet-transport-tcp/">packet.transport.tcp</a>(3),</code> <code><a href="/docs/linux/man/3-packet-transport-udp/">packet.transport.udp</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
