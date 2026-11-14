---
title: "asn1_parser2tree(3)"
name: "asn1_parser2tree"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_parser2tree/"
description: "asn1_parser2tree – API function"
---

<h2>NAME</h2>
<p> asn1_parser2tree &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>int asn1_parser2tree(const char * </code><i>file</i><code>, asn1_node * </code><i>definitions</i><code>, char * </code><i>error_desc</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * file</p>
<dd> specify the path and the name of file that contains ASN.1 declarations.</p>
<dt>asn1_node * definitions</p>
<dd> return the pointer to the structure created from &quot;file&quot; ASN.1 declarations.</p>
<dt>char * error_desc</p>
<dd> return the error description or an empty string if success.</dl>
<h2>DESCRIPTION</h2>
<p> Function used to start the parse algorithm. Creates the structures needed to manage the definitions included in <i>file</i> file.</p>
<h2>RETURNS</h2>
<p> <code>ASN1_SUCCESS</code> if the file has a correct syntax and every identifier is known, <code>ASN1_ELEMENT_NOT_EMPTY</code> if <i>definitions</i> not <code>NULL</code>, <code>ASN1_FILE_NOT_FOUND</code> if an error occured while opening <i>file</i> , <code>ASN1_SYNTAX_ERROR</code> if the syntax is not correct, <code>ASN1_IDENTIFIER_NOT_FOUND</code> if in the file there is an identifier that is not defined, <code>ASN1_NAME_TOO_LONG</code> if in the file there is an identifier whith more than <code>ASN1_MAX_NAME_SIZE</code> characters.</p>
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
