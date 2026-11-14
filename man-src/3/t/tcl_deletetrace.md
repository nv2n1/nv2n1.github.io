---
title: "tcl_deletetrace(3)"
name: "tcl_deletetrace"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_deletetrace/"
description: "Tcl_CreateTrace, Tcl_CreateObjTrace, Tcl_DeleteTrace – arrange for command execution to be traced"
---

<p>Tcl_CreateTrace, Tcl_CreateObjTrace, Tcl_DeleteTrace &#8211; arrange for command execution to be traced </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Trace
<code>Tcl_CreateTrace</code>(<i>interp, level, proc, clientData</i>)
Tcl_Trace
<code>Tcl_CreateObjTrace</code>(<i>interp, level, flags, objProc, clientData, deleteProc</i>)
<code>Tcl_DeleteTrace</code>(<i>interp, trace</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter containing command to be traced or untraced.</p>
<dd>int <i>level</i> (in) Only commands at or below this nesting level will be traced unless 0 is specified. 1 means top-level commands only, 2 means top-level commands or those that are invoked as immediate consequences of executing top-level commands (procedure bodies, bracketed commands, etc.) and so on. A value of 0 means that commands at any level are traced.</p>
<dd>int <i>flags</i> (in) Flags governing the trace execution. See below for details.</p>
<dd>Tcl_CmdObjTraceProc <i>*objProc</i> (in) Procedure to call for each command that is executed. See below for details of the calling sequence.</p>
<dd>Tcl_CmdTraceProc <i>*proc</i> (in) Procedure to call for each command that is executed. See below for details on the calling sequence.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>objProc</i> or <i>proc</i>.</p>
<dd>Tcl_CmdObjTraceDeleteProc <i>*deleteProc</i> (in) Procedure to call when the trace is deleted. See below for details of the calling sequence. A NULL pointer is permissible and results in no callback when the trace is deleted.</p>
<dd>Tcl_Trace <i>trace</i> (in) Token for trace to be removed (return value from previous call to <code>Tcl_CreateTrace</code>).
</dl>
<h2>Description</h2>
<p><code>Tcl_CreateObjTrace</code> arranges for command tracing. After it is called, <i>objProc</i> will be invoked before the Tcl interpreter calls any command procedure when evaluating commands in <i>interp</i>. The return value from <code>Tcl_CreateObjTrace</code> is a token for the trace, which may be passed to <code>Tcl_DeleteTrace</code> to remove the trace. There may be many traces in effect simultaneously for the same interpreter. </p>
<p> <i>objProc</i> should have arguments and result that match the type, <code>Tcl_CmdObjTraceProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef int <code>Tcl_CmdObjTraceProc</code>( 
 <code>ClientData</code> <i>clientData</i>,
 <code>Tcl_Interp</code>* <i>interp</i>,
 int <i>level</i>,
 const char *<i>command</i>,
 <code>Tcl_Command</code> <i>commandToken</i>,
 int <i>objc</i>,
 <code>Tcl_Obj</code> *const <i>objv</i>[] );</pre>
</dl>
<p> The <i>clientData</i> and <i>interp</i> parameters are copies of the corresponding arguments given to <code>Tcl_CreateTrace</code>. <i>ClientData</i> typically points to an application-specific data structure that describes what to do when <i>objProc</i> is invoked. The <i>level</i> parameter gives the nesting level of the command (1 for top-level commands passed to <code>Tcl_Eval</code> by the application, 2 for the next-level commands passed to <code>Tcl_Eval</code> as part of parsing or interpreting level-1 commands, and so on). The <i>command</i> parameter points to a string containing the text of the command, before any argument substitution. The <i>commandToken</i> parameter is a Tcl command token that identifies the command to be invoked. The token may be passed to <code>Tcl_GetCommandName</code>, <code>Tcl_GetCommandInfoFromToken</code>, or <code>Tcl_SetCommandInfoFromToken</code> to manipulate the definition of the command. The <i>objc</i> and <i>objv</i> parameters designate the final parameter count and parameter vector that will be passed to the command, and have had all substitutions performed. </p>
<p> The <i>objProc</i> callback is expected to return a standard Tcl status return code. If this code is <code>TCL_OK</code> (the normal case), then the Tcl interpreter will invoke the command. Any other return code is treated as if the command returned that status, and the command is <i>not</i> invoked. </p>
<p> The <i>objProc</i> callback must not modify <i>objv</i> in any way. It is, however, permissible to change the command by calling <code>Tcl_SetCommandTokenInfo</code> prior to returning. Any such change takes effect immediately, and the command is invoked with the new information. </p>
<p> Tracing will only occur for commands at nesting level less than or equal to the <i>level</i> parameter (i.e. the <i>level</i> parameter to <i>objProc</i> will always be less than or equal to the <i>level</i> parameter to <code>Tcl_CreateTrace</code>). </p>
<p> Tracing has a significant effect on runtime performance because it causes the bytecode compiler to refrain from generating in-line code for Tcl commands such as <code>if</code> and <code>while</code> in order that they may be traced. If traces for the built-in commands are not required, the <i>flags</i> parameter may be set to the constant value <code>TCL_ALLOW_INLINE_COMPILATION</code>. In this case, traces on built-in commands may or may not result in trace callbacks, depending on the state of the interpreter, but run-time performance will be improved significantly. (This functionality is desirable, for example, when using <code>Tcl_CreateObjTrace</code> to implement an execution time profiler.) </p>
<p> Calls to <i>objProc</i> will be made by the Tcl parser immediately before it calls the command procedure for the command (<i>cmdProc</i>). This occurs after argument parsing and substitution, so tracing for substituted commands occurs before tracing of the commands containing the substitutions. If there is a syntax error in a command, or if there is no command procedure associated with a command name, then no tracing will occur for that command. If a string passed to Tcl_Eval contains multiple commands (bracketed, or on different lines) then multiple calls to <i>objProc</i> will occur, one for each command. </p>
<p> <code>Tcl_DeleteTrace</code> removes a trace, so that no future calls will be made to the procedure associated with the trace. After <code>Tcl_DeleteTrace</code> returns, the caller should never again use the <i>trace</i> token. </p>
<p> When <code>Tcl_DeleteTrace</code> is called, the interpreter invokes the <i>deleteProc</i> that was passed as a parameter to <code>Tcl_CreateObjTrace</code>. The <i>deleteProc</i> must match the type, <code>Tcl_CmdObjTraceDeleteProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef void <code>Tcl_CmdObjTraceDeleteProc</code>( 
 <code>ClientData</code> <i>clientData</i>);</pre>
</dl>
<p> The <i>clientData</i> parameter will be the same as the <i>clientData</i> parameter that was originally passed to <code>Tcl_CreateObjTrace</code>. </p>
<p> <code>Tcl_CreateTrace</code> is an alternative interface for command tracing, <i>not recommended for new applications</i>. It is provided for backward compatibility with code that was developed for older versions of the Tcl interpreter. It is similar to <code>Tcl_CreateObjTrace</code>, except that its <i>proc</i> parameter should have arguments and result that match the type <code>Tcl_CmdTraceProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_CmdTraceProc(
 ClientData <i>clientData</i>,
 Tcl_Interp *<i>interp</i>,
 int <i>level</i>,
 char *<i>command</i>,
 Tcl_CmdProc *<i>cmdProc</i>,
 ClientData <i>cmdClientData</i>,
 int <i>argc</i>,
 const char *<i>argv</i>[]);</pre>
</dl>
<p> The parameters to the <i>proc</i> callback are similar to those of the <i>objProc</i> callback above. The <i>commandToken</i> is replaced with <i>cmdProc</i>, a pointer to the (string-based) command procedure that will be invoked; and <i>cmdClientData</i>, the client data that will be passed to the procedure. The <i>objc</i> parameter is replaced with an <i>argv</i> parameter, that gives the arguments to the command as character strings. <i>Proc</i> must not modify the <i>command</i> or <i>argv</i> strings. </p>
<p> If a trace created with <code>Tcl_CreateTrace</code> is in effect, inline compilation of Tcl commands such as <code>if</code> and <code>while</code> is always disabled. There is no notification when a trace created with <code>Tcl_CreateTrace</code> is deleted. There is no way to be notified when the trace created by <code>Tcl_CreateTrace</code> is deleted. There is no way for the <i>proc</i> associated with a call to <code>Tcl_CreateTrace</code> to abort execution of <i>command</i>.</p>
<h2>Keywords</h2>
<p>command, create, delete, interpreter, trace</p>
