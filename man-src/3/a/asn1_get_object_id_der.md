---
title: "asn1_get_object_id_der(3)"
name: "asn1_get_object_id_der"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_get_object_id_der/"
description: "asn1_get_object_id_der – API function"
---

<h2>NAME</h2>
<p> asn1_get_object_id_der &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_get_object_id_der(const unsigned char * </code><i>der</i><code>, int </code><i>der_len</i><code>, int * </code><i>ret_len</i><code>, char * </code><i>str</i><code>, int </code><i>str_size</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const unsigned char * der</p>
<dd> DER data to decode containing the OBJECT IDENTIFIER</p>
<dt>int der_len</p>
<dd> Length of DER data to decode.</p>
<dt>int * ret_len</p>
<dd> Output variable containing the length of the DER data.</p>
<dt>char * str</p>
<dd> Pre-allocated output buffer to put the textual object id in.</p>
<dt>int str_size</p>
<dd> Length of pre-allocated output buffer.</dl>
<h2>DESCRIPTION</h2>
<p> Converts a DER encoded object identifier to its textual form.</p>
<h2>RETURNS</h2>
<p> <code>ASN1_SUCCESS</code> on success, or an error.</p>
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
