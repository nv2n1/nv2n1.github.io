---
title: "packet-record(3)"
name: "packet-record"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-record/"
description: "packet.record – Record module"
---

<p>packet.record &#8211; Record module</p>
<h2>Description</h2>
<p>Provides the object for a record and the string representation of the record in a tcpdump trace file.</p>
<h2>Classes</h2>
<h3>class Record(baseobj.BaseObj)</h3>
<pre>Record object
Usage:
 from packet.record import Record
 x = Record(pktt, data)
Object definition:
Record(
 index = int, # Frame number
 seconds = int, # Seconds
 usecs = int, # Microseconds
 length_inc = int, # Number of bytes included in trace
 length_orig = int, # Number of bytes in packet
 secs = float, # Absolute seconds including microseconds
 rsecs = float, # Seconds relative to first packet
)
<code>Methods defined here:</code>
---------------------
<code>__init__(self, pktt, data)</code>
Constructor
Initialize object's private data.
<dl><dt><dd><dl><dt><code>pktt:</code>
<dd>Packet trace object (packet.pktt.Pktt) so this layer has
access to the parent layers.
<dt><code>data:</code>
<dd>Raw packet data for this layer.
</dl></dl>
<code>__str__(self)</code>
String representation of object
The representation depends on the verbose level set by debug_repr().
If set to 0 the generic object representation is returned.
If set to 1 the representation of the object is condensed to display
the frame number and the timestamp:
 '57 2014-03-16 13:42:56.530957 '
If set to 2 the representation of the object also includes the number
of bytes on the wire, number of bytes captured and a little bit more
<dl><dt><dd><dl><dt><code>verbose:</code>
<dd></dl></dl></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
