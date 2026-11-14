---
title: "ldns_rdf_new(3)"
name: "ldns_rdf_new"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_rdf_new/"
description: "ldns_rdf_new, ldns_rdf_clone, ldns_rdf_new_frm_data, ldns_rdf_new_frm_str, ldns_rdf_new_frm_fp, ldns_rdf_free, ldns_rdf_deep_free, ldns_rdf_print"
---

<h2>NAME</h2>
<p> ldns_rdf_new, ldns_rdf_clone, ldns_rdf_new_frm_data, ldns_rdf_new_frm_str, ldns_rdf_new_frm_fp, ldns_rdf_free, ldns_rdf_deep_free, ldns_rdf_print </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> ldns_rdf* ldns_rdf_new(ldns_rdf_type type, size_t size, void *data); </p>
<p> ldns_rdf* ldns_rdf_clone(const ldns_rdf *rd); </p>
<p> ldns_rdf* ldns_rdf_new_frm_data(ldns_rdf_type type, size_t size, const void *data); </p>
<p> ldns_rdf* ldns_rdf_new_frm_str(ldns_rdf_type type, const char *str); </p>
<p> ldns_status ldns_rdf_new_frm_fp(ldns_rdf **r, ldns_rdf_type type, FILE *fp); </p>
<p> void ldns_rdf_free(ldns_rdf *rd); </p>
<p> void ldns_rdf_deep_free(ldns_rdf *rd); </p>
<p> void ldns_rdf_print(FILE *output, const ldns_rdf *rdf); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_rdf_new</i>()</p>
<dd>allocates a new rdf structure and fills it. This function DOES NOT copy the contents from the buffer, unlinke ldns_rdf_new_frm_data() .br <code>type</code>: type of the rdf .br <code>size</code>: size of the buffer .br <code>data</code>: pointer to the buffer to be copied .br Returns the new rdf structure or NULL on failure</dl>
<dl>
<dt> <i>ldns_rdf_clone</i>()</p>
<dd>clones a rdf structure. The data is copied. .br <code>rd</code>: rdf to be copied .br Returns a new rdf structure</dl>
<dl>
<dt> <i>ldns_rdf_new_frm_data</i>()</p>
<dd>allocates a new rdf structure and fills it. This function _does_ copy the contents from the buffer, unlinke ldns_rdf_new() .br <code>type</code>: type of the rdf .br <code>size</code>: size of the buffer .br <code>data</code>: pointer to the buffer to be copied .br Returns the new rdf structure or NULL on failure</dl>
<dl>
<dt> <i>ldns_rdf_new_frm_str</i>()</p>
<dd>creates a new rdf from a string. .br <code>type</code>: type to use .br <code>str</code>: string to use .br Returns ldns_rdf* or NULL in case of an error</dl>
<dl>
<dt> <i>ldns_rdf_new_frm_fp</i>()</p>
<dd>creates a new rdf from a file containing a string. .br <code>r</code>: the new rdf .br <code>type</code>: type to use .br <code>fp</code>: the file pointer to use .br Returns LDNS_STATUS_OK or the error</dl>
<dl>
<dt> <i>ldns_rdf_free</i>()</p>
<dd>frees a rdf structure, leaving the data pointer intact. .br <code>rd</code>: the pointer to be freed .br Returns void</dl>
<dl>
<dt> <i>ldns_rdf_deep_free</i>()</p>
<dd>frees a rdf structure _and_ frees the data. rdf should be created with _new_frm_data .br <code>rd</code>: the rdf structure to be freed .br Returns void</dl>
<dl>
<dt> <i>ldns_rdf_print</i>()</p>
<dd>Prints the data in the rdata field to the given file stream (in presentation format) </p>
<p> .br <code>output</code>: the file stream to print to .br <code>rdf</code>: the rdata field to print .br Returns void</dl>
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
