---
title: "tcl_createcommand(3)"
name: "tcl_createcommand"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_createcommand/"
description: "Tcl_CreateCommand – implement new commands in C"
---

<p>Tcl_CreateCommand &#8211; implement new commands in C </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Command
<code>Tcl_CreateCommand</code>(<i>interp, cmdName, proc, clientData, deleteProc</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which to create new command.</p>
<dd>const char <i>*cmdName</i> (in) Name of command.</p>
<dd>Tcl_CmdProc <i>*proc</i> (in) Implementation of new command: <i>proc</i> will be called whenever <i>cmdName</i> is invoked as a command.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i> and <i>deleteProc</i>.</p>
<dd>Tcl_CmdDeleteProc <i>*deleteProc</i> (in) Procedure to call before <i>cmdName</i> is deleted from the interpreter; allows for command-specific cleanup. If NULL, then no procedure is called before the command is deleted. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_CreateCommand</code> defines a new command in <i>interp</i> and associates it with procedure <i>proc</i> such that whenever <i>cmdName</i> is invoked as a Tcl command (via a call to <code>Tcl_Eval</code>) the Tcl interpreter will call <i>proc</i> to process the command. It differs from <code>Tcl_CreateObjCommand</code> in that a new string-based command is defined; that is, a command procedure is defined that takes an array of argument strings instead of objects. The object-based command procedures registered by <code>Tcl_CreateObjCommand</code> can execute significantly faster than the string-based command procedures defined by <code>Tcl_CreateCommand</code>. This is because they take Tcl objects as arguments and those objects can retain an internal representation that can be manipulated more efficiently. Also, Tcl&#8217;s interpreter now uses objects internally. In order to invoke a string-based command procedure registered by <code>Tcl_CreateCommand</code>, it must generate and fetch a string representation from each argument object before the call and create a new Tcl object to hold the string result returned by the string-based command procedure. New commands should be defined using <code>Tcl_CreateObjCommand</code>. We support <code>Tcl_CreateCommand</code> for backwards compatibility. </p>
<p> The procedures <code>Tcl_DeleteCommand</code>, <code>Tcl_GetCommandInfo</code>, and <code>Tcl_SetCommandInfo</code> are used in conjunction with <code>Tcl_CreateCommand</code>. </p>
<p> <code>Tcl_CreateCommand</code> will delete an existing command <i>cmdName</i>, if one is already associated with the interpreter. It returns a token that may be used to refer to the command in subsequent calls to <code>Tcl_GetCommandName</code>. If <i>cmdName</i> contains any <code>::</code> namespace qualifiers, then the command is added to the specified namespace; otherwise the command is added to the global namespace. If <code>Tcl_CreateCommand</code> is called for an interpreter that is in the process of being deleted, then it does not create a new command and it returns NULL. <i>Proc</i> should have arguments and result that match the type <code>Tcl_CmdProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_CmdProc(
 ClientData <i>clientData</i>,
 Tcl_Interp *<i>interp</i>,
 int <i>argc</i>,
 const char *<i>argv</i>[]);</pre>
</dl>
<p> When <i>proc</i> is invoked the <i>clientData</i> and <i>interp</i> parameters will be copies of the <i>clientData</i> and <i>interp</i> arguments given to <code>Tcl_CreateCommand</code>. Typically, <i>clientData</i> points to an application-specific data structure that describes what to do when the command procedure is invoked. <i>Argc</i> and <i>argv</i> describe the arguments to the command, <i>argc</i> giving the number of arguments (including the command name) and <i>argv</i> giving the values of the arguments as strings. The <i>argv</i> array will contain <i>argc</i>+1 values; the first <i>argc</i> values point to the argument strings, and the last value is NULL. Note that the argument strings should not be modified as they may point to constant strings or may be shared with other parts of the interpreter. </p>
<p> Note that the argument strings are encoded in normalized UTF-8 since version 8.1 of Tcl. </p>
<p> <i>Proc</i> must return an integer code that is expected to be one of <code>TCL_OK</code>, <code>TCL_ERROR</code>, <code>TCL_RETURN</code>, <code>TCL_BREAK</code>, or <code>TCL_CONTINUE</code>. See the Tcl overview man page for details on what these codes mean. Most normal commands will only return <code>TCL_OK</code> or <code>TCL_ERROR</code>. In addition, <i>proc</i> must set the interpreter result to point to a string value; in the case of a <code>TCL_OK</code> return code this gives the result of the command, and in the case of <code>TCL_ERROR</code> it gives an error message. The <code>Tcl_SetResult</code> procedure provides an easy interface for setting the return value; for complete details on how the interpreter result field is managed, see the <code>Tcl_Interp</code> man page. Before invoking a command procedure, <code>Tcl_Eval</code> sets the interpreter result to point to an empty string, so simple commands can return an empty result by doing nothing at all. </p>
<p> The contents of the <i>argv</i> array belong to Tcl and are not guaranteed to persist once <i>proc</i> returns: <i>proc</i> should not modify them, nor should it set the interpreter result to point anywhere within the <i>argv</i> values. Call <code>Tcl_SetResult</code> with status <code>TCL_VOLATILE</code> if you want to return something from the <i>argv</i> array. </p>
<p> <i>DeleteProc</i> will be invoked when (if) <i>cmdName</i> is deleted. This can occur through a call to <code>Tcl_DeleteCommand</code> or <code>Tcl_DeleteInterp</code>, or by replacing <i>cmdName</i> in another call to <code>Tcl_CreateCommand</code>. <i>DeleteProc</i> is invoked before the command is deleted, and gives the application an opportunity to release any structures associated with the command. <i>DeleteProc</i> should have arguments and result that match the type <code>Tcl_CmdDeleteProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_CmdDeleteProc(
 ClientData <i>clientData</i>);</pre>
</dl>
<p> The <i>clientData</i> argument will be the same as the <i>clientData</i> argument passed to <code>Tcl_CreateCommand</code>. </p>
<h2>See Also</h2>
<p>Tcl_CreateObjCommand, Tcl_DeleteCommand, Tcl_GetCommandInfo, Tcl_SetCommandInfo, Tcl_GetCommandName, Tcl_SetObjResult </p>
<h2>Keywords</h2>
<p>bind, command, create, delete, interpreter, namespace</p>
