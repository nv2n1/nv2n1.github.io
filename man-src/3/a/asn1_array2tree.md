---
title: "asn1_array2tree(3)"
name: "asn1_array2tree"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_array2tree/"
description: "asn1_array2tree – API function"
---

<h2>NAME</h2>
<p> asn1_array2tree &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_array2tree(const asn1_static_node * </code><i>array</i><code>, asn1_node * </code><i>definitions</i><code>, char * </code><i>errorDescription</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const asn1_static_node * array</p>
<dd> specify the array that contains ASN.1 declarations</p>
<dt>asn1_node * definitions</p>
<dd> return the pointer to the structure created by *ARRAY ASN.1 declarations</p>
<dt>char * errorDescription</p>
<dd> return the error description.</dl>
<h2>DESCRIPTION</h2>
<p> Creates the structures needed to manage the ASN.1 definitions.<br />
&nbsp;<wbr><i>array</i>&nbsp;<wbr>is a vector created by&nbsp;<wbr><code>asn1_parser2array()</code>.</p>
<h2>RETURNS</h2>
<p> <code>ASN1_SUCCESS</code> if structure was created correctly, <code>ASN1_ELEMENT_NOT_EMPTY</code> if * <i>definitions</i> not NULL, <code>ASN1_IDENTIFIER_NOT_FOUND</code> if in the file there is an identifier that is not defined (see <i>errorDescription</i> for more information), <code>ASN1_ARRAY_ERROR</code> if the array pointed by <i>array</i> is wrong.</p>
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
