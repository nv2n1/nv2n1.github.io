---
title: "ldns_dnssec_data_chain(3)"
name: "ldns_dnssec_data_chain"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_dnssec_data_chain/"
description: "ldns_dnssec_data_chain, ldns_dnssec_data_chain_struct, ldns_dnssec_trust_tree"
---

<h2>NAME</h2>
<p> ldns_dnssec_data_chain, ldns_dnssec_data_chain_struct, ldns_dnssec_trust_tree </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p>&nbsp;<wbr>ldns_dnssec_data_chain_struct(); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_dnssec_data_chain</i></p>
<dd>
<dd>Chain structure that contains all DNSSEC data needed to<br />
 verify an rrset<br />
 struct ldns_dnssec_data_chain_struct<br />
 {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr_list *rrset;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr_list *signatures;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr_type parent_type;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_dnssec_data_chain *parent;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_pkt_rcode packet_rcode;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr_type packet_qtype;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>bool packet_nodata;</p>
<p> }; </p>
<p> typedef struct ldns_dnssec_data_chain_struct ldns_dnssec_data_chain;</dl>
<dl>
<dt> <i>ldns_dnssec_data_chain_struct</i>()</dl>
<dl>
<dt> <i>ldns_dnssec_trust_tree</i></p>
<dd>
<dd>Tree structure that contains the relation of DNSSEC data,<br />
 and their cryptographic status. </p>
<p> This tree is derived from a data_chain, and can be used<br />
 to look whether there is a connection between an RRSET<br />
 and a trusted key. The tree only contains pointers to the<br />
 data_chain, and therefore one should *never* free() the<br />
 data_chain when there is still a trust tree derived from<br />
 that chain. </p>
<p> Example tree: </p>
<p>&nbsp;<wbr>key&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>key&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>key </p>
<p>\&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/ </p>
<p>&nbsp;<wbr>\&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>\&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&nbsp;<wbr>/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ds </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>key </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>key </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>| </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>rr </p>
<p> For each signature there is a parent; if the parent<br />
 pointer is null, it couldn&#8217;t be found and there was no<br />
 denial; otherwise is a tree which contains either a<br />
 DNSKEY, a DS, or a NSEC rr<br />
 struct ldns_dnssec_trust_tree_struct<br />
 {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr *rr;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/* the complete rrset this rr was in */</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr_list *rrset;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_dnssec_trust_tree *parents[LDNS_DNSSEC_TRUST_TREE_MAX_PARENTS];</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_status parent_status[LDNS_DNSSEC_TRUST_TREE_MAX_PARENTS];</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/** for debugging, add signatures too (you might want</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> those if they contain errors) */</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr *parent_signature[LDNS_DNSSEC_TRUST_TREE_MAX_PARENTS];</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>size_t parent_count;</p>
<p> }; </p>
<p> typedef struct ldns_dnssec_trust_tree_struct ldns_dnssec_trust_tree;</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_dnssec_data_chain_new</i>, <i>ldns_dnssec_trust_tree_new</i>, <i>ldns_dnssec_verify_denial</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
