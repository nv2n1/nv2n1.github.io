---
title: "asn1_der_decoding(3)"
name: "asn1_der_decoding"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_der_decoding/"
description: "asn1_der_decoding – API function"
---

<h2>NAME</h2>
<p> asn1_der_decoding &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_der_decoding(asn1_node * </code><i>element</i><code>, const void * </code><i>ider</i><code>, int </code><i>ider_len</i><code>, char * </code><i>errorDescription</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>asn1_node * element</p>
<dd> pointer to an ASN1 structure.</p>
<dt>const void * ider</p>
<dd> vector that contains the DER encoding.</p>
<dt>int ider_len</p>
<dd> number of bytes of * <i>ider</i> : <i>ider</i> [0].. <i>ider</i> [len-1].</p>
<dt>char * errorDescription</p>
<dd> null-terminated string contains details when an error occurred.</dl>
<h2>DESCRIPTION</h2>
<p> Fill the structure * <i>element</i> with values of a DER encoding string. The structure must just be created with function <code>asn1_create_element()</code>. </p>
<p> Note that the * <i>element</i> variable is provided as a pointer for historical reasons.</p>
<h2>RETURNS</h2>
<p> <code>ASN1_SUCCESS</code> if DER encoding OK, <code>ASN1_ELEMENT_NOT_FOUND</code> if <i>ELEMENT</i> is <code>NULL</code>, and <code>ASN1_TAG_ERROR</code> or <code>ASN1_DER_ERROR</code> if the der encoding doesn&#8217;t match the structure name (* <i>ELEMENT</i> deleted).</p>
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
