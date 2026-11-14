---
title: "tcl_evalfile(3)"
name: "tcl_evalfile"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_evalfile/"
description: "Tcl_EvalObjEx, Tcl_EvalFile, Tcl_EvalObjv, Tcl_Eval, Tcl_EvalEx, Tcl_GlobalEval, Tcl_GlobalEvalObj, Tcl_VarEval, Tcl_VarEvalVA – execute Tcl scripts"
---

<p>Tcl_EvalObjEx, Tcl_EvalFile, Tcl_EvalObjv, Tcl_Eval, Tcl_EvalEx, Tcl_GlobalEval, Tcl_GlobalEvalObj, Tcl_VarEval, Tcl_VarEvalVA &#8211; execute Tcl scripts </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_EvalObjEx</code>(<i>interp, objPtr, flags</i>)
int
<code>Tcl_EvalFile</code>(<i>interp, fileName</i>)
int
<code>Tcl_EvalObjv</code>(<i>interp, objc, objv, flags</i>)
int
<code>Tcl_Eval</code>(<i>interp, script</i>)
int
<code>Tcl_EvalEx</code>(<i>interp, script, numBytes, flags</i>)
int
<code>Tcl_GlobalEval</code>(<i>interp, script</i>)
int
<code>Tcl_GlobalEvalObj</code>(<i>interp, objPtr</i>)
int
<code>Tcl_VarEval</code>(<i>interp, part, part, ... </i><code>(char *) NULL</code>)
int
<code>Tcl_VarEvalVA</code>(<i>interp, argList</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which to execute the script. The interpreter&#8217;s result is modified to hold the result or error message from the script.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in) A Tcl object containing the script to execute.</p>
<dd>int <i>flags</i> (in) ORed combination of flag bits that specify additional options. <code>TCL_EVAL_GLOBAL</code> and <code>TCL_EVAL_DIRECT</code> are currently supported.</p>
<dd>const char <i>*fileName</i> (in) Name of a file containing a Tcl script.</p>
<dd>int <i>objc</i> (in) The number of objects in the array pointed to by <i>objPtr</i>; this is also the number of words in the command.</p>
<dd>Tcl_Obj <i>**objv</i> (in) Points to an array of pointers to objects; each object holds the value of a single word in the command to execute.</p>
<dd>int <i>numBytes</i> (in) The number of bytes in <i>script</i>, not including any null terminating character. If -1, then all characters up to the first null byte are used.</p>
<dd>const char <i>*script</i> (in) Points to first byte of script to execute (null-terminated and UTF-8).</p>
<dd>char <i>*part</i> (in) String forming part of a Tcl script.</p>
<dd>va_list <i>argList</i> (in) An argument list which must have been initialized using <code>va_start</code>, and cleared using <code>va_end</code>. </p>
</dl>
<h2>Description</h2>
<p>The procedures described here are invoked to execute Tcl scripts in various forms. <code>Tcl_EvalObjEx</code> is the core procedure and is used by many of the others. It executes the commands in the script stored in <i>objPtr</i> until either an error occurs or the end of the script is reached. If this is the first time <i>objPtr</i> has been executed, its commands are compiled into bytecode instructions which are then executed. The bytecodes are saved in <i>objPtr</i> so that the compilation step can be skipped if the object is evaluated again in the future. </p>
<p> The return value from <code>Tcl_EvalObjEx</code> (and all the other procedures described here) is a Tcl completion code with one of the values <code>TCL_OK</code>, <code>TCL_ERROR</code>, <code>TCL_RETURN</code>, <code>TCL_BREAK</code>, or <code>TCL_CONTINUE</code>, or possibly some other integer value originating in an extension. In addition, a result value or error message is left in <i>interp</i>&#8216;s result; it can be retrieved using <code>Tcl_GetObjResult</code>. </p>
<p> <code>Tcl_EvalFile</code> reads the file given by <i>fileName</i> and evaluates its contents as a Tcl script. It returns the same information as <code>Tcl_EvalObjEx</code>. If the file could not be read then a Tcl error is returned to describe why the file could not be read. The eofchar for files is &#8220;\32&#8221; (^Z) for all platforms. If you require a &#8220;^Z&#8221; in code for string comparison, you can use &#8220;&#8221; or &#8220;&#8221;, which will be safely substituted by the Tcl interpreter into &#8220;^Z&#8221;. </p>
<p> <code>Tcl_EvalObjv</code> executes a single pre-parsed command instead of a script. The <i>objc</i> and <i>objv</i> arguments contain the values of the words for the Tcl command, one word in each object in <i>objv</i>. <code>Tcl_EvalObjv</code> evaluates the command and returns a completion code and result just like <code>Tcl_EvalObjEx</code>. The caller of <code>Tcl_EvalObjv</code> has to manage the reference count of the elements of <i>objv</i>, insuring that the objects are valid until <code>Tcl_EvalObjv</code> returns. </p>
<p> <code>Tcl_Eval</code> is similar to <code>Tcl_EvalObjEx</code> except that the script to be executed is supplied as a string instead of an object and no compilation occurs. The string should be a proper UTF-8 string as converted by <code>Tcl_ExternalToUtfDString</code> or <code>Tcl_ExternalToUtf</code> when it is known to possibly contain upper ASCII characters whose possible combinations might be a UTF-8 special code. The string is parsed and executed directly (using <code>Tcl_EvalObjv</code>) instead of compiling it and executing the bytecodes. In situations where it is known that the script will never be executed again, <code>Tcl_Eval</code> may be faster than <code>Tcl_EvalObjEx</code>.<br />
&nbsp;<wbr><code>Tcl_Eval</code>&nbsp;<wbr>returns a completion code and result just like&nbsp;<wbr> <code>Tcl_EvalObjEx</code>. Note: for backward compatibility with versions before Tcl 8.0, <code>Tcl_Eval</code> copies the object result in <i>interp</i> to <i>interp-&gt;result</i> (use is deprecated) where it can be accessed directly.<br />
&nbsp;<wbr>This makes&nbsp;<wbr><code>Tcl_Eval</code>&nbsp;<wbr>somewhat slower than&nbsp;<wbr><code>Tcl_EvalEx</code>, which does not do the copy. </p>
<p> <code>Tcl_EvalEx</code> is an extended version of <code>Tcl_Eval</code> that takes additional arguments <i>numBytes</i> and <i>flags</i>. For the efficiency reason given above, <code>Tcl_EvalEx</code> is generally preferred over <code>Tcl_Eval</code>. </p>
<p> <code>Tcl_GlobalEval</code> and <code>Tcl_GlobalEvalObj</code> are older procedures that are now deprecated. They are similar to <code>Tcl_EvalEx</code> and <code>Tcl_EvalObjEx</code> except that the script is evaluated in the global namespace and its variable context consists of global variables only (it ignores any Tcl procedures that are active). These functions are equivalent to using the <code>TCL_EVAL_GLOBAL</code> flag (see below). </p>
<p> <code>Tcl_VarEval</code> takes any number of string arguments of any length, concatenates them into a single string, then calls <code>Tcl_Eval</code> to execute that string as a Tcl command. It returns the result of the command and also modifies <i>interp-&gt;result</i> in the same way as <code>Tcl_Eval</code>. The last argument to <code>Tcl_VarEval</code> must be NULL to indicate the end of arguments. <code>Tcl_VarEval</code> is now deprecated. </p>
<p> <code>Tcl_VarEvalVA</code> is the same as <code>Tcl_VarEval</code> except that instead of taking a variable number of arguments it takes an argument list. Like <code>Tcl_VarEval</code>, <code>Tcl_VarEvalVA</code> is deprecated. </p>
<h2>Flag Bits</h2>
<p>Any ORed combination of the following values may be used for the <i>flags</i> argument to procedures such as <code>Tcl_EvalObjEx</code>:</p>
<dl COMPACT>
<dt><code>TCL_EVAL_DIRECT</code></p>
<dd>This flag is only used by <code>Tcl_EvalObjEx</code>; it is ignored by other procedures. If this flag bit is set, the script is not compiled to bytecodes; instead it is executed directly as is done by <code>Tcl_EvalEx</code>. The <code>TCL_EVAL_DIRECT</code> flag is useful in situations where the contents of an object are going to change immediately, so the bytecodes will not be reused in a future execution. In this case, it is faster to execute the script directly.</p>
<dt><code>TCL_EVAL_GLOBAL</code></p>
<dd>If this flag is set, the script is processed at global level. This means that it is evaluated in the global namespace and its variable context consists of global variables only (it ignores any Tcl procedures at are active). </p>
</dl>
<h2>Miscellaneous Details</h2>
<p>During the processing of a Tcl command it is legal to make nested calls to evaluate other commands (this is how procedures and some control structures are implemented). If a code other than <code>TCL_OK</code> is returned from a nested <code>Tcl_EvalObjEx</code> invocation, then the caller should normally return immediately, passing that same return code back to its caller, and so on until the top-level application is reached. A few commands, like <code>for</code>, will check for certain return codes, like <code>TCL_BREAK</code> and <code>TCL_CONTINUE</code>, and process them specially without returning. </p>
<p> <code>Tcl_EvalObjEx</code> keeps track of how many nested <code>Tcl_EvalObjEx</code> invocations are in progress for <i>interp</i>. If a code of <code>TCL_RETURN</code>, <code>TCL_BREAK</code>, or <code>TCL_CONTINUE</code> is about to be returned from the topmost <code>Tcl_EvalObjEx</code> invocation for <i>interp</i>, it converts the return code to <code>TCL_ERROR</code> and sets <i>interp</i>&#8216;s result to an error message indicating that the <code>return</code>, <code>break</code>, or <code>continue</code> command was invoked in an inappropriate place. This means that top-level applications should never see a return code from <code>Tcl_EvalObjEx</code> other then <code>TCL_OK</code> or <code>TCL_ERROR</code>. </p>
<h2>Keywords</h2>
<p>execute, file, global, object, result, script</p>
