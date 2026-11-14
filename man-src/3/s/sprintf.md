---
title: "sprintf(3)"
name: "sprintf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sprintf/"
description: "printf, fprintf, dprintf, sprintf, snprintf, vprintf, vfprintf, vdprintf, vsprintf, vsnprintf – formatted output conversion"
---

<p>printf, fprintf, dprintf, sprintf, snprintf, vprintf, vfprintf, vdprintf, vsprintf, vsnprintf &#8211; formatted output conversion </p>
<h2>Synopsis</h2>
<pre>
<code>#include &lt;stdio.h&gt;</code>
<code>int printf(const char *</code><i>format</i><code>, ...);</code>
<code>int fprintf(FILE *</code><i>stream</i><code>, const char *</code><i>format</i><code>, ...);</code>
<code>int dprintf(int </code><i>fd</i><code>, const char *</code><i>format</i><code>, ...);</code>
<code>int sprintf(char *</code><i>str</i><code>, const char *</code><i>format</i><code>, ...);</code>
<code>int snprintf(char *</code><i>str</i><code>, size_t </code><i>size</i><code>, const char *</code><i>format</i><code>, ...);</code>
<code>#include &lt;stdarg.h&gt;</code>
<code>int vprintf(const char *</code><i>format</i><code>, va_list </code><i>ap</i><code>);</code>
<code>int vfprintf(FILE *</code><i>stream</i><code>, const char *</code><i>format</i><code>, va_list </code><i>ap</i><code>);</code>
<code>int vdprintf(int </code><i>fd</i><code>, const char *</code><i>format</i><code>, va_list </code><i>ap</i><code>);</code>
<code>int vsprintf(char *</code><i>str</i><code>, const char *</code><i>format</i><code>, va_list </code><i>ap</i><code>);</code>
<code>int vsnprintf(char *</code><i>str</i><code>, size_t </code><i>size</i><code>, const char *</code><i>format</i><code>, va_list </code><i>ap</i><code>);</code>
</pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>snprintf</code>(), <code>vsnprintf</code>():</p>
<dl COMPACT>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500 || _ISOC99_SOURCE ||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE</dl>
<p> <code>dprintf</code>(), <code>vdprintf</code>():</p>
<dl COMPACT>
<dt>
<dd>
<dl COMPACT>
<dt>Since glibc 2.10:</p>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd> _GNU_SOURCE</dl>
</dl>
<h2>Description</h2>
<p> The functions in the <code>printf</code>() family produce output according to a <i>format</i> as described below. The functions <code>printf</code>() and <code>vprintf</code>() write output to <i>stdout</i>, the standard output stream; <code>fprintf</code>() and <code>vfprintf</code>() write output to the given output <i>stream</i>; <code>sprintf</code>(), <code>snprintf</code>(), <code>vsprintf</code>(), and <code>vsnprintf</code>() write to the character string <i>str</i>. </p>
<p> The function <code>dprintf</code>() is the same as <code>fprintf</code>() except that it outputs to a file descriptor, <i>fd</i>, instead of to a <i>stdio</i> stream. </p>
<p> The functions <code>snprintf</code>() and <code>vsnprintf</code>() write at most <i>size</i> bytes (including the terminating null byte (&#8216;
