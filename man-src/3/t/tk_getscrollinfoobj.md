---
title: "tk_getscrollinfoobj(3)"
name: "tk_getscrollinfoobj"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getscrollinfoobj/"
description: "Tk_GetScrollInfo, Tk_GetScrollInfoObj – parse arguments for scrolling commands"
---

<p>Tk_GetScrollInfo, Tk_GetScrollInfoObj &#8211; parse arguments for scrolling commands </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_GetScrollInfo(</code><i>interp, argc, argv, dblPtr, intPtr</i><code>)</code>
int
<code>Tk_GetScrollInfoObj(</code><i>interp, objc, objv, dblPtr, intPtr</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter to use for error reporting.</p>
<dd>int <i>argc</i> (in) Number of strings in <i>argv</i> array.</p>
<dd>const char <i>*argv[]</i> (in) Argument strings. These represent the entire widget command, of which the first word is typically the widget name and the second word is typically <code>xview</code> or <code>yview</code>.</p>
<dd>int <i>objc</i> (in) Number of Tcl_Obj&#8217;s in <i>objv</i> array.</p>
<dd>Tcl_Obj *const <i>objv[]</i> (in) Argument objects. These represent the entire widget command, of which the first word is typically the widget name and the second word is typically <code>xview</code> or <code>yview</code>.</p>
<dd>double <i>*dblPtr</i> (out) Filled in with fraction from <code>moveto</code> option, if any.</p>
<dd>int <i>*intPtr</i> (out) Filled in with line or page count from <code>scroll</code> option, if any. The value may be negative. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_GetScrollInfo</code> parses the arguments expected by widget scrolling commands such as <code>xview</code> and <code>yview</code>. It receives the entire list of words that make up a widget command and parses the words starting with <i>argv</i>[2]. The words starting with <i>argv</i>[2] must have one of the following forms:</p>
<dl COMPACT>
<dd>
<pre><code>moveto </code><i>fraction</i>
<code>scroll </code><i>number</i><code> units</code>
<code>scroll </code><i>number</i><code> pages</code></pre>
</dl>
<p> Any of the <code>moveto</code>, <code>scroll</code>, <code>units</code>, and <code>pages</code> keywords may be abbreviated. If <i>argv</i> has the <code>moveto</code> form, <code>TK_SCROLL_MOVETO</code> is returned as result and <i>*dblPtr</i> is filled in with the <i>fraction</i> argument to the command, which must be a proper real value. If <i>argv</i> has the <code>scroll</code> form, <code>TK_SCROLL_UNITS</code> or <code>TK_SCROLL_PAGES</code> is returned and <i>*intPtr</i> is filled in with the <i>number</i> value, which must be a proper integer. If an error occurs in parsing the arguments, <code>TK_SCROLL_ERROR</code> is returned and an error message is left in <i>interp-&gt;result</i>. </p>
<p> <code>Tk_GetScrollInfoObj</code> is identical in function to <code>Tk_GetScrollInfo</code>. However, <code>Tk_GetScrollInfoObj</code> accepts Tcl_Obj style arguments, making it more appropriate for use with new development. </p>
<h2>Keywords</h2>
<p>parse, scrollbar, scrolling command, xview, yview</p>
