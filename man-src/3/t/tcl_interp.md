---
title: "tcl_interp(3)"
name: "tcl_interp"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_interp/"
description: "Tcl_Interp – client-visible fields of interpreter structures"
---

<p>Tcl_Interp &#8211; client-visible fields of interpreter structures </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
typedef struct {
 char *<i>result</i>;
 Tcl_FreeProc *<i>freeProc</i>;
 int <i>errorLine</i>;
} Tcl_Interp;
typedef void Tcl_FreeProc(char *<i>blockPtr</i>);
<br>
<hr></pre>
<h2>Description</h2>
<p>The <code>Tcl_CreateInterp</code> procedure returns a pointer to a Tcl_Interp structure. This pointer is then passed into other Tcl procedures to process commands in the interpreter and perform other operations on the interpreter. Interpreter structures contain many fields that are used by Tcl, but only three that may be accessed by clients: <i>result</i>, <i>freeProc</i>, and <i>errorLine</i>. </p>
<p> <code>Note that access to all three fields, </code><i>result</i><code>, </code><i>freeProc</i><code> and </code><i>errorLine</i><code> is deprecated.</code> Use <code>Tcl_SetResult</code>, <code>Tcl_GetResult</code>, and <code>Tcl_GetReturnOptions</code> instead. </p>
<p> The <i>result</i> and <i>freeProc</i> fields are used to return results or error messages from commands. This information is returned by command procedures back to <code>Tcl_Eval</code>, and by <code>Tcl_Eval</code> back to its callers. The <i>result</i> field points to the string that represents the result or error message, and the <i>freeProc</i> field tells how to dispose of the storage for the string when it is not needed anymore. The easiest way for command procedures to manipulate these fields is to call procedures like <code>Tcl_SetResult</code> or <code>Tcl_AppendResult</code>; they will hide all the details of managing the fields. The description below is for those procedures that manipulate the fields directly. </p>
<p> Whenever a command procedure returns, it must ensure that the <i>result</i> field of its interpreter points to the string being returned by the command. The <i>result</i> field must always point to a valid string. If a command wishes to return no result then <i>interp-&gt;result</i> should point to an empty string. Normally, results are assumed to be statically allocated, which means that the contents will not change before the next time <code>Tcl_Eval</code> is called or some other command procedure is invoked. In this case, the <i>freeProc</i> field must be zero. Alternatively, a command procedure may dynamically allocate its return value (e.g. using <code>Tcl_Alloc</code>) and store a pointer to it in <i>interp-&gt;result</i>. In this case, the command procedure must also set <i>interp-&gt;freeProc</i> to the address of a procedure that can free the value, or <code>TCL_DYNAMIC</code> if the storage was allocated directly by Tcl or by a call to <code>Tcl_Alloc</code>. If <i>interp-&gt;freeProc</i> is non-zero, then Tcl will call <i>freeProc</i> to free the space pointed to by <i>interp-&gt;result</i> before it invokes the next command. If a client procedure overwrites <i>interp-&gt;result</i> when <i>interp-&gt;freeProc</i> is non-zero, then it is responsible for calling <i>freeProc</i> to free the old <i>interp-&gt;result</i> (the <code>Tcl_FreeResult</code> macro should be used for this purpose). </p>
<p> <i>FreeProc</i> should have arguments and result that match the <code>Tcl_FreeProc</code> declaration above: it receives a single argument which is a pointer to the result value to free. In most applications <code>TCL_DYNAMIC</code> is the only non-zero value ever used for <i>freeProc</i>. However, an application may store a different procedure address in <i>freeProc</i> in order to use an alternate memory allocator or in order to do other cleanup when the result memory is freed. </p>
<p> As part of processing each command, <code>Tcl_Eval</code> initializes <i>interp-&gt;result</i> and <i>interp-&gt;freeProc</i> just before calling the command procedure for the command. The <i>freeProc</i> field will be initialized to zero, and <i>interp-&gt;result</i> will point to an empty string. Commands that do not return any value can simply leave the fields alone. Furthermore, the empty string pointed to by <i>result</i> is actually part of an array of <code>TCL_RESULT_SIZE</code> characters (approximately 200). If a command wishes to return a short string, it can simply copy it to the area pointed to by <i>interp-&gt;result</i>. Or, it can use the sprintf procedure to generate a short result string at the location pointed to by <i>interp-&gt;result</i>. </p>
<p> It is a general convention in Tcl-based applications that the result of an interpreter is normally in the initialized state described in the previous paragraph. Procedures that manipulate an interpreter&#8217;s result (e.g. by returning an error) will generally assume that the result has been initialized when the procedure is called. If such a procedure is to be called after the result has been changed, then <code>Tcl_ResetResult</code> should be called first to reset the result to its initialized state. The direct use of <i>interp-&gt;result</i> is strongly deprecated (see <code>Tcl_SetResult</code>). </p>
<p> The <i>errorLine</i> field is valid only after <code>Tcl_Eval</code> returns a <code>TCL_ERROR</code> return code. In this situation the <i>errorLine</i> field identifies the line number of the command being executed when the error occurred. The line numbers are relative to the command being executed: 1 means the first line of the command passed to <code>Tcl_Eval</code>, 2 means the second line, and so on. The <i>errorLine</i> field is typically used in conjunction with <code>Tcl_AddErrorInfo</code> to report information about where an error occurred. <i>ErrorLine</i> should not normally be modified except by <code>Tcl_Eval</code>. </p>
<h2>Keywords</h2>
<p>free, initialized, interpreter, malloc, result</p>
