---
title: "xtcreatemanagedwidget(3)"
name: "xtcreatemanagedwidget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtcreatemanagedwidget/"
---

XtCreateWidget, XtVaCreateWidget, XtCreateManagedWidget, XtVaCreateManagedWidget, XtDestroyWidget - create and destroy widgets 

<h2>Syntax</h2>#include &lt;X11/Intrinsic.h&gt;
<dl COMPACT><dd>Widget XtCreateWidget(const char *<i>name</i>, WidgetClass <i>widget_class</i>, Widget <i>parent</i>, ArgList <i>args</i>, Cardinal <i>num_args</i>);
<dd>Widget XtVaCreateWidget(const char *<i>name</i>, WidgetClass <i>widget_class</i>, Widget <i>parent</i>, ...);
<dd>Widget XtCreateManagedWidget(const char *<i>name</i>, WidgetClass <i>widget_class</i>, Widget <i>parent</i>, ArgList <i>args</i>, Cardinal <i>num_args</i>);
<dd>Widget XtVaCreateManagedWidget(const char *<i>name</i>, WidgetClass <i>widget_class</i>, Widget <i>parent</i>, ...);
<dd>void XtDestroyWidget(Widget <i>w</i>);</dl><h2>Arguments</h2><dl COMPACT><dt><i>args</i>
<dd>Specifies the argument list to override the resource defaults.
<dt><i>name</i>
<dd>Specifies the resource name for the created widget, which is used for retrieving resources and, for that reason, should not be the same as any other widget that is a child of same parent.
<dt><i>num_args</i>
<dd>Specifies the number of arguments in the argument list.
<dt><i>parent</i>
<dd>Specifies the parent widget.
<dt><i>w</i>
<dd>Specifies the widget.
<dt><i>widget_class</i>
<dd>Specifies the widget class pointer for the created widget.
<dt><i>...</i>
<dd>Specifies the variable argument list to override the resource defaults.</dl><h2>Description</h2>The <b>XtCreateWidget</b> function performs much of the boilerplate operations of widget creation:
<dl COMPACT><dt>&bull;
<dd>Checks to see if the class_initialize procedure has been called for this class and for all superclasses and, if not, calls those necessary in a superclass-to-subclass order.
<dt>&bull;
<dd>Allocates memory for the widget instance.
<dt>&bull;
<dd>If the parent is a subclass of <b>constraintWidgetClass</b>, it allocates memory for the parent's constraints and stores the address of this memory into the constraints field.
<dt>&bull;
<dd>Initializes the core nonresource data fields (for example, parent and visible).
<dt>&bull;
<dd>Initializes the resource fields (for example, background_pixel) by using the resource lists specified for this class and all superclasses.
<dt>&bull;
<dd>If the parent is a subclass of <b>constraintWidgetClass</b>, it initializes the resource fields of the constraints record by using the constraint resource list specified for the parent's class and all superclasses up to <b>constraintWidgetClass</b>.
<dt>&bull;
<dd>Calls the initialize procedures for the widget by starting at the <b>Core</b> initialize procedure on down to the widget's initialize procedure.
<dt>&bull;
<dd>If the parent is a subclass of <b>compositeWidgetClass</b>, it puts the widget into its parent's children list by calling its parent's insert_child procedure. For further information, see Section 3.5.
<dt>&bull;
<dd>If the parent is a subclass of <b>constraintWidgetClass</b>, it calls the constraint initialize procedures, starting at <b>constraintWidgetClass</b> on down to the parent's constraint initialize procedure.</dl>
 

 Note that you can determine the number of arguments in an argument list by using the <b>XtNumber</b> macro. For further information, see Section 11.1. 

 The <b>XtCreateManagedWidget</b> function is a convenience routine that calls <b>XtCreateWidget</b> and <b>XtManageChild</b>. 

 The <b>XtDestroyWidget</b> function provides the only method of destroying a widget, including widgets that need to destroy themselves. It can be called at any time, including from an application callback routine of the widget being destroyed. This requires a two-phase destroy process in order to avoid dangling references to destroyed widgets. 

 In phase one, <b>XtDestroyWidget</b> performs the following:
<dl COMPACT><dt>&bull;
<dd>If the being_destroyed field of the widget is <b>True</b>, it returns immediately.
<dt>&bull;
<dd>Recursively descends the widget tree and sets the being_destroyed field to <b>True</b> for the widget and all children.
<dt>&bull;
<dd>Adds the widget to a list of widgets (the destroy list) that should be destroyed when it is safe to do so.</dl>
 

 Entries on the destroy list satisfy the invariant that if w2 occurs after w1 on the destroy list then w2 is not a descendent of w1. (A descendant refers to both normal and pop-up children.) 

 Phase two occurs when all procedures that should execute as a result of the current event have been called (including all procedures registered with the event and translation managers), that is, when the current invocation of <b>XtDispatchEvent</b> is about to return or immediately if not in <b>XtDispatchEvent</b>. 

 In phase two, <b>XtDestroyWidget</b> performs the following on each entry in the destroy list:
<dl COMPACT><dt>&bull;
<dd>Calls the destroy callback procedures registered on the widget (and all descendants) in post-order (it calls children callbacks before parent callbacks).
<dt>&bull;
<dd>If the widget's parent is a subclass of <b>compositeWidgetClass</b> and if the parent is not being destroyed, it calls <b>XtUnmanageChild</b> on the widget and then calls the widget's parent's delete_child procedure (see Section 3.4).
<dt>&bull;
<dd>If the widget's parent is a subclass of <b>constraintWidgetClass</b>, it calls the constraint destroy procedure for the parent, then the parent's superclass, until finally it calls the constraint destroy procedure for <b>constraintWidgetClass</b>.
<dt>&bull;
<dd>Calls the destroy methods for the widget (and all descendants) in post-order. For each such widget, it calls the destroy procedure declared in the widget class, then the destroy procedure declared in its superclass, until finally it calls the destroy procedure declared in the Core class record.
<dt>&bull;
<dd>Calls <b>XDestroyWindow</b> if the widget is realized (that is, has an X window). The server recursively destroys all descendant windows.
<dt>&bull;
<dd>Recursively descends the tree and deallocates all pop-up widgets, constraint records, callback lists and, if the widget is a subclass of <b>compositeWidgetClass</b>, children.</dl><h2>See Also</h2><a HREF="/docs/linux/man/3-xtappcreateshell/">XtAppCreateShell</a>(3), <a HREF="/docs/linux/man/3-xtcreatepopupshell/">XtCreatePopupShell</a>(3) 
 <i>X Toolkit Intrinsics - C Language Interface</i> 
 <i>Xlib - C Language X Interface</i>
