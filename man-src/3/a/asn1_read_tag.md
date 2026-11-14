---
title: "asn1_read_tag(3)"
name: "asn1_read_tag"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_read_tag/"
description: "asn1_read_tag – API function"
---

<h2>NAME</h2>
<p> asn1_read_tag &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_read_tag(asn1_node </code><i>root</i><code>, const char * </code><i>name</i><code>, int * </code><i>tagValue</i><code>, int * </code><i>classValue</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>asn1_node root</p>
<dd> pointer to a structure</p>
<dt>const char * name</p>
<dd> the name of the element inside a structure.</p>
<dt>int * tagValue</p>
<dd> variable that will contain the TAG value.</p>
<dt>int * classValue</p>
<dd> variable that will specify the TAG type.</dl>
<h2>DESCRIPTION</h2>
<p> Returns the TAG and the CLASS of one element inside a structure. CLASS can have one of these constants: <code>ASN1_CLASS_APPLICATION</code>, <code>ASN1_CLASS_UNIVERSAL</code>, <code>ASN1_CLASS_PRIVATE</code> or <code>ASN1_CLASS_CONTEXT_SPECIFIC</code>.</p>
<h2>RETURNS</h2>
<p> <code>ASN1_SUCCESS</code> if successful, <code>ASN1_ELEMENT_NOT_FOUND</code> if<br />
&nbsp;<wbr><i>name</i>&nbsp;<wbr>is not a valid element.</p>
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
