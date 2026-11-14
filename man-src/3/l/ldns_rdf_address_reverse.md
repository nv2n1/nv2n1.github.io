---
title: "ldns_rdf_address_reverse(3)"
name: "ldns_rdf_address_reverse"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_rdf_address_reverse/"
description: "ldns_rdf_address_reverse"
---

<h2>NAME</h2>
<p> ldns_rdf_address_reverse </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_rdf* ldns_rdf_address_reverse(ldns_rdf *rd); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_rdf_address_reverse</i>()</p>
<dd>reverses an rdf, only actually useful for AAAA and A records. The returned rdf has the type LDNS_RDF_TYPE_DNAME! .br <code>*rd</code>: rdf to be reversed .br Returns the reversed rdf (a newly created rdf)</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_rdf</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
