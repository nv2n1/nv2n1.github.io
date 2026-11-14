---
title: "xgetimage(3)"
name: "xgetimage"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xgetimage/"
description: "XPutImage, XGetImage, XGetSubImage – transfer images"
---

<p>XPutImage, XGetImage, XGetSubImage &#8211; transfer images </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XPutImage(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, XImage *<i>image</i>, int <i>src_x</i>, int <i>src_y</i>, int <i>dest_x</i>, int <i>dest_y</i>, unsigned int <i>width</i>, unsigned int <i>height</i>);</p>
<dd>XImage *XGetImage(Display *<i>display</i>, Drawable <i>d</i>, int <i>x</i>, int <i>y</i>, unsigned int <i>width</i>, unsigned int <i>height</i>, unsigned long <i>plane_mask</i>, int <i>format</i>);</p>
<dd>XImage *XGetSubImage(Display *<i>display</i>, Drawable <i>d</i>, int <i>x</i>, int <i>y</i>, unsigned int <i>width</i>, unsigned int <i>height</i>, unsigned long <i>plane_mask</i>, int <i>format</i>, XImage *<i>dest_image</i>, int <i>dest_x</i>, <i>dest_y</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>d</i></p>
<dd>Specifies the drawable.</p>
<dt><i>dest_image</i></p>
<dd>Specifies the destination image.</p>
<dt><i>dest_x</i></p>
<dd>
<dt><i>dest_y</i></p>
<dd>Specify the x and y coordinates, which are relative to the origin of the drawable and are the coordinates of the subimage or which are relative to the origin of the destination rectangle, specify its upper-left corner, and determine where the subimage is placed in the destination image.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>format</i></p>
<dd>Specifies the format for the image. You can pass <code>XYPixmap</code> or <code>ZPixmap</code>.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</p>
<dt><i>image</i></p>
<dd>Specifies the image you want combined with the rectangle.</p>
<dt><i>plane_mask</i></p>
<dd>Specifies the plane mask.</p>
<dt><i>src_x</i></p>
<dd>Specifies the offset in X from the left edge of the image defined by the <code>XImage</code> structure.</p>
<dt><i>src_y</i></p>
<dd>Specifies the offset in Y from the top edge of the image defined by the <code>XImage</code> structure.</p>
<dt><i>width</i></p>
<dd>
<dt><i>height</i></p>
<dd>Specify the width and height of the subimage, which define the dimensions of the rectangle.</p>
<dt><i>x</i></p>
<dd>
<dt><i>y</i></p>
<dd>Specify the x and y coordinates, which are relative to the origin of the drawable and define the upper-left corner of the rectangle.</dl>
<h2>Description</h2>
<p>The <code>XPutImage</code> function combines an image with a rectangle of the specified drawable. The section of the image defined by the src_x, src_y, width, and height arguments is drawn on the specified part of the drawable. If <code>XYBitmap</code> format is used, the depth of the image must be one, or a <code>BadMatch</code> error results. The foreground pixel in the GC defines the source for the one bits in the image, and the background pixel defines the source for the zero bits. For <code>XYPixmap</code> and <code>ZPixmap</code>, the depth of the image must match the depth of the drawable, or a <code>BadMatch</code> error results. </p>
<p> If the characteristics of the image (for example, byte_order and bitmap_unit) differ from what the server requires, <code>XPutImage</code> automatically makes the appropriate conversions. </p>
<p> This function uses these GC components: function, plane-mask, subwindow-mode, clip-x-origin, clip-y-origin, and clip-mask. It also uses these GC mode-dependent components: foreground and background. </p>
<p> <code>XPutImage</code> can generate <code>BadDrawable</code>, <code>BadGC</code>, <code>BadMatch</code>, and <code>BadValue</code> errors. </p>
<p> The <code>XGetImage</code> function returns a pointer to an <code>XImage</code> structure. This structure provides you with the contents of the specified rectangle of the drawable in the format you specify. If the format argument is <code>XYPixmap</code>, the image contains only the bit planes you passed to the plane_mask argument. If the plane_mask argument only requests a subset of the planes of the display, the depth of the returned image will be the number of planes requested. If the format argument is <code>ZPixmap</code>, <code>XGetImage</code> returns as zero the bits in all planes not specified in the plane_mask argument. The function performs no range checking on the values in plane_mask and ignores extraneous bits. </p>
<p> <code>XGetImage</code> returns the depth of the image to the depth member of the <code>XImage</code> structure. The depth of the image is as specified when the drawable was created, except when getting a subset of the planes in <code>XYPixmap</code> format, when the depth is given by the number of bits set to 1 in plane_mask. </p>
<p> If the drawable is a pixmap, the given rectangle must be wholly contained within the pixmap, or a <code>BadMatch</code> error results. If the drawable is a window, the window must be viewable, and it must be the case that if there were no inferiors or overlapping windows, the specified rectangle of the window would be fully visible on the screen and wholly contained within the outside edges of the window, or a <code>BadMatch</code> error results. Note that the borders of the window can be included and read with this request. If the window has backing-store, the backing-store contents are returned for regions of the window that are obscured by noninferior windows. If the window does not have backing-store, the returned contents of such obscured regions are undefined. The returned contents of visible regions of inferiors of a different depth than the specified window&#8217;s depth are also undefined. The pointer cursor image is not included in the returned contents. If a problem occurs, <code>XGetImage</code> returns NULL. </p>
<p> <code>XGetImage</code> can generate <code>BadDrawable</code>, <code>BadMatch</code>, and <code>BadValue</code> errors. </p>
<p> The <code>XGetSubImage</code> function updates dest_image with the specified subimage in the same manner as <code>XGetImage</code>. If the format argument is <code>XYPixmap</code>, the image contains only the bit planes you passed to the plane_mask argument. If the format argument is <code>ZPixmap</code>, <code>XGetSubImage</code> returns as zero the bits in all planes not specified in the plane_mask argument. The function performs no range checking on the values in plane_mask and ignores extraneous bits. As a convenience, <code>XGetSubImage</code> returns a pointer to the same <code>XImage</code> structure specified by dest_image. </p>
<p> The depth of the destination <code>XImage</code> structure must be the same as that of the drawable. If the specified subimage does not fit at the specified location on the destination image, the right and bottom edges are clipped. If the drawable is a pixmap, the given rectangle must be wholly contained within the pixmap, or a <code>BadMatch</code> error results. If the drawable is a window, the window must be viewable, and it must be the case that if there were no inferiors or overlapping windows, the specified rectangle of the window would be fully visible on the screen and wholly contained within the outside edges of the window, or a <code>BadMatch</code> error results. If the window has backing-store, then the backing-store contents are returned for regions of the window that are obscured by noninferior windows. If the window does not have backing-store, the returned contents of such obscured regions are undefined. The returned contents of visible regions of inferiors of a different depth than the specified window&#8217;s depth are also undefined. If a problem occurs, <code>XGetSubImage</code> returns NULL. </p>
<p> <code>XGetSubImage</code> can generate <code>BadDrawable</code>, <code>BadGC</code>, <code>BadMatch</code>, and <code>BadValue</code> errors.</p>
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
<p><i>Xlib &#8211; C Language X Interface</i></p>
