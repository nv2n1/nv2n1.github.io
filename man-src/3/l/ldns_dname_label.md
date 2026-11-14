---
title: "ldns_dname_label(3)"
name: "ldns_dname_label"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_dname_label/"
description: "ldns_dname_is_subdomain, ldns_dname_str_absolute, ldns_dname_label"
---

<h2>NAME</h2>
<p> ldns_dname_is_subdomain, ldns_dname_str_absolute, ldns_dname_label </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> bool ldns_dname_is_subdomain(const ldns_rdf *sub, const ldns_rdf *parent); </p>
<p> bool ldns_dname_str_absolute(const char *dname_str); </p>
<p> ldns_rdf * ldns_dname_label(const ldns_rdf *rdf, uint8_t labelpos); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_dname_is_subdomain</i>()</p>
<dd>test wether the name sub falls under parent (i.e. is a subdomain of parent). This function will return false if the given dnames are equal. .br <code>sub</code>: the name to test .br <code>parent</code>: the parent&#8217;s name .br Returns true if sub falls under parent, otherwise false</dl>
<dl>
<dt> <i>ldns_dname_str_absolute</i>()</p>
<dd>Checks whether the given dname string is absolute (i.e. ends with a &#8216;.&#8217;) .br <code>*dname_str</code>: a string representing the dname .br Returns true or false</dl>
<dl>
<dt> <i>ldns_dname_label</i>()</p>
<dd>look inside the rdf and if it is an LDNS_RDF_TYPE_DNAME try and retrieve a specific label. The labels are numbered starting from 0 (left most). .br <code>rdf</code>: the rdf to look in .br <code>labelpos</code>: return the label with this number .br Returns a ldns_rdf* with the label as name or NULL on error</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_dname</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
