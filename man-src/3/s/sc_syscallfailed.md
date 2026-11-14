---
title: "sc_syscallfailed(3)"
name: "sc_syscallfailed"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_syscallfailed/"
description: "sc::SyscallFailed –"
---

<p>sc::SyscallFailed &#8211; </p>
<p> This is thrown when an system call fails with an errno.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;scexception.h&gt;</code></pre>
<p> Inherits <code>sc::SystemException</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SyscallFailed (const char *description=0, const char *source_file=0, int line=0, const char *syscall=0, int err=0, const ClassDesc *class_desc=0, const char *exception_type='SyscallFailed')  throw ()



SyscallFailed (const SyscallFailed &amp;)  throw ()



const char * syscall () const   throw ()


Returns the file name of the file that caused the error, if known.


int err () const   throw ()</code></pre>
<h2>Detailed Description</h2>
<p>This is thrown when an system call fails with an errno.</p>
<h2>Member Function Documentation</h2>
<h3>const char* sc::SyscallFailed::syscall () const throw () [inline]</h3>
<p>Returns the file name of the file that caused the error, if known. Otherwise 0 is returned.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
