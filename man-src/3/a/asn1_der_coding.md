---
title: "asn1_der_coding(3)"
name: "asn1_der_coding"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_der_coding/"
description: "asn1_der_coding – API function"
---

<h2>NAME</h2>
<p> asn1_der_coding &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_der_coding(asn1_node </code><i>element</i><code>, const char * </code><i>name</i><code>, void * </code><i>ider</i><code>, int * </code><i>len</i><code>, char * </code><i>ErrorDescription</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>asn1_node element</p>
<dd> pointer to an ASN1 element</p>
<dt>const char * name</p>
<dd> the name of the structure you want to encode (it must be inside *POINTER).</p>
<dt>void * ider</p>
<dd> vector that will contain the DER encoding. DER must be a pointer to memory cells already allocated.</p>
<dt>int * len</p>
<dd> number of bytes of * <i>ider</i> : <i>ider</i> [0].. <i>ider</i> [len-1], Initialy holds the sizeof of der vector.</p>
<dt>char * ErrorDescription</p>
<dd> return the error description or an empty string if success.</dl>
<h2>DESCRIPTION</h2>
<p> Creates the DER encoding for the NAME structure (inside *POINTER structure).</p>
<h2>RETURNS</h2>
<p> <code>ASN1_SUCCESS</code> if DER encoding OK, <code>ASN1_ELEMENT_NOT_FOUND</code> if <i>name</i> is not a valid element, <code>ASN1_VALUE_NOT_FOUND</code> if there is an element without a value, <code>ASN1_MEM_ERROR</code> if the <i>ider</i> vector isn&#8217;t big enough and in this case <i>len</i> will contain the length needed.</p>
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
