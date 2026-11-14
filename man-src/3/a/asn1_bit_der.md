---
title: "asn1_bit_der(3)"
name: "asn1_bit_der"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_bit_der/"
description: "asn1_bit_der – API function"
---

<h2>NAME</h2>
<p> asn1_bit_der &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>void asn1_bit_der(const unsigned char * </code><i>str</i><code>, int </code><i>bit_len</i><code>, unsigned char * </code><i>der</i><code>, int * </code><i>der_len</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const unsigned char * str</p>
<dd> BIT string.</p>
<dt>int bit_len</p>
<dd> number of meaningful bits in STR.</p>
<dt>unsigned char * der</p>
<dd> string returned.</p>
<dt>int * der_len</p>
<dd> number of meaningful bytes of DER (der[0]..der[ans_len-1]).</dl>
<h2>DESCRIPTION</h2>
<p> Creates a length-value DER encoding for the input data as it would have been for a BIT STRING. The DER encoded data will be copied in <i>der</i> . </p>
<p> Note that the BIT STRING tag is not included in the output. </p>
<p> This function does not return any value because it is expected that <i>der_len</i> will contain enough bytes to store the string plus the DER encoding. The DER encoding size can be obtained using <code>asn1_length_der()</code>.</p>
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
