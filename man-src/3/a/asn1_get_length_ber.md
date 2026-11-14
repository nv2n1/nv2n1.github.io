---
title: "asn1_get_length_ber(3)"
name: "asn1_get_length_ber"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_get_length_ber/"
description: "asn1_get_length_ber – API function"
---

<h2>NAME</h2>
<p> asn1_get_length_ber &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>long asn1_get_length_ber(const unsigned char * </code><i>ber</i><code>, int </code><i>ber_len</i><code>, int * </code><i>len</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const unsigned char * ber</p>
<dd> BER data to decode.</p>
<dt>int ber_len</p>
<dd> Length of BER data to decode.</p>
<dt>int * len</p>
<dd> Output variable containing the length of the BER length field.</dl>
<h2>DESCRIPTION</h2>
<p> Extract a length field from BER data. The difference to <code>asn1_get_length_der()</code> is that this function will return a length even if the value has indefinite encoding.</p>
<h2>RETURNS</h2>
<p> Return the decoded length value, or negative value when the value was too big.</p>
<h2>SINCE</h2>
<p> 2.0</p>
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
