---
title: "xtappaddtimeout(3)"
name: "xtappaddtimeout"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtappaddtimeout/"
description: "XtAppAddTimeOut, XtRemoveTimeOut – register and remove timeouts"
---

<p>XtAppAddTimeOut, XtRemoveTimeOut &#8211; register and remove timeouts </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XtIntervalId XtAppAddTimeOut(XtAppContext <i>app_context</i>, unsigned long <i>interval</i>, XtTimerCallbackProc <i>proc</i>, XtPointer <i>client_data</i>);</p>
<dd>void XtRemoveTimeOut(XtIntervalId <i>timer</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context for which the timer is to be set.</p>
<dt><i>client_data</i></p>
<dd>Specifies the argument that is to be passed to the specified procedure when handling the callback.</p>
<dt><i>interval</i></p>
<dd>Specifies the time interval in milliseconds.</p>
<dt><i>proc</i></p>
<dd>Specifies the procedure that is to be called when time expires.</p>
<dt><i>timer</i></p>
<dd>Specifies the ID for the timeout request to be destroyed.</dl>
<h2>Description</h2>
<p>The <code>XtAppAddTimeOut</code> function creates a timeout and returns an identifier for it. The timeout value is set to interval. The callback procedure is called when the time interval elapses, and then the timeout is removed. </p>
<p> The <code>XtRemoveTimeOut</code> function removes the timeout. Note that timeouts are automatically removed once they trigger.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtappaddinput/">XtAppAddInput</a>(3),<a href="/docs/linux/man/3-xtappaddsignal/">XtAppAddSignal</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
