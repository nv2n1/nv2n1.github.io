---
title: "sc_maxiterexceeded(3)"
name: "sc_maxiterexceeded"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_maxiterexceeded/"
description: "sc::MaxIterExceeded –"
---

<p>sc::MaxIterExceeded &#8211; </p>
<p> This is thrown when an iterative algorithm attempts to use more iterations than allowed.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;scexception.h&gt;</code></pre>
<p> Inherits <code>sc::AlgorithmException</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>MaxIterExceeded (const char *description=0, const char *file=0, int line=0, int maxiter=0, const ClassDesc *class_desc=0, const char *exception_type='MaxIterExceeded')  throw ()



MaxIterExceeded (const MaxIterExceeded &amp;)  throw ()



int max_iter () const   throw ()</code></pre>
<h2>Detailed Description</h2>
<p>This is thrown when an iterative algorithm attempts to use more iterations than allowed.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
