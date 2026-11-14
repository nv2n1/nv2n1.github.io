---
title: "tcl_exprdouble(3)"
name: "tcl_exprdouble"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_exprdouble/"
description: "Tcl_ExprLong, Tcl_ExprDouble, Tcl_ExprBoolean, Tcl_ExprString – evaluate an expression"
---

<p>Tcl_ExprLong, Tcl_ExprDouble, Tcl_ExprBoolean, Tcl_ExprString &#8211; evaluate an expression </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_ExprLong</code>(<i>interp, expr, longPtr</i>)
int
<code>Tcl_ExprDouble</code>(<i>interp, expr, doublePtr</i>)
int
<code>Tcl_ExprBoolean</code>(<i>interp, expr, booleanPtr</i>)
int
<code>Tcl_ExprString</code>(<i>interp, expr</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in whose context to evaluate <i>expr</i>.</p>
<dd>const char <i>*expr</i> (in) Expression to be evaluated.</p>
<dd>long <i>*longPtr</i> (out) Pointer to location in which to store the integer value of the expression.</p>
<dd>int <i>*doublePtr</i> (out) Pointer to location in which to store the floating-point value of the expression.</p>
<dd>int <i>*booleanPtr</i> (out) Pointer to location in which to store the 0/1 boolean value of the expression. </p>
</dl>
<h2>Description</h2>
<p>These four procedures all evaluate the expression given by the <i>expr</i> argument and return the result in one of four different forms. The expression can have any of the forms accepted by the <code>expr</code> command. Note that these procedures have been largely replaced by the object-based procedures <code>Tcl_ExprLongObj</code>, <code>Tcl_ExprDoubleObj</code>, <code>Tcl_ExprBooleanObj</code>, and <code>Tcl_ExprObj</code>. Those object-based procedures evaluate an expression held in a Tcl object instead of a string. The object argument can retain an internal representation that is more efficient to execute. </p>
<p> The <i>interp</i> argument refers to an interpreter used to evaluate the expression (e.g. for variables and nested Tcl commands) and to return error information. </p>
<p> For all of these procedures the return value is a standard Tcl result: <code>TCL_OK</code> means the expression was successfully evaluated, and <code>TCL_ERROR</code> means that an error occurred while evaluating the expression. If <code>TCL_ERROR</code> is returned then the interpreter&#8217;s result will hold a message describing the error. If an error occurs while executing a Tcl command embedded in the expression then that error will be returned. </p>
<p> If the expression is successfully evaluated, then its value is returned in one of four forms, depending on which procedure is invoked. <code>Tcl_ExprLong</code> stores an integer value at <i>*longPtr</i>. If the expression&#8217;s actual value is a floating-point number, then it is truncated to an integer. If the expression&#8217;s actual value is a non-numeric string then an error is returned. </p>
<p> <code>Tcl_ExprDouble</code> stores a floating-point value at <i>*doublePtr</i>. If the expression&#8217;s actual value is an integer, it is converted to floating-point. If the expression&#8217;s actual value is a non-numeric string then an error is returned. </p>
<p> <code>Tcl_ExprBoolean</code> stores a 0/1 integer value at <i>*booleanPtr</i>. If the expression&#8217;s actual value is an integer or floating-point number, then they store 0 at <i>*booleanPtr</i> if the value was zero and 1 otherwise. If the expression&#8217;s actual value is a non-numeric string then it must be one of the values accepted by <code>Tcl_GetBoolean</code> such as &#8220;yes&#8221; or &#8220;no&#8221;, or else an error occurs. </p>
<p> <code>Tcl_ExprString</code> returns the value of the expression as a string stored in the interpreter&#8217;s result. </p>
<h2>See Also</h2>
<p>Tcl_ExprLongObj, Tcl_ExprDoubleObj, Tcl_ExprBooleanObj, Tcl_ExprObj </p>
<h2>Keywords</h2>
<p>boolean, double, evaluate, expression, integer, object, string</p>
