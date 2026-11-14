---
title: "sc_featurenotimplemented(3)"
name: "sc_featurenotimplemented"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_featurenotimplemented/"
description: "sc::FeatureNotImplemented –"
---

<p>sc::FeatureNotImplemented &#8211; </p>
<p> This is thrown when an attempt is made to use a feature that is not yet implemented.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;scexception.h&gt;</code></pre>
<p> Inherits <code>sc::ProgrammingError</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>FeatureNotImplemented (const char *description=0, const char *file=0, int line=0, const ClassDesc *class_desc=0, const char *exception_type='FeatureNotImplemented')  throw ()



FeatureNotImplemented (const FeatureNotImplemented &amp;)  throw ()</code></pre>
<h2>Detailed Description</h2>
<p>This is thrown when an attempt is made to use a feature that is not yet implemented.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
