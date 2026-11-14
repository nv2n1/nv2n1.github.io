---
title: "ldns_dnssec_verify_denial(3)"
name: "ldns_dnssec_verify_denial"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_dnssec_verify_denial/"
description: "ldns_dnssec_verify_denial, ldns_dnssec_verify_denial_nsec3"
---

<h2>NAME</h2>
<p> ldns_dnssec_verify_denial, ldns_dnssec_verify_denial_nsec3 </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_status ldns_dnssec_verify_denial(ldns_rr *rr, ldns_rr_list *nsecs, ldns_rr_list *rrsigs); </p>
<p> ldns_status ldns_dnssec_verify_denial_nsec3(ldns_rr *rr, ldns_rr_list *nsecs, ldns_rr_list *rrsigs, ldns_pkt_rcode packet_rcode, ldns_rr_type packet_qtype, bool packet_nodata); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_dnssec_verify_denial</i>()</p>
<dd>denial is not just a river in egypt </p>
<p> .br <code>rr</code>: The (query) RR to check the denial of existence for .br <code>nsecs</code>: The list of NSEC RRs that are supposed to deny the existence of the RR .br <code>rrsigs</code>: The RRSIG RR covering the NSEC RRs .br Returns LDNS_STATUS_OK if the NSEC RRs deny the existence, error code containing the reason they do not otherwise</dl>
<dl>
<dt> <i>ldns_dnssec_verify_denial_nsec3</i>()</p>
<dd>Denial of existence using NSEC3 records Since NSEC3 is a bit more complicated than normal denial, some context arguments are needed </p>
<p> .br <code>rr</code>: The (query) RR to check the denial of existence for .br <code>nsecs</code>: The list of NSEC3 RRs that are supposed to deny the existence of the RR .br <code>rrsigs</code>: The RRSIG rr covering the NSEC RRs .br <code>packet_rcode</code>: The RCODE value of the packet that provided the NSEC3 RRs .br <code>packet_qtype</code>: The original query RR type .br <code>packet_nodata</code>: True if the providing packet had an empty ANSWER section .br Returns LDNS_STATUS_OK if the NSEC3 RRs deny the existence, error code containing the reason they do not otherwise</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_dnssec_trust_tree</i>, <i>ldns_dnssec_data_chain</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
