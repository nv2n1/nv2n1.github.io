---
title: "xtcallacceptfocus(3)"
name: "xtcallacceptfocus"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtcallacceptfocus/"
description: "XtCallAcceptFocus – calla widget’s accept_focus procedure"
---

<p>XtCallAcceptFocus &#8211; calla widget&#8217;s accept_focus procedure </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>Boolean XtCallAcceptFocus(Widget <i>w</i>, Time *<i>time</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>time</i></p>
<dd>Specifies the X time of the event that is causing the accept focus.</p>
<dt><i>w</i></p>
<dd>Specifies the widget.</dl>
<h2>Description</h2>
<p>The <code>XtCallAcceptFocus</code> function calls the specified widget&#8217;s accept_focus procedure, passing it the specified widget and time, and returns what the accept_focus procedure returns. If accept_focus is NULL, <code>XtCallAcceptFocus</code> returns <code>False</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtsetkeyboardfocus/">XtSetKeyboardFocus</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
