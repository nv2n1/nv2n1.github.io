---
title: "asn1_dup_node(3)"
name: "asn1_dup_node"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_dup_node/"
description: "asn1_dup_node – API function"
---

<h2>NAME</h2>
<p> asn1_dup_node &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>asn1_node asn1_dup_node(asn1_node </code><i>src</i><code>, const char * </code><i>src_name</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>asn1_node src</p>
<dd> Source asn1 node.</p>
<dt>const char * src_name</p>
<dd> Field name in source node.</dl>
<h2>DESCRIPTION</h2>
<p> Create a deep copy of a asn1_node variable. This function will return an exact copy of the provided structure.</p>
<h2>RETURNS</h2>
<p> Return <code>NULL</code> on failure.</p>
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
