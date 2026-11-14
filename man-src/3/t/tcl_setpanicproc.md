---
title: "tcl_setpanicproc(3)"
name: "tcl_setpanicproc"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_setpanicproc/"
description: "Tcl_Panic, Tcl_PanicVA, Tcl_SetPanicProc – report fatal error and abort"
---

<p>Tcl_Panic, Tcl_PanicVA, Tcl_SetPanicProc &#8211; report fatal error and abort </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
void
<code>Tcl_Panic</code>(<i>format</i>, <i>arg</i>, <i>arg</i>, <i>...</i>)
void
<code>Tcl_PanicVA</code>(<i>format</i>, <i>argList</i>)
void
<code>Tcl_SetPanicProc</code>(<i>panicProc</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>const char* <i>format</i> (in) A printf-style format string.</p>
<dd><i>arg</i> (in) Arguments matching the format string.</p>
<dd>va_list <i>argList</i> (in) An argument list of arguments matching the format string. Must have been initialized using <code>va_start</code>, and cleared using <code>va_end</code>.</p>
<dd>Tcl_PanicProc <i>*panicProc</i> (in) Procedure to report fatal error message and abort. </p>
</dl>
<h2>Description</h2>
<p>When the Tcl library detects that its internal data structures are in an inconsistent state, or that its C procedures have been called in a manner inconsistent with their documentation, it calls <code>Tcl_Panic</code> to display a message describing the error and abort the process. The <i>format</i> argument is a format string describing how to format the remaining arguments <i>arg</i> into an error message, according to the same formatting rules used by the <code>printf</code> family of functions. The same formatting rules are also used by the built-in Tcl command <code>format</code>. </p>
<p> In a freshly loaded Tcl library, <code>Tcl_Panic</code> prints the formatted error message to the standard error file of the process, and then calls <code>abort</code> to terminate the process. <code>Tcl_Panic</code> does not return. </p>
<p> <code>Tcl_SetPanicProc</code> may be used to modify the behavior of <code>Tcl_Panic</code>. The <i>panicProc</i> argument should match the type <code>Tcl_PanicProc</code>: </p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_PanicProc(
 const char *<code>format</code>,
 <code>arg</code>, <code>arg</code>,...);</pre>
</dl>
<p> After <code>Tcl_SetPanicProc</code> returns, any future calls to <code>Tcl_Panic</code> will call <i>panicProc</i>, passing along the <i>format</i> and <i>arg</i> arguments. To maintain consistency with the callers of <code>Tcl_Panic</code>, <i>panicProc</i> must not return; it must call <code>abort</code>. <i>panicProc</i> should avoid making calls into the Tcl library, or into other libraries that may call the Tcl library, since the original call to <code>Tcl_Panic</code> indicates the Tcl library is not in a state of reliable operation. </p>
<p> The typical use of <code>Tcl_SetPanicProc</code> arranges for the error message to be displayed or reported in a manner more suitable for the application or the platform. As an example, the Windows implementation of <code>wish</code> calls <code>Tcl_SetPanicProc</code> to force all panic messages to be displayed in a system dialog box, rather than to be printed to the standard error file (usually not visible under Windows). </p>
<p> Although the primary callers of <code>Tcl_Panic</code> are the procedures of the Tcl library, <code>Tcl_Panic</code> is a public function and may be called by any extension or application that wishes to abort the process and have a panic message displayed the same way that panic messages from Tcl will be displayed. </p>
<p> <code>Tcl_PanicVA</code> is the same as <code>Tcl_Panic</code> except that instead of taking a variable number of arguments it takes an argument list. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-abort/">abort</a>(3), <a href="/docs/linux/man/3-printf/">printf</a>(3), <a href="/docs/linux/man/n-exec/">exec</a>(n), <a href="/docs/linux/man/n-format/">format</a>(n) </p>
<h2>Keywords</h2>
<p>abort, fatal, error</p>
