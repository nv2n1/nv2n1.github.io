---
title: "xtquerygeometry(3)"
name: "xtquerygeometry"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtquerygeometry/"
description: "XtQueryGeometry – query the preferred geometry of a child widget"
---

<p>XtQueryGeometry &#8211; query the preferred geometry of a child widget </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XtGeometryResult XtQueryGeometry(Widget <i>w</i>, XtWidgetGeometry *<i>intended</i>, XtWidgetGeometry *<i>preferred_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>intended</i></p>
<dd>Specifies any changes the parent plans to make to the child&#8217;s geometry or NULL.</p>
<dt><i>preferred_return</i></p>
<dd>Returns the child widget&#8217;s preferred geometry.</p>
<dt><i>w</i></p>
<dd>Specifies the widget.</dl>
<h2>Description</h2>
<p>To discover a child&#8217;s preferred geometry, the child&#8217;s parent sets any changes that it intends to make to the child&#8217;s geometry in the corresponding fields of the intended structure, sets the corresponding bits in intended.request_mode, and calls <code>XtQueryGeometry</code>. </p>
<p> <code>XtQueryGeometry</code> clears all bits in the preferred_return-&gt;request_mode and checks the query_geometry field of the specified widget&#8217;s class record. If query_geometry is not NULL, <code>XtQueryGeometry</code> calls the query_geometry procedure and passes as arguments the specified widget, intended, and preferred_return structures. If the intended argument is NULL, <code>XtQueryGeometry</code> replaces it with a pointer to an <code>XtWidgetGeometry</code> structure with request_mode=0 before calling query_geometry.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtconfigurewidget/">XtConfigureWidget</a>(3), <a href="/docs/linux/man/3-xtmakegeometryrequest/">XtMakeGeometryRequest</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
