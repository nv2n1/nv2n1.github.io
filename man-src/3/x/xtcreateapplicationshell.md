---
title: "xtcreateapplicationshell(3)"
name: "xtcreateapplicationshell"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtcreateapplicationshell/"
description: "XtCreateApplicationShell – create top-level widget instance"
---

<p>XtCreateApplicationShell &#8211; create top-level widget instance </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>Widget XtCreateApplicationShell(const char *<i>name</i>, WidgetClass <i>widget_class</i>, ArgList <i>args</i>, Cardinal <i>num_args</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>name</i></p>
<dd>Specifies the name of the shell.</p>
<dt><i>args</i></p>
<dd>Specifies the argument list to override any other resource specifications.</p>
<dt><i>num_args</i></p>
<dd>Specifies the number of arguments in the argument list.</dl>
<h2>Description</h2>
<p>The procedure <code>XtCreateApplicationShell</code> calls <code>XtAppCreateShell</code> with the <i>application</i> NULL, the application class passed to <code>XtInitialize</code>, and the default application context created by <code>XtInitialize</code>. This routine has been replaced by <code>XtAppCreateShell</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappcreateshell/">XtAppCreateShell</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
