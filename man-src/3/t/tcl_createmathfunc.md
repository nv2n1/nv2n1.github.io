---
title: "tcl_createmathfunc(3)"
name: "tcl_createmathfunc"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_createmathfunc/"
description: "Tcl_CreateMathFunc, Tcl_GetMathFuncInfo, Tcl_ListMathFuncs – Define, query and enumerate math functions for expressions"
---

<p>Tcl_CreateMathFunc, Tcl_GetMathFuncInfo, Tcl_ListMathFuncs &#8211; Define, query and enumerate math functions for expressions </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
void
<code>Tcl_CreateMathFunc</code>(<i>interp, name, numArgs, argTypes, proc, clientData</i>)
int
<code>Tcl_GetMathFuncInfo</code>(<i>interp, name, numArgsPtr, argTypesPtr, procPtr,
 clientDataPtr</i>)
Tcl_Obj *
<code>Tcl_ListMathFuncs</code>(<i>interp, pattern</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which new function will be defined.</p>
<dd>const char <i>*name</i> (in) Name for new function.</p>
<dd>int <i>numArgs</i> (in) Number of arguments to new function; also gives size of <i>argTypes</i> array.</p>
<dd>Tcl_ValueType <i>*argTypes</i> (in) Points to an array giving the permissible types for each argument to function.</p>
<dd>Tcl_MathProc <i>*proc</i> (in) Procedure that implements the function.</p>
<dd>ClientData <i>clientData</i> (in) Arbitrary one-word value to pass to <i>proc</i> when it is invoked.</p>
<dd>int <i>*numArgsPtr</i> (out) Points to a variable that will be set to contain the number of arguments to the function.</p>
<dd>Tcl_ValueType <i>**argTypesPtr</i> (out) Points to a variable that will be set to contain a pointer to an array giving the permissible types for each argument to the function which will need to be freed up using <i>Tcl_Free</i>.</p>
<dd>Tcl_MathProc <i>**procPtr</i> (out) Points to a variable that will be set to contain a pointer to the implementation code for the function (or NULL if the function is implemented directly in bytecode).</p>
<dd>ClientData <i>*clientDataPtr</i> (out) Points to a variable that will be set to contain the clientData argument passed to <i>Tcl_CreateMathFunc</i> when the function was created if the function is not implemented directly in bytecode.</p>
<dd>const char <i>*pattern</i> (in) Pattern to match against function names so as to filter them (by passing to <i>Tcl_StringMatch</i>), or NULL to not apply any filter. </p>
</dl>
<h2>Description</h2>
<p>Tcl allows a number of mathematical functions to be used in expressions, such as <code>sin</code>, <code>cos</code>, and <code>hypot</code>. These functions are represented by commands in the namespace, <code>tcl::mathfunc</code>. The <code>Tcl_CreateMathFunc</code> function is an obsolete way for applications to add additional functions to those already provided by Tcl or to replace existing functions. It should not be used by new applications, which should create math functions using <code>Tcl_CreateObjCommand</code> to create a command in the <code>tcl::mathfunc</code> namespace. </p>
<p> In the <code>Tcl_CreateMathFunc</code> interface, <i>Name</i> is the name of the function as it will appear in expressions. If <i>name</i> does not already exist in the <code>::tcl::mathfunc</code> namespace, then a new command is created in that namespace. If <i>name</i> does exist, then the existing function is replaced. <i>NumArgs</i> and <i>argTypes</i> describe the arguments to the function. Each entry in the <i>argTypes</i> array must be one of <code>TCL_INT</code>, <code>TCL_DOUBLE</code>, <code>TCL_WIDE_INT</code>, or <code>TCL_EITHER</code> to indicate whether the corresponding argument must be an integer, a double-precision floating value, a wide (64-bit) integer, or any, respectively. </p>
<p> Whenever the function is invoked in an expression Tcl will invoke <i>proc</i>. <i>Proc</i> should have arguments and result that match the type <code>Tcl_MathProc</code>:</p>
<dl COMPACT>
<dd>
<pre>typedef int Tcl_MathProc(
 ClientData <i>clientData</i>,
 Tcl_Interp *<i>interp</i>,
 Tcl_Value *<i>args</i>,
 Tcl_Value *<i>resultPtr</i>);</pre>
</dl>
<p> When <i>proc</i> is invoked the <i>clientData</i> and <i>interp</i> arguments will be the same as those passed to <code>Tcl_CreateMathFunc</code>. <i>Args</i> will point to an array of <i>numArgs</i> Tcl_Value structures, which describe the actual arguments to the function:</p>
<dl COMPACT>
<dd>
<pre>typedef struct Tcl_Value {
 Tcl_ValueType <i>type</i>;
 long <i>intValue</i>;
 double <i>doubleValue</i>;
 Tcl_WideInt <i>wideValue</i>;
} Tcl_Value;</pre>
</dl>
<p> The <i>type</i> field indicates the type of the argument and is one of <code>TCL_INT</code>, <code>TCL_DOUBLE</code> or <code>TCL_WIDE_INT</code>. It will match the <i>argTypes</i> value specified for the function unless the <i>argTypes</i> value was <code>TCL_EITHER</code>. Tcl converts the argument supplied in the expression to the type requested in <i>argTypes</i>, if that is necessary. Depending on the value of the <i>type</i> field, the <i>intValue</i>, <i>doubleValue</i> or <i>wideValue</i> field will contain the actual value of the argument. </p>
<p> <i>Proc</i> should compute its result and store it either as an integer in <i>resultPtr-&gt;intValue</i> or as a floating value in <i>resultPtr-&gt;doubleValue</i>. It should set also <i>resultPtr-&gt;type</i> to one of <code>TCL_INT</code>, <code>TCL_DOUBLE</code> or <code>TCL_WIDE_INT</code> to indicate which value was set. Under normal circumstances <i>proc</i> should return <code>TCL_OK</code>. If an error occurs while executing the function, <i>proc</i> should return <code>TCL_ERROR</code> and leave an error message in the interpreter&#8217;s result. </p>
<p> <code>Tcl_GetMathFuncInfo</code> retrieves the values associated with function <i>name</i> that were passed to a preceding <code>Tcl_CreateMathFunc</code> call. Normally, the return code is <code>TCL_OK</code> but if the named function does not exist, <code>TCL_ERROR</code> is returned and an error message is placed in the interpreter&#8217;s result. </p>
<p> If an error did not occur, the array reference placed in the variable pointed to by <i>argTypesPtr</i> is newly allocated, and should be released by passing it to <code>Tcl_Free</code>. Some functions (the standard set implemented in the core, and those defined by placing commands in the <code>tcl::mathfunc</code> namespace) do not have argument type information; attempting to retrieve values for them causes a NULL to be stored in the variable pointed to by <i>procPtr</i> and the variable pointed to by <i>clientDataPtr</i> will not be modified. The variable pointed to by <i>numArgsPointer</i> will contain -1, and no argument types will be stored in the variable pointed to by <i>argTypesPointer</i>. </p>
<p> <code>Tcl_ListMathFuncs</code> returns a Tcl object containing a list of all the math functions defined in the interpreter whose name matches <i>pattern</i>. The returned object has a reference count of zero. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/n-expr/">expr</a>(n), <a href="/docs/linux/man/n-info/">info</a>(n), <a href="/docs/linux/man/3-tcl_createobjcommand/">Tcl_CreateObjCommand</a>(3), <a href="/docs/linux/man/3-tcl_free/">Tcl_Free</a>(3), <a href="/docs/linux/man/3-tcl_newlistobj/">Tcl_NewListObj</a>(3) </p>
<h2>Keywords</h2>
<p>expression, mathematical function</p>
