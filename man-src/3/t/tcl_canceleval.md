---
title: "tcl_canceleval(3)"
name: "tcl_canceleval"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_canceleval/"
description: "Tcl_CancelEval, Tcl_Canceled – cancel Tcl scripts"
---

<p>Tcl_CancelEval, Tcl_Canceled &#8211; cancel Tcl scripts </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_CancelEval</code>(<i>interp, clientData, flags</i>)
int
<code>Tcl_Canceled</code>(<i>interp, flags</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which to cancel the script.</p>
<dd>int <i>flags</i> (in) ORed combination of flag bits that specify additional options. For <code>Tcl_CancelEval</code>, only <code>TCL_CANCEL_UNWIND</code> is currently supported. For <code>Tcl_Canceled</code>, only <code>TCL_LEAVE_ERR_MSG</code> and <code>TCL_CANCEL_UNWIND</code> are currently supported.</p>
<dd>ClientData <i>clientData</i> (in) Currently, reserved for future use. It should be set to NULL.
</dl>
<h2>Description</h2>
<p><code>Tcl_CancelEval</code> cancels or unwinds the script in progress soon after the next invocation of asynchronous handlers, causing <code>TCL_ERROR</code> to be the return code for that script. This function is thread-safe and may be called from any thread in the process. </p>
<p> <code>Tcl_Canceled</code> checks if the script in progress has been canceled and returns <code>TCL_ERROR</code> if it has. Otherwise, <code>TCL_OK</code> is returned. Extensions can use this function to check to see if they should abort a long running command. This function is thread sensitive and may only be called from the thread the interpreter was created in.</p>
<h2>Flag Bits</h2>
<p>Any ORed combination of the following values may be used for the <i>flags</i> argument to procedures such as <code>Tcl_CancelEval</code>:</p>
<dl COMPACT>
<dt><code>TCL_CANCEL_UNWIND</code></p>
<dd>This flag is used by <code>Tcl_CancelEval</code> and <code>Tcl_Canceled</code>. For <code>Tcl_CancelEval</code>, if this flag is set, the script in progress is canceled and the evaluation stack for the interpreter is unwound. For <code>Tcl_Canceled</code>, if this flag is set, the script in progress is considered to be canceled only if the evaluation stack for the interpreter is being unwound.</p>
<dt><code>TCL_LEAVE_ERR_MSG</code></p>
<dd>This flag is only used by <code>Tcl_Canceled</code>; it is ignored by other procedures. If an error is returned and this bit is set in <i>flags</i>, then an error message will be left in the interpreter&#8217;s result, where it can be retrieved with <code>Tcl_GetObjResult</code> or <code>Tcl_GetStringResult</code>. If this flag bit is not set then no error message is left and the interpreter&#8217;s result will not be modified.</dl>
<h2>See Also</h2>
<p>TIP 285</p>
<h2>Keywords</h2>
<p>cancel, unwind</p>
