---
title: "xtlasteventprocessed(3)"
name: "xtlasteventprocessed"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtlasteventprocessed/"
description: "XtLastEventProcessed, XtLastTimestampProcessed – last event, last timestamp processed"
---

<p>XtLastEventProcessed, XtLastTimestampProcessed &#8211; last event, last timestamp processed </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XEvent* XtLastEventProcessed(Display* <i>display</i>);</p>
<dd>Time XtLastTimestampProcessed(Display* <i>display</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the open display connection.</dl>
<h2>Description</h2>
<p><code>XtLastEventProcessed</code> returns the last event passed to <code>XtDispatchEvent</code> for the specified display and NULL if there has been no event. The client must not modify the contents of the returned event. </p>
<p> <code>XtLastTimestampProcessed</code> returns the timestamp of the last <code>KeyPress</code>, <code>KeyRelease</code>, <code>ButtonPress</code>, <code>ButtonRelease</code>, <code>MotionNotify</code>, <code>EnterNotify</code>, <code>LeaveNotify</code>, <code>PropertyNotify</code>, or <code>SelectionClear</code> event that has been passed to <code>XtDispatchEvent</code> for the specified display and zero if there has been no such event.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
