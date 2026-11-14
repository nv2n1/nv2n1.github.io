---
title: "xtvacreatemanagedwidget(3)"
name: "xtvacreatemanagedwidget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtvacreatemanagedwidget/"
description: "XtCreateWidget, XtVaCreateWidget, XtCreateManagedWidget, XtVaCreateManagedWidget, XtDestroyWidget – create and destroy widgets"
---

<p>XtCreateWidget, XtVaCreateWidget, XtCreateManagedWidget, XtVaCreateManagedWidget, XtDestroyWidget &#8211; create and destroy widgets </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>Widget XtCreateWidget(const char *<i>name</i>, WidgetClass <i>widget_class</i>, Widget <i>parent</i>, ArgList <i>args</i>, Cardinal <i>num_args</i>);</p>
<dd>Widget XtVaCreateWidget(const char *<i>name</i>, WidgetClass <i>widget_class</i>, Widget <i>parent</i>, &#8230;);</p>
<dd>Widget XtCreateManagedWidget(const char *<i>name</i>, WidgetClass <i>widget_class</i>, Widget <i>parent</i>, ArgList <i>args</i>, Cardinal <i>num_args</i>);</p>
<dd>Widget XtVaCreateManagedWidget(const char *<i>name</i>, WidgetClass <i>widget_class</i>, Widget <i>parent</i>, &#8230;);</p>
<dd>void XtDestroyWidget(Widget <i>w</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>args</i></p>
<dd>Specifies the argument list to override the resource defaults.</p>
<dt><i>name</i></p>
<dd>Specifies the resource name for the created widget, which is used for retrieving resources and, for that reason, should not be the same as any other widget that is a child of same parent.</p>
<dt><i>num_args</i></p>
<dd>Specifies the number of arguments in the argument list.</p>
<dt><i>parent</i></p>
<dd>Specifies the parent widget.</p>
<dt><i>w</i></p>
<dd>Specifies the widget.</p>
<dt><i>widget_class</i></p>
<dd>Specifies the widget class pointer for the created widget.</p>
<dt><i>&#8230;</i></p>
<dd>Specifies the variable argument list to override the resource defaults.</dl>
<h2>Description</h2>
<p>The <code>XtCreateWidget</code> function performs much of the boilerplate operations of widget creation:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Checks to see if the class_initialize procedure has been called for this class and for all superclasses and, if not, calls those necessary in a superclass-to-subclass order.</p>
<dt>&bull;</p>
<dd>Allocates memory for the widget instance.</p>
<dt>&bull;</p>
<dd>If the parent is a subclass of <code>constraintWidgetClass</code>, it allocates memory for the parent&#8217;s constraints and stores the address of this memory into the constraints field.</p>
<dt>&bull;</p>
<dd>Initializes the core nonresource data fields (for example, parent and visible).</p>
<dt>&bull;</p>
<dd>Initializes the resource fields (for example, background_pixel) by using the resource lists specified for this class and all superclasses.</p>
<dt>&bull;</p>
<dd>If the parent is a subclass of <code>constraintWidgetClass</code>, it initializes the resource fields of the constraints record by using the constraint resource list specified for the parent&#8217;s class and all superclasses up to <code>constraintWidgetClass</code>.</p>
<dt>&bull;</p>
<dd>Calls the initialize procedures for the widget by starting at the <code>Core</code> initialize procedure on down to the widget&#8217;s initialize procedure.</p>
<dt>&bull;</p>
<dd>If the parent is a subclass of <code>compositeWidgetClass</code>, it puts the widget into its parent&#8217;s children list by calling its parent&#8217;s insert_child procedure. For further information, see Section 3.5.</p>
<dt>&bull;</p>
<dd>If the parent is a subclass of <code>constraintWidgetClass</code>, it calls the constraint initialize procedures, starting at <code>constraintWidgetClass</code> on down to the parent&#8217;s constraint initialize procedure.</dl>
<p> Note that you can determine the number of arguments in an argument list by using the <code>XtNumber</code> macro. For further information, see Section 11.1. </p>
<p> The <code>XtCreateManagedWidget</code> function is a convenience routine that calls <code>XtCreateWidget</code> and <code>XtManageChild</code>. </p>
<p> The <code>XtDestroyWidget</code> function provides the only method of destroying a widget, including widgets that need to destroy themselves. It can be called at any time, including from an application callback routine of the widget being destroyed. This requires a two-phase destroy process in order to avoid dangling references to destroyed widgets. </p>
<p> In phase one, <code>XtDestroyWidget</code> performs the following:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>If the being_destroyed field of the widget is <code>True</code>, it returns immediately.</p>
<dt>&bull;</p>
<dd>Recursively descends the widget tree and sets the being_destroyed field to <code>True</code> for the widget and all children.</p>
<dt>&bull;</p>
<dd>Adds the widget to a list of widgets (the destroy list) that should be destroyed when it is safe to do so.</dl>
<p> Entries on the destroy list satisfy the invariant that if w2 occurs after w1 on the destroy list then w2 is not a descendent of w1. (A descendant refers to both normal and pop-up children.) </p>
<p> Phase two occurs when all procedures that should execute as a result of the current event have been called (including all procedures registered with the event and translation managers), that is, when the current invocation of <code>XtDispatchEvent</code> is about to return or immediately if not in <code>XtDispatchEvent</code>. </p>
<p> In phase two, <code>XtDestroyWidget</code> performs the following on each entry in the destroy list:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>Calls the destroy callback procedures registered on the widget (and all descendants) in post-order (it calls children callbacks before parent callbacks).</p>
<dt>&bull;</p>
<dd>If the widget&#8217;s parent is a subclass of <code>compositeWidgetClass</code> and if the parent is not being destroyed, it calls <code>XtUnmanageChild</code> on the widget and then calls the widget&#8217;s parent&#8217;s delete_child procedure (see Section 3.4).</p>
<dt>&bull;</p>
<dd>If the widget&#8217;s parent is a subclass of <code>constraintWidgetClass</code>, it calls the constraint destroy procedure for the parent, then the parent&#8217;s superclass, until finally it calls the constraint destroy procedure for <code>constraintWidgetClass</code>.</p>
<dt>&bull;</p>
<dd>Calls the destroy methods for the widget (and all descendants) in post-order. For each such widget, it calls the destroy procedure declared in the widget class, then the destroy procedure declared in its superclass, until finally it calls the destroy procedure declared in the Core class record.</p>
<dt>&bull;</p>
<dd>Calls <code>XDestroyWindow</code> if the widget is realized (that is, has an X window). The server recursively destroys all descendant windows.</p>
<dt>&bull;</p>
<dd>Recursively descends the tree and deallocates all pop-up widgets, constraint records, callback lists and, if the widget is a subclass of <code>compositeWidgetClass</code>, children.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappcreateshell/">XtAppCreateShell</a>(3), <a href="/docs/linux/man/3-xtcreatepopupshell/">XtCreatePopupShell</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
