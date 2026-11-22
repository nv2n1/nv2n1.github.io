---

title: "asn1_get_bit_der(3)"
name: "asn1_get_bit_der"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_get_bit_der/"
description: "asn1_get_bit_der – API function"
---

<p> asn1_get_bit_der &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_get_bit_der(const unsigned char * </code><i>der</i><code>, int </code><i>der_len</i><code>, int * </code><i>ret_len</i><code>, unsigned char * </code><i>str</i><code>, int </code><i>str_size</i><code>, int * </code><i>bit_len</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const unsigned char * der</dt>
<dd> DER data to decode containing the BIT SEQUENCE.</dd>
<dt>int der_len</dt>
<dd> Length of DER data to decode.</dd>
<dt>int * ret_len</dt>
<dd> Output variable containing the length of the DER data.</dd>
<dt>unsigned char * str</dt>
<dd> Pre-allocated output buffer to put decoded BIT SEQUENCE in.</dd>
<dt>int str_size</dt>
<dd> Length of pre-allocated output buffer.</dd>
<dt>int * bit_len</dt>
<dd> Output variable containing the size of the BIT SEQUENCE.</dd></dl>
<h2>DESCRIPTION</h2>
<p> Extract a BIT SEQUENCE from DER data.</p>
<h2>RETURNS</h2>
<p> <code>ASN1_SUCCESS</code> on success, or an error.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006-2015 Free Software Foundation, Inc..<br/>
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>libtasn1</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>libtasn1</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info libtasn1</code></dd></dl>
<p> should give you access to the complete manual. As an alternative you may obtain the manual from:</p>
<dl>
<dt>
</dt><dd> <code><a rel="nofollow" href="http://www.gnu.org/software/libtasn1/manual/">http://www.gnu.org/software/libtasn1/manual/</a></code></dd></dl>
