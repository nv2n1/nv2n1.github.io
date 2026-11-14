---
title: "pmflush(3)"
name: "pmflush"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmflush/"
description: "pmprintf, pmflush – print formatted output in a window or to standard error"
---

<p><code>pmprintf</code>, <code>pmflush</code> &#8211; print formatted output in a window or to standard error</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmprintf(const char *</code><i>fmt</i>, &#8230; /*<i>args</i>*/);<br />
 int pmflush(void); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>The combination of <code>pmprintf</code> and <code>pmflush</code> produces output in either an <code><a href="/docs/linux/man/1-xconfirm/">xconfirm</a></code>(1) window, on the standard error stream, or to a file in a manner similar to <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3). The <i>fmt</i> argument is used to control the conversion, formatting, and printing of the variable length <i>args</i> list. The output technique is controlled via an environment variable. <code>pmprintf</code> appends the formatted message string to an internal buffer shared by the two routines, without actually producing any output. <code>pmflush</code> causes the internal buffer to be either displayed in a window, printed on standard error, or flushed to a file and the internal buffer to be cleared. </p>
<h2>Environment</h2>
<p>The environment variable <code>PCP_STDERR</code> controls the output technique used by <code>pmflush</code>:</p>
<dl>
<dd>If <code>PCP_STDERR</code> is unset, the text is written onto the <i>stderr</i> stream of the caller. </p>
<p> If <code>PCP_STDERR</code> is set to the literal reserved word <code>DISPLAY</code> then the text will be displayed as a GUI dialog using <code><a href="/docs/linux/man/1-xconfirm/">xconfirm</a></code>(1). </p>
<p> If <code>PCP_STDERR</code> is set to any other value then <code>pmflush</code> interprets the value as a file name and appends the text to that file. The file is created if it doesn&#8217;t already exist, and in this case if the file creation fails, then <i>stderr</i> is used instead).</dl>
<h2>Files</h2>
<p><code>pmprintf</code> uses the <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3) function to create a temporary file. This temporary file is deleted when <code>pmflush</code> is called.</p>
<h2>Diagnostics</h2>
<p>On successful completion, <code>pmprintf</code> returns the number of characters transmitted, while <code>pmflush</code> returns a value of zero on successful completion. </p>
<p> For either routine, a negative value is returned if an error was encountered, and this can be passed to <code><a href="/docs/linux/man/3-pmerrstr/">pmErrStr</a></code>(3) to obtain the associated error message.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pmdbg/">pmdbg</a></code>(1), <code><a href="/docs/linux/man/3-fprintf/">fprintf</a></code>(3), <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3), <code><a href="/docs/linux/man/3-pmerrstr/">pmErrStr</a></code>(3) and <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3). </p>
