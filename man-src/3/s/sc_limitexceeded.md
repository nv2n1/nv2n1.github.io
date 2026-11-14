---
title: "sc_limitexceeded(3)"
name: "sc_limitexceeded"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_limitexceeded/"
description: "sc::LimitExceeded –"
---

<p>sc::LimitExceeded &#8211; </p>
<p> This is thrown when a limit is exceeded.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;scexception.h&gt;</code></pre>
<p> Inherits <code>sc::SCException</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>LimitExceeded (const char *description, const char *file, int line, T lim, T val, const ClassDesc *class_desc=0, const char *exception_type='LimitExceeded')  throw ()



LimitExceeded (const LimitExceeded &amp;ref)  throw ()



T tolerance ()  throw ()



T value ()  throw ()</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;class T&gt; class sc::LimitExceeded&lt; T &gt;</h3>
<p>This is thrown when a limit is exceeded. </p>
<p> It is more general than <code>ToleranceExceeded</code>. For problems that are numerical in nature and use double types, then <code>ToleranceExceeded</code> should be used instead.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
