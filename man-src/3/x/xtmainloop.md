---
title: "xtmainloop(3)"
name: "xtmainloop"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtmainloop/"
description: "XtNextEvent, XtPending, XtPeekEvent, XtProcessEvent, XtMainLoop – query and process events and input"
---

<p>XtNextEvent, XtPending, XtPeekEvent, XtProcessEvent, XtMainLoop &#8211; query and process events and input </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtNextEvent(XEvent *<i>event_return</i>);</p>
<dd>Boolean XtPeekEvent(XEvent *<i>event_return</i>);</p>
<dd>Boolean XtPending(void);</p>
<dd>void XtProcessEvent(XtInputMask <i>mask</i>);</p>
<dd>void XtMainLoop(void);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>event</i></p>
<dd>Specifies a pointer to the event structure that is to be dispatched to the appropriate event handler.</p>
<dt><i>event_return</i></p>
<dd>Returns the event information to the specified event structure.</p>
<dt><i>mask</i></p>
<dd>Specifies what types of events to process. The mask is the bitwise inclusive OR of any combination of <code>XtIMXEvent</code>, <code>XtIMTimer</code>, <code>XtIMAlternateInput</code>, and <code>XtIMSignal</code>. As a convenience, the X Toolkit defines the symbolic name <code>XtIMAll</code> to be the bitwise inclusive OR of all event types.</dl>
<h2>Description</h2>
<p><code>XtNextEvent</code> has been replaced by <code>XtAppNextEvent</code>. </p>
<p> <code>XtPeekEvent</code> has been replaced by <code>XtAppPeekEvent</code>. </p>
<p> <code>XtPending</code> has been replaced by <code>XtAppPending</code>. </p>
<p> <code>XtProcessEvent</code> has been replaced by <code>XtAppProcessEvent</code>. </p>
<p> <code>XtMainLoop</code> has been replaced by <code>XtAppMainLoop</code>.</p>
<h2>See Also</h2>
<p>XtAppNextEvent(3xt), <a href="/docs/linux/man/3-xtapppending/">XtAppPending</a>(3), <a href="/docs/linux/man/3-xtapppeekevent/">XtAppPeekEvent</a>(3), <a href="/docs/linux/man/3-xtappprocessevent/">XtAppProcessEvent</a>(3), <a href="/docs/linux/man/3-xtappmainloop/">XtAppMainLoop</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
