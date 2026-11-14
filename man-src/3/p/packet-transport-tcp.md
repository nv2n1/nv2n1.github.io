---
title: "packet-transport-tcp(3)"
name: "packet-transport-tcp"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-transport-tcp/"
description: "packet.transport.tcp – TCP module"
---

<p>packet.transport.tcp &#8211; TCP module</p>
<h2>Description</h2>
<p>Decode TCP layer.</p>
<h2>Classes</h2>
<h3>class Flags(baseobj.BaseObj)</h3>
<pre>Flags object
<code>Methods defined here:</code>
---------------------
<code>__init__(self, data)</code>
Constructor which takes a short integer as input</pre>
<h3>class TCP(baseobj.BaseObj)</h3>
<pre>TCP object
Usage:
 from packet.transport.tcp import TCP
 x = TCP(pktt)
Object definition:
TCP(
 src_port = int, # Source port
 dst_port = int, # Destination port
 seq_number = int, # Sequence number
 ack_number = int, # Acknowledgment number
 hl = int, # Data offset or header length (32bit words)
 header_size = int, # Data offset or header length in bytes
 flags_raw = int, # Raw flags
 flags = Flags( # Individual flags:
 FIN = int, # No more data from sender
 SYN = int, # Synchronize sequence numbers
 RST = int, # Synchronize sequence numbers
 PSH = int, # Push function. Asks to push the buffered
 # data to the receiving application
 ACK = int, # Acknowledgment field is significant
 URG = int, # Urgent pointer field is significant
 ECE = int, # ECN-Echo has a dual role:
 # SYN=1, the TCP peer is ECN capable.
 # SYN=0, packet with Congestion Experienced
 # flag in IP header set is received during
 # normal transmission
 CWR = int, # Congestion Window Reduced
 NS = int, # ECN-nonce concealment protection
 ),
 window_size = int, # Window size
 checksum = int, # Checksum
 urgent_ptr = int, # Urgent pointer
 seq = int, # Relative sequence number
 options = string, # Raw data of TCP options if available
 data = string, # Raw data of payload if unable to decode
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
 'TCP 708 -&gt; 2049, seq: 3294175829, ack: 3395739041, ACK,FIN'
If set to 2 the representation of the object also includes the
length of payload and a little bit more verbose:
 'src port 708 -&gt; dst port 2049, seq: 3294175829, ack: 3395739041, len: 0, flags: ACK,FIN'</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3),</code> <code><a href="/docs/linux/man/3-packet-application-rpc/">packet.application.rpc</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
