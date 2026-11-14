---
title: "xtunregisterdrawable(3)"
name: "xtunregisterdrawable"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtunregisterdrawable/"
description: "XtRegisterDrawable – register a drawable with the Intrinsics event dispatcher"
---

<p>XtRegisterDrawable &#8211; register a drawable with the Intrinsics event dispatcher </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtRegisterDrawable(Display* <i>display</i>, Drawable <i>drawable</i>, Widget <i>widget</i>);</p>
<dd>void XtUnregisterDrawable(Display* <i>display</i>, Drawable <i>drawable</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the drawable&#8217;s display.</p>
<dt><i>drawable</i></p>
<dd>Specifies the drawable to register.</p>
<dt><i>widget</i></p>
<dd>Specifies the widget to register the drawable for.</dl>
<h2>Description</h2>
<p><code>XtRegisterDrawable</code> associates the specified drawable with the specified widget so that future calls to <code>XtWindowToWidget</code> with the drawable will return the widget. The default event dispatcher will dispatch future core events that arrive with the drawable to the widget as though the event contained the widget&#8217;s window, but the event itself will not be changed in any way when being passed to even handler or action procedures. </p>
<p> If the drawable is already registered with another widget, or if the drawable is the window of a widget in the client&#8217;s widget tree, the results of calling <code>XtRegisterDrawable</code> are undefined. </p>
<p> <code>XtUnregisterDrawable</code> removes an association created with <code>XtRegisterDrawable</code>. If the drawable is the window of a widget in the client&#8217;s widget tree the results of calling <code>XtUnregisterDrawable</code> are undefined.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
