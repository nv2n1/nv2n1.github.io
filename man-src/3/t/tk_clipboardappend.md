---
title: "tk_clipboardappend(3)"
name: "tk_clipboardappend"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_clipboardappend/"
description: "Tk_ClipboardClear, Tk_ClipboardAppend – Manage the clipboard"
---

<p>Tk_ClipboardClear, Tk_ClipboardAppend &#8211; Manage the clipboard </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_ClipboardClear</code>(<i>interp, tkwin</i>)
int
<code>Tk_ClipboardAppend</code>(<i>interp, tkwin, target, format, buffer</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for reporting errors.</p>
<dd>Tk_Window <i>tkwin</i> (in) Window that determines which display&#8217;s clipboard to manipulate.</p>
<dd>Atom <i>target</i> (in) Conversion type for this clipboard item; has same meaning as <i>target</i> argument to <code>Tk_CreateSelHandler</code>.</p>
<dd>Atom <i>format</i> (in) Representation to use when data is retrieved; has same meaning as <i>format</i> argument to <code>Tk_CreateSelHandler</code>.</p>
<dd>char <i>*buffer</i> (in) Null terminated string containing the data to be appended to the clipboard. </p>
</dl>
<h2>Description</h2>
<p>These two procedures manage the clipboard for Tk. The clipboard is typically managed by calling <code>Tk_ClipboardClear</code> once, then calling <code>Tk_ClipboardAppend</code> to add data for any number of targets. </p>
<p> <code>Tk_ClipboardClear</code> claims the CLIPBOARD selection and frees any data items previously stored on the clipboard in this application. It normally returns <code>TCL_OK</code>, but if an error occurs it returns <code>TCL_ERROR</code> and leaves an error message in <i>interp-&gt;result</i>. <code>Tk_ClipboardClear</code> must be called before a sequence of <code>Tk_ClipboardAppend</code> calls can be issued. </p>
<p> <code>Tk_ClipboardAppend</code> appends a buffer of data to the clipboard. The first buffer for a given <i>target</i> determines the <i>format</i> for that <i>target</i>. Any successive appends for that <i>target</i> must have the same format or an error will be returned. <code>Tk_ClipboardAppend</code> returns <code>TCL_OK</code> if the buffer is successfully copied onto the clipboard. If the clipboard is not currently owned by the application, either because <code>Tk_ClipboardClear</code> has not been called or because ownership of the clipboard has changed since the last call to <code>Tk_ClipboardClear</code>, <code>Tk_ClipboardAppend</code> returns <code>TCL_ERROR</code> and leaves an error message in <i>interp-&gt;result</i>. </p>
<p> In order to guarantee atomicity, no event handling should occur between <code>Tk_ClipboardClear</code> and the following <code>Tk_ClipboardAppend</code> calls (otherwise someone could retrieve a partially completed clipboard or claim ownership away from this application). </p>
<p> <code>Tk_ClipboardClear</code> may invoke callbacks, including arbitrary Tcl scripts, as a result of losing the CLIPBOARD selection, so any calling function should take care to be reentrant at the point <code>Tk_ClipboardClear</code> is invoked. </p>
<h2>Keywords</h2>
<p>append, clipboard, clear, format, type</p>
