---
title: "xtinitializewidgetclass(3)"
name: "xtinitializewidgetclass"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtinitializewidgetclass/"
description: "XtInitializeWidgetClass – initialize a widget class"
---

<p>XtInitializeWidgetClass &#8211; initialize a widget class </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtInitializeWidgetClass(WidgetClass <i>object_class</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>object_class</i></p>
<dd>Specifies the object class to initialize.</dl>
<h2>Description</h2>
<p>If the specified widget class is already initialized, <code>XtInitializeWidgetClass</code> returns immediately. </p>
<p> If the class initialization procedure registers type converters, these type converters are not available until the first object of the class or subclass is created or <code>XtInitializeWidgetClass</code> is called.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
