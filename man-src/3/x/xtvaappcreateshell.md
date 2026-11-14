---
title: "xtvaappcreateshell(3)"
name: "xtvaappcreateshell"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtvaappcreateshell/"
description: "XtAppCreateShell, XtVaAppCreateShell – create top-level widget instance"
---

<p>XtAppCreateShell, XtVaAppCreateShell &#8211; create top-level widget instance </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>Widget XtAppCreateShell(const char *<i>application_name</i>, const char *<i>application_class</i>, WidgetClass <i>widget_class</i>, Display *<i>display</i>, ArgList <i>args</i>, Cardinal <i>num_args</i>);</p>
<dd>Widget XtVaAppCreateShell(const char * <i>application_name</i>, const char * <i>application_class</i>, WidgetClass <i>widget_class</i>, Display *<i>display</i>, &#8230;);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>application_name</i></p>
<dd>Specifies the name of the application instance.</p>
<dt><i>application_class</i></p>
<dd>Specifies the class name of this application, which usually is the generic name for all instances of this application.</p>
<dt><i>widget_class</i></p>
<dd>Specifies the widget class that the application top-level widget should be.</p>
<dt><i>display</i></p>
<dd>Specifies the display from which to get the resources.</p>
<dt><i>args</i></p>
<dd>Specifies the argument list from which to get the resources.</p>
<dt><i>num_args</i></p>
<dd>Specifies the number of arguments in the argument list.</p>
<dt><i>&#8230;</i></p>
<dd>Specifies the variable argument list from which to get the resources.</dl>
<h2>Description</h2>
<p>The <code>XtAppCreateShell</code> function saves the specified application name and application class for qualifying all widget resource specifiers. The application name and application class are used as the left-most components in all widget resource names for this application. <code>XtAppCreateShell</code> should be used to create a new logical application within a program or to create a shell on another display. In the first case, it allows the specification of a new root in the resource hierarchy. In the second case, it uses the resource database associated with the other display. </p>
<p> Note that the widget returned by <code>XtAppCreateShell</code> has the <font SIZE="-1">WM_COMMAND</font> property set for session managers (see Chapter 4).</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtcreatewidget/">XtCreateWidget</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
