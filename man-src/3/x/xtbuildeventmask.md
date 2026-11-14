---
title: "xtbuildeventmask(3)"
name: "xtbuildeventmask"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtbuildeventmask/"
description: "XtBuildEventMask – retrieve a widget’s event mask"
---

<p>XtBuildEventMask &#8211; retrieve a widget&#8217;s event mask </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>EventMask XtBuildEventMask(Widget <i>w</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>w</i></p>
<dd>Specifies the widget.</dl>
<h2>Description</h2>
<p>The <code>XtBuildEventMask</code> function returns the event mask representing the logical OR of all event masks for event handlers registered on the widget with <code>XtAddEventHandler</code> and all event translations, including accelerators, installed on the widget. This is the same event mask stored into the <code>XSetWindowAttributes</code> structure by <code>XtRealizeWidget</code> and sent to the server when event handlers and translations are installed or removed on the realized widget.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtaddeventhandler/">XtAddEventHandler</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
