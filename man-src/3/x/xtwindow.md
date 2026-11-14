---
title: "xtwindow(3)"
name: "xtwindow"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtwindow/"
description: "XtDisplay, XtDisplayOfObject, XtScreen, XtScreenOfObject, XtWindow, XtWindowOfObject – obtain window information about a widget"
---

<p>XtDisplay, XtDisplayOfObject, XtScreen, XtScreenOfObject, XtWindow, XtWindowOfObject &#8211; obtain window information about a widget </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>Display *XtDisplay(Widget <i>w</i>);</p>
<dd>Display *XtDisplayOfObject(Widget <i>object</i>);</p>
<dd>Screen *XtScreen(Widget <i>w</i>);</p>
<dd>Screen *XtScreenOfObject(Widget <i>object</i>);</p>
<dd>Window XtWindow(Widget <i>w</i>);</p>
<dd>Window XtWindowOfObject(Widget <i>object</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>w</i></p>
<dd>Specifies the widget.</dl>
<dl COMPACT>
<dt><i>object</i></p>
<dd>Specifies the widget.</dl>
<h2>Description</h2>
<p><code>XtDisplay</code> returns the display pointer for the specified widget. </p>
<p> <code>XtDisplayOfObject</code> returns the display pointer for the specified object. </p>
<p> <code>XtScreen</code> returns the screen pointer for the specified widget. </p>
<p> <code>XtScreenOfObject</code> returns the screen pointer for the specified object. </p>
<p> <code>XtWindow</code> returns the window of the specified widget. </p>
<p> <code>XtWindowOfObject</code> returns the window of the specified object.</p>
<h2>See Also</h2>
<p><i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
