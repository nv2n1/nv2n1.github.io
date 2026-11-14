---
title: "asn1_decode_simple_ber(3)"
name: "asn1_decode_simple_ber"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_decode_simple_ber/"
description: "asn1_decode_simple_ber – API function"
---

<h2>NAME</h2>
<p> asn1_decode_simple_ber &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_decode_simple_ber(unsigned int </code><i>etype</i><code>, const unsigned char * </code><i>der</i><code>, unsigned int </code><i>_der_len</i><code>, unsigned char ** </code><i>str</i><code>, unsigned int * </code><i>str_len</i><code>, unsigned int * </code><i>ber_len</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>unsigned int etype</p>
<dd> The type of the string to be encoded (ASN1_ETYPE_)</p>
<dt>const unsigned char * der</p>
<dd> the encoded string</p>
<dt>unsigned int _der_len</p>
<dd> the bytes of the encoded string</p>
<dt>unsigned char ** str</p>
<dd> a pointer to the data</p>
<dt>unsigned int * str_len</p>
<dd> the length of the data</p>
<dt>unsigned int * ber_len</p>
<dd> the total length occupied by BER (may be <code>NULL</code>)</dl>
<h2>DESCRIPTION</h2>
<p> Decodes a BER encoded type. The output is an allocated value of the data. This decodes BER STRINGS only. Other types are decoded as DER.</p>
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
