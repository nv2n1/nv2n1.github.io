---
title: "ldns_rdf_set_data(3)"
name: "ldns_rdf_set_data"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_rdf_set_data/"
description: "ldns_rdf_set_size, ldns_rdf_set_type, ldns_rdf_set_data"
---

<h2>NAME</h2>
<p> ldns_rdf_set_size, ldns_rdf_set_type, ldns_rdf_set_data </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> void ldns_rdf_set_size(ldns_rdf *rd, size_t size); </p>
<p> void ldns_rdf_set_type(ldns_rdf *rd, ldns_rdf_type type); </p>
<p> void ldns_rdf_set_data(ldns_rdf *rd, void *data); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_rdf_set_size</i>()</p>
<dd>sets the size of the rdf. .br <code>*rd</code>: the rdf to operate on .br <code>size</code>: the new size .br Returns void</dl>
<dl>
<dt> <i>ldns_rdf_set_type</i>()</p>
<dd>sets the size of the rdf. .br <code>*rd</code>: the rdf to operate on .br <code>type</code>: the new type .br Returns void</dl>
<dl>
<dt> <i>ldns_rdf_set_data</i>()</p>
<dd>sets the size of the rdf. .br <code>*rd</code>: the rdf to operate on .br <code>*data</code>: pointer to the new data .br Returns void</dl>
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
