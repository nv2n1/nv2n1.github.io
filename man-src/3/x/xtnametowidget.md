---
title: "xtnametowidget(3)"
name: "xtnametowidget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtnametowidget/"
description: "XtNameToWidget, XtWindowToWidget – translating strings to widgets or widgets to windows"
---

<p>XtNameToWidget, XtWindowToWidget &#8211; translating strings to widgets or widgets to windows </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>Widget XtNameToWidget(Widget <i>reference</i>, const char *<i>names</i>);</p>
<dd>Widget XtWindowToWidget(Display *<i>display</i>, Window <i>window</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the display on which the window is defined.</p>
<dt><i>names</i></p>
<dd>Specifies the fully qualified name of the desired widget.</p>
<dt><i>reference</i></p>
<dd>Specifies the widget from which the search is to start.</p>
<dt><i>window</i></p>
<dd>Specify the window for which you want the widget.</dl>
<h2>Description</h2>
<p>The <code>XtNameToWidget</code> function looks for a widget whose name is the first component in the specified names and that is a pop-up child of reference (or a normal child if reference is a subclass of <code>compositeWidgetClass</code>). It then uses that widget as the new reference and repeats the search after deleting the first component from the specified names. If it cannot find the specified widget, <code>XtNameToWidget</code> returns NULL. </p>
<p> Note that the names argument contains the name of a widget with respect to the specified reference widget and can contain more than one widget name (separated by periods) for widgets that are not direct children of the specified reference widget. </p>
<p> If more than one child of the reference widget matches the name, <code>XtNameToWidget</code> can return any of the children. The Intrinsics do not require that all children of a widget have unique names. If the specified names contain more than one component and if more than one child matches the first component, <code>XtNameToWidget</code> can return NULL if the single branch that it follows does not contain the named widget. That is, <code>XtNameToWidget</code> does not back up and follow other matching branches of the widget tree. </p>
<p> The <code>XtWindowToWidget</code> function translates the specified window and display pointer into the appropriate widget instance.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
