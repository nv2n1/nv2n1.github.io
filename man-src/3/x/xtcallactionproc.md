---
title: "xtcallactionproc(3)"
name: "xtcallactionproc"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtcallactionproc/"
description: "XtCallActionProc – invoke an action procedure directly"
---

<p>XtCallActionProc &#8211; invoke an action procedure directly </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtCallActionProc(Widget <i>widget</i>, const char *<i>action</i>, XEvent *<i>event</i>, String *<i>params</i>, Cardinal <i>num_params</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the widget in which the action is to be invoked. Must be of class core of any subclass thereof.</p>
<dt><i>action</i></p>
<dd>Specifies the name of the action routine.</p>
<dt><i>event</i></p>
<dd>Specifies the contents of the <i>event</i> passed to the action routine.</p>
<dt><i>params</i></p>
<dd>Specifies the contents of the <i>params</i> passed to the action routine.</p>
<dt><i>num_params</i></p>
<dd>Specifies the num of entries in <i>params</i>.</dl>
<h2>Description</h2>
<p><code>XtCallActionProc</code> searches for the named action routine in the same manner and order as translation tables are bound. If found, the action routine is invoked with the specified widget, event pointer, and parameters. It is the responsibility of the caller to ensure that the contents of <i>event</i>, <i>params</i>, and <i>num_params</i> arguments are appropriate for the specified routine, and if necessary, that the specified widget is realized or sensitive. If the named action routine cannot be found, <code>XtCallActionProc</code> generates a warning message and returns.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
