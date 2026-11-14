---
title: "ldns_zone_set_soa(3)"
name: "ldns_zone_set_soa"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_zone_set_soa/"
description: "ldns_zone_set_rrs, ldns_zone_set_soa"
---

<h2>NAME</h2>
<p> ldns_zone_set_rrs, ldns_zone_set_soa </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> void ldns_zone_set_rrs(ldns_zone *z, ldns_rr_list *rrlist); </p>
<p> void ldns_zone_set_soa(ldns_zone *z, ldns_rr *soa); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_zone_set_rrs</i>()</p>
<dd>Set the zone&#8217;s contents .br <code>z</code>: the zone to put the new soa in .br <code>rrlist</code>: the rrlist to use</dl>
<dl>
<dt> <i>ldns_zone_set_soa</i>()</p>
<dd>Set the zone&#8217;s soa record .br <code>z</code>: the zone to put the new soa in .br <code>soa</code>: the soa to set</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_zone</i>, <i>ldns_zone_rrs</i>, <i>ldns_zone_soa</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
