---
title: "ldns_create_nsec(3)"
name: "ldns_create_nsec"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_create_nsec/"
description: "ldns_create_nsec"
---

<h2>NAME</h2>
<p> ldns_create_nsec </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_rr * ldns_create_nsec(ldns_rdf *cur_owner, ldns_rdf *next_owner, ldns_rr_list *rrs); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_create_nsec</i>()</p>
<dd>Create a NSEC record .br <code>cur_owner</code>: the current owner which should be taken as the starting point .br <code>next_owner</code>: the rrlist which the nsec rr should point to .br <code>rrs</code>: all rrs from the zone, to find all RR types of cur_owner in .br Returns a ldns_rr with the nsec record in it</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_sign_public</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
