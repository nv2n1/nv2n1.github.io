---
title: "stdios_base_failure(3)"
name: "stdios_base_failure"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_base_failure/"
description: "std::ios_base::failure –"
---

<p>std::ios_base::failure &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>std::exception</code>.</p>
<h3>Public Member Functions</h3>
<p><code>failure</code> (const <code>string</code> &amp;__str) throw () </p>
<p> virtual const char * <code>what</code> () const throw ()</p>
<h2>Detailed Description</h2>
<p>These are thrown to indicate problems with io. </p>
<p> 27.4.2.1.1 Class ios_base::failure. </p>
<p> Definition at line 209 of file ios_base.h.</p>
<h2>Member Function Documentation</h2>
<h3>virtual const char* std::ios_base::failure::what () const [virtual]</h3>
<p>Returns a C-style character string describing the general cause of the current error. </p>
<p> Reimplemented from <code>std::exception</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
