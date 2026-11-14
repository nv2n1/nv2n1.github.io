---
title: "xthascallbacks(3)"
name: "xthascallbacks"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xthascallbacks/"
description: "XtCallCallbacks, XtCallCallbackList, XtHasCallbacks – process callbacks"
---

<p>XtCallCallbacks, XtCallCallbackList, XtHasCallbacks &#8211; process callbacks </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtCallCallbacks(Widget <i>w</i>, const char *<i>callback_name</i>, XtPointer <i>call_data</i>);</p>
<dd>void XtCallCallbackList(Widget <i>w</i>, XtCallbackList <i>callbacks</i>, XtPointer <i>call_data</i>);</dl>
<p> typedef enum {XtCallbackNoList, XtCallbackHasNone, XtCallbackHasSome} XtCallbackStatus;</p>
<dl COMPACT>
<dd>XtCallbackStatus XtHasCallbacks(Widget <i>w</i>, const char *<i>callback_name</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>callback_name</i></p>
<dd>Specifies the callback list to be executed or checked.</p>
<dt><i>call_data</i></p>
<dd>Specifies a callback-list specific data value to pass to each of the callback procedure in the list.</p>
<dt><i>callbacks</i></p>
<dd>Specifies the callback list to be executed.</p>
<dt><i>w</i></p>
<dd>Specifies the widget.</dl>
<h2>Description</h2>
<p>The <code>XtCallCallbacks</code> function calls each procedure that is registered in the specified widget&#8217;s callback list. </p>
<p> If <i>callbacks</i> is not NULL, <code>XtCallCallbackList</code> calls each of the callback procedures in the list, passing client data and <i>call_data</i>. The <i>callbacks</i> parameter must specify the contents of a widget or object resource declared with representation type <code>XtRCallback</code>. </p>
<p> The <code>XtHasCallbacks</code> function first checks to see if the widget has a callback list identified by callback_name. If the callback list does not exist, <code>XtHasCallbacks</code> returns <code>XtCallbackNoList</code>. If the callback list exists but is empty, it returns <code>XtCallbackHasNone</code>. If the callback list exists and has at least one callback registered, it returns <code>XtCallbackHasSome</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtaddcallback/">XtAddCallback</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
