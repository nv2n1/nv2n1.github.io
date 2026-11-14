---
title: "asn1_number_of_elements(3)"
name: "asn1_number_of_elements"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_number_of_elements/"
description: "asn1_number_of_elements – API function"
---

<h2>NAME</h2>
<p> asn1_number_of_elements &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_number_of_elements(asn1_node </code><i>element</i><code>, const char * </code><i>name</i><code>, int * </code><i>num</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>asn1_node element</p>
<dd> pointer to the root of an ASN1 structure.</p>
<dt>const char * name</p>
<dd> the name of a sub-structure of ROOT.</p>
<dt>int * num</p>
<dd> pointer to an integer where the result will be stored</dl>
<h2>DESCRIPTION</h2>
<p> Counts the number of elements of a sub-structure called NAME with names equal to &quot;?1&quot;,&quot;?2&quot;, &#8230;</p>
<h2>RETURNS</h2>
<p> <code>ASN1_SUCCESS</code> if successful, <code>ASN1_ELEMENT_NOT_FOUND</code> if<br />
&nbsp;<wbr><i>name</i>&nbsp;<wbr>is not known,&nbsp;<wbr><code>ASN1_GENERIC_ERROR</code>&nbsp;<wbr>if pointer&nbsp;<wbr>&nbsp;<wbr><i>num</i>&nbsp;<wbr>is&nbsp;<wbr><code>NULL</code>.</p>
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
