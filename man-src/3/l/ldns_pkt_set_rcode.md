---
title: "ldns_pkt_set_rcode(3)"
name: "ldns_pkt_set_rcode"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_pkt_set_rcode/"
description: "ldns_pkt_set_flags, ldns_pkt_set_id, ldns_pkt_set_qr, ldns_pkt_set_aa, ldns_pkt_set_tc, ldns_pkt_set_rd, ldns_pkt_set_cd, ldns_pkt_set_ra, ldns_pkt_set_ad, ldns_pkt_set_opcode, ldns_pkt_set_rcode, ..."
---

<h2>NAME</h2>
<p> ldns_pkt_set_flags, ldns_pkt_set_id, ldns_pkt_set_qr, ldns_pkt_set_aa, ldns_pkt_set_tc, ldns_pkt_set_rd, ldns_pkt_set_cd, ldns_pkt_set_ra, ldns_pkt_set_ad, ldns_pkt_set_opcode, ldns_pkt_set_rcode, ldns_pkt_set_qdcount, ldns_pkt_set_ancount, ldns_pkt_set_nscount, ldns_pkt_set_arcount, ldns_pkt_set_answerfrom, ldns_pkt_set_querytime, ldns_pkt_set_size, ldns_pkt_set_section_count, ldns_pkt_set_tsig </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> bool ldns_pkt_set_flags(ldns_pkt *pkt, uint16_t flags); </p>
<p> void ldns_pkt_set_id(ldns_pkt *p, uint16_t id); </p>
<p> void ldns_pkt_set_qr(ldns_pkt *p, bool b); </p>
<p> void ldns_pkt_set_aa(ldns_pkt *p, bool b); </p>
<p> void ldns_pkt_set_tc(ldns_pkt *p, bool b); </p>
<p> void ldns_pkt_set_rd(ldns_pkt *p, bool b); </p>
<p> void ldns_pkt_set_cd(ldns_pkt *p, bool b); </p>
<p> void ldns_pkt_set_ra(ldns_pkt *p, bool b); </p>
<p> void ldns_pkt_set_ad(ldns_pkt *p, bool b); </p>
<p> void ldns_pkt_set_opcode(ldns_pkt *p, ldns_pkt_opcode c); </p>
<p> void ldns_pkt_set_rcode(ldns_pkt *p, uint8_t c); </p>
<p> void ldns_pkt_set_qdcount(ldns_pkt *p, uint16_t c); </p>
<p> void ldns_pkt_set_ancount(ldns_pkt *p, uint16_t c); </p>
<p> void ldns_pkt_set_nscount(ldns_pkt *p, uint16_t c); </p>
<p> void ldns_pkt_set_arcount(ldns_pkt *p, uint16_t c); </p>
<p> void ldns_pkt_set_answerfrom(ldns_pkt *p, ldns_rdf *r); </p>
<p> void ldns_pkt_set_querytime(ldns_pkt *p, uint32_t t); </p>
<p> void ldns_pkt_set_size(ldns_pkt *p, size_t s); </p>
<p> void ldns_pkt_set_section_count(ldns_pkt *p, ldns_pkt_section s, uint16_t x); </p>
<p> void ldns_pkt_set_tsig(ldns_pkt *p, ldns_rr *t); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_pkt_set_flags</i>()</p>
<dd>sets the flags in a packet. .br <code>pkt</code>: the packet to operate on .br <code>flags</code>: ORed values: LDNS_QR| LDNS_AR for instance .br Returns true on success otherwise false</dl>
<dl>
<dt> <i>ldns_pkt_set_id</i>()</p>
<dd>Set the packet&#8217;s id .br <code>p</code>: the packet .br <code>id</code>: the id to set</dl>
<dl>
<dt> <i>ldns_pkt_set_qr</i>()</p>
<dd>Set the packet&#8217;s qr bit .br <code>p</code>: the packet .br <code>b</code>: the value to set (boolean)</dl>
<dl>
<dt> <i>ldns_pkt_set_aa</i>()</p>
<dd>Set the packet&#8217;s aa bit .br <code>p</code>: the packet .br <code>b</code>: the value to set (boolean)</dl>
<dl>
<dt> <i>ldns_pkt_set_tc</i>()</p>
<dd>Set the packet&#8217;s tc bit .br <code>p</code>: the packet .br <code>b</code>: the value to set (boolean)</dl>
<dl>
<dt> <i>ldns_pkt_set_rd</i>()</p>
<dd>Set the packet&#8217;s rd bit .br <code>p</code>: the packet .br <code>b</code>: the value to set (boolean)</dl>
<dl>
<dt> <i>ldns_pkt_set_cd</i>()</p>
<dd>Set the packet&#8217;s cd bit .br <code>p</code>: the packet .br <code>b</code>: the value to set (boolean)</dl>
<dl>
<dt> <i>ldns_pkt_set_ra</i>()</p>
<dd>Set the packet&#8217;s ra bit .br <code>p</code>: the packet .br <code>b</code>: the value to set (boolean)</dl>
<dl>
<dt> <i>ldns_pkt_set_ad</i>()</p>
<dd>Set the packet&#8217;s ad bit .br <code>p</code>: the packet .br <code>b</code>: the value to set (boolean)</dl>
<dl>
<dt> <i>ldns_pkt_set_opcode</i>()</p>
<dd>Set the packet&#8217;s opcode .br <code>p</code>: the packet .br <code>c</code>: the opcode</dl>
<dl>
<dt> <i>ldns_pkt_set_rcode</i>()</p>
<dd>Set the packet&#8217;s respons code .br <code>p</code>: the packet .br <code>c</code>: the rcode</dl>
<dl>
<dt> <i>ldns_pkt_set_qdcount</i>()</p>
<dd>Set the packet&#8217;s qd count .br <code>p</code>: the packet .br <code>c</code>: the count</dl>
<dl>
<dt> <i>ldns_pkt_set_ancount</i>()</p>
<dd>Set the packet&#8217;s an count .br <code>p</code>: the packet .br <code>c</code>: the count</dl>
<dl>
<dt> <i>ldns_pkt_set_nscount</i>()</p>
<dd>Set the packet&#8217;s ns count .br <code>p</code>: the packet .br <code>c</code>: the count</dl>
<dl>
<dt> <i>ldns_pkt_set_arcount</i>()</p>
<dd>Set the packet&#8217;s arcount .br <code>p</code>: the packet .br <code>c</code>: the count</dl>
<dl>
<dt> <i>ldns_pkt_set_answerfrom</i>()</p>
<dd>Set the packet&#8217;s answering server .br <code>p</code>: the packet .br <code>r</code>: the address</dl>
<dl>
<dt> <i>ldns_pkt_set_querytime</i>()</p>
<dd>Set the packet&#8217;s query time .br <code>p</code>: the packet .br <code>t</code>: the querytime in msec</dl>
<dl>
<dt> <i>ldns_pkt_set_size</i>()</p>
<dd>Set the packet&#8217;s size .br <code>p</code>: the packet .br <code>s</code>: the size</dl>
<dl>
<dt> <i>ldns_pkt_set_section_count</i>()</p>
<dd>Set a packet&#8217;s section count to x .br <code>p</code>: the packet .br <code>s</code>: the section .br <code>x</code>: the section count</dl>
<dl>
<dt> <i>ldns_pkt_set_tsig</i>()</p>
<dd>Set the packet&#8217;s tsig rr .br <code>p</code>: the packet .br <code>t</code>: the tsig rr</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_pkt </i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
