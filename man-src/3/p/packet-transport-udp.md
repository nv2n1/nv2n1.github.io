---
title: "packet-transport-udp(3)"
name: "packet-transport-udp"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-transport-udp/"
description: "packet.transport.udp – UDP module"
---

<p>packet.transport.udp &#8211; UDP module</p>
<h2>Description</h2>
<p>Decode UDP layer.</p>
<h2>Classes</h2>
<h3>class UDP(baseobj.BaseObj)</h3>
<pre>UDP object
Usage:
 from packet.transport.udp import UDP
 x = UDP(pktt)
Object definition:
UDP(
 src_port = int,
 dst_port = int,
 length = int,
 checksum = int,
 data = string, # raw data of payload if unable to decode
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
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3),</code> <code><a href="/docs/linux/man/3-packet-application-rpc/">packet.application.rpc</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
