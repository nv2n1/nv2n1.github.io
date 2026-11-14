---
title: "asn1_delete_element(3)"
name: "asn1_delete_element"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_delete_element/"
description: "asn1_delete_element – API function"
---

<h2>NAME</h2>
<p> asn1_delete_element &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_delete_element(asn1_node </code><i>structure</i><code>, const char * </code><i>element_name</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>asn1_node structure</p>
<dd> pointer to the structure that contains the element you want to delete.</p>
<dt>const char * element_name</p>
<dd> element&#8217;s name you want to delete.</dl>
<h2>DESCRIPTION</h2>
<p> Deletes the element named * <i>element_name</i> inside * <i>structure</i> .</p>
<h2>RETURNS</h2>
<p> <code>ASN1_SUCCESS</code> if successful, <code>ASN1_ELEMENT_NOT_FOUND</code> if the <i>element_name</i> was not found.</p>
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
