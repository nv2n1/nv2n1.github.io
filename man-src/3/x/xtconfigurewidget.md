---
title: "xtconfigurewidget(3)"
name: "xtconfigurewidget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtconfigurewidget/"
description: "XtConfigureWidget, XtMoveWidget, XtResizeWidget – move and resize widgets"
---

<p>XtConfigureWidget, XtMoveWidget, XtResizeWidget &#8211; move and resize widgets </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtConfigureWidget(Widget <i>w</i>, Position <i>x</i>, Position <i>y</i>, Dimension <i>width</i>, Dimension <i>height</i>, Dimension <i>border_width</i>);</p>
<dd>void XtMoveWidget(Widget <i>w</i>, Position <i>x</i>, Position <i>y</i>);</p>
<dd>void XtResizeWidget(Widget <i>w</i>, Dimension <i>width</i>, Dimension <i>height</i>, Dimension <i>border_width</i>);</p>
<dd>void XtResizeWindow(Widget <i>w</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>width</i></p>
<dd>
<dt><i>height</i></p>
<dd>
<dt><i>border_width</i></p>
<dd>Specify the new widget size.</p>
<dt><i>w</i></p>
<dd>Specifies the widget.</p>
<dt><i>x</i></p>
<dd>
<dt><i>y</i></p>
<dd>Specify the new widget x and y coordinates.</dl>
<h2>Description</h2>
<p>The <code>XtConfigureWidget</code> function returns immediately if the specified geometry fields are the same as the old values. Otherwise, <code>XtConfigureWidget</code> writes the new x, y, width, height, and border_width values into the widget and, if the widget is realized, makes an Xlib <code>XConfigureWindow</code> call on the widget&#8217;s window. </p>
<p> If either the new width or height is different from its old value, <code>XtConfigureWidget</code> calls the widget&#8217;s resize procedure to notify it of the size change; otherwise, it simply returns. </p>
<p> The <code>XtMoveWidget</code> function returns immediately if the specified geometry fields are the same as the old values. Otherwise, <code>XtMoveWidget</code> writes the new x and y values into the widget and, if the widget is realized, issues an Xlib <code>XMoveWindow</code> call on the widget&#8217;s window. </p>
<p> The <code>XtResizeWidget</code> function returns immediately if the specified geometry fields are the same as the old values. Otherwise, <code>XtResizeWidget</code> writes the new width, height, and border_width values into the widget and, if the widget is realized, issues an <code>XConfigureWindow</code> call on the widget&#8217;s window. </p>
<p> If the new width or height are different from the old values, <code>XtResizeWidget</code> calls the widget&#8217;s resize procedure to notify it of the size change. </p>
<p> The <code>XtResizeWindow</code> function calls the <code>XConfigureWindow</code> Xlib function to make the window of the specified widget match its width, height, and border width. This request is done unconditionally because there is no way to tell if these values match the current values. Note that the widget&#8217;s resize procedure is not called. </p>
<p> There are very few times to use <code>XtResizeWindow</code>; instead, you should use <code>XtResizeWidget</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtmakegeometryrequest/">XtMakeGeometryRequest</a>(3), <a href="/docs/linux/man/3-xtquerygeometry/">XtQueryGeometry</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
