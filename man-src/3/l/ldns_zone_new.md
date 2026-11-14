---
title: "ldns_zone_new(3)"
name: "ldns_zone_new"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_zone_new/"
description: "ldns_zone_new, ldns_zone_deep_free, ldns_zone_new_frm_fp, ldns_zone_new_frm_fp_l"
---

<h2>NAME</h2>
<p> ldns_zone_new, ldns_zone_deep_free, ldns_zone_new_frm_fp, ldns_zone_new_frm_fp_l </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_zone * ldns_zone_new(void); </p>
<p> void ldns_zone_deep_free(ldns_zone *zone); </p>
<p> ldns_status ldns_zone_new_frm_fp(ldns_zone **z, FILE *fp, ldns_rdf *origin, uint32_t ttl, ldns_rr_class c); </p>
<p> ldns_status ldns_zone_new_frm_fp_l(ldns_zone **z, FILE *fp, ldns_rdf *origin, uint32_t ttl, ldns_rr_class c, int *line_nr); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_zone_new</i>()</p>
<dd>create a new ldns_zone structure .br Returns a pointer to a ldns_zone structure</dl>
<dl>
<dt> <i>ldns_zone_deep_free</i>()</p>
<dd>Frees the allocated memory for the zone, the soa rr in it, and the rr_list structure in it, including the rr&#8217;s in that. etc. .br <code>zone</code>: the zone to free</dl>
<dl>
<dt> <i>ldns_zone_new_frm_fp</i>()</p>
<dd>Create a new zone from a file .br <code>z</code>: the new zone .br <code>*fp</code>: the filepointer to use .br <code>*origin</code>: the zones&#8217; origin .br <code>ttl</code>: default ttl to use .br <code>c</code>: default class to use (IN) </p>
<p> .br Returns ldns_status mesg with an error or LDNS_STATUS_OK</dl>
<dl>
<dt> <i>ldns_zone_new_frm_fp_l</i>()</p>
<dd>Create a new zone from a file, keep track of the line numbering .br <code>z</code>: the new zone .br <code>*fp</code>: the filepointer to use .br <code>*origin</code>: the zones&#8217; origin .br <code>ttl</code>: default ttl to use .br <code>c</code>: default class to use (IN) .br <code>line_nr</code>: used for error msg, to get to the line number </p>
<p> .br Returns ldns_status mesg with an error or LDNS_STATUS_OK</dl>
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
