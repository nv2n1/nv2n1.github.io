---
title: "asn1_check_version(3)"
name: "asn1_check_version"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asn1_check_version/"
description: "asn1_check_version – API function"
---

<h2>NAME</h2>
<p> asn1_check_version &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;libtasn1.h&gt;</code> </p>
<p> <code>const char * asn1_check_version(const char * </code><i>req_version</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>const char * req_version</p>
<dd> Required version number, or <code>NULL</code>.</dl>
<h2>DESCRIPTION</h2>
<p> Check that the version of the library is at minimum the requested one and return the version string; return <code>NULL</code> if the condition is not satisfied. If a <code>NULL</code> is passed to this function, no check is done, but the version string is simply returned. </p>
<p> See <code>ASN1_VERSION</code> for a suitable <i>req_version</i> string.</p>
<h2>RETURNS</h2>
<p> Version string of run-time library, or <code>NULL</code> if the run-time library does not meet the required version number.</p>
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
