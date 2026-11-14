---
title: "ldns_zone_push_rr_list(3)"
name: "ldns_zone_push_rr_list"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_zone_push_rr_list/"
description: "ldns_zone_push_rr, ldns_zone_push_rr_list"
---

<h2>NAME</h2>
<p> ldns_zone_push_rr, ldns_zone_push_rr_list </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> bool ldns_zone_push_rr(ldns_zone *z, ldns_rr *rr); </p>
<p> bool ldns_zone_push_rr_list(ldns_zone *z, ldns_rr_list *list); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_zone_push_rr</i>()</p>
<dd>push an single rr to a zone structure. This function use pointer copying, so the rr_list structure inside z is modified! .br <code>z</code>: the zone to add to .br <code>rr</code>: the rr to add .br Returns a true on succes otherwise falsed</dl>
<dl>
<dt> <i>ldns_zone_push_rr_list</i>()</p>
<dd>push an rrlist to a zone structure. This function use pointer copying, so the rr_list structure inside z is modified! .br <code>z</code>: the zone to add to .br <code>list</code>: the list to add .br Returns a true on succes otherwise falsed</dl>
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
