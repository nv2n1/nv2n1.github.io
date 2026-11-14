---
title: "ldns_get_rr_list_addr_by_name(3)"
name: "ldns_get_rr_list_addr_by_name"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_get_rr_list_addr_by_name/"
description: "ldns_get_rr_list_addr_by_name, ldns_get_rr_list_name_by_addr"
---

<h2>NAME</h2>
<p> ldns_get_rr_list_addr_by_name, ldns_get_rr_list_name_by_addr </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_rr_list* ldns_get_rr_list_addr_by_name(ldns_resolver *r, ldns_rdf *name, ldns_rr_class c, uint16_t flags); </p>
<p> ldns_rr_list* ldns_get_rr_list_name_by_addr(ldns_resolver *r, ldns_rdf *addr, ldns_rr_class c, uint16_t flags); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_get_rr_list_addr_by_name</i>()</p>
<dd>Ask the resolver about name and return all address records .br <code>r</code>: the resolver to use .br <code>name</code>: the name to look for .br <code>c</code>: the class to use .br <code>flags</code>: give some optional flags to the query</dl>
<dl>
<dt> <i>ldns_get_rr_list_name_by_addr</i>()</p>
<dd>ask the resolver about the address and return the name .br <code>r</code>: the resolver to use .br <code>addr</code>: the addr to look for .br <code>c</code>: the class to use .br <code>flags</code>: give some optional flags to the query</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_rr_list</i>, <i>ldns_rr</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
