---
title: "tcl_newbooleanobj(3)"
name: "tcl_newbooleanobj"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_newbooleanobj/"
description: "Tcl_NewBooleanObj, Tcl_SetBooleanObj, Tcl_GetBooleanFromObj – store/retrieve boolean value in a Tcl_Obj"
---

<p>Tcl_NewBooleanObj, Tcl_SetBooleanObj, Tcl_GetBooleanFromObj &#8211; store/retrieve boolean value in a Tcl_Obj </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Obj *
<code>Tcl_NewBooleanObj</code>(<i>boolValue</i>)
<code>Tcl_SetBooleanObj</code>(<i>objPtr, boolValue</i>)
int
<code>Tcl_GetBooleanFromObj</code>(<i>interp, objPtr, boolPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>boolValue</i> (in) Integer value to be stored as a boolean value in a Tcl_Obj.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in/out) Points to the Tcl_Obj in which to store, or from which to retrieve a boolean value.</p>
<dd>Tcl_Interp <i>*interp</i> (in/out) If a boolean value cannot be retrieved, an error message is left in the interpreter&#8217;s result object unless <i>interp</i> is NULL.</p>
<dd>int <i>*boolPtr</i> (out) Points to place where <code>Tcl_GetBooleanFromObj</code> stores the boolean value (0 or 1) obtained from <i>objPtr</i>. </p>
</dl>
<h2>Description</h2>
<p>These procedures are used to pass boolean values to and from Tcl as Tcl_Obj&#8217;s. When storing a boolean value into a Tcl_Obj, any non-zero integer value in <i>boolValue</i> is taken to be the boolean value <code>1</code>, and the integer value <code>0</code> is taken to be the boolean value <code>0</code>. </p>
<p> <code>Tcl_NewBooleanObj</code> creates a new Tcl_Obj, stores the boolean value <i>boolValue</i> in it, and returns a pointer to the new Tcl_Obj. The new Tcl_Obj has reference count of zero. </p>
<p> <code>Tcl_SetBooleanObj</code> accepts <i>objPtr</i>, a pointer to an existing Tcl_Obj, and stores in the Tcl_Obj <i>*objPtr</i> the boolean value <i>boolValue</i>. This is a write operation on <i>*objPtr</i>, so <i>objPtr</i> must be unshared. Attempts to write to a shared Tcl_Obj will panic. A successful write of <i>boolValue</i> into <i>*objPtr</i> implies the freeing of any former value stored in <i>*objPtr</i>. </p>
<p> <code>Tcl_GetBooleanFromObj</code> attempts to retrieve a boolean value from the value stored in <i>*objPtr</i>. If <i>objPtr</i> holds a string value recognized by <code>Tcl_GetBoolean</code>, then the recognized boolean value is written at the address given by <i>boolPtr</i>. If <i>objPtr</i> holds any value recognized as a number by Tcl, then if that value is zero a 0 is written at the address given by <i>boolPtr</i> and if that value is non-zero a 1 is written at the address given by <i>boolPtr</i>. In all cases where a value is written at the address given by <i>boolPtr</i>, <code>Tcl_GetBooleanFromObj</code> returns <code>TCL_OK</code>. If the value of <i>objPtr</i> does not meet any of the conditions above, then <code>TCL_ERROR</code> is returned and an error message is left in the interpreter&#8217;s result unless <i>interp</i> is NULL. <code>Tcl_GetBooleanFromObj</code> may also make changes to the internal fields of <i>*objPtr</i> so that future calls to <code>Tcl_GetBooleanFromObj</code> on the same <i>objPtr</i> can be performed more efficiently. </p>
<p> Note that the routines <code>Tcl_GetBooleanFromObj</code> and <code>Tcl_GetBoolean</code> are not functional equivalents. The set of values for which <code>Tcl_GetBooleanFromObj</code> will return <code>TCL_OK</code> is strictly larger than the set of values for which <code>Tcl_GetBoolean</code> will do the same. For example, the value &#8220;5&#8221; passed to <code>Tcl_GetBooleanFromObj</code> will lead to a <code>TCL_OK</code> return (and the boolean value 1), while the same value passed to <code>Tcl_GetBoolean</code> will lead to a <code>TCL_ERROR</code> return. </p>
<h2>See Also</h2>
<p>Tcl_NewObj, Tcl_IsShared, Tcl_GetBoolean </p>
<h2>Keywords</h2>
<p>boolean, object</p>
