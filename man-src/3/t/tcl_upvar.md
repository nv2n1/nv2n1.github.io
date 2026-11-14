---
title: "tcl_upvar(3)"
name: "tcl_upvar"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_upvar/"
description: "Tcl_UpVar, Tcl_UpVar2 – link one variable to another"
---

<p>Tcl_UpVar, Tcl_UpVar2 &#8211; link one variable to another </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_UpVar(</code><i>interp, frameName, sourceName, destName, flags</i><code>)</code>
int
<code>Tcl_UpVar2(</code><i>interp, frameName, name1, name2, destName, flags</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter containing variables; also used for error reporting.</p>
<dd>const char <i>*frameName</i> (in) Identifies the stack frame containing source variable. May have any of the forms accepted by the <code>upvar</code> command, such as <code>#0</code> or <code>1</code>.</p>
<dd>const char <i>*sourceName</i> (in) Name of source variable, in the frame given by <i>frameName</i>. May refer to a scalar variable or to an array variable with a parenthesized index.</p>
<dd>const char <i>*destName</i> (in) Name of destination variable, which is to be linked to source variable so that references to <i>destName</i> refer to the other variable. Must not currently exist except as an upvar-ed variable.</p>
<dd>int <i>flags</i> (in) One of <code>TCL_GLOBAL_ONLY</code>, <code>TCL_NAMESPACE_ONLY</code> or 0; if non-zero, then <i>destName</i> is a global or namespace variable; otherwise it is local to the current procedure (or current namespace if no procedure is active).</p>
<dd>const char <i>*name1</i> (in) First part of source variable&#8217;s name (scalar name, or name of array without array index).</p>
<dd>const char <i>*name2</i> (in) If source variable is an element of an array, gives the index of the element. For scalar source variables, is NULL. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_UpVar</code> and <code>Tcl_UpVar2</code> provide the same functionality as the <code>upvar</code> command: they make a link from a source variable to a destination variable, so that references to the destination are passed transparently through to the source. The name of the source variable may be specified either as a single string such as <code>xyx</code> or <code>a(24)</code> (by calling <code>Tcl_UpVar</code>) or in two parts where the array name has been separated from the element name (by calling <code>Tcl_UpVar2</code>). The destination variable name is specified in a single string; it may not be an array element. </p>
<p> Both procedures return either <code>TCL_OK</code> or <code>TCL_ERROR</code>, and they leave an error message in the interpreter&#8217;s result if an error occurs. </p>
<p> As with the <code>upvar</code> command, the source variable need not exist; if it does exist, unsetting it later does not destroy the link. The destination variable may exist at the time of the call, but if so it must exist as a linked variable. </p>
<h2>Keywords</h2>
<p>linked variable, upvar, variable</p>
