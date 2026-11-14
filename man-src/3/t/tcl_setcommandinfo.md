---
title: "tcl_setcommandinfo(3)"
name: "tcl_setcommandinfo"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_setcommandinfo/"
description: "Tcl_CreateObjCommand, Tcl_DeleteCommand, Tcl_DeleteCommandFromToken, Tcl_GetCommandInfo, Tcl_GetCommandInfoFromToken, Tcl_SetCommandInfo, Tcl_SetCommandInfoFromToken, Tcl_GetCommandName, Tcl_GetCom..."
---

<p>Tcl_CreateObjCommand, Tcl_DeleteCommand, Tcl_DeleteCommandFromToken, Tcl_GetCommandInfo, Tcl_GetCommandInfoFromToken, Tcl_SetCommandInfo, Tcl_SetCommandInfoFromToken, Tcl_GetCommandName, Tcl_GetCommandFullName, Tcl_GetCommandFromObj &#8211; implement new commands in C </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Command
<code>Tcl_CreateObjCommand</code>(<i>interp, cmdName, proc, clientData, deleteProc</i>)
int
<code>Tcl_DeleteCommand</code>(<i>interp, cmdName</i>)
int
<code>Tcl_DeleteCommandFromToken</code>(<i>interp, token</i>)
int
<code>Tcl_GetCommandInfo</code>(<i>interp, cmdName, infoPtr</i>)
int
<code>Tcl_SetCommandInfo</code>(<i>interp, cmdName, infoPtr</i>)
int
<code>Tcl_GetCommandInfoFromToken</code>(<i>token, infoPtr</i>)
int
<code>Tcl_SetCommandInfoFromToken</code>(<i>token, infoPtr</i>)
const char *
<code>Tcl_GetCommandName</code>(<i>interp, token</i>)
void
<code>Tcl_GetCommandFullName</code>(<i>interp, token, objPtr</i>)
Tcl_Command
<code>Tcl_GetCommandFromObj</code>(<i>interp, objPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which to create a new command or that contains a command.</p>
<dd>char <i>*cmdName</i> (in) Name of command.</p>
<dd>Tcl_ObjCmdProc <i>*proc</i> (in) Implementation of the new command: <i>proc</i> will be called whenever <i>cmdName</i> is invoked as a command.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i> and <i>deleteProc</i>.</p>
<dd>Tcl_CmdDeleteProc <i>*deleteProc</i> (in) Procedure to call before <i>cmdName</i> is deleted from the interpreter; allows for command-specific cleanup. If NULL, then no procedure is called before the command is deleted.</p>
<dd>Tcl_Command <i>token</i> (in) Token for command, returned by previous call to <code>Tcl_CreateObjCommand</code>. The command must not have been deleted.</p>
<dd>Tcl_CmdInfo <i>*infoPtr</i> (in/out) Pointer to structure containing various information about a Tcl command.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in) Object containing the name of a Tcl command.
</dl>
<h2>Description</h2>
<p><code>Tcl_CreateObjCommand</code> defines a new command in <i>interp</i> and associates it with procedure <i>proc</i> such that whenever <i>name</i> is invoked as a Tcl command (e.g., via a call to <code>Tcl_EvalObjEx</code>) the Tcl interpreter will call <i>proc</i> to process the command. </p>
<p> <code>Tcl_CreateObjCommand</code> deletes any existing command <i>name</i> already associated with the interpreter (however see below for an exception where the existing command is not deleted). It returns a token that may be used to refer to the command in subsequent calls to <code>Tcl_GetCommandName</code>. If <i>name</i> contains any <code>::</code> namespace qualifiers, then the command is added to the specified namespace; otherwise the command is added to the global namespace. If <code>Tcl_CreateObjCommand</code> is called for an interpreter that is in the process of being deleted, then it does not create a new command and it returns NULL. <i>proc</i> should have arguments and result that match the type <code>Tcl_ObjCmdProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_ObjCmdProc(
 ClientData <i>clientData</i>,
 Tcl_Interp *<i>interp</i>,
 int <i>objc</i>,
 Tcl_Obj *const <i>objv</i>[]);</pre>
</dl>
<p> When <i>proc</i> is invoked, the <i>clientData</i> and <i>interp</i> parameters will be copies of the <i>clientData</i> and <i>interp</i> arguments given to <code>Tcl_CreateObjCommand</code>. Typically, <i>clientData</i> points to an application-specific data structure that describes what to do when the command procedure is invoked. <i>Objc</i> and <i>objv</i> describe the arguments to the command, <i>objc</i> giving the number of argument objects (including the command name) and <i>objv</i> giving the values of the arguments. The <i>objv</i> array will contain <i>objc</i> values, pointing to the argument objects. Unlike <i>argv</i>[<i>argv</i>] used in a string-based command procedure, <i>objv</i>[<i>objc</i>] will not contain NULL. </p>
<p> Additionally, when <i>proc</i> is invoked, it must not modify the contents of the <i>objv</i> array by assigning new pointer values to any element of the array (for example, <i>objv</i>[<code>2</code>] = <code>NULL</code>) because this will cause memory to be lost and the runtime stack to be corrupted. The <code>const</code> in the declaration of <i>objv</i> will cause ANSI-compliant compilers to report any such attempted assignment as an error. However, it is acceptable to modify the internal representation of any individual object argument. For instance, the user may call <code>Tcl_GetIntFromObj</code> on <i>objv</i>[<code>2</code>] to obtain the integer representation of that object; that call may change the type of the object that <i>objv</i>[<code>2</code>] points at, but will not change where <i>objv</i>[<code>2</code>] points. </p>
<p> <i>proc</i> must return an integer code that is either <code>TCL_OK</code>, <code>TCL_ERROR</code>, <code>TCL_RETURN</code>, <code>TCL_BREAK</code>, or <code>TCL_CONTINUE</code>. See the Tcl overview man page for details on what these codes mean. Most normal commands will only return <code>TCL_OK</code> or <code>TCL_ERROR</code>. In addition, if <i>proc</i> needs to return a non-empty result, it can call <code>Tcl_SetObjResult</code> to set the interpreter&#8217;s result. In the case of a <code>TCL_OK</code> return code this gives the result of the command, and in the case of <code>TCL_ERROR</code> this gives an error message. Before invoking a command procedure, <code>Tcl_EvalObjEx</code> sets interpreter&#8217;s result to point to an object representing an empty string, so simple commands can return an empty result by doing nothing at all. </p>
<p> The contents of the <i>objv</i> array belong to Tcl and are not guaranteed to persist once <i>proc</i> returns: <i>proc</i> should not modify them. Call <code>Tcl_SetObjResult</code> if you want to return something from the <i>objv</i> array. </p>
<p> Ordinarily, <code>Tcl_CreateObjCommand</code> deletes any existing command <i>name</i> already associated with the interpreter. However, if the existing command was created by a previous call to <code>Tcl_CreateCommand</code>, <code>Tcl_CreateObjCommand</code> does not delete the command but instead arranges for the Tcl interpreter to call the <code>Tcl_ObjCmdProc</code> <i>proc</i> in the future. The old string-based <code>Tcl_CmdProc</code> associated with the command is retained and its address can be obtained by subsequent <code>Tcl_GetCommandInfo</code> calls. This is done for backwards compatibility. </p>
<p> <i>DeleteProc</i> will be invoked when (if) <i>name</i> is deleted. This can occur through a call to <code>Tcl_DeleteCommand</code>, <code>Tcl_DeleteCommandFromToken</code>, or <code>Tcl_DeleteInterp</code>, or by replacing <i>name</i> in another call to <code>Tcl_CreateObjCommand</code>. <i>DeleteProc</i> is invoked before the command is deleted, and gives the application an opportunity to release any structures associated with the command. <i>DeleteProc</i> should have arguments and result that match the type <code>Tcl_CmdDeleteProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef void Tcl_CmdDeleteProc(
 ClientData <i>clientData</i>);</pre>
</dl>
<p> The <i>clientData</i> argument will be the same as the <i>clientData</i> argument passed to <code>Tcl_CreateObjCommand</code>. </p>
<p> <code>Tcl_DeleteCommand</code> deletes a command from a command interpreter. Once the call completes, attempts to invoke <i>cmdName</i> in <i>interp</i> will result in errors. If <i>cmdName</i> is not bound as a command in <i>interp</i> then <code>Tcl_DeleteCommand</code> does nothing and returns -1; otherwise it returns 0. There are no restrictions on <i>cmdName</i>: it may refer to a built-in command, an application-specific command, or a Tcl procedure. If <i>name</i> contains any <code>::</code> namespace qualifiers, the command is deleted from the specified namespace. </p>
<p> Given a token returned by <code>Tcl_CreateObjCommand</code>, <code>Tcl_DeleteCommandFromToken</code> deletes the command from a command interpreter. It will delete a command even if that command has been renamed. Once the call completes, attempts to invoke the command in <i>interp</i> will result in errors. If the command corresponding to <i>token</i> has already been deleted from <i>interp</i> then <code>Tcl_DeleteCommand</code> does nothing and returns -1; otherwise it returns 0. </p>
<p> <code>Tcl_GetCommandInfo</code> checks to see whether its <i>cmdName</i> argument exists as a command in <i>interp</i>. <i>cmdName</i> may include <code>::</code> namespace qualifiers to identify a command in a particular namespace. If the command is not found, then it returns 0. Otherwise it places information about the command in the <code>Tcl_CmdInfo</code> structure pointed to by <i>infoPtr</i> and returns 1. A <code>Tcl_CmdInfo</code> structure has the following fields:</p>
<dl COMPACT>
<dd>
<pre>typedef struct Tcl_CmdInfo {
 int <i>isNativeObjectProc</i>;
 Tcl_ObjCmdProc *<i>objProc</i>;
 ClientData <i>objClientData</i>;
 Tcl_CmdProc *<i>proc</i>;
 ClientData <i>clientData</i>;
 Tcl_CmdDeleteProc *<i>deleteProc</i>;
 ClientData <i>deleteData</i>;
 Tcl_Namespace *<i>namespacePtr</i>;
} Tcl_CmdInfo;</pre>
</dl>
<p> The <i>isNativeObjectProc</i> field has the value 1 if <code>Tcl_CreateObjCommand</code> was called to register the command; it is 0 if only <code>Tcl_CreateCommand</code> was called. It allows a program to determine whether it is faster to call <i>objProc</i> or <i>proc</i>: <i>objProc</i> is normally faster if <i>isNativeObjectProc</i> has the value 1. The fields <i>objProc</i> and <i>objClientData</i> have the same meaning as the <i>proc</i> and <i>clientData</i> arguments to <code>Tcl_CreateObjCommand</code>; they hold information about the object-based command procedure that the Tcl interpreter calls to implement the command. The fields <i>proc</i> and <i>clientData</i> hold information about the string-based command procedure that implements the command. If <code>Tcl_CreateCommand</code> was called for this command, this is the procedure passed to it; otherwise, this is a compatibility procedure registered by <code>Tcl_CreateObjCommand</code> that simply calls the command&#8217;s object-based procedure after converting its string arguments to Tcl objects. The field <i>deleteData</i> is the ClientData value to pass to <i>deleteProc</i>; it is normally the same as <i>clientData</i> but may be set independently using the <code>Tcl_SetCommandInfo</code> procedure. The field <i>namespacePtr</i> holds a pointer to the Tcl_Namespace that contains the command. </p>
<p> <code>Tcl_GetCommandInfoFromToken</code> is identical to <code>Tcl_GetCommandInfo</code> except that it uses a command token returned from <code>Tcl_CreateObjCommand</code> in place of the command name. If the <i>token</i> parameter is NULL, it returns 0; otherwise, it returns 1 and fills in the structure designated by <i>infoPtr</i>. </p>
<p> <code>Tcl_SetCommandInfo</code> is used to modify the procedures and ClientData values associated with a command. Its <i>cmdName</i> argument is the name of a command in <i>interp</i>. <i>cmdName</i> may include <code>::</code> namespace qualifiers to identify a command in a particular namespace. If this command does not exist then <code>Tcl_SetCommandInfo</code> returns 0. Otherwise, it copies the information from <i>*infoPtr</i> to Tcl&#8217;s internal structure for the command and returns 1. </p>
<p> <code>Tcl_SetCommandInfoFromToken</code> is identical to <code>Tcl_SetCommandInfo</code> except that it takes a command token as returned by <code>Tcl_CreateObjCommand</code> instead of the command name. If the <i>token</i> parameter is NULL, it returns 0. Otherwise, it copies the information from <i>*infoPtr</i> to Tcl&#8217;s internal structure for the command and returns 1. </p>
<p> Note that <code>Tcl_SetCommandInfo</code> and <code>Tcl_SetCommandInfoFromToken</code> both allow the ClientData for a command&#8217;s deletion procedure to be given a different value than the ClientData for its command procedure. </p>
<p> Note that neither <code>Tcl_SetCommandInfo</code> nor <code>Tcl_SetCommandInfoFromToken</code> will change a command&#8217;s namespace. Use <code>Tcl_Eval</code> to call the <code>rename</code> command to do that. </p>
<p> <code>Tcl_GetCommandName</code> provides a mechanism for tracking commands that have been renamed. Given a token returned by <code>Tcl_CreateObjCommand</code> when the command was created, <code>Tcl_GetCommandName</code> returns the string name of the command. If the command has been renamed since it was created, then <code>Tcl_GetCommandName</code> returns the current name. This name does not include any <code>::</code> namespace qualifiers. The command corresponding to <i>token</i> must not have been deleted. The string returned by <code>Tcl_GetCommandName</code> is in dynamic memory owned by Tcl and is only guaranteed to retain its value as long as the command is not deleted or renamed; callers should copy the string if they need to keep it for a long time. </p>
<p> <code>Tcl_GetCommandFullName</code> produces the fully qualified name of a command from a command token. The name, including all namespace prefixes, is appended to the object specified by <i>objPtr</i>. </p>
<p> <code>Tcl_GetCommandFromObj</code> returns a token for the command specified by the name in a <code>Tcl_Obj</code>. The command name is resolved relative to the current namespace. Returns NULL if the command is not found.</p>
<h2>See Also</h2>
<p>Tcl_CreateCommand, Tcl_ResetResult, Tcl_SetObjResult </p>
<h2>Keywords</h2>
<p>bind, command, create, delete, namespace, object</p>
