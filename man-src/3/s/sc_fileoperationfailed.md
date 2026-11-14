---
title: "sc_fileoperationfailed(3)"
name: "sc_fileoperationfailed"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_fileoperationfailed/"
description: "sc::FileOperationFailed –"
---

<p>sc::FileOperationFailed &#8211; </p>
<p> This is thrown when an operation on a file fails.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;scexception.h&gt;</code></pre>
<p> Inherits <code>sc::SystemException</code>.</p>
<h3>Public Types</h3>
<p>enum <code>FileOperation</code> { <code>Unknown</code>, <code>OpenR</code>, <code>OpenW</code>, <code>OpenRW</code>, <code>Close</code>, <code>Read</code>, <code>Write</code>, <code>Corrupt</code>, <code>Other</code> }</p>
<h3>Public Member Functions</h3>
<pre><code>FileOperationFailed (const char *description=0, const char *source_file=0, int line=0, const char *filename=0, FileOperation operation=Unknown, const ClassDesc *class_desc=0, const char *exception_type='FileOperationFailed')  throw ()



FileOperationFailed (const FileOperationFailed &amp;)  throw ()



const char * filename () const   throw ()


Returns the file name of the file that caused the error, if known.


FileOperation operation () const   throw ()</code></pre>
<h2>Detailed Description</h2>
<p>This is thrown when an operation on a file fails.</p>
<h2>Member Function Documentation</h2>
<h3>const char* sc::FileOperationFailed::filename () const throw () [inline]</h3>
<p>Returns the file name of the file that caused the error, if known. Otherwise 0 is returned.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
