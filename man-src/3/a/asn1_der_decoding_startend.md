---
title: "asn1_der_decoding_startend(3)"
name: "asn1_der_decoding_startend"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_der_decoding_startend/"
description: "asn1_der_decoding_startEnd – API function"
---

<p>asn1_der_decoding_startEnd &#8211; API function</p>
<h2>Synopsis</h2>
<p><code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_der_decoding_startEnd(asn1_node </code><i>element</i><code>, const void * </code><i>ider</i><code>, int </code><i>ider_len</i><code>, const char * </code><i>name_element</i><code>, int * </code><i>start</i><code>, int * </code><i>end</i><code>);</code></p>
<h2>Arguments</h2>
<dl COMPACT>
<dt>asn1_node element</p>
<dd>pointer to an ASN1 element</p>
<dt>const void * ider</p>
<dd>vector that contains the DER encoding.</p>
<dt>int ider_len</p>
<dd>number of bytes of * <i>ider</i> : <i>ider</i> [0].. <i>ider</i> [len-1]</p>
<dt>const char * name_element</p>
<dd>an element of NAME structure.</p>
<dt>int * start</p>
<dd>the position of the first byte of NAME_ELEMENT decoding ( <i>ider</i> [*start])</p>
<dt>int * end</p>
<dd>the position of the last byte of NAME_ELEMENT decoding ( <i>ider</i> [*end])</dl>
<h2>Description</h2>
<p>Find the start and end point of an element in a DER encoding string. I mean that if you have a der encoding and you have already used the function <code>asn1_der_decoding()</code> to fill a structure, it may happen that you want to find the piece of string concerning an element of the structure. </p>
<p> One example is the sequence &quot;tbsCertificate&quot; inside an X509 certificate. </p>
<p> Note that since libtasn1 3.7 the <i>ider</i> and <i>ider_len</i> parameters can be omitted, if the element is already decoded using <code>asn1_der_decoding()</code>.</p>
<h2>Returns</h2>
<p><code>ASN1_SUCCESS</code> if DER encoding OK, <code>ASN1_ELEMENT_NOT_FOUND</code> if ELEMENT is <code>asn1_node</code> EMPTY or <i>name_element</i> is not a valid element, <code>ASN1_TAG_ERROR</code> or <code>ASN1_DER_ERROR</code> if the der encoding doesn&#8217;t match the structure ELEMENT.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006-2015 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>See Also</h2>
<p>The full documentation for <code>libtasn1</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>libtasn1</code> programs are properly installed at your site, the command</p>
<dl COMPACT>
<dd><code>info libtasn1</code></dl>
<p> should give you access to the complete manual. As an alternative you may obtain the manual from:</p>
<dl COMPACT>
<dd><code><a rel="nofollow" href="http://www.gnu.org/software/libtasn1/manual/">http://www.gnu.org/software/libtasn1/manual/</a></code></dl>
