---
title: "sc_systemexception(3)"
name: "sc_systemexception"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_systemexception/"
description: "sc::SystemException –"
---

<p>sc::SystemException &#8211; </p>
<p> This is thrown when a system problem occurs.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;scexception.h&gt;</code></pre>
<p> Inherits <code>sc::SCException</code>. Inherited by <code>sc::FileOperationFailed</code>, <code>sc::MemAllocFailed</code>, and <code>sc::SyscallFailed</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SystemException (const char *description=0, const char *file=0, int line=0, const ClassDesc *class_desc=0, const char *exception_type='SystemException')  throw ()



SystemException (const SystemException &amp;)  throw ()</code></pre>
<h2>Detailed Description</h2>
<p>This is thrown when a system problem occurs.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
