---
title: "sc_toleranceexceeded(3)"
name: "sc_toleranceexceeded"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_toleranceexceeded/"
description: "sc::ToleranceExceeded –"
---

<p>sc::ToleranceExceeded &#8211; </p>
<p> This is thrown when when some tolerance is exceeded.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;scexception.h&gt;</code></pre>
<p> Inherits <code>sc::AlgorithmException</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>ToleranceExceeded (const char *description=0, const char *file=0, int line=0, double tol=0, double val=0, const ClassDesc *class_desc=0, const char *exception_type='ToleranceExceeded')  throw ()



ToleranceExceeded (const ToleranceExceeded &amp;)  throw ()



double tolerance ()  throw ()



double value ()  throw ()</code></pre>
<h2>Detailed Description</h2>
<p>This is thrown when when some tolerance is exceeded.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
