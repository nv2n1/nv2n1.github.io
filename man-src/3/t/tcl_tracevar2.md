---
title: "tcl_tracevar2(3)"
name: "tcl_tracevar2"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_tracevar2/"
description: "Tcl_TraceVar, Tcl_TraceVar2, Tcl_UntraceVar, Tcl_UntraceVar2, Tcl_VarTraceInfo, Tcl_VarTraceInfo2 – monitor accesses to a variable"
---

<p>Tcl_TraceVar, Tcl_TraceVar2, Tcl_UntraceVar, Tcl_UntraceVar2, Tcl_VarTraceInfo, Tcl_VarTraceInfo2 &#8211; monitor accesses to a variable </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_TraceVar(</code><i>interp, varName, flags, proc, clientData</i><code>)</code>
int
<code>Tcl_TraceVar2(</code><i>interp, name1, name2, flags, proc, clientData</i><code>)</code>
<code>Tcl_UntraceVar(</code><i>interp, varName, flags, proc, clientData</i><code>)</code>
<code>Tcl_UntraceVar2(</code><i>interp, name1, name2, flags, proc, clientData</i><code>)</code>
ClientData
<code>Tcl_VarTraceInfo(</code><i>interp, varName, flags, proc, prevClientData</i><code>)</code>
ClientData
<code>Tcl_VarTraceInfo2(</code><i>interp, name1, name2, flags, proc, prevClientData</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter containing variable.</p>
<dd>const char <i>*varName</i> (in) Name of variable. May refer to a scalar variable, to an array variable with no index, or to an array variable with a parenthesized index.</p>
<dd>int <i>flags</i> (in) OR-ed combination of the values <code>TCL_TRACE_READS</code>, <code>TCL_TRACE_WRITES</code>, <code>TCL_TRACE_UNSETS</code>, <code>TCL_TRACE_ARRAY</code>, <code>TCL_GLOBAL_ONLY</code>, <code>TCL_NAMESPACE_ONLY</code>, <code>TCL_TRACE_RESULT_DYNAMIC</code> and <code>TCL_TRACE_RESULT_OBJECT</code>. Not all flags are used by all procedures. See below for more information.</p>
<dd>Tcl_VarTraceProc <i>*proc</i> (in) Procedure to invoke whenever one of the traced operations occurs.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i>.</p>
<dd>const char <i>*name1</i> (in) Name of scalar or array variable (without array index).</p>
<dd>const char <i>*name2</i> (in) For a trace on an element of an array, gives the index of the element. For traces on scalar variables or on whole arrays, is NULL.</p>
<dd>ClientData <i>prevClientData</i> (in) If non-NULL, gives last value returned by <code>Tcl_VarTraceInfo</code> or <code>Tcl_VarTraceInfo2</code>, so this call will return information about next trace. If NULL, this call will return information about first trace.
</dl>
<h2>Description</h2>
<p><code>Tcl_TraceVar</code> allows a C procedure to monitor and control access to a Tcl variable, so that the C procedure is invoked whenever the variable is read or written or unset. If the trace is created successfully then <code>Tcl_TraceVar</code> returns <code>TCL_OK</code>. If an error occurred (e.g. <i>varName</i> specifies an element of an array, but the actual variable is not an array) then <code>TCL_ERROR</code> is returned and an error message is left in the interpreter&#8217;s result. </p>
<p> The <i>flags</i> argument to <code>Tcl_TraceVar</code> indicates when the trace procedure is to be invoked and provides information for setting up the trace. It consists of an OR-ed combination of any of the following values:</p>
<dl COMPACT>
<dt><code>TCL_GLOBAL_ONLY</code></p>
<dd>Normally, the variable will be looked up at the current level of procedure call; if this bit is set then the variable will be looked up at global level, ignoring any active procedures.</p>
<dt><code>TCL_NAMESPACE_ONLY</code></p>
<dd>Normally, the variable will be looked up at the current level of procedure call; if this bit is set then the variable will be looked up in the current namespace, ignoring any active procedures.</p>
<dt><code>TCL_TRACE_READS</code></p>
<dd>Invoke <i>proc</i> whenever an attempt is made to read the variable.</p>
<dt><code>TCL_TRACE_WRITES</code></p>
<dd>Invoke <i>proc</i> whenever an attempt is made to modify the variable.</p>
<dt><code>TCL_TRACE_UNSETS</code></p>
<dd>Invoke <i>proc</i> whenever the variable is unset. A variable may be unset either explicitly by an <code>unset</code> command, or implicitly when a procedure returns (its local variables are automatically unset) or when the interpreter is deleted (all variables are automatically unset).</p>
<dt><code>TCL_TRACE_ARRAY</code></p>
<dd>Invoke <i>proc</i> whenever the array command is invoked. This gives the trace procedure a chance to update the array before array names or array get is called. Note that this is called before an array set, but that will trigger write traces.</p>
<dt><code>TCL_TRACE_RESULT_DYNAMIC</code></p>
<dd>The result of invoking the <i>proc</i> is a dynamically allocated string that will be released by the Tcl library via a call to <code>ckfree</code>. Must not be specified at the same time as <code>TCL_TRACE_RESULT_OBJECT</code>.</p>
<dt><code>TCL_TRACE_RESULT_OBJECT</code></p>
<dd>The result of invoking the <i>proc</i> is a Tcl_Obj* (cast to a char*) with a reference count of at least one. The ownership of that reference will be transferred to the Tcl core for release (when the core has finished with it) via a call to <code>Tcl_DecrRefCount</code>. Must not be specified at the same time as <code>TCL_TRACE_RESULT_DYNAMIC</code>.</dl>
<p> Whenever one of the specified operations occurs on the variable, <i>proc</i> will be invoked. It should have arguments and result that match the type <code>Tcl_VarTraceProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef char *Tcl_VarTraceProc(
 ClientData <i>clientData</i>,
 Tcl_Interp *<i>interp</i>,
 char *<i>name1</i>,
 char *<i>name2</i>,
 int <i>flags</i>);</pre>
</dl>
<p> The <i>clientData</i> and <i>interp</i> parameters will have the same values as those passed to <code>Tcl_TraceVar</code> when the trace was created. <i>ClientData</i> typically points to an application-specific data structure that describes what to do when <i>proc</i> is invoked. <i>Name1</i> and <i>name2</i> give the name of the traced variable in the normal two-part form (see the description of <code>Tcl_TraceVar2</code> below for details). <i>Flags</i> is an OR-ed combination of bits providing several pieces of information. One of the bits <code>TCL_TRACE_READS</code>, <code>TCL_TRACE_WRITES</code>, <code>TCL_TRACE_ARRAY</code>, or <code>TCL_TRACE_UNSETS</code> will be set in <i>flags</i> to indicate which operation is being performed on the variable. The bit <code>TCL_GLOBAL_ONLY</code> will be set whenever the variable being accessed is a global one not accessible from the current level of procedure call: the trace procedure will need to pass this flag back to variable-related procedures like <code>Tcl_GetVar</code> if it attempts to access the variable. The bit <code>TCL_NAMESPACE_ONLY</code> will be set whenever the variable being accessed is a namespace one not accessible from the current level of procedure call: the trace procedure will need to pass this flag back to variable-related procedures like <code>Tcl_GetVar</code> if it attempts to access the variable. The bit <code>TCL_TRACE_DESTROYED</code> will be set in <i>flags</i> if the trace is about to be destroyed; this information may be useful to <i>proc</i> so that it can clean up its own internal data structures (see the section <code>TCL_TRACE_DESTROYED</code> below for more details). Lastly, the bit <code>TCL_INTERP_DESTROYED</code> will be set if the entire interpreter is being destroyed. When this bit is set, <i>proc</i> must be especially careful in the things it does (see the section <code>TCL_INTERP_DESTROYED</code> below). The trace procedure&#8217;s return value should normally be NULL; see <code>ERROR RETURNS</code> below for information on other possibilities. </p>
<p> <code>Tcl_UntraceVar</code> may be used to remove a trace. If the variable specified by <i>interp</i>, <i>varName</i>, and <i>flags</i> has a trace set with <i>flags</i>, <i>proc</i>, and <i>clientData</i>, then the corresponding trace is removed. If no such trace exists, then the call to <code>Tcl_UntraceVar</code> has no effect. The same bits are valid for <i>flags</i> as for calls to <code>Tcl_TraceVar</code>. </p>
<p> <code>Tcl_VarTraceInfo</code> may be used to retrieve information about traces set on a given variable. The return value from <code>Tcl_VarTraceInfo</code> is the <i>clientData</i> associated with a particular trace. The trace must be on the variable specified by the <i>interp</i>, <i>varName</i>, and <i>flags</i> arguments (only the <code>TCL_GLOBAL_ONLY</code> and <code>TCL_NAMESPACE_ONLY</code> bits from <i>flags</i> is used; other bits are ignored) and its trace procedure must the same as the <i>proc</i> argument. If the <i>prevClientData</i> argument is NULL then the return value corresponds to the first (most recently created) matching trace, or NULL if there are no matching traces. If the <i>prevClientData</i> argument is not NULL, then it should be the return value from a previous call to <code>Tcl_VarTraceInfo</code>. In this case, the new return value will correspond to the next matching trace after the one whose <i>clientData</i> matches <i>prevClientData</i>, or NULL if no trace matches <i>prevClientData</i> or if there are no more matching traces after it. This mechanism makes it possible to step through all of the traces for a given variable that have the same <i>proc</i>.</p>
<h2>Two-Part Names</h2>
<p>The procedures <code>Tcl_TraceVar2</code>, <code>Tcl_UntraceVar2</code>, and <code>Tcl_VarTraceInfo2</code> are identical to <code>Tcl_TraceVar</code>, <code>Tcl_UntraceVar</code>, and <code>Tcl_VarTraceInfo</code>, respectively, except that the name of the variable consists of two parts. <i>Name1</i> gives the name of a scalar variable or array, and <i>name2</i> gives the name of an element within an array. When <i>name2</i> is NULL, <i>name1</i> may contain both an array and an element name: if the name contains an open parenthesis and ends with a close parenthesis, then the value between the parentheses is treated as an element name (which can have any string value) and the characters before the first open parenthesis are treated as the name of an array variable. If <i>name2</i> is NULL and <i>name1</i> does not refer to an array element it means that either the variable is a scalar or the trace is to be set on the entire array rather than an individual element (see WHOLE-ARRAY TRACES below for more information).</p>
<h2>Accessing Variables During Traces</h2>
<p>During read, write, and array traces, the trace procedure can read, write, or unset the traced variable using <code>Tcl_GetVar2</code>, <code>Tcl_SetVar2</code>, and other procedures. While <i>proc</i> is executing, traces are temporarily disabled for the variable, so that calls to <code>Tcl_GetVar2</code> and <code>Tcl_SetVar2</code> will not cause <i>proc</i> or other trace procedures to be invoked again. Disabling only occurs for the variable whose trace procedure is active; accesses to other variables will still be traced. However, if a variable is unset during a read or write trace then unset traces will be invoked. </p>
<p> During unset traces the variable has already been completely expunged. It is possible for the trace procedure to read or write the variable, but this will be a new version of the variable. Traces are not disabled during unset traces as they are for read and write traces, but existing traces have been removed from the variable before any trace procedures are invoked. If new traces are set by unset trace procedures, these traces will be invoked on accesses to the variable by the trace procedures.</p>
<h2>Callback Timing</h2>
<p>When read tracing has been specified for a variable, the trace procedure will be invoked whenever the variable&#8217;s value is read. This includes <code>set</code> Tcl commands, <code>$</code>-notation in Tcl commands, and invocations of the <code>Tcl_GetVar</code> and <code>Tcl_GetVar2</code> procedures. <i>Proc</i> is invoked just before the variable&#8217;s value is returned. It may modify the value of the variable to affect what is returned by the traced access. If it unsets the variable then the access will return an error just as if the variable never existed. </p>
<p> When write tracing has been specified for a variable, the trace procedure will be invoked whenever the variable&#8217;s value is modified. This includes <code>set</code> commands, commands that modify variables as side effects (such as <code>catch</code> and <code>scan</code>), and calls to the <code>Tcl_SetVar</code> and <code>Tcl_SetVar2</code> procedures). <i>Proc</i> will be invoked after the variable&#8217;s value has been modified, but before the new value of the variable has been returned. It may modify the value of the variable to override the change and to determine the value actually returned by the traced access. If it deletes the variable then the traced access will return an empty string. </p>
<p> When array tracing has been specified, the trace procedure will be invoked at the beginning of the array command implementation, before any of the operations like get, set, or names have been invoked. The trace procedure can modify the array elements with <code>Tcl_SetVar</code> and <code>Tcl_SetVar2</code>. </p>
<p> When unset tracing has been specified, the trace procedure will be invoked whenever the variable is destroyed. The traces will be called after the variable has been completely unset.</p>
<h2>Whole-Array Traces</h2>
<p>If a call to <code>Tcl_TraceVar</code> or <code>Tcl_TraceVar2</code> specifies the name of an array variable without an index into the array, then the trace will be set on the array as a whole. This means that <i>proc</i> will be invoked whenever any element of the array is accessed in the ways specified by <i>flags</i>. When an array is unset, a whole-array trace will be invoked just once, with <i>name1</i> equal to the name of the array and <i>name2</i> NULL; it will not be invoked once for each element.</p>
<h2>Multiple Traces</h2>
<p>It is possible for multiple traces to exist on the same variable. When this happens, all of the trace procedures will be invoked on each access, in order from most-recently-created to least-recently-created. When there exist whole-array traces for an array as well as traces on individual elements, the whole-array traces are invoked before the individual-element traces. If a read or write trace unsets the variable then all of the unset traces will be invoked but the remainder of the read and write traces will be skipped.</p>
<h2>Error Returns</h2>
<p>Under normal conditions trace procedures should return NULL, indicating successful completion. If <i>proc</i> returns a non-NULL value it signifies that an error occurred. The return value must be a pointer to a static character string containing an error message, unless (<i>exactly</i> one of) the <code>TCL_TRACE_RESULT_DYNAMIC</code> and <code>TCL_TRACE_RESULT_OBJECT</code> flags is set, which specify that the result is either a dynamic string (to be released with <code>ckfree</code>) or a Tcl_Obj* (cast to char* and to be released with <code>Tcl_DecrRefCount</code>) containing the error message. If a trace procedure returns an error, no further traces are invoked for the access and the traced access aborts with the given message. Trace procedures can use this facility to make variables read-only, for example (but note that the value of the variable will already have been modified before the trace procedure is called, so the trace procedure will have to restore the correct value). </p>
<p> The return value from <i>proc</i> is only used during read and write tracing. During unset traces, the return value is ignored and all relevant trace procedures will always be invoked.</p>
<h2>Restrictions</h2>
<p>A trace procedure can be called at any time, even when there is a partially formed result in the interpreter&#8217;s result area. If the trace procedure does anything that could damage this result (such as calling <code>Tcl_Eval</code>) then it must save the original values of the interpreter&#8217;s <code>result</code> and <code>freeProc</code> fields and restore them before it returns.</p>
<h2>Undefined Variables</h2>
<p>It is legal to set a trace on an undefined variable. The variable will still appear to be undefined until the first time its value is set. If an undefined variable is traced and then unset, the unset will fail with an error (&#8220;no such variable&#8221;), but the trace procedure will still be invoked.</p>
<h2>Tcl_Trace_Destroyed Flag</h2>
<p>In an unset callback to <i>proc</i>, the <code>TCL_TRACE_DESTROYED</code> bit is set in <i>flags</i> if the trace is being removed as part of the deletion. Traces on a variable are always removed whenever the variable is deleted; the only time <code>TCL_TRACE_DESTROYED</code> is not set is for a whole-array trace invoked when only a single element of an array is unset.</p>
<h2>Tcl_Interp_Destroyed</h2>
<p>When an interpreter is destroyed, unset traces are called for all of its variables. The <code>TCL_INTERP_DESTROYED</code> bit will be set in the <i>flags</i> argument passed to the trace procedures. Trace procedures must be extremely careful in what they do if the <code>TCL_INTERP_DESTROYED</code> bit is set. It is not safe for the procedures to invoke any Tcl procedures on the interpreter, since its state is partially deleted. All that trace procedures should do under these circumstances is to clean up and free their own internal data structures.</p>
<h2>Bugs</h2>
<p>Tcl does not do any error checking to prevent trace procedures from misusing the interpreter during traces with <code>TCL_INTERP_DESTROYED</code> set. </p>
<p> Array traces are not yet integrated with the Tcl <code>info exists</code> command, nor is there Tcl-level access to array traces.</p>
<h2>Keywords</h2>
<p>clientData, trace, variable</p>
