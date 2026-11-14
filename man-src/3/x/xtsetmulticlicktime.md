---
title: "xtsetmulticlicktime(3)"
name: "xtsetmulticlicktime"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtsetmulticlicktime/"
description: "XtSetMultiClickTime, XtGetMultiClickTime – set and get multi-click times"
---

<p>XtSetMultiClickTime, XtGetMultiClickTime &#8211; set and get multi-click times </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtSetMultiClickTime(Display* <i>display</i>, int <i>time</i>);</p>
<dd>int XtGetMultiClickTime(Display* <i>display</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the display connection.</p>
<dt><i>time</i></p>
<dd>Specifies the multi-click time in milliseconds.</dl>
<h2>Description</h2>
<p><code>XtSetMultiClickTime</code> sets the time interval used by the translation manager to determine when multiple events are interpreted as a repeated event. </p>
<p> <code>XtGetMultiClickTime</code> returns the time in milliseconds that the translation manager uses to determine if multiple events are to be interpreted as a repeated event for purposes of matching a translation entry containing a repeat count.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
