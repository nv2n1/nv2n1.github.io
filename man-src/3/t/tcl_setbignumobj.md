---
title: "tcl_setbignumobj(3)"
name: "tcl_setbignumobj"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_setbignumobj/"
description: "Tcl_NewIntObj, Tcl_NewLongObj, Tcl_NewWideIntObj, Tcl_SetIntObj, Tcl_SetLongObj, Tcl_SetWideIntObj, Tcl_GetIntFromObj, Tcl_GetLongFromObj, Tcl_GetWideIntFromObj, Tcl_NewBignumObj, Tcl_SetBignumObj,..."
---

<p>Tcl_NewIntObj, Tcl_NewLongObj, Tcl_NewWideIntObj, Tcl_SetIntObj, Tcl_SetLongObj, Tcl_SetWideIntObj, Tcl_GetIntFromObj, Tcl_GetLongFromObj, Tcl_GetWideIntFromObj, Tcl_NewBignumObj, Tcl_SetBignumObj, Tcl_GetBignumFromObj, Tcl_TakeBignumFromObj &#8211; manipulate Tcl objects as integer values </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Obj *
<code>Tcl_NewIntObj</code>(<i>intValue</i>)
Tcl_Obj *
<code>Tcl_NewLongObj</code>(<i>longValue</i>)
Tcl_Obj *
<code>Tcl_NewWideIntObj</code>(<i>wideValue</i>)
<code>Tcl_SetIntObj</code>(<i>objPtr, intValue</i>)
<code>Tcl_SetLongObj</code>(<i>objPtr, longValue</i>)
<code>Tcl_SetWideIntObj</code>(<i>objPtr, wideValue</i>)
int
<code>Tcl_GetIntFromObj</code>(<i>interp, objPtr, intPtr</i>)
int
<code>Tcl_GetLongFromObj</code>(<i>interp, objPtr, longPtr</i>)
int
<code>Tcl_GetWideIntFromObj</code>(<i>interp, objPtr, widePtr</i>)
<code>#include &lt;tclTomMath.h&gt;</code>
Tcl_Obj *
<code>Tcl_NewBignumObj</code>(<i>bigValue</i>)
<code>Tcl_SetBignumObj</code>(<i>objPtr, bigValue</i>)
int
<code>Tcl_GetBignumFromObj</code>(<i>interp, objPtr, bigValue</i>)
int
<code>Tcl_TakeBignumFromObj</code>(<i>interp, objPtr, bigValue</i>)
int
<code>Tcl_InitBignumFromDouble</code>(<i>interp, doubleValue, bigValue</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>int <i>intValue</i> (in) Integer value used to initialize or set a Tcl object.</p>
<dd>long <i>longValue</i> (in) Long integer value used to initialize or set a Tcl object.</p>
<dd>Tcl_WideInt <i>wideValue</i> (in) Wide integer value used to initialize or set a Tcl object.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in/out) For <code>Tcl_SetIntObj</code>, <code>Tcl_SetLongObj</code>, <code>Tcl_SetWideIntObj</code>, and <code>Tcl_SetBignumObj</code>, this points to the object in which to store an integral value. For <code>Tcl_GetIntFromObj</code>, <code>Tcl_GetLongFromObj</code>, <code>Tcl_GetWideIntFromObj</code>, <code>Tcl_GetBignumFromObj</code>, and <code>Tcl_TakeBignumFromObj</code>, this refers to the object from which to retrieve an integral value.</p>
<dd>Tcl_Interp <i>*interp</i> (in/out) When non-NULL, an error message is left here when integral value retrieval fails.</p>
<dd>int <i>*intPtr</i> (out) Points to place to store the integer value retrieved from <i>objPtr</i>.</p>
<dd>long <i>*longPtr</i> (out) Points to place to store the long integer value retrieved from <i>objPtr</i>.</p>
<dd>Tcl_WideInt <i>*widePtr</i> (out) Points to place to store the wide integer value retrieved from <i>objPtr</i>.</p>
<dd>mp_int <i>*bigValue</i> (in/out) Points to a multi-precision integer structure declared by the LibTomMath library.</p>
<dd>double <i>doubleValue</i> (in) Double value from which the integer part is determined and used to initialize a multi-precision integer value. </p>
</dl>
<h2>Description</h2>
<p>These procedures are used to create, modify, and read Tcl objects that hold integral values. </p>
<p> The different routines exist to accommodate different integral types in C with which values might be exchanged. The C integral types for which Tcl provides value exchange routines are <code>int</code>, <code>long int</code>, <code>Tcl_WideInt</code>, and <code>mp_int</code>. The <code>int</code> and <code>long int</code> types are provided by the C language standard. The <code>Tcl_WideInt</code> type is a typedef defined to be whatever signed integral type covers at least the 64-bit integer range (-9223372036854775808 to 9223372036854775807). Depending on the platform and the C compiler, the actual type might be <code>long int</code>, <code>long long int</code>, <code>int64</code>, or something else. The <code>mp_int</code> type is a multiple-precision integer type defined by the LibTomMath multiple-precision integer library. </p>
<p> The <code>Tcl_NewIntObj</code>, <code>Tcl_NewLongObj</code>, <code>Tcl_NewWideIntObj</code>, and <code>Tcl_NewBignumObj</code> routines each create and return a new Tcl object initialized to the integral value of the argument. The returned Tcl object is unshared. </p>
<p> The <code>Tcl_SetIntObj</code>, <code>Tcl_SetLongObj</code>, <code>Tcl_SetWideIntObj</code>, and <code>Tcl_SetBignumObj</code> routines each set the value of an existing Tcl object pointed to by <i>objPtr</i> to the integral value provided by the other argument. The <i>objPtr</i> argument must point to an unshared Tcl object. Any attempt to set the value of a shared Tcl object violates Tcl&#8217;s copy-on-write policy. Any existing string representation or internal representation in the unshared Tcl object will be freed as a consequence of setting the new value. </p>
<p> The <code>Tcl_GetIntFromObj</code>, <code>Tcl_GetLongFromObj</code>, <code>Tcl_GetWideIntFromObj</code>, <code>Tcl_GetBignumFromObj</code>, and <code>Tcl_TakeBignumFromObj</code> routines attempt to retrieve an integral value of the appropriate type from the Tcl object <i>objPtr</i>. If the attempt succeeds, then <code>TCL_OK</code> is returned, and the value is written to the storage provided by the caller. The attempt might fail if <i>objPtr</i> does not hold an integral value, or if the value exceeds the range of the target type. If the attempt fails, then <code>TCL_ERROR</code> is returned, and if <i>interp</i> is non-NULL, an error message is left in <i>interp</i>. The <code>Tcl_ObjType</code> of <i>objPtr</i> may be changed to make subsequent calls to the same routine more efficient. Unlike the other functions, <code>Tcl_TakeBignumFromObj</code> may set the content of the Tcl object <i>objPtr</i> to an empty string in the process of retrieving the multiple-precision integer value. </p>
<p> The choice between <code>Tcl_GetBignumFromObj</code> and <code>Tcl_TakeBignumFromObj</code> is governed by how the caller will continue to use <i>objPtr</i>. If after the <code>mp_int</code> value is retrieved from <i>objPtr</i>, the caller will make no more use of <i>objPtr</i>, then using <code>Tcl_TakeBignumFromObj</code> permits Tcl to detect when an unshared <i>objPtr</i> permits the value to be moved instead of copied, which should be more efficient. If anything later in the caller requires <i>objPtr</i> to continue to hold the same value, then <code>Tcl_GetBignumFromObj</code> must be chosen. </p>
<p> The <code>Tcl_InitBignumFromDouble</code> routine is a utility procedure that extracts the integer part of <i>doubleValue</i> and stores that integer value in the <code>mp_int</code> value <i>bigValue</i>.</p>
<h2>See Also</h2>
<p>Tcl_NewObj, Tcl_DecrRefCount, Tcl_IncrRefCount, Tcl_GetObjResult</p>
<h2>Keywords</h2>
<p>integer, integer object, integer type, internal representation, object, object type, string representation</p>
