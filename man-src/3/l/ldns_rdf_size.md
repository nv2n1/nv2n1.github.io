---
title: "ldns_rdf_size(3)"
name: "ldns_rdf_size"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_rdf_size/"
description: "ldns_rdf_size, ldns_rdf_get_type, ldns_rdf_data, ldns_rdf_compare"
---

<h2>NAME</h2>
<p> ldns_rdf_size, ldns_rdf_get_type, ldns_rdf_data, ldns_rdf_compare </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> size_t ldns_rdf_size(const ldns_rdf *rd); </p>
<p> ldns_rdf_type ldns_rdf_get_type(const ldns_rdf *rd); </p>
<p> uint8_t* ldns_rdf_data(const ldns_rdf *rd); </p>
<p> int ldns_rdf_compare(const ldns_rdf *rd1, const ldns_rdf *rd2); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_rdf_size</i>()</p>
<dd>returns the size of the rdf. .br <code>*rd</code>: the rdf to read from .br Returns uint16_t with the size</dl>
<dl>
<dt> <i>ldns_rdf_get_type</i>()</p>
<dd>returns the type of the rdf. We need to insert _get_ here to prevent conflict the the rdf_type TYPE. .br <code>*rd</code>: the rdf to read from .br Returns ldns_rdf_type with the type</dl>
<dl>
<dt> <i>ldns_rdf_data</i>()</p>
<dd>returns the data of the rdf. .br <code>*rd</code>: the rdf to read from </p>
<p> .br Returns uint8_t* pointer to the rdf&#8217;s data</dl>
<dl>
<dt> <i>ldns_rdf_compare</i>()</p>
<dd>compares two rdf&#8217;s on their wire formats. (To order dnames according to rfc4034, use ldns_dname_compare) .br <code>rd1</code>: the first one .br <code>rd2</code>: the second one .br Returns 0 if equal .br Returns -1 if rd1 comes before rd2 .br Returns +1 if rd2 comes before rd1</dl>
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
