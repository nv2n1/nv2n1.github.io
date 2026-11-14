---
title: "vscanf(3)"
name: "vscanf"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vscanf/"
description: "scanf, fscanf, sscanf, vscanf, vsscanf, vfscanf – input format conversion"
---

<p>scanf, fscanf, sscanf, vscanf, vsscanf, vfscanf &#8211; input format conversion</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdio.h&gt;

int scanf(const char *format, ...);
int fscanf(FILE *stream, const char *format, ...);
int sscanf(const char *str, const char *format, ...);

#include &lt;stdarg.h&gt;

int vscanf(const char *format, va_list ap);
int vsscanf(const char *str, const char *format, va_list ap);
int vfscanf(FILE *stream, const char *format, va_list ap);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>vscanf</code>(), <code>vsscanf</code>(), <code>vfscanf</code>():</p>
<dl>
<dd>_ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>Description</h2>
<p>The <code>scanf</code>() family of functions scans input according to <i>format</i> as described below. This format may contain <i>conversion specifications</i>; the results from such conversions, if any, are stored in the locations pointed to by the <i>pointer</i> arguments that follow <i>format</i>. Each <i>pointer</i> argument must be of a type that is appropriate for the value returned by the corresponding conversion specification. </p>
<p> If the number of conversion specifications in <i>format</i> exceeds the number of <i>pointer</i> arguments, the results are undefined. If the number of <i>pointer</i> arguments exceeds the number of conversion specifications, then the excess <i>pointer</i> arguments are evaluated, but are otherwise ignored. </p>
<p> The <code>scanf</code>() function reads input from the standard input stream <i>stdin</i>, <code>fscanf</code>() reads input from the stream pointer <i>stream</i>, and <code>sscanf</code>() reads its input from the character string pointed to by <i>str</i>. </p>
<p> The <code>vfscanf</code>() function is analogous to <code><a href="/docs/linux/man/3-vfprintf/">vfprintf</a></code>(3) and reads input from the stream pointer <i>stream</i> using a variable argument list of pointers (see <code><a href="/docs/linux/man/3-stdarg/">stdarg</a></code>(3). The <code>vscanf</code>() function scans a variable argument list from the standard input and the <code>vsscanf</code>() function scans it from a string; these are analogous to the <code><a href="/docs/linux/man/3-vprintf/">vprintf</a></code>(3) and <code><a href="/docs/linux/man/3-vsprintf/">vsprintf</a></code>(3) functions respectively. </p>
<p> The <i>format</i> string consists of a sequence of <i>directives</i> which describe how to process the sequence of input characters. If processing of a directive fails, no further input is read, and <code>scanf</code>() returns. A &quot;failure&quot; can be either of the following: <i>input failure</i>, meaning that input characters were unavailable, or <i>matching failure</i>, meaning that the input was inappropriate (see below). </p>
<p> A directive is one of the following:</p>
<dl>
<dt>&bull;</p>
<dd>A sequence of white-space characters (space, tab, newline, etc.; see <code><a href="/docs/linux/man/3-isspace/">isspace</a></code>(3)). This directive matches any amount of white space, including none, in the input.</p>
<dt>&bull;</p>
<dd>An ordinary character (i.e., one other than white space or &#8216;%&#8217;). This character must exactly match the next character of input.</p>
<dt>&bull;</p>
<dd>A conversion specification, which commences with a &#8216;%&#8217; (percent) character. A sequence of characters from the input is converted according to this specification, and the result is placed in the corresponding <i>pointer</i> argument. If the next item of input does not match the conversion specification, the conversion fails&#8212;this is a <i>matching failure</i>.</dl>
<p> Each <i>conversion specification</i> in <i>format</i> begins with either the character &#8216;%&#8217; or the character sequence &quot;<code>%</code><i>n</i><code>$</code>&quot; (see below for the distinction) followed by:</p>
<dl>
<dt>&bull;</p>
<dd>An optional &#8216;*&#8217; assignment-suppression character: <code>scanf</code>() reads input as directed by the conversion specification, but discards the input. No corresponding <i>pointer</i> argument is required, and this specification is not included in the count of successful assignments returned by <code>scanf</code>().</p>
<dt>&bull;</p>
<dd>For decimal conversions, an optional quote character (&#8216;). This specifies that the input number may include thousands&#8217; separators as defined by the <code>LC_NUMERIC</code> category of the current locale. (See <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3).) The quote character may precede or follow the &#8216;*&#8217; assignment-suppression character.</p>
<dt>&bull;</p>
<dd>An optional &#8216;m&#8217; character. This is used with string conversions (<i>%s</i>, <i>%c</i>, <i>%[</i>), and relieves the caller of the need to allocate a corresponding buffer to hold the input: instead, <code>scanf</code>() allocates a buffer of sufficient size, and assigns the address of this buffer to the corresponding <i>pointer</i> argument, which should be a pointer to a <i>char&nbsp;*</i> variable (this variable does not need to be initialized before the call). The caller should subsequently <code><a href="/docs/linux/man/3-free/">free</a></code>(3) this buffer when it is no longer required.</p>
<dt>&bull;</p>
<dd>An optional decimal integer which specifies the <i>maximum field width</i>. Reading of characters stops either when this maximum is reached or when a nonmatching character is found, whichever happens first. Most conversions discard initial white space characters (the exceptions are noted below), and these discarded characters don&#8217;t count toward the maximum field width. String input conversions store a terminating null byte (&#8216;
