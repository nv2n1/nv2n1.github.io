---
title: "xtunmapwidget(3)"
name: "xtunmapwidget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtunmapwidget/"
description: "XtMapWidget, XtSetMappedWhenManaged, XtUnmapWidget – map and unmap widgets"
---

<p>XtMapWidget, XtSetMappedWhenManaged, XtUnmapWidget &#8211; map and unmap widgets </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>void XtMapWidget(Widget <i>w</i>);</p>
<dd>void XtSetMappedWhenManaged(Widget <i>w</i>, Boolean <i>map_when_managed</i>);</p>
<dd>void XtUnmapWidget(Widget <i>w</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>map_when_managed</i></p>
<dd>Specifies a Boolean value that indicates the new value of the map_when_managed field.</p>
<dt><i>w</i></p>
<dd>Specifies the widget.</dl>
<h2>Description</h2>
<p>If the widget is realized and managed and if the new value of map_when_managed is <code>True</code>, <code>XtSetMappedWhenManaged</code> maps the window. If the widget is realized and managed and if the new value of map_when_managed is <code>False</code>, it unmaps the window. <code>XtSetMappedWhenManaged</code> is a convenience function that is equivalent to (but slightly faster than) calling <code>XtSetValues</code> and setting the new value for the mappedWhenManaged resource. As an alternative to using <code>XtSetMappedWhenManaged</code> to control mapping, a client may set mapped_when_managed to <code>False</code> and use <code>XtMapWidget</code> and <code>XtUnmapWidget</code> explicitly.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtmanagechildren/">XtManageChildren</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
