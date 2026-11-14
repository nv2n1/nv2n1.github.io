---
title: "xcopyarea(3)"
name: "xcopyarea"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcopyarea/"
description: "XCopyArea, XCopyPlane – copy areas"
---

<p>XCopyArea, XCopyPlane &#8211; copy areas </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XCopyArea(Display *<i>display</i>, Drawable <i>src</i>, Drawable <i>dest</i>, GC <i>gc</i>, int <i>src_x</i>, int <i>src_y</i>, unsigned int <i>width</i>, unsigned <i>height</i>, int <i>dest_x</i>, int <i>dest_y</i>);</p>
<dd>int XCopyPlane(Display *<i>display</i>, Drawable <i>src</i>, Drawable <i>dest</i>, GC <i>gc</i>, int <i>src_x</i>, int <i>src_y</i>, unsigned <i>width</i>, int <i>height</i>, int <i>dest_x</i>, int <i>dest_y</i>, unsigned long <i>plane</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dest_x</i></p>
<dd>
<dt><i>dest_y</i></p>
<dd>Specify the x and y coordinates, which are relative to the origin of the destination rectangle and specify its upper-left corner.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</p>
<dt><i>plane</i></p>
<dd>Specifies the bit plane. You must set exactly one bit to 1.</p>
<dt><i>src</i></p>
<dd>
<dt><i>dest</i></p>
<dd>Specify the source and destination rectangles to be combined.</p>
<dt><i>src_x</i></p>
<dd>
<dt><i>src_y</i></p>
<dd>Specify the x and y coordinates, which are relative to the origin of the source rectangle and specify its upper-left corner.</p>
<dt><i>width</i></p>
<dd>
<dt><i>height</i></p>
<dd>Specify the width and height, which are the dimensions of both the source and destination rectangles.</dl>
<h2>Description</h2>
<p>The <code>XCopyArea</code> function combines the specified rectangle of src with the specified rectangle of dest. The drawables must have the same root and depth, or a <code>BadMatch</code> error results. </p>
<p> If regions of the source rectangle are obscured and have not been retained in backing store or if regions outside the boundaries of the source drawable are specified, those regions are not copied. Instead, the following occurs on all corresponding destination regions that are either visible or are retained in backing store. If the destination is a window with a background other than <code>None</code>, corresponding regions of the destination are tiled with that background (with plane-mask of all ones and <code>GXcopy</code> function). Regardless of tiling or whether the destination is a window or a pixmap, if graphics-exposures is <code>True</code>, then <code>GraphicsExpose</code> events for all corresponding destination regions are generated. If graphics-exposures is <code>True</code> but no <code>GraphicsExpose</code> events are generated, a <code>NoExpose</code> event is generated. Note that by default graphics-exposures is <code>True</code> in new GCs. </p>
<p> This function uses these GC components: function, plane-mask, subwindow-mode, graphics-exposures, clip-x-origin, clip-y-origin, and clip-mask. </p>
<p> <code>XCopyArea</code> can generate <code>BadDrawable</code>, <code>BadGC</code>, and <code>BadMatch</code> errors. </p>
<p> The <code>XCopyPlane</code> function uses a single bit plane of the specified source rectangle combined with the specified GC to modify the specified rectangle of dest. The drawables must have the same root but need not have the same depth. If the drawables do not have the same root, a <code>BadMatch</code> error results. If plane does not have exactly one bit set to 1 and the value of plane is not less than %2 sup n%, where <i>n</i> is the depth of src, a <code>BadValue</code> error results. </p>
<p> Effectively, <code>XCopyPlane</code> forms a pixmap of the same depth as the rectangle of dest and with a size specified by the source region. It uses the foreground/background pixels in the GC (foreground everywhere the bit plane in src contains a bit set to 1, background everywhere the bit plane in src contains a bit set to 0) and the equivalent of a <code>CopyArea</code> protocol request is performed with all the same exposure semantics. This can also be thought of as using the specified region of the source bit plane as a stipple with a fill-style of <code>FillOpaqueStippled</code> for filling a rectangular area of the destination. </p>
<p> This function uses these GC components: function, plane-mask, foreground, background, subwindow-mode, graphics-exposures, clip-x-origin, clip-y-origin, and clip-mask. </p>
<p> <code>XCopyPlane</code> can generate <code>BadDrawable</code>, <code>BadGC</code>, <code>BadMatch</code>, and <code>BadValue</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadDrawable</code></p>
<dd>A value for a Drawable argument does not name a defined Window or Pixmap.</p>
<dt><code>BadGC</code></p>
<dd>A value for a GContext argument does not name a defined GContext.</p>
<dt><code>BadMatch</code></p>
<dd>An <code>InputOnly</code> window is used as a Drawable.</p>
<dt><code>BadMatch</code></p>
<dd>Some argument or pair of arguments has the correct type and range but fails to match in some other way required by the request.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcleararea/">XClearArea</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
