---
title: "asn1_expand_octet_string(3)"
name: "asn1_expand_octet_string"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_expand_octet_string/"
description: "asn1_expand_octet_string – API function"
---

<h2>NAME</h2>
<p> asn1_expand_octet_string &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_expand_octet_string(asn1_node </code><i>definitions</i><code>, asn1_node * </code><i>element</i><code>, const char * </code><i>octetName</i><code>, const char * </code><i>objectName</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>asn1_node definitions</p>
<dd> ASN1 definitions</p>
<dt>asn1_node * element</p>
<dd> pointer to an ASN1 structure</p>
<dt>const char * octetName</p>
<dd> name of the OCTECT STRING field to expand.</p>
<dt>const char * objectName</p>
<dd> name of the OBJECT IDENTIFIER field to use to define the type for expansion.</dl>
<h2>DESCRIPTION</h2>
<p> Expands an &quot;OCTET STRING&quot; element of a structure created from a DER decoding process (the <code>asn1_der_decoding()</code> function). The type used for expansion is the first one following the definition of the actual value of the OBJECT IDENTIFIER indicated by OBJECTNAME.</p>
<h2>RETURNS</h2>
<p> <code>ASN1_SUCCESS</code> if substitution OK, <code>ASN1_ELEMENT_NOT_FOUND</code> if <i>objectName</i> or <i>octetName</i> are not correct, <code>ASN1_VALUE_NOT_VALID</code> if it wasn&#8217;t possible to find the type to use for expansion, or other errors depending on DER decoding.</p>
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
