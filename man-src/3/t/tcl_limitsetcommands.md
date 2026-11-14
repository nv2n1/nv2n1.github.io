---
title: "tcl_limitsetcommands(3)"
name: "tcl_limitsetcommands"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_limitsetcommands/"
description: "Tcl_LimitAddHandler, Tcl_LimitCheck, Tcl_LimitExceeded, Tcl_LimitGetCommands, Tcl_LimitGetGranularity, Tcl_LimitGetTime, Tcl_LimitReady, Tcl_LimitRemoveHandler, Tcl_LimitSetCommands, Tcl_LimitSetGr..."
---

<p>Tcl_LimitAddHandler, Tcl_LimitCheck, Tcl_LimitExceeded, Tcl_LimitGetCommands, Tcl_LimitGetGranularity, Tcl_LimitGetTime, Tcl_LimitReady, Tcl_LimitRemoveHandler, Tcl_LimitSetCommands, Tcl_LimitSetGranularity, Tcl_LimitSetTime, Tcl_LimitTypeEnabled, Tcl_LimitTypeExceeded, Tcl_LimitTypeReset, Tcl_LimitTypeSet &#8211; manage and check resource limits on interpreters </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_LimitCheck</code>(<i>interp</i>)
int
<code>Tcl_LimitReady</code>(<i>interp</i>)
int
<code>Tcl_LimitExceeded</code>(<i>interp</i>)
int
<code>Tcl_LimitTypeExceeded</code>(<i>interp, type</i>)
int
<code>Tcl_LimitTypeEnabled</code>(<i>interp, type</i>)
void
<code>Tcl_LimitTypeSet</code>(<i>interp, type</i>)
void
<code>Tcl_LimitTypeReset</code>(<i>interp, type</i>)
int
<code>Tcl_LimitGetCommands</code>(<i>interp</i>)
void
<code>Tcl_LimitSetCommands</code>(<i>interp, commandLimit</i>)
void
<code>Tcl_LimitGetTime</code>(<i>interp, timeLimitPtr</i>)
void
<code>Tcl_LimitSetTime</code>(<i>interp, timeLimitPtr</i>)
int
<code>Tcl_LimitGetGranularity</code>(<i>interp, type</i>)
void
<code>Tcl_LimitSetGranularity</code>(<i>interp, type, granularity</i>)
void
<code>Tcl_LimitAddHandler</code>(<i>interp, type, handlerProc, clientData, deleteProc</i>)
void
<code>Tcl_LimitRemoveHandler</code>(<i>interp, type, handlerProc, clientData</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter that the limit being managed applies to or that will have its limits checked.</p>
<dd>int <i>type</i> (in) The type of limit that the operation refers to. This must be either <code>TCL_LIMIT_COMMANDS</code> or <code>TCL_LIMIT_TIME</code>.</p>
<dd>int <i>commandLimit</i> (in) The maximum number of commands (as reported by <code>info cmdcount</code>) that may be executed in the interpreter.</p>
<dd>Tcl_Time <i>*timeLimitPtr</i> (in/out) A pointer to a structure that will either have the new time limit read from (<code>Tcl_LimitSetTime</code>) or the current time limit written to (<code>Tcl_LimitGetTime</code>).</p>
<dd>int <i>granularity</i> (in) Divisor that indicates how often a particular limit should really be checked. Must be at least 1.</p>
<dd>Tcl_LimitHandlerProc <i>*handlerProc</i> (in) Function to call when a particular limit is exceeded. If the <i>handlerProc</i> removes or raises the limit during its processing, the limited interpreter will be permitted to continue to process after the handler returns. Many handlers may be attached to the same interpreter limit; their order of execution is not defined, and they must be identified by <i>handlerProc</i> and <i>clientData</i> when they are deleted.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary pointer-sized word used to pass some context to the <i>handlerProc</i> function.</p>
<dd>Tcl_LimitHandlerDeleteProc <i>*deleteProc</i> (in) Function to call whenever a handler is deleted. May be NULL if the <i>clientData</i> requires no deletion. </p>
</dl>
<h2>Description</h2>
<p>Tcl&#8217;s interpreter resource limit subsystem allows for close control over how much computation time a script may use, and is useful for cases where a program is divided into multiple pieces where some parts are more trusted than others (e.g. web application servers). </p>
<p> Every interpreter may have a limit on the wall-time for execution, and a limit on the number of commands that the interpreter may execute. Since checking of these limits is potentially expensive (especially the time limit), each limit also has a checking granularity, which is a divisor for an internal count of the number of points in the core where a check may be performed (which is immediately before executing a command and at an unspecified frequency between running commands, which can happen in empty-bodied <code>while</code> loops). </p>
<p> The final component of the limit engine is a callback scheme which allows for notifications of when a limit has been exceeded. These callbacks can just provide logging, or may allocate more resources to the interpreter to permit it to continue processing longer. </p>
<p> When a limit is exceeded (and the callbacks have run; the order of execution of the callbacks is unspecified) execution in the limited interpreter is stopped by raising an error and setting a flag that prevents the <code>catch</code> command in that interpreter from trapping that error. It is up to the context that started execution in that interpreter (typically a master interpreter) to handle the error.</p>
<h2>Limit Checking Api</h2>
<p>To check the resource limits for an interpreter, call <code>Tcl_LimitCheck</code>, which returns <code>TCL_OK</code> if the limit was not exceeded (after processing callbacks) and <code>TCL_ERROR</code> if the limit was exceeded (in which case an error message is also placed in the interpreter result). That function should only be called when <code>Tcl_LimitReady</code> returns non-zero so that granularity policy is enforced. This API is designed to be similar in usage to <code>Tcl_AsyncReady</code> and <code>Tcl_AsyncInvoke</code>. </p>
<p> When writing code that may behave like <code>catch</code> in respect of errors, you should only trap an error if <code>Tcl_LimitExceeded</code> returns zero. If it returns non-zero, the interpreter is in a limit-exceeded state and errors should be allowed to propagate to the calling context. You can also check whether a particular type of limit has been exceeded using <code>Tcl_LimitTypeExceeded</code>.</p>
<h2>Limit Configuration</h2>
<p>To check whether a limit has been set (but not whether it has actually been exceeded) on an interpreter, call <code>Tcl_LimitTypeEnabled</code> with the type of limit you want to check. To enable a particular limit call <code>Tcl_LimitTypeSet</code>, and to disable a limit call <code>Tcl_LimitTypeReset</code>. </p>
<p> The level of a command limit may be set using <code>Tcl_LimitSetCommands</code>, and retrieved using <code>Tcl_LimitGetCommands</code>. Similarly for a time limit with <code>Tcl_LimitSetTime</code> and <code>Tcl_LimitGetTime</code> respectively, but with that API the time limit is copied from and to the Tcl_Time structure that the <i>timeLimitPtr</i> argument points to. </p>
<p> The checking granularity for a particular limit may be set using <code>Tcl_LimitSetGranularity</code> and retrieved using <code>Tcl_LimitGetGranularity</code>. Note that granularities must always be positive.</p>
<h3>Limit Callbacks</h3>
<p>To add a handler callback to be invoked when a limit is exceeded, call <code>Tcl_LimitAddHandler</code>. The <i>handlerProc</i> argument describes the function that will actually be called; it should have the following prototype: </p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_LimitHandlerProc(
 ClientData <i>clientData</i>,
 Tcl_Interp *<i>interp</i>);</pre>
</dl>
<p> The <i>clientData</i> argument to the handler will be whatever is passed to the <i>clientData</i> argument to <code>Tcl_LimitAddHandler</code>, and the <i>interp</i> is the interpreter that had its limit exceeded. </p>
<p> The <i>deleteProc</i> argument to <code>Tcl_LimitAddHandler</code> is a function to call to delete the <i>clientData</i> value. It may be <code>TCL_STATIC</code> or NULL if no deletion action is necessary, or <code>TCL_DYNAMIC</code> if all that is necessary is to free the structure with <code>Tcl_Free</code>. Otherwise, it should refer to a function with the following prototype: </p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_LimitHandlerDeleteProc(
 ClientData <i>clientData</i>);</pre>
</dl>
<p> A limit handler may be deleted using <code>Tcl_LimitRemoveHandler</code>; the handler removed will be the first one found (out of the handlers added with <code>Tcl_LimitAddHandler</code>) with exactly matching <i>type</i>, <i>handlerProc</i> and <i>clientData</i> arguments. This function always invokes the <i>deleteProc</i> on the <i>clientData</i> (unless the <i>deleteProc</i> was NULL or <code>TCL_STATIC</code>). </p>
<h2>Keywords</h2>
<p>interpreter, resource, limit, commands, time, callback</p>
