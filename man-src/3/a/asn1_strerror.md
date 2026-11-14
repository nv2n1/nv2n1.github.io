---
title: "asn1_strerror(3)"
name: "asn1_strerror"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_strerror/"
description: "asn1_strerror – API function"
---

<h2>NAME</h2>
<p> asn1_strerror &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>const char * asn1_strerror(int </code><i>error</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>int error</p>
<dd> is an error returned by a libtasn1 function.</dl>
<h2>DESCRIPTION</h2>
<p> Returns a string with a description of an error. This function is similar to strerror. The only difference is that it accepts an error (number) returned by a libtasn1 function.</p>
<h2>RETURNS</h2>
<p> Pointer to static zero-terminated string describing error code.</p>
<h2>SINCE</h2>
<p> 1.6</p>
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
