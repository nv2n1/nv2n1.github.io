---
title: "xsetclipmask(3)"
name: "xsetclipmask"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetclipmask/"
description: "XSetClipOrigin, XSetClipMask, XSetClipRectangles – GC convenience routines"
---

<p>XSetClipOrigin, XSetClipMask, XSetClipRectangles &#8211; GC convenience routines </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XSetClipOrigin(Display *<i>display</i>, GC <i>gc</i>, int <i>clip_x_origin</i>, int <i>clip_y_origin</i>);</p>
<dd>int XSetClipMask(Display *<i>display</i>, GC <i>gc</i>, Pixmap <i>pixmap</i>);</p>
<dd>int XSetClipRectangles(Display *<i>display</i>, GC <i>gc</i>, int <i>clip_x_origin</i>, int <i>clip_y_origin</i>, XRectangle <i>rectangles</i>[], int <i>n</i>, int <i>ordering</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>clip_x_origin</i></p>
<dd>
<dt><i>clip_y_origin</i></p>
<dd>Specify the x and y coordinates of the clip-mask origin.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</p>
<dt><i>n</i></p>
<dd>Specifies the number of rectangles.</p>
<dt><i>ordering</i></p>
<dd>Specifies the ordering relations on the rectangles. You can pass <code>Unsorted</code>, <code>YSorted</code>, <code>YXSorted</code>, or <code>YXBanded</code>.</p>
<dt><i>pixmap</i></p>
<dd>Specifies the pixmap or <code>None</code>.</p>
<dt><i>rectangles</i></p>
<dd>Specifies an array of rectangles that define the clip-mask.</dl>
<h2>Description</h2>
<p>The <code>XSetClipOrigin</code> function sets the clip origin in the specified GC. The clip-mask origin is interpreted relative to the origin of whatever destination drawable is specified in the graphics request. </p>
<p> <code>XSetClipOrigin</code> can generate <code>BadAlloc</code> and <code>BadGC</code> errors. </p>
<p> The <code>XSetClipMask</code> function sets the clip-mask in the specified GC to the specified pixmap. If the clip-mask is set to <code>None</code>, the pixels are are always drawn (regardless of the clip-origin). </p>
<p> <code>XSetClipMask</code> can generate <code>BadAlloc</code>, <code>BadGC</code>, <code>BadMatch</code>, and <code>BadValue</code> errors. </p>
<p> The <code>XSetClipRectangles</code> function changes the clip-mask in the specified GC to the specified list of rectangles and sets the clip origin. The output is clipped to remain contained within the rectangles. The clip-origin is interpreted relative to the origin of whatever destination drawable is specified in a graphics request. The rectangle coordinates are interpreted relative to the clip-origin. The rectangles should be nonintersecting, or the graphics results will be undefined. Note that the list of rectangles can be empty, which effectively disables output. This is the opposite of passing <code>None</code> as the clip-mask in <code>XCreateGC</code>, <code>XChangeGC</code>, and <code>XSetClipMask</code>. </p>
<p> If known by the client, ordering relations on the rectangles can be specified with the ordering argument. This may provide faster operation by the server. If an incorrect ordering is specified, the X server may generate a <code>BadMatch</code> error, but it is not required to do so. If no error is generated, the graphics results are undefined. <code>Unsorted</code> means the rectangles are in arbitrary order. <code>YSorted</code> means that the rectangles are nondecreasing in their Y origin. <code>YXSorted</code> additionally constrains <code>YSorted</code> order in that all rectangles with an equal Y origin are nondecreasing in their X origin. <code>YXBanded</code> additionally constrains <code>YXSorted</code> by requiring that, for every possible Y scanline, all rectangles that include that scanline have an identical Y origins and Y extents. </p>
<p> <code>XSetClipRectangles</code> can generate <code>BadAlloc</code>, <code>BadGC</code>, <code>BadMatch</code>, and <code>BadValue</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadGC</code></p>
<dd>A value for a GContext argument does not name a defined GContext.</p>
<dt><code>BadMatch</code></p>
<dd>Some argument or pair of arguments has the correct type and range but fails to match in some other way required by the request.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreategc/">XCreateGC</a>(3), <a href="/docs/linux/man/3-xdrawrectangle/">XDrawRectangle</a>(3), <a href="/docs/linux/man/3-xquerybestsize/">XQueryBestSize</a>(3), <a href="/docs/linux/man/3-xsetarcmode/">XSetArcMode</a>(3), <a href="/docs/linux/man/3-xsetfillstyle/">XSetFillStyle</a>(3), <a href="/docs/linux/man/3-xsetfont/">XSetFont</a>(3), <a href="/docs/linux/man/3-xsetlineattributes/">XSetLineAttributes</a>(3), <a href="/docs/linux/man/3-xsetstate/">XSetState</a>(3), <a href="/docs/linux/man/3-xsettile/">XSetTile</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
