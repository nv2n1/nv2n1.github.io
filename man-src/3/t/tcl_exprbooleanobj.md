---
title: "tcl_exprbooleanobj(3)"
name: "tcl_exprbooleanobj"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_exprbooleanobj/"
description: "Tcl_ExprLongObj, Tcl_ExprDoubleObj, Tcl_ExprBooleanObj, Tcl_ExprObj – evaluate an expression"
---

<p>Tcl_ExprLongObj, Tcl_ExprDoubleObj, Tcl_ExprBooleanObj, Tcl_ExprObj &#8211; evaluate an expression </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_ExprLongObj</code>(<i>interp, objPtr, longPtr</i>)
int
<code>Tcl_ExprDoubleObj</code>(<i>interp, objPtr, doublePtr</i>)
int
<code>Tcl_ExprBooleanObj</code>(<i>interp, objPtr, booleanPtr</i>)
int
<code>Tcl_ExprObj</code>(<i>interp, objPtr, resultPtrPtr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in whose context to evaluate <i>objPtr</i>.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in) Pointer to an object containing the expression to evaluate.</p>
<dd>long <i>*longPtr</i> (out) Pointer to location in which to store the integer value of the expression.</p>
<dd>int <i>*doublePtr</i> (out) Pointer to location in which to store the floating-point value of the expression.</p>
<dd>int <i>*booleanPtr</i> (out) Pointer to location in which to store the 0/1 boolean value of the expression.</p>
<dd>Tcl_Obj <i>**resultPtrPtr</i> (out) Pointer to location in which to store a pointer to the object that is the result of the expression. </p>
</dl>
<h2>Description</h2>
<p>These four procedures all evaluate an expression, returning the result in one of four different forms. The expression is given by the <i>objPtr</i> argument, and it can have any of the forms accepted by the <code>expr</code> command. </p>
<p> The <i>interp</i> argument refers to an interpreter used to evaluate the expression (e.g. for variables and nested Tcl commands) and to return error information. </p>
<p> For all of these procedures the return value is a standard Tcl result: <code>TCL_OK</code> means the expression was successfully evaluated, and <code>TCL_ERROR</code> means that an error occurred while evaluating the expression. If <code>TCL_ERROR</code> is returned, then a message describing the error can be retrieved using <code>Tcl_GetObjResult</code>. If an error occurs while executing a Tcl command embedded in the expression then that error will be returned. </p>
<p> If the expression is successfully evaluated, then its value is returned in one of four forms, depending on which procedure is invoked. <code>Tcl_ExprLongObj</code> stores an integer value at <i>*longPtr</i>. If the expression&#8217;s actual value is a floating-point number, then it is truncated to an integer. If the expression&#8217;s actual value is a non-numeric string then an error is returned. </p>
<p> <code>Tcl_ExprDoubleObj</code> stores a floating-point value at <i>*doublePtr</i>. If the expression&#8217;s actual value is an integer, it is converted to floating-point. If the expression&#8217;s actual value is a non-numeric string then an error is returned. </p>
<p> <code>Tcl_ExprBooleanObj</code> stores a 0/1 integer value at <i>*booleanPtr</i>. If the expression&#8217;s actual value is an integer or floating-point number, then they store 0 at <i>*booleanPtr</i> if the value was zero and 1 otherwise. If the expression&#8217;s actual value is a non-numeric string then it must be one of the values accepted by <code>Tcl_GetBoolean</code> such as &#8220;yes&#8221; or &#8220;no&#8221;, or else an error occurs. </p>
<p> If <code>Tcl_ExprObj</code> successfully evaluates the expression, it stores a pointer to the Tcl object containing the expression&#8217;s value at <i>*resultPtrPtr</i>. In this case, the caller is responsible for calling <code>Tcl_DecrRefCount</code> to decrement the object&#8217;s reference count when it is finished with the object. </p>
<h2>See Also</h2>
<p>Tcl_ExprLong, Tcl_ExprDouble, Tcl_ExprBoolean, Tcl_ExprString, Tcl_GetObjResult </p>
<h2>Keywords</h2>
<p>boolean, double, evaluate, expression, integer, object, string</p>
