---
title: "xtchecksubclass(3)"
name: "xtchecksubclass"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtchecksubclass/"
description: "XtClass, XtSuperclass, XtIsSubclass, XtCheckSubclass, XtIsObject, XtIsRectObj, XtIsWidget, XtIsComposite, XtIsConstraint, XtIsShell, XtIsOverrideShell, XtIsWMShell, XtIsVendorShell, XtIsTransientSh..."
---

<p>XtClass, XtSuperclass, XtIsSubclass, XtCheckSubclass, XtIsObject, XtIsRectObj, XtIsWidget, XtIsComposite, XtIsConstraint, XtIsShell, XtIsOverrideShell, XtIsWMShell, XtIsVendorShell, XtIsTransientShell, XtIsTopLevelShell, XtIsApplicationShell, XtIsSessionShell &#8211; obtain and verify a widget&#8217;s class </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>WidgetClass XtClass(Widget <i>w</i>);</p>
<dd>WidgetClass XtSuperclass(Widget <i>w</i>);</p>
<dd>Boolean XtIsSubclass(Widget <i>w</i>, WidgetClass <i>widget_class</i>);</p>
<dd>void XtCheckSubclass(Widget <i>widget</i>, WidgetClass <i>widget_class</i>, String <i>message</i>);</p>
<dd>Boolean XtIsObject(Widget <i>w</i>);</p>
<dd>Boolean XtIsRectObj(Widget <i>w</i>);</p>
<dd>Boolean XtIsWidget(Widget <i>w</i>);</p>
<dd>Boolean XtIsComposite(Widget <i>w</i>);</p>
<dd>Boolean XtIsConstraint(Widget <i>w</i>);</p>
<dd>Boolean XtIsShell(Widget <i>w</i>);</p>
<dd>Boolean XtIsOverrideShell(Widget <i>w</i>);</p>
<dd>Boolean XtIsWMShell(Widget <i>w</i>);</p>
<dd>Boolean XtIsVendorShell(Widget <i>w</i>);</p>
<dd>Boolean XtIsTransientShell(Widget <i>w</i>);</p>
<dd>Boolean XtIsTopLevelShell(Widget <i>w</i>);</p>
<dd>Boolean XtIsApplicationShell(Widget <i>w</i>);</p>
<dd>Boolean XtIsSessionShell(Widget <i>w</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>w</i></p>
<dd>Specifies the widget.</p>
<dt><i>widget_class</i></p>
<dd>Specifies the widget class.</p>
<dt><i>message</i></p>
<dd>Specifies the message that is to be used.</dl>
<h2>Description</h2>
<p>The <code>XtClass</code> function returns a pointer to the widget&#8217;s class structure. </p>
<p> The <code>XtSuperclass</code> function returns a pointer to the widget&#8217;s superclass class structure. </p>
<p> The <code>XtIsSubclass</code> function returns <code>True</code> if the class of the specified widget is equal to or is a subclass of the specified class. The widget&#8217;s class can be any number of subclasses down the chain and need not be an immediate subclass of the specified class. Composite widgets that need to restrict the class of the items they contain can use <code>XtIsSubclass</code> to find out if a widget belongs to the desired class of objects. </p>
<p> The <code>XtCheckSubclass</code> macro determines if the class of the specified widget is equal to or is a subclass of the specified widget class. The widget can be any number of subclasses down the chain and need not be an immediate subclass of the specified widget class. If the specified widget is not a subclass, <code>XtCheckSubclass</code> constructs an error message from the supplied message, the widget&#8217;s actual class, and the expected class and calls <code>XtErrorMsg</code>. <code>XtCheckSubclass</code> should be used at the entry point of exported routines to ensure that the client has passed in a valid widget class for the exported operation. </p>
<p> <code>XtCheckSubclass</code> is only executed when the widget has been compiled with the compiler symbol DEBUG defined; otherwise, it is defined as the empty string and generates no code. </p>
<p> To test if a given widget belongs to a subclass of an Intrinsics-defined class, the Intrinsics defines macros or functions equivalent to <code>XtIsSubclass</code> for each of the built-in classes. These procedures are <code>XtIsObject</code>, <code>XtIsRectObj</code>, <code>XtIsWidget</code>, <code>XtIsComposite</code>, <code>XtIsConstraint</code>, <code>XtIsShell</code>, <code>XtIsOverrideShell</code>, <code>XtIsWMShell</code>, <code>XtIsVendorShell</code>, <code>XtIsTransientShell</code>, <code>XtIsTopLevelShell</code>, <code>XtIsApplicationShell</code>, and <code>XtIsSessionShell</code>. </p>
<p> The</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtapperrormsg/">XtAppErrorMsg</a>(3), <a href="/docs/linux/man/3-xtdisplay/">XtDisplay</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
