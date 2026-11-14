---
title: "asn1_expand_any_defined_by(3)"
name: "asn1_expand_any_defined_by"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_expand_any_defined_by/"
description: "asn1_expand_any_defined_by – API function"
---

<h2>NAME</h2>
<p> asn1_expand_any_defined_by &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_expand_any_defined_by(asn1_node </code><i>definitions</i><code>, asn1_node * </code><i>element</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>asn1_node definitions</p>
<dd> ASN1 definitions</p>
<dt>asn1_node * element</p>
<dd> pointer to an ASN1 structure</dl>
<h2>DESCRIPTION</h2>
<p> Expands every &quot;ANY DEFINED BY&quot; element of a structure created from a DER decoding process (asn1_der_decoding function). The element ANY must be defined by an OBJECT IDENTIFIER. The type used to expand the element ANY is the first one following the definition of the actual value of the OBJECT IDENTIFIER.</p>
<h2>RETURNS</h2>
<p> <code>ASN1_SUCCESS</code> if Substitution OK, <code>ASN1_ERROR_TYPE_ANY</code> if some &quot;ANY DEFINED BY&quot; element couldn&#8217;t be expanded due to a problem in OBJECT_ID -&gt; TYPE association, or other error codes depending on DER decoding.</p>
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
