---
title: "packet-link-ethernet(3)"
name: "packet-link-ethernet"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-link-ethernet/"
description: "packet.link.ethernet – ETHERNET module"
---

<p>packet.link.ethernet &#8211; ETHERNET module</p>
<h2>Description</h2>
<p>Decode ethernet layer (RFC 894) Ethernet II.</p>
<h2>Classes</h2>
<h3>class ETHERNET(baseobj.BaseObj)</h3>
<pre>Ethernet object
Usage:
 from packet.link.ethernet import ETHERNET
 x = ETHERNET(pktt)
Object definition:
ETHERNET(
 dst = MacAddr(), # destination MAC address
 src = MacAddr(), # source MAC address
 type = int, # payload type
 data = string, # raw data of payload if type is not supported
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
 '00:0c:29:54:09:ef -&gt; 60:33:4b:29:6e:9d '
If set to 2 the representation of the object also includes the type
of payload:
 '00:0c:29:54:09:ef -&gt; 60:33:4b:29:6e:9d, type: 0x800(IPv4)'</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3),</code> <code><a href="/docs/linux/man/3-packet-internet-ipv4/">packet.internet.ipv4</a>(3),</code> <code><a href="/docs/linux/man/3-packet-internet-ipv6/">packet.internet.ipv6</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
