---
title: "getline(3)"
name: "getline"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getline/"
description: "getline, getdelim – delimited string input"
---

<h2 class="name">NAME</h2>
<p> getline, getdelim &#8211; delimited string input </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdio.h&gt;
ssize_t getline(char **lineptr, size_t *n, FILE *stream);
ssize_t getdelim(char **lineptr, size_t *n, int delim, FILE *stream);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getline</code>(), <code>getdelim</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd> _GNU_SOURCE</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>getline</code>() reads an entire line from <i>stream</i>, storing the address of the buffer containing the text into <i>*lineptr</i>. The buffer is null-terminated and includes the newline character, if one was found. </p>
<p> If <i>*lineptr</i> is set to NULL and <i>*n</i> is set 0 before the call, then <code>getline</code>() will allocate a buffer for storing the line. This buffer should be freed by the user program even if <code>getline</code>() failed. </p>
<p> Alternatively, before calling <code>getline</code>(), <i>*lineptr</i> can contain a pointer to a <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)-allocated buffer <i>*n</i> bytes in size. If the buffer is not large enough to hold the line, <code>getline</code>() resizes it with <code><a href="/docs/linux/man/3-realloc/">realloc</a></code>(3), updating <i>*lineptr</i> and <i>*n</i> as necessary. </p>
<p> In either case, on a successful call, <i>*lineptr</i> and <i>*n</i> will be updated to reflect the buffer address and allocated size respectively. </p>
<p> <code>getdelim</code>() works like <code>getline</code>(), except that a line delimiter other than newline can be specified as the <i>delimiter</i> argument. As with <code>getline</code>(), a delimiter character is not added if one was not present in the input before end of file was reached.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>getline</code>() and <code>getdelim</code>() return the number of characters read, including the delimiter character, but not including the terminating null byte (&#8216;
