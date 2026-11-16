---
title: "xfreepixmap(3)"
name: "xfreepixmap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xfreepixmap/"
description: "XCreatePixmap, XFreePixmap – create or destroy pixmaps"
---

<p>XCreatePixmap, XFreePixmap &#8211; create or destroy pixmaps </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Pixmap XCreatePixmap(Display *<i>display</i>, Drawable <i>d</i>, unsigned int <i>width</i>, unsigned int <i>height</i>, unsigned int <i>depth</i>);</dd>
<dd>int XFreePixmap(Display *<i>display</i>, Pixmap <i>pixmap</i>);</dd></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>d</i></dt>
<dd>Specifies which screen the pixmap is created on.</dd>
<dt><i>depth</i></dt>
<dd>Specifies the depth of the pixmap.</dd>
<dt><i>display</i></dt>
<dd>Specifies the connection to the X server.</dd>
<dt><i>pixmap</i></dt>
<dd>Specifies the pixmap.</dd>
<dt><i>width</i></dt>
<dd>
</dd><dt><i>height</i></dt>
<dd>Specify the width and height, which define the dimensions of the pixmap.</dd></dl>
<h2>Description</h2>
<p>The <code>XCreatePixmap</code> function creates a pixmap of the width, height, and depth you specified and returns a pixmap ID that identifies it. It is valid to pass an <code>InputOnly</code> window to the drawable argument. The width and height arguments must be nonzero, or a <code>BadValue</code> error results. The depth argument must be one of the depths supported by the screen of the specified drawable, or a <code>BadValue</code> error results. </p>
<p> The server uses the specified drawable to determine on which screen to create the pixmap. The pixmap can be used only on this screen and only with other drawables of the same depth (see <code>XCopyPlane</code> for an exception to this rule). The initial contents of the pixmap are undefined. </p>
<p> <code>XCreatePixmap</code> can generate <code>BadAlloc</code>, <code>BadDrawable</code>, and <code>BadValue</code> errors. </p>
<p> The <code>XFreePixmap</code> function first deletes the association between the pixmap ID and the pixmap. Then, the X server frees the pixmap storage when there are no references to it. The pixmap should never be referenced again. </p>
<p> <code>XFreePixmap</code> can generate a <code>BadPixmap</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></dt>
<dd>The server failed to allocate the requested resource or server memory.</dd>
<dt><code>BadDrawable</code></dt>
<dd>A value for a Drawable argument does not name a defined Window or Pixmap.</dd>
<dt><code>BadPixmap</code></dt>
<dd>A value for a Pixmap argument does not name a defined Pixmap.</dd>
<dt><code>BadValue</code></dt>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dd></dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcopyarea/">XCopyArea</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
