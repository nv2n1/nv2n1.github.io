---
title: "tcl_unsetvar(3)"
name: "tcl_unsetvar"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_unsetvar/"
description: "Tcl_SetVar2Ex, Tcl_SetVar, Tcl_SetVar2, Tcl_ObjSetVar2, Tcl_GetVar2Ex, Tcl_GetVar, Tcl_GetVar2, Tcl_ObjGetVar2, Tcl_UnsetVar, Tcl_UnsetVar2 – manipulate Tcl variables"
---

<p>Tcl_SetVar2Ex, Tcl_SetVar, Tcl_SetVar2, Tcl_ObjSetVar2, Tcl_GetVar2Ex, Tcl_GetVar, Tcl_GetVar2, Tcl_ObjGetVar2, Tcl_UnsetVar, Tcl_UnsetVar2 &#8211; manipulate Tcl variables </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Obj *
<code>Tcl_SetVar2Ex</code>(<i>interp, name1, name2, newValuePtr, flags</i>)
const char *
<code>Tcl_SetVar</code>(<i>interp, varName, newValue, flags</i>)
const char *
<code>Tcl_SetVar2</code>(<i>interp, name1, name2, newValue, flags</i>)
Tcl_Obj *
<code>Tcl_ObjSetVar2</code>(<i>interp, part1Ptr, part2Ptr, newValuePtr, flags</i>)
Tcl_Obj *
<code>Tcl_GetVar2Ex</code>(<i>interp, name1, name2, flags</i>)
const char *
<code>Tcl_GetVar</code>(<i>interp, varName, flags</i>)
const char *
<code>Tcl_GetVar2</code>(<i>interp, name1, name2, flags</i>)
Tcl_Obj *
<code>Tcl_ObjGetVar2</code>(<i>interp, part1Ptr, part2Ptr, flags</i>)
int
<code>Tcl_UnsetVar</code>(<i>interp, varName, flags</i>)
int
<code>Tcl_UnsetVar2</code>(<i>interp, name1, name2, flags</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter containing variable.</p>
<dd>const char <i>*name1</i> (in) Contains the name of an array variable (if <i>name2</i> is non-NULL) or (if <i>name2</i> is NULL) either the name of a scalar variable or a complete name including both variable name and index. May include <code>::</code> namespace qualifiers to specify a variable in a particular namespace.</p>
<dd>const char <i>*name2</i> (in) If non-NULL, gives name of element within array; in this case <i>name1</i> must refer to an array variable.</p>
<dd>Tcl_Obj <i>*newValuePtr</i> (in) Points to a Tcl object containing the new value for the variable.</p>
<dd>int <i>flags</i> (in) OR-ed combination of bits providing additional information. See below for valid values.</p>
<dd>const char <i>*varName</i> (in) Name of variable. May include <code>::</code> namespace qualifiers to specify a variable in a particular namespace. May refer to a scalar variable or an element of an array.</p>
<dd>const char <i>*newValue</i> (in) New value for variable, specified as a null-terminated string. A copy of this value is stored in the variable.</p>
<dd>Tcl_Obj <i>*part1Ptr</i> (in) Points to a Tcl object containing the variable&#8217;s name. The name may include a series of <code>::</code> namespace qualifiers to specify a variable in a particular namespace. May refer to a scalar variable or an element of an array variable.</p>
<dd>Tcl_Obj <i>*part2Ptr</i> (in) If non-NULL, points to an object containing the name of an element within an array and <i>part1Ptr</i> must refer to an array variable. </p>
</dl>
<h2>Description</h2>
<p>These procedures are used to create, modify, read, and delete Tcl variables from C code. </p>
<p> <code>Tcl_SetVar2Ex</code>, <code>Tcl_SetVar</code>, <code>Tcl_SetVar2</code>, and <code>Tcl_ObjSetVar2</code> will create a new variable or modify an existing one. These procedures set the given variable to the value given by <i>newValuePtr</i> or <i>newValue</i> and return a pointer to the variable&#8217;s new value, which is stored in Tcl&#8217;s variable structure. <code>Tcl_SetVar2Ex</code> and <code>Tcl_ObjSetVar2</code> take the new value as a Tcl_Obj and return a pointer to a Tcl_Obj. <code>Tcl_SetVar</code> and <code>Tcl_SetVar2</code> take the new value as a string and return a string; they are usually less efficient than <code>Tcl_ObjSetVar2</code>. Note that the return value may be different than the <i>newValuePtr</i> or <i>newValue</i> argument, due to modifications made by write traces. If an error occurs in setting the variable (e.g. an array variable is referenced without giving an index into the array) NULL is returned and an error message is left in <i>interp</i>&#8216;s result if the <code>TCL_LEAVE_ERR_MSG</code> <i>flag</i> bit is set. </p>
<p> <code>Tcl_GetVar2Ex</code>, <code>Tcl_GetVar</code>, <code>Tcl_GetVar2</code>, and <code>Tcl_ObjGetVar2</code> return the current value of a variable. The arguments to these procedures are treated in the same way as the arguments to the procedures described above. Under normal circumstances, the return value is a pointer to the variable&#8217;s value. For <code>Tcl_GetVar2Ex</code> and <code>Tcl_ObjGetVar2</code> the value is returned as a pointer to a Tcl_Obj. For <code>Tcl_GetVar</code> and <code>Tcl_GetVar2</code> the value is returned as a string; this is usually less efficient, so <code>Tcl_GetVar2Ex</code> or <code>Tcl_ObjGetVar2</code> are preferred. If an error occurs while reading the variable (e.g. the variable does not exist or an array element is specified for a scalar variable), then NULL is returned and an error message is left in <i>interp</i>&#8216;s result if the <code>TCL_LEAVE_ERR_MSG</code> <i>flag</i> bit is set. </p>
<p> <code>Tcl_UnsetVar</code> and <code>Tcl_UnsetVar2</code> may be used to remove a variable, so that future attempts to read the variable will return an error. The arguments to these procedures are treated in the same way as the arguments to the procedures above. If the variable is successfully removed then <code>TCL_OK</code> is returned. If the variable cannot be removed because it does not exist then <code>TCL_ERROR</code> is returned and an error message is left in <i>interp</i>&#8216;s result if the <code>TCL_LEAVE_ERR_MSG</code> <i>flag</i> bit is set. If an array element is specified, the given element is removed but the array remains. If an array name is specified without an index, then the entire array is removed. </p>
<p> The name of a variable may be specified to these procedures in four ways:</p>
<dl COMPACT>
<dt>[1]</p>
<dd>If <code>Tcl_SetVar</code>, <code>Tcl_GetVar</code>, or <code>Tcl_UnsetVar</code> is invoked, the variable name is given as a single string, <i>varName</i>. If <i>varName</i> contains an open parenthesis and ends with a close parenthesis, then the value between the parentheses is treated as an index (which can have any string value) and the characters before the first open parenthesis are treated as the name of an array variable. If <i>varName</i> does not have parentheses as described above, then the entire string is treated as the name of a scalar variable.</p>
<dt>[2]</p>
<dd>If the <i>name1</i> and <i>name2</i> arguments are provided and <i>name2</i> is non-NULL, then an array element is specified and the array name and index have already been separated by the caller: <i>name1</i> contains the name and <i>name2</i> contains the index. An error is generated if <i>name1</i> contains an open parenthesis and ends with a close parenthesis (array element) and <i>name2</i> is non-NULL.</p>
<dt>[3]</p>
<dd>If <i>name2</i> is NULL, <i>name1</i> is treated just like <i>varName</i> in case [1] above (it can be either a scalar or an array element variable name).</dl>
<p> The <i>flags</i> argument may be used to specify any of several options to the procedures. It consists of an OR-ed combination of the following bits.</p>
<dl COMPACT>
<dt><code>TCL_GLOBAL_ONLY</code></p>
<dd>Under normal circumstances the procedures look up variables as follows. If a procedure call is active in <i>interp</i>, the variable is looked up at the current level of procedure call. Otherwise, the variable is looked up first in the current namespace, then in the global namespace. However, if this bit is set in <i>flags</i> then the variable is looked up only in the global namespace even if there is a procedure call active. If both <code>TCL_GLOBAL_ONLY</code> and <code>TCL_NAMESPACE_ONLY</code> are given, <code>TCL_GLOBAL_ONLY</code> is ignored.</p>
<dt><code>TCL_NAMESPACE_ONLY</code></p>
<dd>If this bit is set in <i>flags</i> then the variable is looked up only in the current namespace; if a procedure is active its variables are ignored, and the global namespace is also ignored unless it is the current namespace.</p>
<dt><code>TCL_LEAVE_ERR_MSG</code></p>
<dd>If an error is returned and this bit is set in <i>flags</i>, then an error message will be left in the interpreter&#8217;s result, where it can be retrieved with <code>Tcl_GetObjResult</code> or <code>Tcl_GetStringResult</code>. If this flag bit is not set then no error message is left and the interpreter&#8217;s result will not be modified.</p>
<dt><code>TCL_APPEND_VALUE</code></p>
<dd>If this bit is set then <i>newValuePtr</i> or <i>newValue</i> is appended to the current value instead of replacing it. If the variable is currently undefined, then the bit is ignored. This bit is only used by the <code>Tcl_Set*</code> procedures.</p>
<dt><code>TCL_LIST_ELEMENT</code></p>
<dd>If this bit is set, then <i>newValue</i> is converted to a valid Tcl list element before setting (or appending to) the variable. A separator space is appended before the new list element unless the list element is going to be the first element in a list or sublist (i.e. the variable&#8217;s current value is empty, or contains the single character &#8220;{&#8221;, or ends in &#8220; }&#8221;). When appending, the original value of the variable must also be a valid list, so that the operation is the appending of a new list element onto a list.</dl>
<p> <code>Tcl_GetVar</code> and <code>Tcl_GetVar2</code> return the current value of a variable. The arguments to these procedures are treated in the same way as the arguments to <code>Tcl_SetVar</code> and <code>Tcl_SetVar2</code>. Under normal circumstances, the return value is a pointer to the variable&#8217;s value (which is stored in Tcl&#8217;s variable structure and will not change before the next call to <code>Tcl_SetVar</code> or <code>Tcl_SetVar2</code>). <code>Tcl_GetVar</code> and <code>Tcl_GetVar2</code> use the flag bits <code>TCL_GLOBAL_ONLY</code> and <code>TCL_LEAVE_ERR_MSG</code>, both of which have the same meaning as for <code>Tcl_SetVar</code>. If an error occurs in reading the variable (e.g. the variable does not exist or an array element is specified for a scalar variable), then NULL is returned. </p>
<p> <code>Tcl_UnsetVar</code> and <code>Tcl_UnsetVar2</code> may be used to remove a variable, so that future calls to <code>Tcl_GetVar</code> or <code>Tcl_GetVar2</code> for the variable will return an error. The arguments to these procedures are treated in the same way as the arguments to <code>Tcl_GetVar</code> and <code>Tcl_GetVar2</code>. If the variable is successfully removed then <code>TCL_OK</code> is returned. If the variable cannot be removed because it does not exist then <code>TCL_ERROR</code> is returned. If an array element is specified, the given element is removed but the array remains. If an array name is specified without an index, then the entire array is removed. </p>
<h2>See Also</h2>
<p>Tcl_GetObjResult, Tcl_GetStringResult, Tcl_TraceVar </p>
<h2>Keywords</h2>
<p>array, get variable, interpreter, object, scalar, set, unset, variable</p>
