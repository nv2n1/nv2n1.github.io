---
title: "packet-internet-ipv4(3)"
name: "packet-internet-ipv4"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-internet-ipv4/"
description: "packet.internet.ipv4 – IPv4 module"
---

<p>packet.internet.ipv4 &#8211; IPv4 module</p>
<h2>Description</h2>
<p>Decode IP version 4 layer.</p>
<h2>Classes</h2>
<h3>class Flags(baseobj.BaseObj)</h3>
<pre>Flags object
<code>Methods defined here:</code>
---------------------
<code>__init__(self, data)</code>
Constructor which takes a single byte as input</pre>
<h3>class IPv4(baseobj.BaseObj)</h3>
<pre>IPv4 object
Usage:
 from packet.internet.ipv4 import IPv4
 x = IPv4(pktt)
Object definition:
IPv4(
 version = int,
 IHL = int, # Internet Header Length (in 32bit words)
 header_size = int, # IHL in actual bytes
 DSCP = int, # Differentiated Services Code Point
 ECN = int, # Explicit Congestion Notification
 total_size = int, # Total length
 id = int, # Identification
 flags = Flags( # Flags:
 DF = int, # Don't Fragment
 MF = int, # More Fragments
 )
 fragment_offset = int, # Fragment offset (in 8-byte blocks)
 TTL = int, # Time to Live
 protocol = int, # Protocol of next layer (RFC790)
 checksum = int, # Header checksum
 src = &quot;%d.%d.%d.%d&quot;, # source IP address
 dst = &quot;%d.%d.%d.%d&quot;, # destination IP address
 options = string, # IP options if available
 data = string, # Raw data of payload if protocol
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
</dl></dl>
<code>__str__(self)</code>
String representation of object
The representation depends on the verbose level set by debug_repr().
If set to 0 the generic object representation is returned.
If set to 1 the representation of the object is condensed:
 '192.168.0.20 -&gt; 192.168.0.61 '
If set to 2 the representation of the object also includes the
protocol and length of payload:
 '192.168.0.20 -&gt; 192.168.0.61, protocol: 17(UDP), len: 84'</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3),</code> <code><a href="/docs/linux/man/3-packet-transport-tcp/">packet.transport.tcp</a>(3),</code> <code><a href="/docs/linux/man/3-packet-transport-udp/">packet.transport.udp</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
