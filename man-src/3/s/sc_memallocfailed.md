---
title: "sc_memallocfailed(3)"
name: "sc_memallocfailed"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_memallocfailed/"
description: "sc::MemAllocFailed –"
---

<p>sc::MemAllocFailed &#8211; </p>
<p> This is thrown when a memory allocation fails.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;scexception.h&gt;</code></pre>
<p> Inherits <code>sc::SystemException</code>.</p>
<h3>Public Member Functions</h3>
<p><code>MemAllocFailed</code> (const char *description=0, const char *file=0, int line=0, size_t nbyte=0, const <code>ClassDesc</code> *class_desc=0, const char *exception_type=&#8217;MemAllocFailed&#8217;) throw () </p>
<p> <code>MemAllocFailed</code> (const <code>MemAllocFailed</code> &amp;) throw () </p>
<p> size_t <code>nbyte</code> () const throw ()<br />
 <i>Returns the number of bytes used in the failed allocation attempt. </i></p>
<h2>Detailed Description</h2>
<p>This is thrown when a memory allocation fails.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
