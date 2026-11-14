---
title: "ldns_rr2wire(3)"
name: "ldns_rr2wire"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_rr2wire/"
description: "ldns_rr2wire, ldns_pkt2wire, ldns_rdf2wire"
---

<h2>NAME</h2>
<p> ldns_rr2wire, ldns_pkt2wire, ldns_rdf2wire </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_status ldns_rr2wire(uint8_t **dest, const ldns_rr *rr, int, size_t *size); </p>
<p> ldns_status ldns_pkt2wire(uint8_t **dest, const ldns_pkt *p, size_t *size); </p>
<p> ldns_status ldns_rdf2wire(uint8_t **dest, const ldns_rdf *rdf, size_t *size); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_rr2wire</i>()</p>
<dd>Allocates an array of uint8_t at dest, and puts the wireformat of the given rr in that array. The result_size value contains the length of the array, if it succeeds, and 0 otherwise (in which case the function also returns NULL) </p>
<p> If the section argument is LDNS_SECTION_QUESTION, data like ttl and rdata are not put into the result </p>
<p> .br <code>dest</code>: pointer to the array of bytes to be created .br <code>rr</code>: the rr to convert .br <code>size</code>: the size of the converted result</dl>
<dl>
<dt> <i>ldns_pkt2wire</i>()</p>
<dd>Allocates an array of uint8_t at dest, and puts the wireformat of the given packet in that array. The result_size value contains the length of the array, if it succeeds, and 0 otherwise (in which case the function also returns NULL)</dl>
<dl>
<dt> <i>ldns_rdf2wire</i>()</p>
<dd>Allocates an array of uint8_t at dest, and puts the wireformat of the given rdf in that array. The result_size value contains the length of the array, if it succeeds, and 0 otherwise (in which case the function also returns NULL) </p>
<p> .br <code>dest</code>: pointer to the array of bytes to be created .br <code>rdf</code>: the rdata field to convert .br <code>size</code>: the size of the converted result</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_wire2rr</i>, <i>ldns_wire2pkt</i>, <i>ldns_wire2rdf</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
