---
title: "asn1_find_node(3)"
name: "asn1_find_node"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_find_node/"
description: "asn1_find_node – API function"
---

<h2>NAME</h2>
<p> asn1_find_node &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>asn1_node asn1_find_node(asn1_node </code><i>pointer</i><code>, const char * </code><i>name</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>asn1_node pointer</p>
<dd> NODE_ASN element pointer.</p>
<dt>const char * name</p>
<dd> null terminated string with the element&#8217;s name to find.</dl>
<h2>DESCRIPTION</h2>
<p> Searches for an element called <i>name</i> starting from <i>pointer</i> . The name is composed by differents identifiers separated by dots. When * <i>pointer</i> has a name, the first identifier must be the name of * <i>pointer</i> , otherwise it must be the name of one child of * <i>pointer</i> .</p>
<h2>RETURNS</h2>
<p> the search result, or <code>NULL</code> if not found.</p>
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
