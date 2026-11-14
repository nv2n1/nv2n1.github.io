---
title: "ldns_buffer2pkt_wire(3)"
name: "ldns_buffer2pkt_wire"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_buffer2pkt_wire/"
description: "ldns_buffer2pkt_wire"
---

<h2>NAME</h2>
<p> ldns_buffer2pkt_wire </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_status ldns_buffer2pkt_wire(ldns_pkt **packet, ldns_buffer *buffer); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_buffer2pkt_wire</i>()</p>
<dd>converts the data on the uint8_t bytearray (in wire format) to a DNS packet. This function will initialize and allocate memory space for the packet structure. </p>
<p> .br <code>packet</code>: pointer to the structure to hold the packet .br <code>buffer</code>: the buffer with the data .br Returns LDNS_STATUS_OK if everything succeeds, error otherwise</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
