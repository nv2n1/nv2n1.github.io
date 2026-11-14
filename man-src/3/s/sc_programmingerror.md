---
title: "sc_programmingerror(3)"
name: "sc_programmingerror"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_programmingerror/"
description: "sc::ProgrammingError –"
---

<p>sc::ProgrammingError &#8211; </p>
<p> This is thrown when a situations arises that should be impossible.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;scexception.h&gt;</code></pre>
<p> Inherits <code>sc::SCException</code>. Inherited by <code>sc::FeatureNotImplemented</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>ProgrammingError (const char *description=0, const char *file=0, int line=0, const ClassDesc *class_desc=0, const char *exception_type='ProgrammingError')  throw ()



ProgrammingError (const ProgrammingError &amp;)  throw ()</code></pre>
<h2>Detailed Description</h2>
<p>This is thrown when a situations arises that should be impossible.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
