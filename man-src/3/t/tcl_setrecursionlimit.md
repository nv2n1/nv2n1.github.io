---
title: "tcl_setrecursionlimit(3)"
name: "tcl_setrecursionlimit"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_setrecursionlimit/"
description: "Tcl_SetRecursionLimit – set maximum allowable nesting depth in interpreter"
---

<p>Tcl_SetRecursionLimit &#8211; set maximum allowable nesting depth in interpreter </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_SetRecursionLimit</code>(<i>interp, depth</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter whose recursion limit is to be set. Must be greater than zero.</p>
<dd>int <i>depth</i> (in) New limit for nested calls to <code>Tcl_Eval</code> for <i>interp</i>. </p>
</dl>
<h2>Description</h2>
<p>At any given time Tcl enforces a limit on the number of recursive calls that may be active for <code>Tcl_Eval</code> and related procedures such as <code>Tcl_GlobalEval</code>. Any call to <code>Tcl_Eval</code> that exceeds this depth is aborted with an error. By default the recursion limit is 1000. </p>
<p> <code>Tcl_SetRecursionLimit</code> may be used to change the maximum allowable nesting depth for an interpreter. The <i>depth</i> argument specifies a new limit for <i>interp</i>, and <code>Tcl_SetRecursionLimit</code> returns the old limit. To read out the old limit without modifying it, invoke <code>Tcl_SetRecursionLimit</code> with <i>depth</i> equal to 0. </p>
<p> The <code>Tcl_SetRecursionLimit</code> only sets the size of the Tcl call stack: it cannot by itself prevent stack overflows on the C stack being used by the application. If your machine has a limit on the size of the C stack, you may get stack overflows before reaching the limit set by <code>Tcl_SetRecursionLimit</code>. If this happens, see if there is a mechanism in your system for increasing the maximum size of the C stack. </p>
<h2>Keywords</h2>
<p>nesting depth, recursion</p>
