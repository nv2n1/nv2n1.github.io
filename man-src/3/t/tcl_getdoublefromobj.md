---
title: "tcl_getdoublefromobj(3)"
name: "tcl_getdoublefromobj"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_getdoublefromobj/"
description: "Tcl_NewDoubleObj, Tcl_SetDoubleObj, Tcl_GetDoubleFromObj – manipulate Tcl objects as floating-point values"
---

<p>Tcl_NewDoubleObj, Tcl_SetDoubleObj, Tcl_GetDoubleFromObj &#8211; manipulate Tcl objects as floating-point values </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Obj *
<code>Tcl_NewDoubleObj</code>(<i>doubleValue</i>)
<code>Tcl_SetDoubleObj</code>(<i>objPtr, doubleValue</i>)
int
<code>Tcl_GetDoubleFromObj</code>(<i>interp, objPtr, doublePtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>double <i>doubleValue</i> (in) A double-precision floating-point value used to initialize or set a Tcl object.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in/out) For <code>Tcl_SetDoubleObj</code>, this points to the object in which to store a double value. For <code>Tcl_GetDoubleFromObj</code>, this refers to the object from which to retrieve a double value.</p>
<dd>Tcl_Interp <i>*interp</i> (in/out) When non-NULL, an error message is left here when double value retrieval fails.</p>
<dd>double <i>*doublePtr</i> (out) Points to place to store the double value obtained from <i>objPtr</i>. </p>
</dl>
<h2>Description</h2>
<p>These procedures are used to create, modify, and read Tcl objects that hold double-precision floating-point values. </p>
<p> <code>Tcl_NewDoubleObj</code> creates and returns a new Tcl object initialized to the double value <i>doubleValue</i>. The returned Tcl object is unshared. </p>
<p> <code>Tcl_SetDoubleObj</code> sets the value of an existing Tcl object pointed to by <i>objPtr</i> to the double value <i>doubleValue</i>. The <i>objPtr</i> argument must point to an unshared Tcl object. Any attempt to set the value of a shared Tcl object violates Tcl&#8217;s copy-on-write policy. Any existing string representation or internal representation in the unshared Tcl object will be freed as a consequence of setting the new value. </p>
<p> <code>Tcl_GetDoubleFromObj</code> attempts to retrieve a double value from the Tcl object <i>objPtr</i>. If the attempt succeeds, then <code>TCL_OK</code> is returned, and the double value is written to the storage pointed to by <i>doublePtr</i>. If the attempt fails, then <code>TCL_ERROR</code> is returned, and if <i>interp</i> is non-NULL, an error message is left in <i>interp</i>. The <code>Tcl_ObjType</code> of <i>objPtr</i> may be changed to make subsequent calls to <code>Tcl_GetDoubleFromObj</code> more efficient.</p>
<h2>See Also</h2>
<p>Tcl_NewObj, Tcl_DecrRefCount, Tcl_IncrRefCount, Tcl_GetObjResult</p>
<h2>Keywords</h2>
<p>double, double object, double type, internal representation, object, object type, string representation</p>
