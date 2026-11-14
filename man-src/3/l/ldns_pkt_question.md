---
title: "ldns_pkt_question(3)"
name: "ldns_pkt_question"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_pkt_question/"
description: "ldns_pkt_id, ldns_pkt_qr, ldns_pkt_aa, ldns_pkt_tc, ldns_pkt_rd, ldns_pkt_cd, ldns_pkt_ra, ldns_pkt_ad, ldns_pkt_get_opcode, ldns_pkt_get_rcode, ldns_pkt_qdcount, ldns_pkt_ancount, ldns_pkt_nscount..."
---

<h2>NAME</h2>
<p> ldns_pkt_id, ldns_pkt_qr, ldns_pkt_aa, ldns_pkt_tc, ldns_pkt_rd, ldns_pkt_cd, ldns_pkt_ra, ldns_pkt_ad, ldns_pkt_get_opcode, ldns_pkt_get_rcode, ldns_pkt_qdcount, ldns_pkt_ancount, ldns_pkt_nscount, ldns_pkt_arcount, ldns_pkt_answerfrom, ldns_pkt_querytime, ldns_pkt_size, ldns_pkt_tsig, ldns_pkt_question, ldns_pkt_answer, ldns_pkt_authority, ldns_pkt_additional, ldns_pkt_get_section_clone, ldns_pkt_rr_list_by_name, ldns_pkt_rr_list_by_type, ldns_pkt_rr_list_by_name_and_type </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p>&nbsp;<wbr>ldns_pkt_id(); </p>
<p> bool ldns_pkt_qr(const ldns_pkt *p); </p>
<p> bool ldns_pkt_aa(const ldns_pkt *p); </p>
<p> bool ldns_pkt_tc(const ldns_pkt *p); </p>
<p> bool ldns_pkt_rd(const ldns_pkt *p); </p>
<p> bool ldns_pkt_cd(const ldns_pkt *p); </p>
<p> bool ldns_pkt_ra(const ldns_pkt *p); </p>
<p> bool ldns_pkt_ad(const ldns_pkt *p); </p>
<p> ldns_pkt_opcode ldns_pkt_get_opcode(const ldns_pkt *p); </p>
<p> ldns_pkt_rcode ldns_pkt_get_rcode(const ldns_pkt *p); </p>
<p> uint16_t ldns_pkt_qdcount(const ldns_pkt *p); </p>
<p> uint16_t ldns_pkt_ancount(const ldns_pkt *p); </p>
<p> uint16_t ldns_pkt_nscount(const ldns_pkt *p); </p>
<p> uint16_t ldns_pkt_arcount(const ldns_pkt *p); </p>
<p> ldns_rdf* ldns_pkt_answerfrom(const ldns_pkt *p); </p>
<p> uint32_t ldns_pkt_querytime(const ldns_pkt *p); </p>
<p> size_t ldns_pkt_size(const ldns_pkt *p); </p>
<p> ldns_rr* ldns_pkt_tsig(const ldns_pkt *p); </p>
<p> ldns_rr_list* ldns_pkt_question(const ldns_pkt *p); </p>
<p> ldns_rr_list* ldns_pkt_answer(const ldns_pkt *p); </p>
<p> ldns_rr_list* ldns_pkt_authority(const ldns_pkt *p); </p>
<p> ldns_rr_list* ldns_pkt_additional(const ldns_pkt *p); </p>
<p> ldns_rr_list* ldns_pkt_get_section_clone(const ldns_pkt *p, ldns_pkt_section s); </p>
<p> ldns_rr_list* ldns_pkt_rr_list_by_name(ldns_pkt *p, ldns_rdf *r, ldns_pkt_section s); </p>
<p> ldns_rr_list* ldns_pkt_rr_list_by_type(const ldns_pkt *p, ldns_rr_type t, ldns_pkt_section s); </p>
<p> ldns_rr_list* ldns_pkt_rr_list_by_name_and_type(const ldns_pkt *packet, const ldns_rdf *ownername, ldns_rr_type type, ldns_pkt_section sec); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_pkt_id</i>()</dl>
<dl>
<dt> <i>ldns_pkt_qr</i>()</p>
<dd>Read the packet&#8217;s qr bit .br <code>p</code>: the packet .br Returns value of the bit</dl>
<dl>
<dt> <i>ldns_pkt_aa</i>()</p>
<dd>Read the packet&#8217;s aa bit .br <code>p</code>: the packet .br Returns value of the bit</dl>
<dl>
<dt> <i>ldns_pkt_tc</i>()</p>
<dd>Read the packet&#8217;s tc bit .br <code>p</code>: the packet .br Returns value of the bit</dl>
<dl>
<dt> <i>ldns_pkt_rd</i>()</p>
<dd>Read the packet&#8217;s rd bit .br <code>p</code>: the packet .br Returns value of the bit</dl>
<dl>
<dt> <i>ldns_pkt_cd</i>()</p>
<dd>Read the packet&#8217;s cd bit .br <code>p</code>: the packet .br Returns value of the bit</dl>
<dl>
<dt> <i>ldns_pkt_ra</i>()</p>
<dd>Read the packet&#8217;s ra bit .br <code>p</code>: the packet .br Returns value of the bit</dl>
<dl>
<dt> <i>ldns_pkt_ad</i>()</p>
<dd>Read the packet&#8217;s ad bit .br <code>p</code>: the packet .br Returns value of the bit</dl>
<dl>
<dt> <i>ldns_pkt_get_opcode</i>()</p>
<dd>Read the packet&#8217;s code .br <code>p</code>: the packet .br Returns the opcode</dl>
<dl>
<dt> <i>ldns_pkt_get_rcode</i>()</p>
<dd>Return the packet&#8217;s respons code .br <code>p</code>: the packet .br Returns the respons code</dl>
<dl>
<dt> <i>ldns_pkt_qdcount</i>()</p>
<dd>Return the packet&#8217;s qd count .br <code>p</code>: the packet .br Returns the qd count</dl>
<dl>
<dt> <i>ldns_pkt_ancount</i>()</p>
<dd>Return the packet&#8217;s an count .br <code>p</code>: the packet .br Returns the an count</dl>
<dl>
<dt> <i>ldns_pkt_nscount</i>()</p>
<dd>Return the packet&#8217;s ns count .br <code>p</code>: the packet .br Returns the ns count</dl>
<dl>
<dt> <i>ldns_pkt_arcount</i>()</p>
<dd>Return the packet&#8217;s ar count .br <code>p</code>: the packet .br Returns the ar count</dl>
<dl>
<dt> <i>ldns_pkt_answerfrom</i>()</p>
<dd>Return the packet&#8217;s answerfrom .br <code>p</code>: packet .br Returns the name of the server</dl>
<dl>
<dt> <i>ldns_pkt_querytime</i>()</p>
<dd>Return the packet&#8217;s querytime .br <code>p</code>: the packet .br Returns the querytime</dl>
<dl>
<dt> <i>ldns_pkt_size</i>()</p>
<dd>Return the packet&#8217;s size in bytes .br <code>p</code>: the packet .br Returns the size</dl>
<dl>
<dt> <i>ldns_pkt_tsig</i>()</p>
<dd>Return the packet&#8217;s tsig pseudo rr&#8217;s .br <code>p</code>: the packet .br Returns the tsig rr</dl>
<dl>
<dt> <i>ldns_pkt_question</i>()</p>
<dd>Return the packet&#8217;s question section .br <code>p</code>: the packet .br Returns the section</dl>
<dl>
<dt> <i>ldns_pkt_answer</i>()</p>
<dd>Return the packet&#8217;s answer section .br <code>p</code>: the packet .br Returns the section</dl>
<dl>
<dt> <i>ldns_pkt_authority</i>()</p>
<dd>Return the packet&#8217;s authority section .br <code>p</code>: the packet .br Returns the section</dl>
<dl>
<dt> <i>ldns_pkt_additional</i>()</p>
<dd>Return the packet&#8217;s additional section .br <code>p</code>: the packet .br Returns the section</dl>
<dl>
<dt> <i>ldns_pkt_get_section_clone</i>()</p>
<dd>return all the rr_list&#8217;s in the packet. Clone the lists, instead of returning pointers. .br <code>p</code>: the packet to look in .br <code>s</code>: what section(s) to return .br Returns ldns_rr_list with the rr&#8217;s or NULL if none were found</dl>
<dl>
<dt> <i>ldns_pkt_rr_list_by_name</i>()</p>
<dd>return all the rr with a specific name from a packet. Optionally specify from which section in the packet .br <code>p</code>: the packet .br <code>r</code>: the name .br <code>s</code>: the packet&#8217;s section .br Returns a list with the rr&#8217;s or NULL if none were found</dl>
<dl>
<dt> <i>ldns_pkt_rr_list_by_type</i>()</p>
<dd>return all the rr with a specific type from a packet. Optionally specify from which section in the packet .br <code>p</code>: the packet .br <code>t</code>: the type .br <code>s</code>: the packet&#8217;s section .br Returns a list with the rr&#8217;s or NULL if none were found</dl>
<dl>
<dt> <i>ldns_pkt_rr_list_by_name_and_type</i>()</p>
<dd>return all the rr with a specific type and type from a packet. Optionally specify from which section in the packet .br <code>packet</code>: the packet .br <code>ownername</code>: the name .br <code>type</code>: the type .br <code>sec</code>: the packet&#8217;s section .br Returns a list with the rr&#8217;s or NULL if none were found</dl>
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
