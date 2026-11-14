---
title: "asn1_octet_der(3)"
name: "asn1_octet_der"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_octet_der/"
description: "asn1_octet_der – API function"
---

<h2>NAME</h2>
<p> asn1_octet_der &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>void asn1_octet_der(const unsigned char * </code><i>str</i><code>, int </code><i>str_len</i><code>, unsigned char * </code><i>der</i><code>, int * </code><i>der_len</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const unsigned char * str</p>
<dd> the input data.</p>
<dt>int str_len</p>
<dd> STR length (str[0]..str[*str_len-1]).</p>
<dt>unsigned char * der</p>
<dd> encoded string returned.</p>
<dt>int * der_len</p>
<dd> number of meaningful bytes of DER (der[0]..der[der_len-1]).</dl>
<h2>DESCRIPTION</h2>
<p> Creates a length-value DER encoding for the input data. The DER encoding of the input data will be placed in the <i>der</i> variable. </p>
<p> Note that the OCTET STRING tag is not included in the output. </p>
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
