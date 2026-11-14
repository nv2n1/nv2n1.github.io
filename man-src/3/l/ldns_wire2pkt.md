---
title: "ldns_wire2pkt(3)"
name: "ldns_wire2pkt"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_wire2pkt/"
description: "ldns_wire2rr, ldns_wire2pkt, ldns_wire2rdf, ldns_wire2dname"
---

<h2>NAME</h2>
<p> ldns_wire2rr, ldns_wire2pkt, ldns_wire2rdf, ldns_wire2dname </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_status ldns_wire2rr(ldns_rr **rr, const uint8_t *wire, size_t max, size_t *pos, ldns_pkt_section section); </p>
<p> ldns_status ldns_wire2pkt(ldns_pkt **packet, const uint8_t *data, size_t len); </p>
<p> ldns_status ldns_wire2rdf(ldns_rr *rr, const uint8_t *wire, size_t max, size_t *pos); </p>
<p> ldns_status ldns_wire2dname(ldns_rdf **dname, const uint8_t *wire, size_t max, size_t *pos); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_wire2rr</i>()</p>
<dd>converts the data on the uint8_t bytearray (in wire format) to a DNS resource record. This function will initialize and allocate memory space for the rr structure. The length of the wiredata of this rr is added to the *pos value. </p>
<p> .br <code>rr</code>: pointer to the structure to hold the rdata value .br <code>wire</code>: pointer to the buffer with the data .br <code>max</code>: the length of the data buffer (in bytes) .br <code>pos</code>: the position of the rr in the buffer (ie. the number of bytes from the start of the buffer) .br <code>section</code>: the section in the packet the rr is meant for .br Returns LDNS_STATUS_OK if everything succeeds, error otherwise</dl>
<dl>
<dt> <i>ldns_wire2pkt</i>()</p>
<dd>converts the data on the uint8_t bytearray (in wire format) to a DNS packet. This function will initialize and allocate memory space for the packet structure. </p>
<p> .br <code>packet</code>: pointer to the structure to hold the packet .br <code>data</code>: pointer to the buffer with the data .br <code>len</code>: the length of the data buffer (in bytes) .br Returns LDNS_STATUS_OK if everything succeeds, error otherwise</dl>
<dl>
<dt> <i>ldns_wire2rdf</i>()</p>
<dd>converts the data on the uint8_t bytearray (in wire format) to DNS rdata fields, and adds them to the list of rdfs of the given rr. This function will initialize and allocate memory space for the dname structures. The length of the wiredata of these rdfs is added to the *pos value. </p>
<p> All rdfs belonging to the RR are read; the rr should have no rdfs yet. An error is returned if the format cannot be parsed. </p>
<p> .br <code>rr</code>: pointer to the ldns_rr structure to hold the rdata value .br <code>wire</code>: pointer to the buffer with the data .br <code>max</code>: the length of the data buffer (in bytes) .br <code>pos</code>: the position of the rdf in the buffer (ie. the number of bytes from the start of the buffer) .br Returns LDNS_STATUS_OK if everything succeeds, error otherwise</dl>
<dl>
<dt> <i>ldns_wire2dname</i>()</p>
<dd>converts the data on the uint8_t bytearray (in wire format) to a DNS dname rdata field. This function will initialize and allocate memory space for the dname structure. The length of the wiredata of this rdf is added to the *pos value. </p>
<p> .br <code>dname</code>: pointer to the structure to hold the rdata value .br <code>wire</code>: pointer to the buffer with the data .br <code>max</code>: the length of the data buffer (in bytes) .br <code>pos</code>: the position of the rdf in the buffer (ie. the number of bytes from the start of the buffer) .br Returns LDNS_STATUS_OK if everything succeeds, error otherwise</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_rr2wire</i>, <i>ldns_pkt2wire</i>, <i>ldns_rdf2wire</i>, <i>ldns_dname2wire</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
