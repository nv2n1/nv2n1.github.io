---
title: "xtmakegeometryrequest(3)"
name: "xtmakegeometryrequest"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtmakegeometryrequest/"
description: "XtMakeGeometryRequest, XtMakeResizeRequest – make geometry manager request"
---

<p>XtMakeGeometryRequest, XtMakeResizeRequest &#8211; make geometry manager request </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>XtGeometryResult XtMakeGeometryRequest(Widget <i>w</i>, XtWidgetGeometry *<i>request</i>, XtWidgetGeometry *<i>reply_return</i>);</p>
<dd>XtGeometryResult XtMakeResizeRequest(Widget <i>w</i>, Dimension <i>width</i>, Dimension <i>height</i>, Dimension *<i>width_return</i>, Dimension *<i>height_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>reply_return</i></p>
<dd>Returns the allowed widget size or may be NULL if the requesting widget is not interested in handling <code>XtGeometryAlmost</code>.</p>
<dt><i>request</i></p>
<dd>Specifies the desired widget geometry (size, position, border width, and stacking order).</p>
<dt><i>w</i></p>
<dd>Specifies the widget that is making the request.</p>
<dt><i>width_return</i></p>
<dd>
<dt><i>height_return</i></p>
<dd>Return the allowed widget width and height.</dl>
<h2>Description</h2>
<p>Depending on the condition, <code>XtMakeGeometryRequest</code> performs the following:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>If the widget is unmanaged or the widget&#8217;s parent is not realized, it makes the changes and returns <code>XtGeometryYes</code>.</p>
<dt>&bull;</p>
<dd>If the parent is not a subclass of <code>compositeWidgetClass</code> or the parent&#8217;s geometry_manager is NULL, it issues an error.</p>
<dt>&bull;</p>
<dd>If the widget&#8217;s being_destroyed field is <code>True</code>, it returns <code>XtGeometryNo</code>.</p>
<dt>&bull;</p>
<dd>If the widget x, y, width, height and border_width fields are all equal to the requested values, it returns <code>XtGeometryYes</code>; otherwise, it calls the parent&#8217;s geometry_manager procedure with the given parameters.</p>
<dt>&bull;</p>
<dd>If the parent&#8217;s geometry manager returns <code>XtGeometryYes</code> and if <code>XtCWQueryOnly</code> is not set in the request_mode and if the widget is realized, <code>XtMakeGeometryRequest</code> calls the <code>XConfigureWindow</code> Xlib function to reconfigure the widget&#8217;s window (set its size, location, and stacking order as appropriate).</p>
<dt>&bull;</p>
<dd>If the geometry manager returns <code>XtGeometryDone</code>, the change has been approved and actually has been done. In this case, <code>XtMakeGeometryRequest</code> does no configuring and returns <code>XtGeometryYes</code>. <code>XtMakeGeometryRequest</code> never returns <code>XtGeometryDone</code>.</dl>
<p> Otherwise, <code>XtMakeGeometryRequest</code> returns the resulting value from the parent&#8217;s geometry manager. </p>
<p> Children of primitive widgets are always unmanaged; thus, <code>XtMakeGeometryRequest</code> always returns <code>XtGeometryYes</code> when called by a child of a primitive widget. </p>
<p> The <code>XtMakeResizeRequest</code> function, a simple interface to <code>XtMakeGeometryRequest</code>, creates a <code>XtWidgetGeometry</code> structure and specifies that width and height should change. The geometry manager is free to modify any of the other window attributes (position or stacking order) to satisfy the resize request. If the return value is <code>XtGeometryAlmost</code>, width_return and height_return contain a compromise width and height. If these are acceptable, the widget should immediately make an <code>XtMakeResizeRequest</code> and request that the compromise width and height be applied. If the widget is not interested in <code>XtGeometryAlmost</code> replies, it can pass NULL for width_return and height_return.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xtconfigurewidget/">XtConfigureWidget</a>(3), <a href="/docs/linux/man/3-xtquerygeometery/">XtQueryGeometery</a>(3)<br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
