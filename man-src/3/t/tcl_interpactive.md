---
title: "tcl_interpactive(3)"
name: "tcl_interpactive"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_interpactive/"
description: "Tcl_CreateInterp, Tcl_DeleteInterp, Tcl_InterpActive, Tcl_InterpDeleted – create and delete Tcl command interpreters"
---

<p>Tcl_CreateInterp, Tcl_DeleteInterp, Tcl_InterpActive, Tcl_InterpDeleted &#8211; create and delete Tcl command interpreters </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Interp *
<code>Tcl_CreateInterp</code>()
<code>Tcl_DeleteInterp</code>(<i>interp</i>)
int
<code>Tcl_InterpDeleted</code>(<i>interp</i>)
int
<code>Tcl_InterpActive</code>(<i>interp</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Token for interpreter to be destroyed or queried.
</dl>
<h2>Description</h2>
<p><code>Tcl_CreateInterp</code> creates a new interpreter structure and returns a token for it. The token is required in calls to most other Tcl procedures, such as <code>Tcl_CreateCommand</code>, <code>Tcl_Eval</code>, and <code>Tcl_DeleteInterp</code>. The token returned by <code>Tcl_CreateInterp</code> may only be passed to Tcl routines called from the same thread as the original <code>Tcl_CreateInterp</code> call. It is not safe for multiple threads to pass the same token to Tcl&#8217;s routines. The new interpreter is initialized with the built-in Tcl commands and with standard variables like <code>tcl_platform</code> and <code>env</code>. To bind in additional commands, call <code>Tcl_CreateCommand</code>, and to create additional variables, call <code>Tcl_SetVar</code>. </p>
<p> <code>Tcl_DeleteInterp</code> marks an interpreter as deleted; the interpreter will eventually be deleted when all calls to <code>Tcl_Preserve</code> for it have been matched by calls to <code>Tcl_Release</code>. At that time, all of the resources associated with it, including variables, procedures, and application-specific command bindings, will be deleted. After <code>Tcl_DeleteInterp</code> returns any attempt to use <code>Tcl_Eval</code> on the interpreter will fail and return <code>TCL_ERROR</code>. After the call to <code>Tcl_DeleteInterp</code> it is safe to examine the interpreter&#8217;s result, query or set the values of variables, define, undefine or retrieve procedures, and examine the runtime evaluation stack. See below, in the section <code>INTERPRETERS AND MEMORY MANAGEMENT</code> for details. </p>
<p> <code>Tcl_InterpDeleted</code> returns nonzero if <code>Tcl_DeleteInterp</code> was called with <i>interp</i> as its argument; this indicates that the interpreter will eventually be deleted, when the last call to <code>Tcl_Preserve</code> for it is matched by a call to <code>Tcl_Release</code>. If nonzero is returned, further calls to <code>Tcl_Eval</code> in this interpreter will return <code>TCL_ERROR</code>. </p>
<p> <code>Tcl_InterpDeleted</code> is useful in deletion callbacks to distinguish between when only the memory the callback is responsible for is being deleted and when the whole interpreter is being deleted. In the former case the callback may recreate the data being deleted, but this would lead to an infinite loop if the interpreter were being deleted. </p>
<p> <code>Tcl_InterpActive</code> is useful for determining whether there is any execution of scripts ongoing in an interpreter, which is a useful piece of information when Tcl is embedded in a garbage-collected environment and it becomes necessary to determine whether the interpreter is a candidate for deletion. The function returns a true value if the interpreter has at least one active execution running inside it, and a false value otherwise.</p>
<h2>Interpreters And Memory Management</h2>
<p><code>Tcl_DeleteInterp</code> can be called at any time on an interpreter that may be used by nested evaluations and C code in various extensions. Tcl implements a simple mechanism that allows callers to use interpreters without worrying about the interpreter being deleted in a nested call, and without requiring special code to protect the interpreter, in most cases. This mechanism ensures that nested uses of an interpreter can safely continue using it even after <code>Tcl_DeleteInterp</code> is called. </p>
<p> The mechanism relies on matching up calls to <code>Tcl_Preserve</code> with calls to <code>Tcl_Release</code>. If <code>Tcl_DeleteInterp</code> has been called, only when the last call to <code>Tcl_Preserve</code> is matched by a call to <code>Tcl_Release</code>, will the interpreter be freed. See the manual entry for <code>Tcl_Preserve</code> for a description of these functions. </p>
<p> The rules for when the user of an interpreter must call <code>Tcl_Preserve</code> and <code>Tcl_Release</code> are simple:</p>
<dl COMPACT>
<dt><code>Interpreters Passed As Arguments</code></p>
<dd>Functions that are passed an interpreter as an argument can safely use the interpreter without any special protection. Thus, when you write an extension consisting of new Tcl commands, no special code is needed to protect interpreters received as arguments. This covers the majority of all uses.</p>
<dt><code>Interpreter Creation And Deletion</code></p>
<dd>When a new interpreter is created and used in a call to <code>Tcl_Eval</code>, <code>Tcl_VarEval</code>, <code>Tcl_GlobalEval</code>, <code>Tcl_SetVar</code>, or <code>Tcl_GetVar</code>, a pair of calls to <code>Tcl_Preserve</code> and <code>Tcl_Release</code> should be wrapped around all uses of the interpreter. Remember that it is unsafe to use the interpreter once <code>Tcl_Release</code> has been called. To ensure that the interpreter is properly deleted when it is no longer needed, call <code>Tcl_InterpDeleted</code> to test if some other code already called <code>Tcl_DeleteInterp</code>; if not, call <code>Tcl_DeleteInterp</code> before calling <code>Tcl_Release</code> in your own code.</p>
<dt><code>Retrieving An Interpreter From A Data Structure</code></p>
<dd>When an interpreter is retrieved from a data structure (e.g. the client data of a callback) for use in one of the evaluation functions (<code>Tcl_Eval</code>, <code>Tcl_VarEval</code>, <code>Tcl_GlobalEval</code>, <code>Tcl_EvalObjv</code>, etc.) or variable access functions (<code>Tcl_SetVar</code>, <code>Tcl_GetVar</code>, <code>Tcl_SetVar2Ex</code>, etc.), a pair of calls to <code>Tcl_Preserve</code> and <code>Tcl_Release</code> should be wrapped around all uses of the interpreter; it is unsafe to reuse the interpreter once <code>Tcl_Release</code> has been called. If an interpreter is stored inside a callback data structure, an appropriate deletion cleanup mechanism should be set up by the code that creates the data structure so that the interpreter is removed from the data structure (e.g. by setting the field to NULL) when the interpreter is deleted. Otherwise, you may be using an interpreter that has been freed and whose memory may already have been reused.</dl>
<p> All uses of interpreters in Tcl and Tk have already been protected. Extension writers should ensure that their code also properly protects any additional interpreters used, as described above. </p>
<p> Note that the protection mechanisms do not work well with conventional garbage collection systems. When in such a managed environment, <code>Tcl_InterpActive</code> should be used to determine when an interpreter is a candidate for deletion due to inactivity.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-tcl_preserve/">Tcl_Preserve</a>(3), <a href="/docs/linux/man/3-tcl_release/">Tcl_Release</a>(3)</p>
<h2>Keywords</h2>
<p>command, create, delete, interpreter</p>
