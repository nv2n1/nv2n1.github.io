---
title: "embryo_error_group(3)"
name: "embryo_error_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-embryo_error_group/"
description: "Error Functions – Functions that set and retrieve error codes in Embryo programs."
---

<p>Error Functions &#8211; Functions that set and retrieve error codes in Embryo programs. </p>
<h3>Functions</h3>
<p>EAPI void <code>embryo_program_error_set</code> (Embryo_Program *ep, int error)<br />
 <i>Sets the error code for the given program to the given code. </i><br />
 EAPI int <code>embryo_program_error_get</code> (Embryo_Program *ep)<br />
 <i>Retrieves the current error code for the given program. </i><br />
 EAPI const char * <code>embryo_error_string_get</code> (int error)<br />
 <i>Retrieves a string describing the given error code. </i></p>
<h2>Detailed Description</h2>
<p>Functions that set and retrieve error codes in Embryo programs.</p>
<h2>Function Documentation</h2>
<h3>EAPI const char* embryo_error_string_get (int error)</h3>
<p>Retrieves a string describing the given error code. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>error</i> The given error code.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>String describing the given error code. If the given code is not known, the string &#8216;(unknown)&#8217; is returned.</dl>
<h3>EAPI int embryo_program_error_get (Embryo_Program * ep)</h3>
<p>Retrieves the current error code for the given program. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The current error code.</dl>
<h3>EAPI void embryo_program_error_set (Embryo_Program * ep, int error)</h3>
<p>Sets the error code for the given program to the given code. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.<br />
 <i>error</i> The given error code.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Embryo from the source code.</p>
