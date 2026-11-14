---
title: "sc_inputerror(3)"
name: "sc_inputerror"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_inputerror/"
description: "sc::InputError –"
---

<p>sc::InputError &#8211; </p>
<p> This is thrown when invalid input is provided.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;scexception.h&gt;</code></pre>
<p> Inherits <code>sc::SCException</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>InputError (const char *description=0, const char *file=0, int line=0, const char *keyword=0, const char *value=0, const ClassDesc *class_desc=0, const char *exception_type='InputError')  throw ()



InputError (const InputError &amp;)  throw ()



const char * keyword () const   throw ()



const char * value () const   throw ()</code></pre>
<h2>Detailed Description</h2>
<p>This is thrown when invalid input is provided. </p>
<p> Note that sometimes input can be internally generated, so what logically would be a <code>ProgrammingError</code> could result in an <code>InputError</code> being thrown.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
