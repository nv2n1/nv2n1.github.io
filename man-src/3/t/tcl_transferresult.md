---
title: "tcl_transferresult(3)"
name: "tcl_transferresult"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_transferresult/"
description: "Tcl_SetObjResult, Tcl_GetObjResult, Tcl_SetResult, Tcl_GetStringResult, Tcl_AppendResult, Tcl_AppendResultVA, Tcl_AppendElement, Tcl_ResetResult, Tcl_TransferResult, Tcl_FreeResult – manipulate Tcl..."
---

<p>Tcl_SetObjResult, Tcl_GetObjResult, Tcl_SetResult, Tcl_GetStringResult, Tcl_AppendResult, Tcl_AppendResultVA, Tcl_AppendElement, Tcl_ResetResult, Tcl_TransferResult, Tcl_FreeResult &#8211; manipulate Tcl result </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_SetObjResult</code>(<i>interp, objPtr</i>)
Tcl_Obj *
<code>Tcl_GetObjResult</code>(<i>interp</i>)
<code>Tcl_SetResult</code>(<i>interp, result, freeProc</i>)
const char *
<code>Tcl_GetStringResult</code>(<i>interp</i>)
<code>Tcl_AppendResult</code>(<i>interp, result, result, ... , </i><code>(char *) NULL</code>)
<code>Tcl_AppendResultVA</code>(<i>interp, argList</i>)
<code>Tcl_ResetResult</code>(<i>interp</i>)
<code>Tcl_TransferResult</code>(<i>sourceInterp, result, targetInterp</i>)
<code>Tcl_AppendElement</code>(<i>interp, element</i>)
<code>Tcl_FreeResult</code>(<i>interp</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (out) Interpreter whose result is to be modified or read.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in) Tcl value to become result for <i>interp</i>.</p>
<dd>char <i>*result</i> (in) String value to become result for <i>interp</i> or to be appended to the existing result.</p>
<dd>const char <i>*element</i> (in) String value to append as a list element to the existing result of <i>interp</i>.</p>
<dd>Tcl_FreeProc <i>*freeProc</i> (in) Address of procedure to call to release storage at <i>result</i>, or <code>TCL_STATIC</code>, <code>TCL_DYNAMIC</code>, or <code>TCL_VOLATILE</code>.</p>
<dd>va_list <i>argList</i> (in) An argument list which must have been initialized using <code>va_start</code>, and cleared using <code>va_end</code>.</p>
<dd>Tcl_Interp <i>*sourceInterp</i> (in) Interpreter that the result and error information should be copied from.</p>
<dd>Tcl_Interp <i>*targetInterp</i> (in) Interpreter that the result and error information should be copied to.</p>
<dd>int <i>result</i> (in) If <code>TCL_OK</code>, only copy the result. If <code>TCL_ERROR</code>, copy the error information as well.
</dl>
<h2>Description</h2>
<p>The procedures described here are utilities for manipulating the result value in a Tcl interpreter. The interpreter result may be either a Tcl value or a string. For example, <code>Tcl_SetObjResult</code> and <code>Tcl_SetResult</code> set the interpreter result to, respectively, a value and a string. Similarly, <code>Tcl_GetObjResult</code> and <code>Tcl_GetStringResult</code> return the interpreter result as a value and as a string. The procedures always keep the string and value forms of the interpreter result consistent. For example, if <code>Tcl_SetObjResult</code> is called to set the result to a value, then <code>Tcl_GetStringResult</code> is called, it will return the value&#8217;s string representation. </p>
<p> <code>Tcl_SetObjResult</code> arranges for <i>objPtr</i> to be the result for <i>interp</i>, replacing any existing result. The result is left pointing to the value referenced by <i>objPtr</i>. <i>objPtr</i>&#8216;s reference count is incremented since there is now a new reference to it from <i>interp</i>. The reference count for any old result value is decremented and the old result value is freed if no references to it remain. </p>
<p> <code>Tcl_GetObjResult</code> returns the result for <i>interp</i> as a value. The value&#8217;s reference count is not incremented; if the caller needs to retain a long-term pointer to the value they should use <code>Tcl_IncrRefCount</code> to increment its reference count in order to keep it from being freed too early or accidentally changed. </p>
<p> <code>Tcl_SetResult</code> arranges for <i>result</i> to be the result for the current Tcl command in <i>interp</i>, replacing any existing result. The <i>freeProc</i> argument specifies how to manage the storage for the <i>result</i> argument; it is discussed in the section <code>THE TCL_FREEPROC ARGUMENT TO TCL_SETRESULT</code> below. If <i>result</i> is <code>NULL</code>, then <i>freeProc</i> is ignored and <code>Tcl_SetResult</code> re-initializes <i>interp</i>&#8216;s result to point to an empty string. </p>
<p> <code>Tcl_GetStringResult</code> returns the result for <i>interp</i> as a string. If the result was set to a value by a <code>Tcl_SetObjResult</code> call, the value form will be converted to a string and returned. If the value&#8217;s string representation contains null bytes, this conversion will lose information. For this reason, programmers are encouraged to write their code to use the new value API procedures and to call <code>Tcl_GetObjResult</code> instead. </p>
<p> <code>Tcl_ResetResult</code> clears the result for <i>interp</i> and leaves the result in its normal empty initialized state. If the result is a value, its reference count is decremented and the result is left pointing to an unshared value representing an empty string. If the result is a dynamically allocated string, its memory is free*d and the result is left as a empty string. <code>Tcl_ResetResult</code> also clears the error state managed by <code>Tcl_AddErrorInfo</code>, <code>Tcl_AddObjErrorInfo</code>, and <code>Tcl_SetErrorCode</code>. </p>
<p> <code>Tcl_AppendResult</code> makes it easy to build up Tcl results in pieces. It takes each of its <i>result</i> arguments and appends them in order to the current result associated with <i>interp</i>. If the result is in its initialized empty state (e.g. a command procedure was just invoked or <code>Tcl_ResetResult</code> was just called), then <code>Tcl_AppendResult</code> sets the result to the concatenation of its <i>result</i> arguments. <code>Tcl_AppendResult</code> may be called repeatedly as additional pieces of the result are produced. <code>Tcl_AppendResult</code> takes care of all the storage management issues associated with managing <i>interp</i>&#8216;s result, such as allocating a larger result area if necessary. It also manages conversion to and from the <i>result</i> field of the <i>interp</i> so as to handle backward-compatibility with old-style extensions. Any number of <i>result</i> arguments may be passed in a single call; the last argument in the list must be a NULL pointer. </p>
<p> <code>Tcl_AppendResultVA</code> is the same as <code>Tcl_AppendResult</code> except that instead of taking a variable number of arguments it takes an argument list. </p>
<p> <code>Tcl_TransferResult</code> moves a result from one interpreter to another, optionally (dependent on the <i>result</i> parameter) including the error information dictionary as well. The interpreters must be in the same thread. The source interpreter will have its result reset by this operation.</p>
<h2>Deprecated Interfaces</h2>
<h3>Old String Procedures</h3>
<p>Use of the following procedures (is deprecated since they manipulate the Tcl result as a string. Procedures such as <code>Tcl_SetObjResult</code> that manipulate the result as a value can be significantly more efficient. </p>
<p> <code>Tcl_AppendElement</code> is similar to <code>Tcl_AppendResult</code> in that it allows results to be built up in pieces. However, <code>Tcl_AppendElement</code> takes only a single <i>element</i> argument and it appends that argument to the current result as a proper Tcl list element. <code>Tcl_AppendElement</code> adds backslashes or braces if necessary to ensure that <i>interp</i>&#8216;s result can be parsed as a list and that <i>element</i> will be extracted as a single element. Under normal conditions, <code>Tcl_AppendElement</code> will add a space character to <i>interp</i>&#8216;s result just before adding the new list element, so that the list elements in the result are properly separated. However if the new list element is the first in a list or sub-list (i.e. <i>interp</i>&#8216;s current result is empty, or consists of the single character &#8220;{&#8221;, or ends in the characters &#8220; {&#8221;) then no space is added. </p>
<p> <code>Tcl_FreeResult</code> performs part of the work of <code>Tcl_ResetResult</code>. It frees up the memory associated with <i>interp</i>&#8216;s result. It also sets <i>interp-&gt;freeProc</i> to zero, but does not change <i>interp-&gt;result</i> or clear error state. <code>Tcl_FreeResult</code> is most commonly used when a procedure is about to replace one result value with another.</p>
<h3>DIRECT ACCESS TO INTERP-&gt;RESULT</h3>
<p>It used to be legal for programs to directly read and write <i>interp-&gt;result</i> to manipulate the interpreter result. The Tcl headers no longer permit this access by default, and C code still doing this must be updated to use supported routines <code>Tcl_GetObjResult</code>, <code>Tcl_GetStringResult</code>, <code>Tcl_SetObjResult</code>, and <code>Tcl_SetResult</code>. As a migration aid, access can be restored with the compiler directive</p>
<dl COMPACT>
<dd>
<pre>#define USE_INTERP_RESULT</pre>
</dl>
<p> but this is meant only to offer life support to otherwise dead code.</p>
<h2>The Tcl_Freeproc Argument To Tcl_Setresult</h2>
<p><code>Tcl_SetResult</code>&#8216;s <i>freeProc</i> argument specifies how the Tcl system is to manage the storage for the <i>result</i> argument. If <code>Tcl_SetResult</code> or <code>Tcl_SetObjResult</code> are called at a time when <i>interp</i> holds a string result, they do whatever is necessary to dispose of the old string result (see the <code>Tcl_Interp</code> manual entry for details on this). </p>
<p> If <i>freeProc</i> is <code>TCL_STATIC</code> it means that <i>result</i> refers to an area of static storage that is guaranteed not to be modified until at least the next call to <code>Tcl_Eval</code>. If <i>freeProc</i> is <code>TCL_DYNAMIC</code> it means that <i>result</i> was allocated with a call to <code>Tcl_Alloc</code> and is now the property of the Tcl system. <code>Tcl_SetResult</code> will arrange for the string&#8217;s storage to be released by calling <code>Tcl_Free</code> when it is no longer needed. If <i>freeProc</i> is <code>TCL_VOLATILE</code> it means that <i>result</i> points to an area of memory that is likely to be overwritten when <code>Tcl_SetResult</code> returns (e.g. it points to something in a stack frame). In this case <code>Tcl_SetResult</code> will make a copy of the string in dynamically allocated storage and arrange for the copy to be the result for the current Tcl command. </p>
<p> If <i>freeProc</i> is not one of the values <code>TCL_STATIC</code>, <code>TCL_DYNAMIC</code>, and <code>TCL_VOLATILE</code>, then it is the address of a procedure that Tcl should call to free the string. This allows applications to use non-standard storage allocators. When Tcl no longer needs the storage for the string, it will call <i>freeProc</i>. <i>FreeProc</i> should have arguments and result that match the type <code>Tcl_FreeProc</code>: </p>
<dl COMPACT>
<dd>
<pre>typedef void <code>Tcl_FreeProc</code>(
 char *<i>blockPtr</i>);</pre>
</dl>
<p> When <i>freeProc</i> is called, its <i>blockPtr</i> will be set to the value of <i>result</i> passed to <code>Tcl_SetResult</code>.</p>
<h2>See Also</h2>
<p>Tcl_AddErrorInfo, Tcl_CreateObjCommand, Tcl_SetErrorCode, Tcl_Interp</p>
<h2>Keywords</h2>
<p>append, command, element, list, value, result, return value, interpreter</p>
