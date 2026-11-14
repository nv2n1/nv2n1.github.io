---
title: "ldns_pkt_edns_version(3)"
name: "ldns_pkt_edns_version"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_pkt_edns_version/"
description: "ldns_pkt_edns, ldns_pkt_edns_udp_size, ldns_pkt_edns_extended_rcode, ldns_pkt_edns_version, ldns_pkt_edns_z, ldns_pkt_edns_data, ldns_pkt_set_edns_udp_size, ldns_pkt_set_edns_extended_rcode, ldns_p..."
---

<h2>NAME</h2>
<p> ldns_pkt_edns, ldns_pkt_edns_udp_size, ldns_pkt_edns_extended_rcode, ldns_pkt_edns_version, ldns_pkt_edns_z, ldns_pkt_edns_data, ldns_pkt_set_edns_udp_size, ldns_pkt_set_edns_extended_rcode, ldns_pkt_set_edns_version, ldns_pkt_set_edns_z, ldns_pkt_set_edns_data </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> bool ldns_pkt_edns(const ldns_pkt *packet); </p>
<p> uint16_t ldns_pkt_edns_udp_size(const ldns_pkt *packet); </p>
<p> uint8_t ldns_pkt_edns_extended_rcode(const ldns_pkt *packet); </p>
<p> uint8_t ldns_pkt_edns_version(const ldns_pkt *packet); </p>
<p> uint16_t ldns_pkt_edns_z(const ldns_pkt *packet); </p>
<p> ldns_rdf* ldns_pkt_edns_data(const ldns_pkt *packet); </p>
<p> void ldns_pkt_set_edns_udp_size(ldns_pkt *packet, uint16_t s); </p>
<p> void ldns_pkt_set_edns_extended_rcode(ldns_pkt *packet, uint8_t c); </p>
<p> void ldns_pkt_set_edns_version(ldns_pkt *packet, uint8_t v); </p>
<p> void ldns_pkt_set_edns_z(ldns_pkt *packet, uint16_t z); </p>
<p> void ldns_pkt_set_edns_data(ldns_pkt *packet, ldns_rdf *data); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_pkt_edns</i>()</p>
<dd>returns true if this packet needs and EDNS rr to be sent. At the moment the only reason is an expected packet size larger than 512 bytes, but for instance dnssec would be a good reason too. </p>
<p> .br <code>packet</code>: the packet to check .br Returns true if packet needs edns rr</dl>
<dl>
<dt> <i>ldns_pkt_edns_udp_size</i>()</p>
<dd>return the packet&#8217;s edns udp size .br <code>packet</code>: the packet .br Returns the size</dl>
<dl>
<dt> <i>ldns_pkt_edns_extended_rcode</i>()</p>
<dd>return the packet&#8217;s edns extended rcode .br <code>packet</code>: the packet .br Returns the rcode</dl>
<dl>
<dt> <i>ldns_pkt_edns_version</i>()</p>
<dd>return the packet&#8217;s edns version .br <code>packet</code>: the packet .br Returns the version</dl>
<dl>
<dt> <i>ldns_pkt_edns_z</i>()</p>
<dd>return the packet&#8217;s edns z value .br <code>packet</code>: the packet .br Returns the z value</dl>
<dl>
<dt> <i>ldns_pkt_edns_data</i>()</p>
<dd>return the packet&#8217;s edns data .br <code>packet</code>: the packet .br Returns the data</dl>
<dl>
<dt> <i>ldns_pkt_set_edns_udp_size</i>()</p>
<dd>Set the packet&#8217;s edns udp size .br <code>packet</code>: the packet .br <code>s</code>: the size</dl>
<dl>
<dt> <i>ldns_pkt_set_edns_extended_rcode</i>()</p>
<dd>Set the packet&#8217;s edns extended rcode .br <code>packet</code>: the packet .br <code>c</code>: the code</dl>
<dl>
<dt> <i>ldns_pkt_set_edns_version</i>()</p>
<dd>Set the packet&#8217;s edns version .br <code>packet</code>: the packet .br <code>v</code>: the version</dl>
<dl>
<dt> <i>ldns_pkt_set_edns_z</i>()</p>
<dd>Set the packet&#8217;s edns z value .br <code>packet</code>: the packet .br <code>z</code>: the value</dl>
<dl>
<dt> <i>ldns_pkt_set_edns_data</i>()</p>
<dd>Set the packet&#8217;s edns data .br <code>packet</code>: the packet .br <code>data</code>: the data</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_pkt</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
