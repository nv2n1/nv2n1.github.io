---
title: "fmemopen(3)"
name: "fmemopen"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fmemopen/"
description: "fmemopen – open memory as stream"
---

<h2 class="name">NAME</h2>
<p> fmemopen &#8211; open memory as stream </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdio.h&gt;
FILE *fmemopen(void *buf, size_t size, const char *mode);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fmemopen</code>():</p>
<dl>
<dl>
<dt>Since glibc 2.10:</dt>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</dd>
<dt>Before glibc 2.10:</dt>
<dd> _GNU_SOURCE</dd></dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>fmemopen</code>() function opens a stream that permits the access specified by <i>mode</i>. The stream allows I/O to be performed on the string or memory buffer pointed to by <i>buf</i>. </p>
<p> The <i>mode</i> argument specifies the semantics of I/O on the stream, and is one of the following:</p>
<dl>
<dt><i>r</i></dt>
<dd> The stream is opened for reading.</dd>
<dt><i>w</i></dt>
<dd> The stream is opened for writing.</dd>
<dt><i>a</i></dt>
<dd> Append; open the stream for writing, with the initial buffer position set to the first null byte.</dd>
<dt><i>r+</i></dt>
<dd> Open the stream for reading and writing.</dd>
<dt><i>w+</i></dt>
<dd> Open the stream for reading and writing. The buffer contents are truncated (i.e., &#8216;
</dd></dl>