---
title: "xquerybestsize(3)"
name: "xquerybestsize"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xquerybestsize/"
description: "XQueryBestSize, XQueryBestTile, XQueryBestStipple – determine efficient sizes"
---

<p>XQueryBestSize, XQueryBestTile, XQueryBestStipple &#8211; determine efficient sizes </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XQueryBestSize(Display *<i>display</i>, int <i>class</i>, Drawable <i>which_screen</i>, unsigned int <i>width</i>, unsigned int <i>height</i>, unsigned int *<i>width_return</i>, unsigned int *<i>height_return</i>);</p>
<dd>Status XQueryBestTile(Display *<i>display</i>, Drawable <i>which_screen</i>, unsigned int <i>width</i>, unsigned int <i>height</i>, unsigned int *<i>width_return</i>, unsigned int *<i>height_return</i>);</p>
<dd>Status XQueryBestStipple(Display *<i>display</i>, Drawable <i>which_screen</i>, unsigned int <i>width</i>, unsigned int <i>height</i>, unsigned int *<i>width_return</i>, unsigned int *<i>height_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>class</i></p>
<dd>Specifies the class that you are interested in. You can pass <code>TileShape</code>, <code>CursorShape</code>, or <code>StippleShape</code>.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>width</i></p>
<dd>
<dt><i>height</i></p>
<dd>Specify the width and height.</p>
<dt><i>which_screen</i></p>
<dd>Specifies any drawable on the screen.</p>
<dt><i>width_return</i></p>
<dd>
<dt><i>height_return</i></p>
<dd>Return the width and height of the object best supported by the display hardware.</dl>
<h2>Description</h2>
<p>The <code>XQueryBestSize</code> function returns the best or closest size to the specified size. For <code>CursorShape</code>, this is the largest size that can be fully displayed on the screen specified by which_screen. For <code>TileShape</code>, this is the size that can be tiled fastest. For <code>StippleShape</code>, this is the size that can be stippled fastest. For <code>CursorShape</code>, the drawable indicates the desired screen. For <code>TileShape</code> and <code>StippleShape</code>, the drawable indicates the screen and possibly the window class and depth. An <code>InputOnly</code> window cannot be used as the drawable for <code>TileShape</code> or <code>StippleShape</code>, or a <code>BadMatch</code> error results. </p>
<p> <code>XQueryBestSize</code> can generate <code>BadDrawable</code>, <code>BadMatch</code>, and <code>BadValue</code> errors. </p>
<p> The <code>XQueryBestTile</code> function returns the best or closest size, that is, the size that can be tiled fastest on the screen specified by which_screen. The drawable indicates the screen and possibly the window class and depth. If an <code>InputOnly</code> window is used as the drawable, a <code>BadMatch</code> error results. </p>
<p> <code>XQueryBestTile</code> can generate <code>BadDrawable</code> and <code>BadMatch</code> errors. </p>
<p> The <code>XQueryBestStipple</code> function returns the best or closest size, that is, the size that can be stippled fastest on the screen specified by which_screen. The drawable indicates the screen and possibly the window class and depth. If an <code>InputOnly</code> window is used as the drawable, a <code>BadMatch</code> error results. </p>
<p> <code>XQueryBestStipple</code> can generate <code>BadDrawable</code> and <code>BadMatch</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadMatch</code></p>
<dd>An <code>InputOnly</code> window is used as a Drawable.</p>
<dt><code>BadDrawable</code></p>
<dd>A value for a Drawable argument does not name a defined Window or Pixmap.</p>
<dt><code>BadMatch</code></p>
<dd>The values do not exist for an <code>InputOnly</code> window.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreategc/">XCreateGC</a>(3), <a href="/docs/linux/man/3-xsetarcmode/">XSetArcMode</a>(3), <a href="/docs/linux/man/3-xsetcliporigin/">XSetClipOrigin</a>(3), <a href="/docs/linux/man/3-xsetfillstyle/">XSetFillStyle</a>(3), <a href="/docs/linux/man/3-xsetfont/">XSetFont</a>(3), <a href="/docs/linux/man/3-xsetlineattributes/">XSetLineAttributes</a>(3), <a href="/docs/linux/man/3-xsetstate/">XSetState</a>(3), <a href="/docs/linux/man/3-xsettile/">XSetTile</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
