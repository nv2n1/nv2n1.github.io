---
title: "tcl_nrcreatecommand(3)"
name: "tcl_nrcreatecommand"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_nrcreatecommand/"
description: "Tcl_NRCreateCommand, Tcl_NRCallObjProc, Tcl_NREvalObj, Tcl_NREvalObjv, Tcl_NRCmdSwap, Tcl_NRExprObj, Tcl_NRAddCallback – Non-Recursive (stackless) evaluation of Tcl scripts."
---

<p>Tcl_NRCreateCommand, Tcl_NRCallObjProc, Tcl_NREvalObj, Tcl_NREvalObjv, Tcl_NRCmdSwap, Tcl_NRExprObj, Tcl_NRAddCallback &#8211; Non-Recursive (stackless) evaluation of Tcl scripts. </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Command
<code>Tcl_NRCreateCommand</code>(<i>interp, cmdName, proc, nreProc, clientData,
 deleteProc</i>)
int
<code>Tcl_NRCallObjProc</code>(<i>interp, nreProc, clientData, objc, objv</i>)
int
<code>Tcl_NREvalObj</code>(<i>interp, objPtr, flags</i>)
int
<code>Tcl_NREvalObjv</code>(<i>interp, objc, objv, flags</i>)
int
<code>Tcl_NRCmdSwap</code>(<i>interp, cmd, objc, objv, flags</i>)
int
<code>Tcl_NRExprObj</code>(<i>interp, objPtr, resultPtr</i>)
void
<code>Tcl_NRAddCallback</code>(<i>interp, postProcPtr, data0, data1, data2, data3</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which to create or evaluate a command.</p>
<dd>char <i>*cmdName</i> (in) Name of a new command to create.</p>
<dd>Tcl_ObjCmdProc <i>*proc</i> (in) Implementation of a command that will be called whenever <i>cmdName</i> is invoked as a command in the unoptimized way.</p>
<dd>Tcl_ObjCmdProc <i>*nreProc</i> (in) Implementation of a command that will be called whenever <i>cmdName</i> is invoked and requested to conserve the C stack.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value that will be passed to <i>proc</i>, <i>nreProc</i>, <i>deleteProc</i> and <i>objProc</i>.</p>
<dd>Tcl_CmdDeleteProc <i>*deleteProc</i> (in/out) Procedure to call before <i>cmdName</i> is deleted from the interpreter. This procedure allows for command-specific cleanup. If <i>deleteProc</i> is <code>NULL</code>, then no procedure is called before the command is deleted.</p>
<dd>int <i>objc</i> (in) Count of parameters provided to the implementation of a command.</p>
<dd>Tcl_Obj <i>**objv</i> (in) Pointer to an array of Tcl values. Each value holds the value of a single word in the command to execute.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in) Pointer to a Tcl_Obj whose value is a script or expression to execute.</p>
<dd>int <i>flags</i> (in) ORed combination of flag bits that specify additional options. <code>TCL_EVAL_GLOBAL</code> is the only flag that is currently supported.</p>
<dd>Tcl_Command <i>cmd</i> (in) Token for a command that is to be used instead of the currently executing command.</p>
<dd>Tcl_Obj <i>*resultPtr</i> (out) Pointer to an unshared Tcl_Obj where the result of expression evaluation is written.</p>
<dd>Tcl_NRPostProc <i>*postProcPtr</i> (in) Pointer to a function that will be invoked when the command currently executing in the interpreter designated by <i>interp</i> completes.</p>
<dd>ClientData <i>data0</i> (in)</p>
<dd>ClientData <i>data1</i> (in)</p>
<dd>ClientData <i>data2</i> (in)</p>
<dd>ClientData <i>data3</i> (in) <i>data0</i> through <i>data3</i> are four one-word values that will be passed to the function designated by <i>postProcPtr</i> when it is invoked.
</dl>
<h2>Description</h2>
<p>This series of C functions provides an interface whereby commands that are implemented in C can be evaluated, and invoke Tcl commands scripts and scripts, without consuming space on the C stack. The non-recursive evaluation is done by installing a <i>trampoline</i>, a small piece of code that invokes a command or script, and then executes a series of callbacks when the command or script returns. </p>
<p> The <code>Tcl_NRCreateCommand</code> function creates a Tcl command in the interpreter designated by <i>interp</i> that is prepared to handle nonrecursive evaluation with a trampoline. The <i>cmdName</i> argument gives the name of the new command. If <i>cmdName</i> contains any namespace qualifiers, then the new command is added to the specified namespace; otherwise, it is added to the global namespace. <i>proc</i> gives the procedure that will be called when the interpreter wishes to evaluate the command in an unoptimized manner, and <i>nreProc</i> is the procedure that will be called when the interpreter wishes to evaluate the command using a trampoline. <i>deleteProc</i> is a function that will be called before the command is deleted from the interpreter. When any of the three functions is invoked, it is passed the <i>clientData</i> parameter. </p>
<p> <code>Tcl_NRCreateCommand</code> deletes any existing command <i>name</i> already associated with the interpreter (however see below for an exception where the existing command is not deleted). It returns a token that may be used to refer to the command in subsequent calls to <code>Tcl_GetCommandName</code>. If <code>Tcl_NRCreateCommand</code> is called for an interpreter that is in the process of being deleted, then it does not create a new command, does not delete any existing command of the same name, and returns NULL. </p>
<p> The <i>proc</i> and <i>nreProc</i> function are expected to conform to all the rules set forth for the <i>proc</i> argument to <code><a href="/docs/linux/man/3-tcl_createobjcommand/">Tcl_CreateObjCommand</a></code>(3) (<i>q.v.</i>). </p>
<p> When a command that is written to cope with evaluation via trampoline is invoked without a trampoline on the stack, it will usually respond to the invocation by creating a trampoline and calling the trampoline-enabled implementation of the same command. This call is done by means of <code>Tcl_NRCallObjProc</code>. In the call to <code>Tcl_NRCallObjProc</code>, the <i>interp</i>, <i>clientData</i>, <i>objc</i> and <i>objv</i> parameters should be the same ones that were passed to <i>proc</i>. The <i>nreProc</i> parameter should designate the trampoline-enabled implementation of the command. </p>
<p> <code>Tcl_NREvalObj</code> arranges for the script contained in <i>objPtr</i> to be evaluated in the interpreter designated by <i>interp</i> after the current command (which must be trampoline-enabled) returns. It is the method by which a command may invoke a script without consuming space on the C stack. Similarly, <code>Tcl_NREvalObjv</code> arranges to invoke a single Tcl command whose words have already been separated and substituted. The <i>objc</i> and <i>objv</i> parameters give the words of the command to be evaluated when execution reaches the trampoline. </p>
<p> <code>Tcl_NRCmdSwap</code> allows for trampoline evaluation of a command whose resolution is already known. The <i>cmd</i> parameter gives a <code>Tcl_Command</code> token (returned from <code>Tcl_CreateObjCommand</code> or <code>Tcl_GetCommandFromObj</code>) identifying the command to be invoked in the trampoline; this command must match the word in <i>objv[0]</i>. The remaining arguments are as for <code>Tcl_NREvalObjv</code>. </p>
<p> <code>Tcl_NREvalObj</code>, <code>Tcl_NREvalObjv</code> and <code>Tcl_NRCmdSwap</code> all accept a <i>flags</i> parameter, which is an OR-ed-together set of bits to control evaluation. At the present time, the only supported flag available to callers is <code>TCL_EVAL_GLOBAL</code>. If the <code>TCL_EVAL_GLOBAL</code> flag is set, the script or command is evaluated in the global namespace. If it is not set, it is evaluated in the current namespace. </p>
<p> <code>Tcl_NRExprObj</code> arranges for the expression contained in <i>objPtr</i> to be evaluated in the interpreter designated by <i>interp</i> after the current command (which must be trampoline-enabled) returns. It is the method by which a command may evaluate a Tcl expression without consuming space on the C stack. The argument <i>resultPtr</i> is a pointer to an unshared Tcl_Obj where the result of expression evaluation is to be written. If expression evaluation returns any code other than TCL_OK, the <i>resultPtr</i> value is left untouched. </p>
<p> All of the routines return <code>TCL_OK</code> if command or expression invocation has been scheduled successfully. If for any reason the scheduling cannot be completed (for example, if the interpreter is unable to find the requested command), they return <code>TCL_ERROR</code> with an appropriate message left in the interpreter&#8217;s result. </p>
<p> <code>Tcl_NRAddCallback</code> arranges to have a C function called when the current trampoline-enabled command in the Tcl interpreter designated by <i>interp</i> returns. The <i>postProcPtr</i> argument is a pointer to the callback function, which must have arguments and return value consistent with the <code>Tcl_NRPostProc</code> data type: </p>
<dl COMPACT>
<dd>
<pre>typedef int
<code>Tcl_NRPostProc</code>(
 <code>ClientData</code> <i>data</i>[],
 <code>Tcl_Interp</code> *<i>interp</i>,
 int <i>result</i>);</pre>
</dl>
<p> When the trampoline invokes the callback function, the <i>data</i> parameter will point to an array containing the four one-word quantities that were passed to <code>Tcl_NRAddCallback</code> in the <i>data0</i> through <i>data3</i> parameters. The Tcl interpreter will be designated by the <i>interp</i> parameter, and the <i>result</i> parameter will contain the result (<code>TCL_OK</code>, <code>TCL_ERROR</code>, <code>TCL_RETURN</code>, <code>TCL_BREAK</code> or <code>TCL_CONTINUE</code>) that was returned by the command evaluation. The callback function is expected, in turn, either to return a <i>result</i> to control further evaluation. </p>
<p> Multiple <code>Tcl_NRAddCallback</code> invocations may request multiple callbacks, which may be to the same or different callback functions. If multiple callbacks are requested, they are executed in last-in, first-out order, that is, the most recently requested callback is executed first.</p>
<h2>Example</h2>
<p>The usual pattern for Tcl commands that invoke other Tcl commands is something like: </p>
<dl COMPACT>
<dd>
<pre>int
<i>TheCmdOldObjProc</i>(
 ClientData clientData,
 Tcl_Interp *interp,
 int objc,
 Tcl_Obj *const objv[])
{
 int result;
 Tcl_Obj *objPtr;
 <i>... preparation ...</i>
 result = <code>Tcl_EvalObjEx</code>(interp, objPtr, 0);
 <i>... postprocessing ...</i>
 return result;
}
<code>Tcl_CreateObjCommand</code>(interp, &quot;theCommand&quot;,
 <i>TheCmdOldObjProc</i>, clientData, TheCmdDeleteProc);</pre>
</dl>
<p> To enable a command like this one for trampoline-based evaluation, it must be split into three pieces:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>A non-trampoline implementation, <i>TheCmdNewObjProc</i>, which will simply create a trampoline and invoke the trampoline-based implementation.</p>
<dt>&bull;</p>
<dd>A trampoline-enabled implementation, <i>TheCmdNRObjProc</i>. This function will perform the initialization, request that the trampoline call the postprocessing routine after command evaluation, and finally, request that the trampoline call the inner command.</p>
<dt>&bull;</p>
<dd>A postprocessing routine, <i>TheCmdPostProc</i>. This function will perform the postprocessing formerly done after the return from the inner command in <i>TheCmdObjProc</i>.</dl>
<p> The non-trampoline implementation is simple and stylized, containing a single statement: </p>
<dl COMPACT>
<dd>
<pre>int
<i>TheCmdNewObjProc</i>(
 ClientData clientData,
 Tcl_Interp *interp,
 int objc,
 Tcl_Obj *const objv[])
{
 return <code>Tcl_NRCallObjProc</code>(interp, <i>TheCmdNRObjProc</i>, 
 clientData, objc, objv);
}</pre>
</dl>
<p> The trampoline-enabled implementation requests postprocessing, and returns to the trampoline requesting command evaluation. </p>
<dl COMPACT>
<dd>
<pre>int
<i>TheCmdNRObjProc</i>
 ClientData clientData,
 Tcl_Interp *interp,
 int objc,
 Tcl_Obj *const objv[])
{
 Tcl_Obj *objPtr;
 <i>... preparation ...</i>
 <code>Tcl_NRAddCallback</code>(interp, <i>TheCmdPostProc</i>,
 data0, data1, data2, data3);
 /* <i>data0 .. data3</i> are up to four one-word items to
 * pass to the postprocessing procedure */
 return <code>Tcl_NREvalObj</code>(interp, objPtr, 0);
}</pre>
</dl>
<p> The postprocessing procedure does whatever the original command did upon return from the inner evaluation. </p>
<dl COMPACT>
<dd>
<pre>int
<i>TheCmdNRPostProc</i>(
 ClientData data[],
 Tcl_Interp *interp,
 int result)
{
 /* <i>data[0] .. data[3]</i> are the four words of data
 * passed to <code>Tcl_NRAddCallback</code> */
 <i>... postprocessing ...</i>
 return result;
}</pre>
</dl>
<p> If <i>theCommand</i> is a command that results in multiple commands or scripts being evaluated, its postprocessing routine may schedule additional postprocessing and then request another command evaluation by means of <code>Tcl_NREvalObj</code> or one of the other evaluation routines. Looping and sequencing constructs may be implemented in this way. </p>
<p> Finally, to install a trampoline-enabled command in the interpreter, <code>Tcl_NRCreateCommand</code> is used in place of <code>Tcl_CreateObjCommand</code>. It accepts two command procedures instead of one. The first is for use when no trampoline is yet on the stack, and the second is for use when there is already a trampoline in place. </p>
<dl COMPACT>
<dd>
<pre><code>Tcl_NRCreateCommand</code>(interp, &quot;theCommand&quot;,
 <i>TheCmdNewObjProc</i>, <i>TheCmdNRObjProc</i>, clientData,
 TheCmdDeleteProc);</pre>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-tcl_createcommand/">Tcl_CreateCommand</a>(3), <a href="/docs/linux/man/3-tcl_createobjcommand/">Tcl_CreateObjCommand</a>(3), <a href="/docs/linux/man/3-tcl_evalobjex/">Tcl_EvalObjEx</a>(3), <a href="/docs/linux/man/3-tcl_getcommandfromobj/">Tcl_GetCommandFromObj</a>(3), <a href="/docs/linux/man/3-tcl_exprobj/">Tcl_ExprObj</a>(3)</p>
<h2>Keywords</h2>
<p>stackless, nonrecursive, execute, command, global, value, result, script</p>
<h2>Copyright</h2>
<p>Copyright (c) 2008 by Kevin B. Kenny</p>
