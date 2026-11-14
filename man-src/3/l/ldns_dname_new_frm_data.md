---
title: "ldns_dname_new_frm_data(3)"
name: "ldns_dname_new_frm_data"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_dname_new_frm_data/"
description: "ldns_dname_new, ldns_dname_new_frm_str, ldns_dname_new_frm_data"
---

<h2>NAME</h2>
<p> ldns_dname_new, ldns_dname_new_frm_str, ldns_dname_new_frm_data </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_rdf* ldns_dname_new(uint16_t s, void *data); </p>
<p> ldns_rdf* ldns_dname_new_frm_str(const char *str); </p>
<p> ldns_rdf* ldns_dname_new_frm_data(uint16_t size, const void *data); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_dname_new</i>()</p>
<dd>Create a new dname rdf from a string .br <code>s</code>: the size of the new dname .br <code>*data</code>: pointer to the actual data </p>
<p> .br Returns ldns_rdf*</dl>
<dl>
<dt> <i>ldns_dname_new_frm_str</i>()</p>
<dd>creates a new dname rdf from a string. .br <code>str</code>: string to use .br Returns ldns_rdf* or NULL in case of an error</dl>
<dl>
<dt> <i>ldns_dname_new_frm_data</i>()</p>
<dd>Create a new dname rdf from data (the data is copied) .br <code>size</code>: the size of the data .br <code>*data</code>: pointer to the actual data </p>
<p> .br Returns ldns_rdf*</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_dname</i>, <i>ldns_pkt_query_new_frm_str</i>, <i>ldns_rdf_new_frm_str</i>, <i>ldns_rr_new_frm_str</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
