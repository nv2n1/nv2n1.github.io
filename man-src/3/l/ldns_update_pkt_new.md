---
title: "ldns_update_pkt_new(3)"
name: "ldns_update_pkt_new"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_update_pkt_new/"
description: "ldns_update_pkt_new"
---

<h2>NAME</h2>
<p> ldns_update_pkt_new </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_pkt* ldns_update_pkt_new(ldns_rdf *zone_rdf, ldns_rr_class clas, ldns_rr_list *pr_rrlist, ldns_rr_list *up_rrlist, ldns_rr_list *ad_rrlist); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_update_pkt_new</i>()</p>
<dd>create an update packet from zone name, class and the rr lists .br <code>zone_rdf</code>: name of the zone .br <code>clas</code>: zone class .br <code>pr_rrlist</code>: list of Prerequisite Section RRs .br <code>up_rrlist</code>: list of Updates Section RRs .br <code>ad_rrlist</code>: list of Additional Data Section RRs (currently unused) .br Returns the new packet</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_update_pkt_tsig_add</i>, <i>ldns_update_pkt_tsig_add</i>, <i>ldns_update_zocount</i>, <i>ldns_update_prcount</i>, <i>ldns_update_upcount</i>, <i>ldns_update_adcount</i>, <i>ldns_update_set_zocount</i>, <i>ldns_update_set_prcount</i>, <i>ldns_update_set_upcount</i>, <i>ldns_update_set_adcount</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
