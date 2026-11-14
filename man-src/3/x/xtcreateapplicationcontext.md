---
title: "xtcreateapplicationcontext(3)"
name: "xtcreateapplicationcontext"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtcreateapplicationcontext/"
description: "XtCreateApplicationContext, XtDestroyApplicationContext, XtWidgetToApplicationContext, XtToolkitInitialize – create, destroy, and obtain an application context"
---

<p>XtCreateApplicationContext, XtDestroyApplicationContext, XtWidgetToApplicationContext, XtToolkitInitialize &#8211; create, destroy, and obtain an application context </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XtAppContext XtCreateApplicationContext(void);</p>
<dd>void XtDestroyApplicationContext(XtAppContext <i>app_context</i>);</p>
<dd>XtAppContext XtWidgetToApplicationContext(Widget <i>w</i>);</p>
<dd>void XtToolkitInitialize(void);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>app_context</i></p>
<dd>Specifies the application context.</p>
<dt><i>w</i></p>
<dd>Specifies the widget that you want the application context for.</dl>
<h2>Description</h2>
<p>The <code>XtCreateApplicationContext</code> function returns an application context, which is an opaque type. Every application must have at least one application context. </p>
<p> The <code>XtDestroyApplicationContext</code> function destroys the specified application context as soon as it is safe to do so. If called from with an event dispatch (for example, a callback procedure), <code>XtDestroyApplicationContext</code> does not destroy the application context until the dispatch is complete. </p>
<p> The <code>XtWidgetToApplicationContext</code> function returns the application context for the specified widget. </p>
<p> The <code>XtToolkitInitialize</code> function initializes the Intrinsics internals. If <code>XtToolkitInitialize</code> was previously called it returns immediately. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtdisplayinitialize/">XtDisplayInitialize</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
