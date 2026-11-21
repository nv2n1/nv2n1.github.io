---

title: "asn1_der_decoding2(3)"
name: "asn1_der_decoding2"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_der_decoding2/"
description: "asn1_der_decoding2 – API function"
---

<p> asn1_der_decoding2 &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_der_decoding2(asn1_node * </code><i>element</i><code>, const void * </code><i>ider</i><code>, int * </code><i>max_ider_len</i><code>, unsigned int </code><i>flags</i><code>, char * </code><i>errorDescription</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>asn1_node * element</dt>
<dd> pointer to an ASN1 structure.</dd>
<dt>const void * ider</dt>
<dd> vector that contains the DER encoding.</dd>
<dt>int * max_ider_len</dt>
<dd> pointer to an integer giving the information about the maximal number of bytes occupied by * <i>ider</i> . The real size of the DER encoding is returned through this pointer.</dd>
<dt>unsigned int flags</dt>
<dd> flags controlling the behaviour of the function.</dd>
<dt>char * errorDescription</dt>
<dd> null-terminated string contains details when an error occurred.</dd></dl>
<h2>DESCRIPTION</h2>
<p> Fill the structure * <i>element</i> with values of a DER encoding string. The structure must just be created with function <code>asn1_create_element()</code>. </p>
<p> If <code>ASN1_DECODE_FLAG_ALLOW_PADDING</code> flag is set then the function will ignore padding after the decoded DER data. Upon a successful return the value of * <i>max_ider_len</i> will be set to the number of bytes decoded. </p>
<p> If <code>ASN1_DECODE_FLAG_STRICT_DER</code> flag is set then the function will not decode any BER-encoded elements.</p>
<h2>RETURNS</h2>
<p> <code>ASN1_SUCCESS</code> if DER encoding OK, <code>ASN1_ELEMENT_NOT_FOUND</code> if <i>ELEMENT</i> is <code>NULL</code>, and <code>ASN1_TAG_ERROR</code> or <code>ASN1_DER_ERROR</code> if the der encoding doesn&#8217;t match the structure name (* <i>ELEMENT</i> deleted).</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006-2015 Free Software Foundation, Inc..<br />
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
