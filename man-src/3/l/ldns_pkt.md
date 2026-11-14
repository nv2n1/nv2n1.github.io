---
title: "ldns_pkt(3)"
name: "ldns_pkt"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_pkt/"
description: "ldns_pkt, ldns_pkt_section, ldns_pkt_type"
---

<h2>NAME</h2>
<p> ldns_pkt, ldns_pkt_section, ldns_pkt_type </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p>&nbsp;<wbr>ldns_pkt_section(); </p>
<p>&nbsp;<wbr>ldns_pkt_type(); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_pkt</i></p>
<dd>
<dd>DNS packet </p>
<p> This structure contains a complete DNS packet (either a query or an answer) </p>
<p> It is the complete representation of what you actually send to a<br />
 nameserver, and what it sends back (assuming you are the client here).<br />
 struct ldns_struct_pkt<br />
 {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>Header section:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_hdr *_header;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/* extra items needed in a packet */</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>The size of the wire format of the packet in octets:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rdf *_answerfrom;</p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>Timestamp of the time the packet was sent or created:</code><br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>struct timeval timestamp;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>The duration of the query this packet is an answer to:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>uint32_t _querytime;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>The size of the wire format of the packet in octets:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>size_t _size;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>Optional tsig rr:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr *_tsig_rr;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>EDNS0 available buffer size, see RFC2671:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>uint16_t _edns_udp_size;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>EDNS0 Extended rcode:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>uint8_t _edns_extended_rcode;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>EDNS Version:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>uint8_t _edns_version;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>Reserved EDNS data bits:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>uint16_t _edns_z;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>Arbitrary EDNS rdata:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rdf *_edns_data;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>Question section:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr_list<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>*_question;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>Answer section:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr_list<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>*_answer;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>Authority section:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr_list<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>*_authority;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>Additional section:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr_list<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>*_additional;</p>
<p> };<br />
 typedef struct ldns_struct_pkt ldns_pkt;</dl>
<dl>
<dt> <i>ldns_pkt_section</i>()</dl>
<dl>
<dt> <i>ldns_pkt_type</i>()</dl>
<h2>AUTHOR</h2>
<dd>The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_pkt_new</i>, <i>ldns_pkt_free</i>, <i>ldns_pkt_print</i>, <i>ldns_pkt_query_new</i>, <i>ldns_pkt_query_new_frm_str</i>, <i>ldns_pkt_reply_type</i>, <i>ldns_pkt_id</i>, <i>ldns_pkt_qr</i>, <i>ldns_pkt_aa</i>, <i>ldns_pkt_tc</i>, <i>ldns_pkt_rd</i>, <i>ldns_pkt_cd</i>, <i>ldns_pkt_ra</i>, <i>ldns_pkt_ad</i>, <i>ldns_pkt_get_opcode</i>, <i>ldns_pkt_get_rcode</i>, <i>ldns_pkt_qdcount</i>, <i>ldns_pkt_ancount</i>, <i>ldns_pkt_nscount</i>, <i>ldns_pkt_arcount</i>, <i>ldns_pkt_answerfrom</i>, <i>ldns_pkt_querytime</i>, <i>ldns_pkt_size</i>, <i>ldns_pkt_tsig</i>, <i>ldns_pkt_question</i>, <i>ldns_pkt_answer</i>, <i>ldns_pkt_authority</i>, <i>ldns_pkt_additional</i>, <i>ldns_pkt_get_section_clone</i>, <i>ldns_pkt_rr_list_by_name</i>, <i>ldns_pkt_rr_list_by_type</i>, <i>ldns_pkt_rr_list_by_name_and_type</i>, <i>ldns_pkt_set_flags</i>, <i>ldns_pkt_set_id</i>, <i>ldns_pkt_set_qr</i>, <i>ldns_pkt_set_aa</i>, <i>ldns_pkt_set_tc</i>, <i>ldns_pkt_set_rd</i>, <i>ldns_pkt_set_cd</i>, <i>ldns_pkt_set_ra</i>, <i>ldns_pkt_set_ad</i>, <i>ldns_pkt_set_opcode</i>, <i>ldns_pkt_set_rcode</i>, <i>ldns_pkt_set_qdcount</i>, <i>ldns_pkt_set_ancount</i>, <i>ldns_pkt_set_nscount</i>, <i>ldns_pkt_set_arcount</i>, <i>ldns_pkt_set_answerfrom</i>, <i>ldns_pkt_set_querytime</i>, <i>ldns_pkt_set_size</i>, <i>ldns_pkt_set_section_count</i>, <i>ldns_pkt_set_tsig</i>, <i>ldns_pkt_edns</i>, <i>ldns_pkt_edns_udp_size</i>, <i>ldns_pkt_edns_extended_rcode</i>, <i>ldns_pkt_edns_version</i>, <i>ldns_pkt_edns_z</i>, <i>ldns_pkt_edns_data</i>, <i>ldns_pkt_set_edns_udp_size</i>, <i>ldns_pkt_set_edns_extended_rcode</i>, <i>ldns_pkt_set_edns_version</i>, <i>ldns_pkt_set_edns_z</i>, <i>ldns_pkt_set_edns_data</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
