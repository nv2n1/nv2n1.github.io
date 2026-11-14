---
title: "tk_grab(3)"
name: "tk_grab"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_grab/"
description: "Tk_Grab, Tk_Ungrab – manipulate grab state in an application"
---

<p>Tk_Grab, Tk_Ungrab &#8211; manipulate grab state in an application </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_Grab</code>(<i>interp, tkwin, grabGlobal</i>)
void
<code>Tk_Ungrab</code>(<i>tkwin</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting</p>
<dd>Tk_Window <i>tkwin</i> (in) Window on whose behalf the pointer is to be grabbed or released</p>
<dd>int <i>grabGlobal</i> (in) Boolean indicating whether the grab is global or application local </p>
</dl>
<h2>Description</h2>
<p>These functions are used to set or release a global or application local grab. When a grab is set on a particular window in a Tk application, mouse and keyboard events can only be received by that window and its descendants. Mouse and keyboard events for windows outside the tree rooted at <i>tkwin</i> will be redirected to <i>tkwin</i>. If the grab is global, then all mouse and keyboard events for windows outside the tree rooted at <i>tkwin</i> (even those intended for windows in other applications) will be redirected to <i>tkwin</i>. If the grab is application local, only mouse and keyboard events intended for a windows within the same application (but outside the tree rooted at <i>tkwin</i>) will be redirected. </p>
<p> <code>Tk_Grab</code> sets a grab on a particular window. <i>Tkwin</i> specifies the window on whose behalf the pointer is to be grabbed. <i>GrabGlobal</i> indicates whether the grab should be global or application local; if it is non-zero, it means the grab should be global. Normally, <code>Tk_Grab</code> returns <code>TCL_OK</code>; if an error occurs and the grab cannot be set, <code>TCL_ERROR</code> is returned and an error message is left if <i>interp</i>&#8216;s result. Once this call completes successfully, no window outside the tree rooted at <i>tkwin</i> will receive pointer- or keyboard-related events until the next call to Tk_Ungrab. If a previous grab was in effect within the application, then it is replaced with a new one. </p>
<p> <code>Tcl_Ungrab</code> releases a grab on the mouse pointer and keyboard, if there is one set on the window given by <i>tkwin</i>. Once a grab is released, pointer and keyboard events will start being delivered to other windows again. </p>
<h2>Keywords</h2>
<p>grab, window</p>
