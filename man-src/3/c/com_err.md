---
title: "com_err(3)"
name: "com_err"
section: "3"
letter: "c"
url: "/docs/linux/man/3-com_err/"
description: "com_err – common error display routine"
---

<h2>NAME</h2>
<p> com_err &#8211; common error display routine</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;et/com_err.h&gt;
void (*proc)(const char *, long, const char *, va_list);
void com_err(const char *whoami, long code, const char *format, ...);
proc = set_com_err_hook(proc);
proc = reset_com_err_hook();
void initialize_XXXX_error_table();
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>Com_err</i> displays an error message on the standard error stream <i>stderr</i> (see <i><a href="//www.systutorials.com/docs/linux/man/3S-stdio/">stdio</a></i>(3S)) composed of the <i>whoami</i> string, which should specify the program name or some subportion of a program, followed by an error message generated from the <i>code</i> value (derived from <i><a href="/docs/linux/man/1-compile_et/">compile_et</a></i>(1)), and a string produced using the <i>format</i> string and any following arguments, in the same style as <i><a href="/docs/linux/man/3-fprintf/">fprintf</a></i>(3). </p>
<p> The behavior of <i>com_err</i> can be modified using <i>set_com_err_hook;</i> this defines a procedure which is called with the arguments passed to <i>com_err,</i> instead of the default internal procedure which sends the formatted text to error output. Thus the error messages from a program can all easily be diverted to another form of diagnostic logging, such as <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3). <i>Reset_com_err_hook</i> may be used to restore the behavior of <i>com_err</i> to its default form. Both procedures return the previous &#8220;hook&#8221; value. These &#8220;hook&#8221; procedures must have the declaration given for <i>proc</i> above in the synopsis. </p>
<p> The <i>initialize_XXXX_error_table</i> routine is generated mechanically by <i><a href="/docs/linux/man/1-compile_et/">compile_et</a></i>(1) from a source file containing names and associated strings. Each table has a name of up to four characters, which is used in place of the <code>XXXX</code> in the name of the routine. These routines should be called before any of the corresponding error codes are used, so that the <i>com_err</i> library will recognize error codes from these tables when they are used. </p>
<p> The <code>com_err.h</code> header file should be included in any source file that uses routines from the <i>com_err</i> library; executable files must be linked using <i>&#8220;-lcom_err&#8221;</i> in order to cause the <i>com_err</i> library to be included. </p>
<h2>SEE ALSO</h2>
<p> compile_et (1), syslog (3). </p>
<p> Ken Raeburn, &quot;A Common Error Description Library for UNIX&quot;. </p>
<h2>Index</h2>
