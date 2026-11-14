---
title: "ldns_dnssec_rrs(3)"
name: "ldns_dnssec_rrs"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_dnssec_rrs/"
description: "ldns_dnssec_zone, ldns_dnssec_name, ldns_dnssec_rrs, ldns_dnssec_rrsets"
---

<h2>NAME</h2>
<p> ldns_dnssec_zone, ldns_dnssec_name, ldns_dnssec_rrs, ldns_dnssec_rrsets </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p>&nbsp;<wbr>ldns_dnssec_zone(); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_dnssec_zone</i>()</dl>
<dl>
<dt> <i>ldns_dnssec_name</i></p>
<dd>
<dd>Structure containing all resource records for a domain name<br />
 Including the derived NSEC3, if present<br />
 struct ldns_struct_dnssec_name<br />
 {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/**</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * pointer to a dname containing the name.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * Usually points to the owner name of the first RR of the first RRset</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> */</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rdf *name;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/** </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * Usually, the name is a pointer to the owner name of the first rr for</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * this name, but sometimes there is no actual data to point to, </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * for instance in</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * names representing empty nonterminals. If so, set alloced to true to</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * indicate that this data must also be freed when the name is freed</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> */</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>bool name_alloced;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/**</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * The rrsets for this name</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> */</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_dnssec_rrsets *rrsets;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/**</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * NSEC pointing to the next name (or NSEC3 pointing to the next NSEC3)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> */</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr *nsec;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/**</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * signatures for the NSEC record</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> */</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_dnssec_rrs *nsec_signatures;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/**</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * Unlike what the name is_glue suggests, this field is set to true by</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * ldns_dnssec_zone_mark_glue() or ldns_dnssec_zone_mark_and_get_glue()</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * when the name, this dnssec_name struct represents, is occluded.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * Names that contain other occluded rrsets and records with glue on</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * the delegation point will NOT have this bool set to true.</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * This field should NOT be read directly, but only via the </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * ldns_dnssec_name_is_glue() function!</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> */</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>bool is_glue;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/**</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> * pointer to store the hashed name (only used when in an NSEC3 zone</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> */</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rdf *hashed_name;</p>
<p> }; </p>
<p> typedef struct ldns_struct_dnssec_name ldns_dnssec_name;</dl>
<dl>
<dt> <i>ldns_dnssec_rrs</i></p>
<dd>
<dd>Singly linked list of rrs<br />
 struct ldns_struct_dnssec_rrs<br />
 {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr *rr;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_dnssec_rrs *next;</p>
<p> }; </p>
<p> typedef struct ldns_struct_dnssec_rrs ldns_dnssec_rrs;</dl>
<dl>
<dt> <i>ldns_dnssec_rrsets</i></p>
<dd>
<dd>Singly linked list of RRsets<br />
 struct ldns_struct_dnssec_rrsets<br />
 {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_dnssec_rrs *rrs;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr_type type;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_dnssec_rrs *signatures;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_dnssec_rrsets *next;</p>
<p> }; </p>
<p> typedef struct ldns_struct_dnssec_rrsets ldns_dnssec_rrsets;</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_dnssec_zone_new</i>, <i>ldns_dnssec_name_new</i>, <i>ldns_dnssec_rrs_new</i>, <i>ldns_dnssec_rrsets_new</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
