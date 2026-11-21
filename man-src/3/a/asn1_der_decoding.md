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
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_der_decoding(asn1_node * </code><i>element</i><code>, const void * </code><i>ider</i><code>, int </code><i>ider_len</i><code>, char * </code><i>errorDescription</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>asn1_node * element</dt>
<dd> pointer to an ASN1 structure.</dd>
<dt>const void * ider</dt>
<dd> vector that contains the DER encoding.</dd>
<dt>int ider_len</dt>
<dd> number of bytes of * <i>ider</i> : <i>ider</i> [0].. <i>ider</i> [len-1].</dd>
<dt>char * errorDescription</dt>
<dd> null-terminated string contains details when an error occurred.</dd></dl>
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
</dt><dd> <code>info libtasn1</code></dd></dl>
<p> should give you access to the complete manual. As an alternative you may obtain the manual from:</p>
<dl>
<dt>
</dt><dd> <code><a rel="nofollow" href="http://www.gnu.org/software/libtasn1/manual/">http://www.gnu.org/software/libtasn1/manual/</a></code></dd></dl>
