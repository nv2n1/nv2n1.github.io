---
title: "ldns_rr_ttl(3)"
name: "ldns_rr_ttl"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_rr_ttl/"
description: "ldns_rr_rdf, ldns_rr_owner, ldns_rr_rd_count, ldns_rr_ttl, ldns_rr_get_class"
---

<h2>NAME</h2>
<p> ldns_rr_rdf, ldns_rr_owner, ldns_rr_rd_count, ldns_rr_ttl, ldns_rr_get_class </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_rdf* ldns_rr_rdf(const ldns_rr *rr, size_t nr); </p>
<p> ldns_rdf* ldns_rr_owner(const ldns_rr *rr); </p>
<p> size_t ldns_rr_rd_count(const ldns_rr *rr); </p>
<p> uint32_t ldns_rr_ttl(const ldns_rr *rr); </p>
<p> ldns_rr_class ldns_rr_get_class(const ldns_rr *rr); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_rr_rdf</i>()</p>
<dd>returns the rdata field member counter. .br <code>*rr</code>: rr to operate on .br <code>nr</code>: the number of the rdf to return .br Returns ldns_rdf *</dl>
<dl>
<dt> <i>ldns_rr_owner</i>()</p>
<dd>returns the owner name of an rr structure. .br <code>*rr</code>: rr to operate on .br Returns ldns_rdf *</dl>
<dl>
<dt> <i>ldns_rr_rd_count</i>()</p>
<dd>returns the rd_count of an rr structure. .br <code>*rr</code>: the rr to read from .br Returns the rd count of the rr</dl>
<dl>
<dt> <i>ldns_rr_ttl</i>()</p>
<dd>returns the ttl of an rr structure. .br <code>*rr</code>: the rr to read from .br Returns the ttl of the rr</dl>
<dl>
<dt> <i>ldns_rr_get_class</i>()</p>
<dd>returns the class of the rr. .br <code>*rr</code>: the rr to read from .br Returns the class of the rr</dl>
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
