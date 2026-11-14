---
title: "ldns_zone_glue_rr_list(3)"
name: "ldns_zone_glue_rr_list"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_zone_glue_rr_list/"
description: "ldns_zone_sort, ldns_zone_glue_rr_list"
---

<h2>NAME</h2>
<p> ldns_zone_sort, ldns_zone_glue_rr_list </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> void ldns_zone_sort(ldns_zone *zone); </p>
<p> ldns_rr_list* ldns_zone_glue_rr_list(const ldns_zone *z); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_zone_sort</i>()</p>
<dd>Sort the rrs in a zone, with the current impl. this is slow .br <code>zone</code>: the zone to sort</dl>
<dl>
<dt> <i>ldns_zone_glue_rr_list</i>()</p>
<dd>Retrieve all resource records from the zone that are glue records. The resulting list does are pointer references to the zone&#8217;s data. </p>
<p> Due to the current zone implementation (as a list of rr&#8217;s), this function is extremely slow. Another (probably better) way to do this is to use an ldns_dnssec_zone structure and the ldns_dnssec_mark_and_get_glue() function. </p>
<p> .br <code>z</code>: the zone to look for glue .br Returns the rr_list with the glue</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_zone</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
