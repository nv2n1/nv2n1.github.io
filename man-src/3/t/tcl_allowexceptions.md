---
title: "tcl_allowexceptions(3)"
name: "tcl_allowexceptions"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_allowexceptions/"
description: "Tcl_AllowExceptions – allow all exceptions in next script evaluation"
---

<p>Tcl_AllowExceptions &#8211; allow all exceptions in next script evaluation </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_AllowExceptions</code>(<i>interp</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which script will be evaluated. </p>
</dl>
<h2>Description</h2>
<p>If a script is evaluated at top-level (i.e. no other scripts are pending evaluation when the script is invoked), and if the script terminates with a completion code other than <code>TCL_OK</code>, <code>TCL_ERROR</code> or <code>TCL_RETURN</code>, then Tcl normally converts this into a <code>TCL_ERROR</code> return with an appropriate message. The particular script evaluation procedures of Tcl that act in the manner are <code>Tcl_EvalObjEx</code>, <code>Tcl_EvalObjv</code>, <code>Tcl_Eval</code>, <code>Tcl_EvalEx</code>, <code>Tcl_GlobalEval</code>, <code>Tcl_GlobalEvalObj</code>, <code>Tcl_VarEval</code> and <code>Tcl_VarEvalVA</code>. </p>
<p> However, if <code>Tcl_AllowExceptions</code> is invoked immediately before calling one of those a procedures, then arbitrary completion codes are permitted from the script, and they are returned without modification. This is useful in cases where the caller can deal with exceptions such as <code>TCL_BREAK</code> or <code>TCL_CONTINUE</code> in a meaningful way. </p>
<h2>Keywords</h2>
<p>continue, break, exception, interpreter</p>
