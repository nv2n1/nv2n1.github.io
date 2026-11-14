---
title: "asn1_encode_simple_der(3)"
name: "asn1_encode_simple_der"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_encode_simple_der/"
description: "asn1_encode_simple_der – API function"
---

<h2>NAME</h2>
<p> asn1_encode_simple_der &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_encode_simple_der(unsigned int </code><i>etype</i><code>, const unsigned char * </code><i>str</i><code>, unsigned int </code><i>str_len</i><code>, unsigned char * </code><i>tl</i><code>, unsigned int * </code><i>tl_len</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>unsigned int etype</p>
<dd> The type of the string to be encoded (ASN1_ETYPE_)</p>
<dt>const unsigned char * str</p>
<dd> the string data.</p>
<dt>unsigned int str_len</p>
<dd> the string length</p>
<dt>unsigned char * tl</p>
<dd> the encoded tag and length</p>
<dt>unsigned int * tl_len</p>
<dd> the bytes of the <i>tl</i> field</dl>
<h2>DESCRIPTION</h2>
<p> Creates the DER encoding for various simple ASN.1 types like strings etc. It stores the tag and length in <i>tl</i> , which should have space for at least <code>ASN1_MAX_TL_SIZE</code> bytes. Initially <i>tl_len</i> should contain the size of <i>tl</i> . </p>
<p> The complete DER encoding should consist of the value in <i>tl</i> appended with the provided <i>str</i> .</p>
<h2>RETURNS</h2>
<p> <code>ASN1_SUCCESS</code> if successful or an error value.</p>
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
