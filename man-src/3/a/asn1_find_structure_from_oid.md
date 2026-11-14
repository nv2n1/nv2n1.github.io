---
title: "asn1_find_structure_from_oid(3)"
name: "asn1_find_structure_from_oid"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_find_structure_from_oid/"
description: "asn1_find_structure_from_oid – API function"
---

<h2>NAME</h2>
<p> asn1_find_structure_from_oid &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>const char * asn1_find_structure_from_oid(asn1_node </code><i>definitions</i><code>, const char * </code><i>oidValue</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>asn1_node definitions</p>
<dd> ASN1 definitions</p>
<dt>const char * oidValue</p>
<dd> value of the OID to search (e.g. &quot;1.2.3.4&quot;).</dl>
<h2>DESCRIPTION</h2>
<p> Search the structure that is defined just after an OID definition.</p>
<h2>RETURNS</h2>
<p> <code>NULL</code> when <i>oidValue</i> not found, otherwise the pointer to a constant string that contains the element name defined just after the OID.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006-2015 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>libtasn1</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>libtasn1</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info libtasn1</code></dl>
<p> should give you access to the complete manual. As an alternative you may obtain the manual from:</p>
<dl>
<dt>
<dd> <code><a rel="nofollow" href="http://www.gnu.org/software/libtasn1/manual/">http://www.gnu.org/software/libtasn1/manual/</a></code></dl>
<h2>Index</h2>
