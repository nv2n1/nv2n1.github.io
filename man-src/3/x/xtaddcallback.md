---
title: "xtaddcallback(3)"
name: "xtaddcallback"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtaddcallback/"
description: "XtAddCallback, XtAddCallbacks, XtRemoveCallback, XtRemoveCallbacks, XtRemoveAllCallbacks – add and remove callback procedures"
---

<p>XtAddCallback, XtAddCallbacks, XtRemoveCallback, XtRemoveCallbacks, XtRemoveAllCallbacks &#8211; add and remove callback procedures </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtAddCallback(Widget <i>w</i>, const char *<i>callback_name</i>, XtCallbackProc <i>callback</i>, XtPointer <i>client_data</i>);</dd>
<dd>void XtAddCallbacks(Widget <i>w</i>, const char *<i>callback_name</i>, XtCallbackList <i>callbacks</i>);</dd>
<dd>void XtRemoveCallback(Widget <i>w</i>, const char *<i>callback_name</i>, XtCallbackProc <i>callback</i>, XtPointer <i>client_data</i>);</dd>
<dd>void XtRemoveCallbacks(Widget <i>w</i>, const char *<i>callback_name</i>, XtCallbackList <i>callbacks</i>);</dd>
<dd>void XtRemoveAllCallbacks(Widget <i>w</i>, const char *<i>callback_name</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>callback</i></dt>
<dd>Specifies the callback procedure.</dd>
<dt><i>callbacks</i></dt>
<dd>Specifies the null-terminated list of callback procedures and corresponding client data.</dd>
<dt><i>callback_name</i></dt>
<dd>Specifies the callback list to which the procedure is to be appended or deleted.</dd>
<dt><i>client_data</i></dt>
<dd>Specifies the argument that is to be passed to the specified procedure when it is invoked by XtCallbacks or NULL, or the client data to match on the registered callback procedures.</dd>
<dt><i>w</i></dt>
<dd>Specifies the widget.</dd></dl>
<h2>Description</h2>
<p>The <code>XtAddCallback</code> function adds the specified callback procedure to the specified widget&#8217;s callback list. </p>
<p> The <code>XtAddCallbacks</code> add the specified list of callbacks to the specified widget&#8217;s callback list. </p>
<p> The <code>XtRemoveCallback</code> function removes a callback only if both the procedure and the client data match. </p>
<p> The <code>XtRemoveCallbacks</code> function removes the specified callback procedures from the specified widget&#8217;s callback list. </p>
<p> The <code>XtRemoveAllCallbacks</code> function removes all the callback procedures from the specified widget&#8217;s callback list.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtcallcallbacks/">XtCallCallbacks</a>(3)<br/>
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br/>
 <i>Xlib &#8211; C Language X Interface</i></p>
