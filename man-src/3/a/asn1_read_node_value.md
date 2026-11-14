---
title: "asn1_read_node_value(3)"
name: "asn1_read_node_value"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_read_node_value/"
description: "asn1_read_node_value – API function"
---

<h2>NAME</h2>
<p> asn1_read_node_value &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_read_node_value(asn1_node </code><i>node</i><code>, asn1_data_node_st * </code><i>data</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>asn1_node node</p>
<dd> pointer to a node.</p>
<dt>asn1_data_node_st * data</p>
<dd> a point to a asn1_data_node_st</dl>
<h2>DESCRIPTION</h2>
<p> Returns the value a data node inside a asn1_node structure. The data returned should be handled as constant values.</p>
<h2>RETURNS</h2>
<p> <code>ASN1_SUCCESS</code> if the node exists.</p>
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
