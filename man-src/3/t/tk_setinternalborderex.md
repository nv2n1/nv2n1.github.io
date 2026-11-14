---
title: "tk_setinternalborderex(3)"
name: "tk_setinternalborderex"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_setinternalborderex/"
description: "Tk_GeometryRequest, Tk_SetMinimumRequestSize, Tk_SetInternalBorder, Tk_SetInternalBorderEx – specify desired geometry or internal border for a window"
---

<p>Tk_GeometryRequest, Tk_SetMinimumRequestSize, Tk_SetInternalBorder, Tk_SetInternalBorderEx &#8211; specify desired geometry or internal border for a window </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
<code>Tk_GeometryRequest</code>(<i>tkwin, reqWidth, reqHeight</i>)
<code>Tk_SetMinimumRequestSize</code>(<i>tkwin, minWidth, minHeight</i>)
<code>Tk_SetInternalBorder</code>(<i>tkwin, width</i>)
<code>Tk_SetInternalBorderEx</code>(<i>tkwin, left, right, top, bottom</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Window <i>tkwin</i> (in) Window for which geometry is being requested.</p>
<dd>int <i>reqWidth</i> (in) Desired width for <i>tkwin</i>, in pixel units.</p>
<dd>int <i>reqHeight</i> (in) Desired height for <i>tkwin</i>, in pixel units.</p>
<dd>int <i>minWidth</i> (in) Desired minimum requested width for <i>tkwin</i>, in pixel units.</p>
<dd>int <i>minHeight</i> (in) Desired minimum requested height for <i>tkwin</i>, in pixel units.</p>
<dd>int <i>width</i> (in) Space to leave for internal border for <i>tkwin</i>, in pixel units.</p>
<dd>int <i>left</i> (in) Space to leave for left side of internal border for <i>tkwin</i>, in pixel units.</p>
<dd>int <i>right</i> (in) Space to leave for right side of internal border for <i>tkwin</i>, in pixel units.</p>
<dd>int <i>top</i> (in) Space to leave for top side of internal border for <i>tkwin</i>, in pixel units.</p>
<dd>int <i>bottom</i> (in) Space to leave for bottom side of internal border for <i>tkwin</i>, in pixel units. </p>
</dl>
<h2>Description</h2>
<p><code>Tk_GeometryRequest</code> is called by widget code to indicate its preference for the dimensions of a particular window. The arguments to <code>Tk_GeometryRequest</code> are made available to the geometry manager for the window, which then decides on the actual geometry for the window. Although geometry managers generally try to satisfy requests made to <code>Tk_GeometryRequest</code>, there is no guarantee that this will always be possible. Widget code should not assume that a geometry request will be satisfied until it receives a <code>ConfigureNotify</code> event indicating that the geometry change has occurred. Widget code should never call procedures like <code>Tk_ResizeWindow</code> directly. Instead, it should invoke <code>Tk_GeometryRequest</code> and leave the final geometry decisions to the geometry manager. </p>
<p> If <i>tkwin</i> is a top-level window, then the geometry information will be passed to the window manager using the standard ICCCM protocol. </p>
<p> <code>Tk_SetInternalBorder</code> is called by widget code to indicate that the widget has an internal border. This means that the widget draws a decorative border inside the window instead of using the standard X borders, which are external to the window&#8217;s area. For example, internal borders are used to draw 3-D effects. <i>Width</i> specifies the width of the border in pixels. Geometry managers will use this information to avoid placing any children of <i>tkwin</i> overlapping the outermost <i>width</i> pixels of <i>tkwin</i>&#8216;s area. </p>
<p> <code>Tk_SetInternalBorderEx</code> works like <code>Tk_SetInternalBorder</code> but lets you specify different widths for different sides of the window. </p>
<p> <code>Tk_SetMinimumRequestSize</code> is called by widget code to indicate that a geometry manager should request at least this size for the widget. This allows a widget to have some control over its size when a propagating geometry manager is used inside it. </p>
<p> The information specified in calls to <code>Tk_GeometryRequest</code>, <code>Tk_SetMinimumRequestSize</code>, <code>Tk_SetInternalBorder</code> and <code>Tk_SetInternalBorderEx</code> can be retrieved using the macros <code>Tk_ReqWidth</code>, <code>Tk_ReqHeight</code>, <code>Tk_MinReqWidth</code>, <code>Tk_MinReqHeight</code>, <code>Tk_MinReqWidth</code>, <code>Tk_InternalBorderLeft</code>, <code>Tk_InternalBorderRight</code>, <code>Tk_InternalBorderTop</code> and <code>Tk_InternalBorderBottom</code>. See the <code>Tk_WindowId</code> manual entry for details. </p>
<h2>Keywords</h2>
<p>geometry, request</p>
