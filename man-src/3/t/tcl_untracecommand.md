---
title: "tcl_untracecommand(3)"
name: "tcl_untracecommand"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_untracecommand/"
description: "Tcl_CommandTraceInfo, Tcl_TraceCommand, Tcl_UntraceCommand – monitor renames and deletes of a command"
---

<p>Tcl_CommandTraceInfo, Tcl_TraceCommand, Tcl_UntraceCommand &#8211; monitor renames and deletes of a command </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
ClientData
<code>Tcl_CommandTraceInfo(</code><i>interp, cmdName, flags, proc, prevClientData</i><code>)</code>
int
<code>Tcl_TraceCommand(</code><i>interp, cmdName, flags, proc, clientData</i><code>)</code>
void
<code>Tcl_UntraceCommand(</code><i>interp, cmdName, flags, proc, clientData</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter containing the command.</p>
<dd>const char <i>*cmdName</i> (in) Name of command.</p>
<dd>int <i>flags</i> (in) OR&#8217;ed collection of the values <code>TCL_TRACE_RENAME</code> and <code>TCL_TRACE_DELETE</code>.</p>
<dd>Tcl_CommandTraceProc <i>*proc</i> (in) Procedure to call when specified operations occur to <i>cmdName</i>.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary argument to pass to <i>proc</i>.</p>
<dd>ClientData <i>prevClientData</i> (in) If non-NULL, gives last value returned by <code>Tcl_CommandTraceInfo</code>, so this call will return information about next trace. If NULL, this call will return information about first trace.
</dl>
<h2>Description</h2>
<p><code>Tcl_TraceCommand</code> allows a C procedure to monitor operations performed on a Tcl command, so that the C procedure is invoked whenever the command is renamed or deleted. If the trace is created successfully then <code>Tcl_TraceCommand</code> returns <code>TCL_OK</code>. If an error occurred (e.g. <i>cmdName</i> specifies a non-existent command) then <code>TCL_ERROR</code> is returned and an error message is left in the interpreter&#8217;s result. </p>
<p> The <i>flags</i> argument to <code>Tcl_TraceCommand</code> indicates when the trace procedure is to be invoked. It consists of an OR&#8217;ed combination of any of the following values:</p>
<dl COMPACT>
<dt><code>TCL_TRACE_RENAME</code></p>
<dd>Invoke <i>proc</i> whenever the command is renamed.</p>
<dt><code>TCL_TRACE_DELETE</code></p>
<dd>Invoke <i>proc</i> when the command is deleted.</dl>
<p> Whenever one of the specified operations occurs to the command, <i>proc</i> will be invoked. It should have arguments and result that match the type <code>Tcl_CommandTraceProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_CommandTraceProc(
 ClientData <i>clientData</i>,
 Tcl_Interp *<i>interp</i>,
 const char *<i>oldName</i>,
 const char *<i>newName</i>,
 int <i>flags</i>);</pre>
</dl>
<p> The <i>clientData</i> and <i>interp</i> parameters will have the same values as those passed to <code>Tcl_TraceCommand</code> when the trace was created. <i>ClientData</i> typically points to an application-specific data structure that describes what to do when <i>proc</i> is invoked. <i>OldName</i> gives the name of the command being renamed, and <i>newName</i> gives the name that the command is being renamed to (or an empty string or NULL when the command is being deleted.) <i>Flags</i> is an OR&#8217;ed combination of bits potentially providing several pieces of information. One of the bits <code>TCL_TRACE_RENAME</code> and <code>TCL_TRACE_DELETE</code> will be set in <i>flags</i> to indicate which operation is being performed on the command. The bit <code>TCL_TRACE_DESTROYED</code> will be set in <i>flags</i> if the trace is about to be destroyed; this information may be useful to <i>proc</i> so that it can clean up its own internal data structures (see the section <code>TCL_TRACE_DESTROYED</code> below for more details). Lastly, the bit <code>TCL_INTERP_DESTROYED</code> will be set if the entire interpreter is being destroyed. When this bit is set, <i>proc</i> must be especially careful in the things it does (see the section <code>TCL_INTERP_DESTROYED</code> below). </p>
<p> <code>Tcl_UntraceCommand</code> may be used to remove a trace. If the command specified by <i>interp</i>, <i>cmdName</i>, and <i>flags</i> has a trace set with <i>flags</i>, <i>proc</i>, and <i>clientData</i>, then the corresponding trace is removed. If no such trace exists, then the call to <code>Tcl_UntraceCommand</code> has no effect. The same bits are valid for <i>flags</i> as for calls to <code>Tcl_TraceCommand</code>. </p>
<p> <code>Tcl_CommandTraceInfo</code> may be used to retrieve information about traces set on a given command. The return value from <code>Tcl_CommandTraceInfo</code> is the <i>clientData</i> associated with a particular trace. The trace must be on the command specified by the <i>interp</i>, <i>cmdName</i>, and <i>flags</i> arguments (note that currently the flags are ignored; <i>flags</i> should be set to 0 for future compatibility) and its trace procedure must the same as the <i>proc</i> argument. If the <i>prevClientData</i> argument is NULL then the return value corresponds to the first (most recently created) matching trace, or NULL if there are no matching traces. If the <i>prevClientData</i> argument is not NULL, then it should be the return value from a previous call to <code>Tcl_CommandTraceInfo</code>. In this case, the new return value will correspond to the next matching trace after the one whose <i>clientData</i> matches <i>prevClientData</i>, or NULL if no trace matches <i>prevClientData</i> or if there are no more matching traces after it. This mechanism makes it possible to step through all of the traces for a given command that have the same <i>proc</i>.</p>
<h2>Calling Commands During Traces</h2>
<p>During rename traces, the command being renamed is visible with both names simultaneously, and the command still exists during delete traces (if <code>TCL_INTERP_DESTROYED</code> is not set). However, there is no mechanism for signaling that an error occurred in a trace procedure, so great care should be taken that errors do not get silently lost.</p>
<h2>Multiple Traces</h2>
<p>It is possible for multiple traces to exist on the same command. When this happens, all of the trace procedures will be invoked on each access, in order from most-recently-created to least-recently-created. Attempts to delete the command during a delete trace will fail silently, since the command is already scheduled for deletion anyway. If the command being renamed is renamed by one of its rename traces, that renaming takes precedence over the one that triggered the trace and the collection of traces will not be reexecuted; if several traces rename the command, the last renaming takes precedence.</p>
<h2>Tcl_Trace_Destroyed Flag</h2>
<p>In a delete callback to <i>proc</i>, the <code>TCL_TRACE_DESTROYED</code> bit is set in <i>flags</i>.</p>
<h2>Tcl_Interp_Destroyed</h2>
<p>When an interpreter is destroyed, unset traces are called for all of its commands. The <code>TCL_INTERP_DESTROYED</code> bit will be set in the <i>flags</i> argument passed to the trace procedures. Trace procedures must be extremely careful in what they do if the <code>TCL_INTERP_DESTROYED</code> bit is set. It is not safe for the procedures to invoke any Tcl procedures on the interpreter, since its state is partially deleted. All that trace procedures should do under these circumstances is to clean up and free their own internal data structures.</p>
<h2>Bugs</h2>
<p>Tcl does not do any error checking to prevent trace procedures from misusing the interpreter during traces with <code>TCL_INTERP_DESTROYED</code> set.</p>
<h2>Keywords</h2>
<p>clientData, trace, command</p>
