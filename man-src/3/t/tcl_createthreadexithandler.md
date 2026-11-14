---
title: "tcl_createthreadexithandler(3)"
name: "tcl_createthreadexithandler"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_createthreadexithandler/"
description: "Tcl_Exit, Tcl_Finalize, Tcl_CreateExitHandler, Tcl_DeleteExitHandler, Tcl_ExitThread, Tcl_FinalizeThread, Tcl_CreateThreadExitHandler, Tcl_DeleteThreadExitHandler, Tcl_SetExitProc – end the applica..."
---

<p>Tcl_Exit, Tcl_Finalize, Tcl_CreateExitHandler, Tcl_DeleteExitHandler, Tcl_ExitThread, Tcl_FinalizeThread, Tcl_CreateThreadExitHandler, Tcl_DeleteThreadExitHandler, Tcl_SetExitProc &#8211; end the application or thread (and invoke exit handlers) </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_Exit</code>(<i>status</i>)
<code>Tcl_Finalize</code>()
<code>Tcl_CreateExitHandler</code>(<i>proc, clientData</i>)
<code>Tcl_DeleteExitHandler</code>(<i>proc, clientData</i>)
<code>Tcl_ExitThread</code>(<i>status</i>)
<code>Tcl_FinalizeThread</code>()
<code>Tcl_CreateThreadExitHandler</code>(<i>proc, clientData</i>)
<code>Tcl_DeleteThreadExitHandler</code>(<i>proc, clientData</i>)
Tcl_ExitProc *
<code>Tcl_SetExitProc</code>(<i>proc</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>status</i> (in) Provides information about why the application or thread exited. Exact meaning may be platform-specific. 0 usually means a normal exit, any nonzero value usually means that an error occurred.</p>
<dd>Tcl_ExitProc <i>*proc</i> (in) Procedure to invoke before exiting application, or (for <code>Tcl_SetExitProc</code>) NULL to uninstall the current application exit procedure.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i>. </p>
</dl>
<h2>Description</h2>
<p>The procedures described here provide a graceful mechanism to end the execution of a <code>Tcl</code> application. Exit handlers are invoked to cleanup the application&#8217;s state before ending the execution of <code>Tcl</code> code. </p>
<p> Invoke <code>Tcl_Exit</code> to end a <code>Tcl</code> application and to exit from this process. This procedure is invoked by the <code>exit</code> command, and can be invoked anyplace else to terminate the application. No-one should ever invoke the <code>exit</code> system procedure directly; always invoke <code>Tcl_Exit</code> instead, so that it can invoke exit handlers. Note that if other code invokes <code>exit</code> system procedure directly, or otherwise causes the application to terminate without calling <code>Tcl_Exit</code>, the exit handlers will not be run. <code>Tcl_Exit</code> internally invokes the <code>exit</code> system call, thus it never returns control to its caller. If an application exit handler has been installed (see <code>Tcl_SetExitProc</code>), that handler is invoked with an argument consisting of the exit status (cast to ClientData); the application exit handler should not return control to Tcl. </p>
<p> <code>Tcl_Finalize</code> is similar to <code>Tcl_Exit</code> except that it does not exit from the current process. It is useful for cleaning up when a process is finished using <code>Tcl</code> but wishes to continue executing, and when <code>Tcl</code> is used in a dynamically loaded extension that is about to be unloaded. On some systems <code>Tcl</code> is automatically notified when it is being unloaded, and it calls <code>Tcl_Finalize</code> internally; on these systems it not necessary for the caller to explicitly call <code>Tcl_Finalize</code>. However, to ensure portability, your code should always invoke <code>Tcl_Finalize</code> when <code>Tcl</code> is being unloaded, to ensure that the code will work on all platforms. <code>Tcl_Finalize</code> can be safely called more than once. </p>
<p> <code>Tcl_ExitThread</code> is used to terminate the current thread and invoke per-thread exit handlers. This finalization is done by <code>Tcl_FinalizeThread</code>, which you can call if you just want to clean up per-thread state and invoke the thread exit handlers. <code>Tcl_Finalize</code> calls <code>Tcl_FinalizeThread</code> for the current thread automatically. </p>
<p> <code>Tcl_CreateExitHandler</code> arranges for <i>proc</i> to be invoked by <code>Tcl_Finalize</code> and <code>Tcl_Exit</code>. <code>Tcl_CreateThreadExitHandler</code> arranges for <i>proc</i> to be invoked by <code>Tcl_FinalizeThread</code> and <code>Tcl_ExitThread</code>. This provides a hook for cleanup operations such as flushing buffers and freeing global memory. <i>Proc</i> should match the type <code>Tcl_ExitProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_ExitProc(ClientData <i>clientData</i>);</pre>
</dl>
<p> The <i>clientData</i> parameter to <i>proc</i> is a copy of the <i>clientData</i> argument given to <code>Tcl_CreateExitHandler</code> or <code>Tcl_CreateThreadExitHandler</code> when the callback was created. Typically, <i>clientData</i> points to a data structure containing application-specific information about what to do in <i>proc</i>. </p>
<p> <code>Tcl_DeleteExitHandler</code> and <code>Tcl_DeleteThreadExitHandler</code> may be called to delete a previously-created exit handler. It removes the handler indicated by <i>proc</i> and <i>clientData</i> so that no call to <i>proc</i> will be made. If no such handler exists then <code>Tcl_DeleteExitHandler</code> or <code>Tcl_DeleteThreadExitHandler</code> does nothing. </p>
<p> <code>Tcl_Finalize</code> and <code>Tcl_Exit</code> execute all registered exit handlers, in reverse order from the order in which they were registered. This matches the natural order in which extensions are loaded and unloaded; if extension <code>A</code> loads extension <code>B</code>, it usually unloads <code>B</code> before it itself is unloaded. If extension <code>A</code> registers its exit handlers before loading extension <code>B</code>, this ensures that any exit handlers for <code>B</code> will be executed before the exit handlers for <code>A</code>. </p>
<p> <code>Tcl_Finalize</code> and <code>Tcl_Exit</code> call <code>Tcl_FinalizeThread</code> and the thread exit handlers <i>after</i> the process-wide exit handlers. This is because thread finalization shuts down the I/O channel system, so any attempt at I/O by the global exit handlers will vanish into the bitbucket. </p>
<p> <code>Tcl_SetExitProc</code> installs an application exit handler, returning the previously-installed application exit handler or NULL if no application handler was installed. If an application exit handler is installed, that exit handler takes over complete responsibility for finalization of Tcl&#8217;s subsystems via <code>Tcl_Finalize</code> at an appropriate time. The argument passed to <i>proc</i> when it is invoked will be the exit status code (as passed to <code>Tcl_Exit</code>) cast to a ClientData value. </p>
<h2>Keywords</h2>
<p>callback, cleanup, dynamic loading, end application, exit, unloading, thread</p>
