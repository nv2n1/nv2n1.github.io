---
title: "xmwidgetgetdisplayrect(3)"
name: "xmwidgetgetdisplayrect"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmwidgetgetdisplayrect/"
description: "XmWidgetGetDisplayRect — Retrieves display rectangle information for a widget"
---

<p><code>XmWidgetGetDisplayRect</code> &#8212; Retrieves display rectangle information for a widget</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmWidgetGetDisplayRect</code>(
<code>Widget widget</code>,
<code>XRectangle *displayrect</code>);</pre>
<h2>Description</h2>
<p><code>XmWidgetGetDisplayRect</code> returns the width, height and the x and y-coordinates of the upper left corner of the display rectangle of the specified widget. The display rectangle is the smallest rectangle that encloses either a string or a pixmap. </p>
<p> If the widget contains a string, the return values specify the x and y-coordinates of the upper left corner of the display rectangle relative to the origin of the widget and the width and height in pixels. </p>
<p> In the case of a pixmap, the return values specify the x and y-coordinates of the upper left corner of the pixmap relative to the origin, and the width and height of the pixmap in pixels.</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the widget ID</p>
<dt><i>displayrect</i></p>
<dd>Specifies a pointer to an XRectangle structure in which the x and y-coordinates, width and height of the display rectangle are returned</dl>
<h2>Return</h2>
<p>Returns True if the specified widget has an associated display rectangle; otherwise, returns False.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmwidgetgetbaselines/">XmWidgetGetBaselines</a></code>(3).</p>
