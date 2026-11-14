---
title: "tcl_dontcallwhendeleted(3)"
name: "tcl_dontcallwhendeleted"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_dontcallwhendeleted/"
description: "Tcl_CallWhenDeleted, Tcl_DontCallWhenDeleted – Arrange for callback when interpreter is deleted"
---

<p>Tcl_CallWhenDeleted, Tcl_DontCallWhenDeleted &#8211; Arrange for callback when interpreter is deleted </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_CallWhenDeleted</code>(<i>interp</i>, <i>proc</i>, <i>clientData</i>)
<code>Tcl_DontCallWhenDeleted</code>(<i>interp</i>, <i>proc</i>, <i>clientData</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter with which to associated callback.</p>
<dd>Tcl_InterpDeleteProc <i>*proc</i> (in) Procedure to call when <i>interp</i> is deleted.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i>. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_CallWhenDeleted</code> arranges for <i>proc</i> to be called by <code>Tcl_DeleteInterp</code> if/when <i>interp</i> is deleted at some future time. <i>Proc</i> will be invoked just before the interpreter is deleted, but the interpreter will still be valid at the time of the call. <i>Proc</i> should have arguments and result that match the type <code>Tcl_InterpDeleteProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_InterpDeleteProc(
 ClientData <i>clientData</i>,
 Tcl_Interp *<i>interp</i>);</pre>
</dl>
<p> The <i>clientData</i> and <i>interp</i> parameters are copies of the <i>clientData</i> and <i>interp</i> arguments given to <code>Tcl_CallWhenDeleted</code>. Typically, <i>clientData</i> points to an application-specific data structure that <i>proc</i> uses to perform cleanup when an interpreter is about to go away. <i>Proc</i> does not return a value. </p>
<p> <code>Tcl_DontCallWhenDeleted</code> cancels a previous call to <code>Tcl_CallWhenDeleted</code> with the same arguments, so that <i>proc</i> will not be called after all when <i>interp</i> is deleted. If there is no deletion callback that matches <i>interp</i>, <i>proc</i>, and <i>clientData</i> then the call to <code>Tcl_DontCallWhenDeleted</code> has no effect. </p>
<h2>Keywords</h2>
<p>callback, delete, interpreter</p>
