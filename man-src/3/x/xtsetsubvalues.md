---
title: "xtsetsubvalues(3)"
name: "xtsetsubvalues"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtsetsubvalues/"
description: "XtSetValues, XtVaSetValues, XtSetSubvalues, XtVaSetSubvalues, XtGetValues, XtVaGetValues, XtGetSubvalues, XtVaGetSubvalues – obtain and set widget resources"
---

<p>XtSetValues, XtVaSetValues, XtSetSubvalues, XtVaSetSubvalues, XtGetValues, XtVaGetValues, XtGetSubvalues, XtVaGetSubvalues &#8211; obtain and set widget resources </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtSetValues(Widget <i>w</i>, ArgList <i>args</i>, Cardinal <i>num_args</i>);</p>
<dd>void XtVaSetValues(Widget <i>w</i>, &#8230;);</p>
<dd>void XtSetSubvalues(XtPointer <i>base</i>, XtResourceList <i>resources</i>, Cardinal <i>num_resources</i>, ArgList <i>args</i>, Cardinal <i>num_args</i>);</p>
<dd>void XtVaSetSubvalues(XtPointer <i>base</i>, XtResourceList <i>resources</i>, Cardinal <i>num_resources</i>, &#8230;);</p>
<dd>void XtGetValues(Widget <i>w</i>, ArgList <i>args</i>, Cardinal <i>num_args</i>);</p>
<dd>void XtVaGetValues(Widget <i>w</i>, &#8230;);</p>
<dd>void XtGetSubvalues(XtPointer <i>base</i>, XtResourceList <i>resources</i>, Cardinal <i>num_resources</i>, ArgList <i>args</i>, Cardinal <i>num_args</i>);</p>
<dd>void XtVaGetSubvalues(XtPointer <i>base</i>, XtResourceList <i>resources</i>, Cardinal <i>num_resources</i>, &#8230;);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>args</i></p>
<dd>Specifies the argument list of name/address pairs that contain the resource name and either the address into which the resource value is to be stored or their new values.</p>
<dt><i>base</i></p>
<dd>Specifies the base address of the subpart data structure where the resources should be retrieved or written.</p>
<dt><i>num_args</i></p>
<dd>Specifies the number of arguments in the argument list.</p>
<dt><i>resources</i></p>
<dd>Specifies the nonwidget resource list or values.</p>
<dt><i>num_resources</i></p>
<dd>Specifies the number of resources in the resource list.</p>
<dt><i>w</i></p>
<dd>Specifies the widget.</p>
<dt><i>&#8230;</i></p>
<dd>Specifies the variable argument list of name/address pairs that contain the resource name and either the address into which the resource value is to be stored or their new values.</dl>
<h2>Description</h2>
<p>The <code>XtSetValues</code> function starts with the resources specified for the <code>Core</code> widget fields and proceeds down the subclass chain to the widget. At each stage, it writes the new value (if specified by one of the arguments) or the existing value (if no new value is specified) to a new widget data record. <code>XtSetValues</code> then calls the set_values procedures for the widget in superclass-to-subclass order. If the widget has any non-NULL set_values_hook fields, these are called immediately after the corresponding set_values procedure. This procedure permits subclasses to set nonwidget data for <code>XtSetValues</code>. </p>
<p> If the widget&#8217;s parent is a subclass of <code>constraintWidgetClass</code>, <code>XtSetValues</code> also updates the widget&#8217;s constraints. It starts with the constraint resources specified for <code>constraintWidgetClass</code> and proceeds down the subclass chain to the parent&#8217;s class. At each stage, it writes the new value or the existing value to a new constraint record. It then calls the constraint set_values procedures from <code>constraintWidgetClass</code> down to the parent&#8217;s class. The constraint set_values procedures are called with widget arguments, as for all set_values procedures, not just the constraint record arguments, so that they can make adjustments to the desired values based on full information about the widget. </p>
<p> <code>XtSetValues</code> determines if a geometry request is needed by comparing the current widget to the new widget. If any geometry changes are required, it makes the request, and the geometry manager returns <code>XtGeometryYes</code>, <code>XtGeometryAlmost</code>, or <code>XtGeometryNo</code>. If <code>XtGeometryYes</code>, <code>XtSetValues</code> calls the widget&#8217;s resize procedure. If <code>XtGeometryNo</code>, <code>XtSetValues</code> resets the geometry fields to their original values. If <code>XtGeometryAlmost</code>, <code>XtSetValues</code> calls the set_values_almost procedure, which determines what should be done and writes new values for the geometry fields into the new widget. <code>XtSetValues</code> then repeats this process, deciding once more whether the geometry manager should be called. </p>
<p> Finally, if any of the set_values procedures returned <code>True</code>, <code>XtSetValues</code> causes the widget&#8217;s expose procedure to be invoked by calling the Xlib <code>XClearArea</code> function on the widget&#8217;s window. </p>
<p> The <code>XtSetSubvalues</code> function stores resources into the structure identified by base. </p>
<p> The <code>XtGetValues</code> function starts with the resources specified for the core widget fields and proceeds down the subclass chain to the widget. The value field of a passed argument list should contain the address into which to store the corresponding resource value. It is the caller&#8217;s responsibility to allocate and deallocate this storage according to the size of the resource representation type used within the widget. </p>
<p> If the widget&#8217;s parent is a subclass of <code>constraintWidgetClass</code>, <code>XtGetValues</code> then fetches the values for any constraint resources requested. It starts with the constraint resources specified for <code>constraintWidgetClass</code> and proceeds down to the subclass chain to the parent&#8217;s constraint resources. If the argument list contains a resource name that is not found in any of the resource lists searched, the value at the corresponding address is not modified. Finally, if the get_values_hook procedures are non-NULL, they are called in superclass-to-subclass order after all the resource values have been fetched by <code>XtGetValues</code>. This permits a subclass to provide nonwidget resource data to <code>XtGetValues</code>. </p>
<p> The <code>XtGetSubvalues</code> function obtains resource values from the structure identified by base.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
