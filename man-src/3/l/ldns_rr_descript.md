---
title: "ldns_rr_descript(3)"
name: "ldns_rr_descript"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_rr_descript/"
description: "ldns_rr_descriptor, ldns_rr_descript, ldns_rr_descriptor_minimum, ldns_rr_descriptor_maximum, ldns_rr_descriptor_field_type"
---

<h2>NAME</h2>
<p> ldns_rr_descriptor, ldns_rr_descript, ldns_rr_descriptor_minimum, ldns_rr_descriptor_maximum, ldns_rr_descriptor_field_type </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> const ldns_rr_descriptor* ldns_rr_descript(uint16_t type); </p>
<p> size_t ldns_rr_descriptor_minimum(const ldns_rr_descriptor *descriptor); </p>
<p> size_t ldns_rr_descriptor_maximum(const ldns_rr_descriptor *descriptor); </p>
<p> ldns_rdf_type ldns_rr_descriptor_field_type(const ldns_rr_descriptor *descriptor, size_t field); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_rr_descriptor</i></p>
<dd>
<dd>Contains all information about resource record types. </p>
<p> This structure contains, for all rr types, the rdata fields that are defined.<br />
 struct ldns_struct_rr_descriptor<br />
 {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>Type of the RR that is described here:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr_type _type;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>Textual name of the RR type.:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>const char *_name;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>Minimum number of rdata fields in the RRs of this type.:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>uint8_t _minimum;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>Maximum number of rdata fields in the RRs of this type.:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>uint8_t _maximum;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>Wireformat specification for the rr, i.e. the types of rdata fields in their respective order.:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>const ldns_rdf_type *_wireformat;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>Special rdf types:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rdf_type _variable;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>Specifies whether compression can be used for dnames in this RR type.:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ldns_rr_compress _compress;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>The number of DNAMEs in the _wireformat string, for parsing.:</code></p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>uint8_t _dname_count;</p>
<p> };<br />
 typedef struct ldns_struct_rr_descriptor ldns_rr_descriptor;</dl>
<dl>
<dt> <i>ldns_rr_descript</i>()</p>
<dd>returns the resource record descriptor for the given rr type. </p>
<p> .br <code>type</code>: the type value of the rr type .br Returns the ldns_rr_descriptor for this type</dl>
<dl>
<dt> <i>ldns_rr_descriptor_minimum</i>()</p>
<dd>returns the minimum number of rdata fields of the rr type this descriptor describes. </p>
<p> .br <code>descriptor</code>: for an rr type .br Returns the minimum number of rdata fields</dl>
<dl>
<dt> <i>ldns_rr_descriptor_maximum</i>()</p>
<dd>returns the maximum number of rdata fields of the rr type this descriptor describes. </p>
<p> .br <code>descriptor</code>: for an rr type .br Returns the maximum number of rdata fields</dl>
<dl>
<dt> <i>ldns_rr_descriptor_field_type</i>()</p>
<dd>returns the rdf type for the given rdata field number of the rr type for the given descriptor. </p>
<p> .br <code>descriptor</code>: for an rr type .br <code>field</code>: the field number .br Returns the rdf type for the field</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_rr</i>, <i>ldns_rdf</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
