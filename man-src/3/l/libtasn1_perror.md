---
title: "libtasn1_perror(3)"
name: "libtasn1_perror"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libtasn1_perror/"
description: "libtasn1_perror – prints a string to stderr with a description of an error"
---

<h2>NAME</h2>
<p> libtasn1_perror &#8211; prints a string to stderr with a description of an error</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/libtasn1.h">libtasn1.h</a>&gt;</code> </p>
<p> <code>void libtasn1_perror(asn1_retCode </code><i>error</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>asn1_retCode error</p>
<dd> is an error returned by a libtasn1 function.</dl>
<h2>DESCRIPTION</h2>
<p> This function is like <code>perror()</code>. The only difference is that it accepts an error returned by a libtasn1 function.</p>
<h2>DEPRECATED</h2>
<p> Use <code>asn1_perror()</code> instead.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006, 2007, 2008, 2009 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>libtasn1</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>libtasn1</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info libtasn1</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
