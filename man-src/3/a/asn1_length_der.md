---
title: "asn1_length_der(3)"
name: "asn1_length_der"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_length_der/"
description: "asn1_length_der – API function"
---

<h2>NAME</h2>
<p> asn1_length_der &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>void asn1_length_der(unsigned long int </code><i>len</i><code>, unsigned char * </code><i>der</i><code>, int * </code><i>der_len</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>unsigned long int len</p>
<dd> value to convert.</p>
<dt>unsigned char * der</p>
<dd> buffer to hold the returned encoding (may be <code>NULL</code>).</p>
<dt>int * der_len</p>
<dd> number of meaningful bytes of ANS (der[0]..der[der_len-1]).</dl>
<h2>DESCRIPTION</h2>
<p> Creates the DER encoding of the provided length value. The <i>der</i> buffer must have enough room for the output. The maximum length this function will encode is <code>ASN1_MAX_LENGTH_SIZE</code>. </p>
<p> To know the size of the DER encoding use a <code>NULL</code> value for <i>der</i> .</p>
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
