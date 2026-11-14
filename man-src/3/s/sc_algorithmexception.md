---
title: "sc_algorithmexception(3)"
name: "sc_algorithmexception"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_algorithmexception/"
description: "sc::AlgorithmException –"
---

<p>sc::AlgorithmException &#8211; </p>
<p> This exception is thrown whenever a problem with an algorithm is encountered.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;scexception.h&gt;</code></pre>
<p> Inherits <code>sc::SCException</code>. Inherited by <code>sc::MaxIterExceeded</code>, and <code>sc::ToleranceExceeded</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>AlgorithmException (const char *description=0, const char *file=0, int line=0, const ClassDesc *class_desc=0, const char *exception_type='AlgorithmException')  throw ()



AlgorithmException (const AlgorithmException &amp;)  throw ()</code></pre>
<h2>Detailed Description</h2>
<p>This exception is thrown whenever a problem with an algorithm is encountered.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
