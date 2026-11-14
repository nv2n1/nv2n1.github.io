---
title: "tcl_createalias(3)"
name: "tcl_createalias"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_createalias/"
description: "Tcl_IsSafe, Tcl_MakeSafe, Tcl_CreateSlave, Tcl_GetSlave, Tcl_GetMaster, Tcl_GetInterpPath, Tcl_CreateAlias, Tcl_CreateAliasObj, Tcl_GetAlias, Tcl_GetAliasObj, Tcl_ExposeCommand, Tcl_HideCommand – m..."
---

<p>Tcl_IsSafe, Tcl_MakeSafe, Tcl_CreateSlave, Tcl_GetSlave, Tcl_GetMaster, Tcl_GetInterpPath, Tcl_CreateAlias, Tcl_CreateAliasObj, Tcl_GetAlias, Tcl_GetAliasObj, Tcl_ExposeCommand, Tcl_HideCommand &#8211; manage multiple Tcl interpreters, aliases and hidden commands </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_IsSafe</code>(<i>interp</i>)
int
<code>Tcl_MakeSafe</code>(<i>interp</i>)
Tcl_Interp *
<code>Tcl_CreateSlave</code>(<i>interp, slaveName, isSafe</i>)
Tcl_Interp *
<code>Tcl_GetSlave</code>(<i>interp, slaveName</i>)
Tcl_Interp *
<code>Tcl_GetMaster</code>(<i>interp</i>)
int
<code>Tcl_GetInterpPath</code>(<i>askingInterp, slaveInterp</i>)
int
<code>Tcl_CreateAlias</code>(<i>slaveInterp, slaveCmd, targetInterp, targetCmd,
 argc, argv</i>)
int
<code>Tcl_CreateAliasObj</code>(<i>slaveInterp, slaveCmd, targetInterp, targetCmd,
 objc, objv</i>)
int
<code>Tcl_GetAlias</code>(<i>interp, slaveCmd, targetInterpPtr, targetCmdPtr,
 argcPtr, argvPtr</i>)
int
<code>Tcl_GetAliasObj</code>(<i>interp, slaveCmd, targetInterpPtr, targetCmdPtr,
 objcPtr, objvPtr</i>)
int
<code>Tcl_ExposeCommand</code>(<i>interp, hiddenCmdName, cmdName</i>)
int
<code>Tcl_HideCommand</code>(<i>interp, cmdName, hiddenCmdName</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which to execute the specified command.</p>
<dd>const char <i>*slaveName</i> (in) Name of slave interpreter to create or manipulate.</p>
<dd>int <i>isSafe</i> (in) If non-zero, a &#8220;safe&#8221; slave that is suitable for running untrusted code is created, otherwise a trusted slave is created.</p>
<dd>Tcl_Interp <i>*slaveInterp</i> (in) Interpreter to use for creating the source command for an alias (see below).</p>
<dd>const char <i>*slaveCmd</i> (in) Name of source command for alias.</p>
<dd>Tcl_Interp <i>*targetInterp</i> (in) Interpreter that contains the target command for an alias.</p>
<dd>const char <i>*targetCmd</i> (in) Name of target command for alias in <i>targetInterp</i>.</p>
<dd>int <i>argc</i> (in) Count of additional arguments to pass to the alias command.</p>
<dd>const char *const <i>*argv</i> (in) Vector of strings, the additional arguments to pass to the alias command. This storage is owned by the caller.</p>
<dd>int <i>objc</i> (in) Count of additional object arguments to pass to the alias object command.</p>
<dd>Tcl_Obj <i>**objv</i> (in) Vector of Tcl_Obj structures, the additional object arguments to pass to the alias object command. This storage is owned by the caller.</p>
<dd>Tcl_Interp <i>**targetInterpPtr</i> (in) Pointer to location to store the address of the interpreter where a target command is defined for an alias.</p>
<dd>const char <i>**targetCmdPtr</i> (out) Pointer to location to store the address of the name of the target command for an alias.</p>
<dd>int <i>*argcPtr</i> (out) Pointer to location to store count of additional arguments to be passed to the alias. The location is in storage owned by the caller.</p>
<dd>const char <i>***argvPtr</i> (out) Pointer to location to store a vector of strings, the additional arguments to pass to an alias. The location is in storage owned by the caller, the vector of strings is owned by the called function.</p>
<dd>int <i>*objcPtr</i> (out) Pointer to location to store count of additional object arguments to be passed to the alias. The location is in storage owned by the caller.</p>
<dd>Tcl_Obj <i>***objvPtr</i> (out) Pointer to location to store a vector of Tcl_Obj structures, the additional arguments to pass to an object alias command. The location is in storage owned by the caller, the vector of Tcl_Obj structures is owned by the called function.</p>
<dd>const char <i>*cmdName</i> (in) Name of an exposed command to hide or create.</p>
<dd>const char <i>*hiddenCmdName</i> (in) Name under which a hidden command is stored and with which it can be exposed or invoked. </p>
</dl>
<h2>Description</h2>
<p>These procedures are intended for access to the multiple interpreter facility from inside C programs. They enable managing multiple interpreters in a hierarchical relationship, and the management of aliases, commands that when invoked in one interpreter execute a command in another interpreter. The return value for those procedures that return an <code>int</code> is either <code>TCL_OK</code> or <code>TCL_ERROR</code>. If <code>TCL_ERROR</code> is returned then the <code>result</code> field of the interpreter contains an error message. </p>
<p> <code>Tcl_CreateSlave</code> creates a new interpreter as a slave of <i>interp</i>. It also creates a slave command named <i>slaveName</i> in <i>interp</i> which allows <i>interp</i> to manipulate the new slave. If <i>isSafe</i> is zero, the command creates a trusted slave in which Tcl code has access to all the Tcl commands. If it is <code>1</code>, the command creates a &#8220;safe&#8221; slave in which Tcl code has access only to set of Tcl commands defined as &#8220;Safe Tcl&#8221;; see the manual entry for the Tcl <code>interp</code> command for details. If the creation of the new slave interpreter failed, <code>NULL</code> is returned. </p>
<p> <code>Tcl_IsSafe</code> returns <code>1</code> if <i>interp</i> is &#8220;safe&#8221; (was created with the <code>TCL_SAFE_INTERPRETER</code> flag specified), <code>0</code> otherwise. </p>
<p> <code>Tcl_MakeSafe</code> marks <i>interp</i> as &#8220;safe&#8221;, so that future calls to <code>Tcl_IsSafe</code> will return 1. It also removes all known potentially-unsafe core functionality (both commands and variables) from <i>interp</i>. However, it cannot know what parts of an extension or application are safe and does not make any attempt to remove those parts, so safety is not guaranteed after calling <code>Tcl_MakeSafe</code>. Callers will want to take care with their use of <code>Tcl_MakeSafe</code> to avoid false claims of safety. For many situations, <code>Tcl_CreateSlave</code> may be a better choice, since it creates interpreters in a known-safe state. </p>
<p> <code>Tcl_GetSlave</code> returns a pointer to a slave interpreter of <i>interp</i>. The slave interpreter is identified by <i>slaveName</i>. If no such slave interpreter exists, <code>NULL</code> is returned. </p>
<p> <code>Tcl_GetMaster</code> returns a pointer to the master interpreter of <i>interp</i>. If <i>interp</i> has no master (it is a top-level interpreter) then <code>NULL</code> is returned. </p>
<p> <code>Tcl_GetInterpPath</code> sets the <i>result</i> field in <i>askingInterp</i> to the relative path between <i>askingInterp</i> and <i>slaveInterp</i>; <i>slaveInterp</i> must be a slave of <i>askingInterp</i>. If the computation of the relative path succeeds, <code>TCL_OK</code> is returned, else <code>TCL_ERROR</code> is returned and the <i>result</i> field in <i>askingInterp</i> contains the error message. </p>
<p> <code>Tcl_CreateAlias</code> creates an object command named <i>slaveCmd</i> in <i>slaveInterp</i> that when invoked, will cause the command <i>targetCmd</i> to be invoked in <i>targetInterp</i>. The arguments specified by the strings contained in <i>argv</i> are always prepended to any arguments supplied in the invocation of <i>slaveCmd</i> and passed to <i>targetCmd</i>. This operation returns <code>TCL_OK</code> if it succeeds, or <code>TCL_ERROR</code> if it fails; in that case, an error message is left in the object result of <i>slaveInterp</i>. Note that there are no restrictions on the ancestry relationship (as created by <code>Tcl_CreateSlave</code>) between <i>slaveInterp</i> and <i>targetInterp</i>. Any two interpreters can be used, without any restrictions on how they are related. </p>
<p> <code>Tcl_CreateAliasObj</code> is similar to <code>Tcl_CreateAlias</code> except that it takes a vector of objects to pass as additional arguments instead of a vector of strings. </p>
<p> <code>Tcl_GetAlias</code> returns information about an alias <i>aliasName</i> in <i>interp</i>. Any of the result fields can be <code>NULL</code>, in which case the corresponding datum is not returned. If a result field is non-<code>NULL</code>, the address indicated is set to the corresponding datum. For example, if <i>targetNamePtr</i> is non-<code>NULL</code> it is set to a pointer to the string containing the name of the target command. </p>
<p> <code>Tcl_GetAliasObj</code> is similar to <code>Tcl_GetAlias</code> except that it returns a pointer to a vector of Tcl_Obj structures instead of a vector of strings. </p>
<p> <code>Tcl_ExposeCommand</code> moves the command named <i>hiddenCmdName</i> from the set of hidden commands to the set of exposed commands, putting it under the name <i>cmdName</i>. <i>HiddenCmdName</i> must be the name of an existing hidden command, or the operation will return <code>TCL_ERROR</code> and leave an error message in the <i>result</i> field in <i>interp</i>. If an exposed command named <i>cmdName</i> already exists, the operation returns <code>TCL_ERROR</code> and leaves an error message in the object result of <i>interp</i>. If the operation succeeds, it returns <code>TCL_OK</code>. After executing this command, attempts to use <i>cmdName</i> in a call to <code>Tcl_Eval</code> or with the Tcl <code>eval</code> command will again succeed. </p>
<p> <code>Tcl_HideCommand</code> moves the command named <i>cmdName</i> from the set of exposed commands to the set of hidden commands, under the name <i>hiddenCmdName</i>. <i>CmdName</i> must be the name of an existing exposed command, or the operation will return <code>TCL_ERROR</code> and leave an error message in the object result of <i>interp</i>. Currently both <i>cmdName</i> and <i>hiddenCmdName</i> must not contain namespace qualifiers, or the operation will return <code>TCL_ERROR</code> and leave an error message in the object result of <i>interp</i>. The <i>CmdName</i> will be looked up in the global namespace, and not relative to the current namespace, even if the current namespace is not the global one. If a hidden command whose name is <i>hiddenCmdName</i> already exists, the operation also returns <code>TCL_ERROR</code> and the <i>result</i> field in <i>interp</i> contains an error message. If the operation succeeds, it returns <code>TCL_OK</code>. After executing this command, attempts to use <i>cmdName</i> in a call to <code>Tcl_Eval</code> or with the Tcl <code>eval</code> command will fail. </p>
<p> For a description of the Tcl interface to multiple interpreters, see <i><a href="/docs/linux/man/n-interp/">interp</a>(n)</i>.</p>
<h2>See Also</h2>
<p>interp </p>
<h2>Keywords</h2>
<p>alias, command, exposed commands, hidden commands, interpreter, invoke, master, slave</p>
