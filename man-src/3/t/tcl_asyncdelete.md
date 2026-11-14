---
title: "tcl_asyncdelete(3)"
name: "tcl_asyncdelete"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_asyncdelete/"
description: "Tcl_AsyncCreate, Tcl_AsyncMark, Tcl_AsyncInvoke, Tcl_AsyncDelete, Tcl_AsyncReady – handle asynchronous events"
---

<p>Tcl_AsyncCreate, Tcl_AsyncMark, Tcl_AsyncInvoke, Tcl_AsyncDelete, Tcl_AsyncReady &#8211; handle asynchronous events </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_AsyncHandler
<code>Tcl_AsyncCreate</code>(<i>proc, clientData</i>)
<code>Tcl_AsyncMark</code>(<i>async</i>)
int
<code>Tcl_AsyncInvoke</code>(<i>interp, code</i>)
<code>Tcl_AsyncDelete</code>(<i>async</i>)
int
<code>Tcl_AsyncReady</code>()</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_AsyncProc <i>*proc</i> (in) Procedure to invoke to handle an asynchronous event.</p>
<dd>ClientData <i>clientData</i> (in) One-word value to pass to <i>proc</i>.</p>
<dd>Tcl_AsyncHandler <i>async</i> (in) Token for asynchronous event handler.</p>
<dd>Tcl_Interp <i>*interp</i> (in) Tcl interpreter in which command was being evaluated when handler was invoked, or NULL if handler was invoked when there was no interpreter active.</p>
<dd>int <i>code</i> (in) Completion code from command that just completed in <i>interp</i>, or 0 if <i>interp</i> is NULL. </p>
</dl>
<h2>Description</h2>
<p>These procedures provide a safe mechanism for dealing with asynchronous events such as signals. If an event such as a signal occurs while a Tcl script is being evaluated then it is not safe to take any substantive action to process the event. For example, it is not safe to evaluate a Tcl script since the interpreter may already be in the middle of evaluating a script; it may not even be safe to allocate memory, since a memory allocation could have been in progress when the event occurred. The only safe approach is to set a flag indicating that the event occurred, then handle the event later when the world has returned to a clean state, such as after the current Tcl command completes. </p>
<p> <code>Tcl_AsyncCreate</code>, <code>Tcl_AsyncDelete</code>, and <code>Tcl_AsyncReady</code> are thread sensitive. They access and/or set a thread-specific data structure in the event of a core built with <i>&#8211;enable-threads</i>. The token created by <code>Tcl_AsyncCreate</code> contains the needed thread information it was called from so that calling <code>Tcl_AsyncMark</code>(<i>token</i>) will only yield the origin thread into the asynchronous handler. </p>
<p> <code>Tcl_AsyncCreate</code> creates an asynchronous handler and returns a token for it. The asynchronous handler must be created before any occurrences of the asynchronous event that it is intended to handle (it is not safe to create a handler at the time of an event). When an asynchronous event occurs the code that detects the event (such as a signal handler) should call <code>Tcl_AsyncMark</code> with the token for the handler. <code>Tcl_AsyncMark</code> will mark the handler as ready to execute, but it will not invoke the handler immediately. Tcl will call the <i>proc</i> associated with the handler later, when the world is in a safe state, and <i>proc</i> can then carry out the actions associated with the asynchronous event. <i>Proc</i> should have arguments and result that match the type <code>Tcl_AsyncProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_AsyncProc(
 ClientData <i>clientData</i>,
 Tcl_Interp *<i>interp</i>,
 int <i>code</i>);</pre>
</dl>
<p> The <i>clientData</i> will be the same as the <i>clientData</i> argument passed to <code>Tcl_AsyncCreate</code> when the handler was created. If <i>proc</i> is invoked just after a command has completed execution in an interpreter, then <i>interp</i> will identify the interpreter in which the command was evaluated and <i>code</i> will be the completion code returned by that command. The command&#8217;s result will be present in the interpreter&#8217;s result. When <i>proc</i> returns, whatever it leaves in the interpreter&#8217;s result will be returned as the result of the command and the integer value returned by <i>proc</i> will be used as the new completion code for the command. </p>
<p> It is also possible for <i>proc</i> to be invoked when no interpreter is active. This can happen, for example, if an asynchronous event occurs while the application is waiting for interactive input or an X event. In this case <i>interp</i> will be NULL and <i>code</i> will be 0, and the return value from <i>proc</i> will be ignored. </p>
<p> The procedure <code>Tcl_AsyncInvoke</code> is called to invoke all of the handlers that are ready. The procedure <code>Tcl_AsyncReady</code> will return non-zero whenever any asynchronous handlers are ready; it can be checked to avoid calls to <code>Tcl_AsyncInvoke</code> when there are no ready handlers. Tcl calls <code>Tcl_AsyncReady</code> after each command is evaluated and calls <code>Tcl_AsyncInvoke</code> if needed. Applications may also call <code>Tcl_AsyncInvoke</code> at interesting times for that application. For example, Tcl&#8217;s event handler calls <code>Tcl_AsyncReady</code> after each event and calls <code>Tcl_AsyncInvoke</code> if needed. The <i>interp</i> and <i>code</i> arguments to <code>Tcl_AsyncInvoke</code> have the same meaning as for <i>proc</i>: they identify the active interpreter, if any, and the completion code from the command that just completed. </p>
<p> <code>Tcl_AsyncDelete</code> removes an asynchronous handler so that its <i>proc</i> will never be invoked again. A handler can be deleted even when ready, and it will still not be invoked. </p>
<p> If multiple handlers become active at the same time, the handlers are invoked in the order they were created (oldest handler first). The <i>code</i> and the interpreter&#8217;s result for later handlers reflect the values returned by earlier handlers, so that the most recently created handler has last say about the interpreter&#8217;s result and completion code. If new handlers become ready while handlers are executing, <code>Tcl_AsyncInvoke</code> will invoke them all; at each point it invokes the highest-priority (oldest) ready handler, repeating this over and over until there are no longer any ready handlers.</p>
<h2>Warning</h2>
<p>It is almost always a bad idea for an asynchronous event handler to modify the interpreter&#8217;s result or return a code different from its <i>code</i> argument. This sort of behavior can disrupt the execution of scripts in subtle ways and result in bugs that are extremely difficult to track down. If an asynchronous event handler needs to evaluate Tcl scripts then it should first save the interpreter&#8217;s state by calling <code>Tcl_SaveInterpState</code>, passing in the <i>code</i> argument. When the asynchronous handler is finished it should restore the interpreter&#8217;s state by calling <code>Tcl_RestoreInterpState</code>, and then returning the <i>code</i> argument. </p>
<h2>Keywords</h2>
<p>asynchronous event, handler, signal, Tcl_SaveInterpState, thread</p>
