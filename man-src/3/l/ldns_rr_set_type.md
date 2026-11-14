---
title: "ldns_rr_set_type(3)"
name: "ldns_rr_set_type"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_rr_set_type/"
description: "ldns_rr_set_owner, ldns_rr_set_ttl, ldns_rr_set_type, ldns_rr_set_rd_count, ldns_rr_set_class, ldns_rr_set_rdf"
---

<h2>NAME</h2>
<p> ldns_rr_set_owner, ldns_rr_set_ttl, ldns_rr_set_type, ldns_rr_set_rd_count, ldns_rr_set_class, ldns_rr_set_rdf </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> void ldns_rr_set_owner(ldns_rr *rr, ldns_rdf *owner); </p>
<p> void ldns_rr_set_ttl(ldns_rr *rr, uint32_t ttl); </p>
<p> void ldns_rr_set_type(ldns_rr *rr, ldns_rr_type rr_type); </p>
<p> void ldns_rr_set_rd_count(ldns_rr *rr, size_t count); </p>
<p> void ldns_rr_set_class(ldns_rr *rr, ldns_rr_class rr_class); </p>
<p> ldns_rdf* ldns_rr_set_rdf(ldns_rr *rr, const ldns_rdf *f, size_t position); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_rr_set_owner</i>()</p>
<dd>sets the owner in the rr structure. .br <code>*rr</code>: rr to operate on .br <code>*owner</code>: set to this owner .br Returns void</dl>
<dl>
<dt> <i>ldns_rr_set_ttl</i>()</p>
<dd>sets the ttl in the rr structure. .br <code>*rr</code>: rr to operate on .br <code>ttl</code>: set to this ttl .br Returns void</dl>
<dl>
<dt> <i>ldns_rr_set_type</i>()</p>
<dd>sets the type in the rr. .br <code>*rr</code>: rr to operate on .br <code>rr_type</code>: set to this type .br Returns void</dl>
<dl>
<dt> <i>ldns_rr_set_rd_count</i>()</p>
<dd>sets the rd_count in the rr. .br <code>*rr</code>: rr to operate on .br <code>count</code>: set to this count .br Returns void</dl>
<dl>
<dt> <i>ldns_rr_set_class</i>()</p>
<dd>sets the class in the rr. .br <code>*rr</code>: rr to operate on .br <code>rr_class</code>: set to this class .br Returns void</dl>
<dl>
<dt> <i>ldns_rr_set_rdf</i>()</p>
<dd>sets a rdf member, it will be set on the position given. The old value is returned, like pop. .br <code>*rr</code>: the rr to operate on .br <code>*f</code>: the rdf to set .br <code>position</code>: the position the set the rdf .br Returns the old value in the rr, NULL on failyre</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_rr</i>, <i>ldns_rr_list</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
