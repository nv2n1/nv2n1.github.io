---
title: "xrecolorcursor(3)"
name: "xrecolorcursor"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xrecolorcursor/"
description: "XRecolorCursor, XFreeCursor, XQueryBestCursor – manipulate cursors"
---

<p>XRecolorCursor, XFreeCursor, XQueryBestCursor &#8211; manipulate cursors </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XRecolorCursor(Display *<i>display</i>, Cursor <i>cursor</i>, XColor *<i>foreground_color</i>, XColor *<i>background_color</i>);</p>
<dd>int XFreeCursor(Display *<i>display</i>, Cursor <i>cursor</i>);</p>
<dd>Status XQueryBestCursor(Display *<i>display</i>, Drawable <i>d</i>, unsigned int <i>width</i>, unsigned int <i>height</i>, unsigned int *<i>width_return</i>, unsigned int *<i>height_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>background_color</i></p>
<dd>Specifies the RGB values for the background of the source.</p>
<dt><i>cursor</i></p>
<dd>Specifies the cursor.</p>
<dt><i>d</i></p>
<dd>Specifies the drawable, which indicates the screen.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>foreground_color</i></p>
<dd>Specifies the RGB values for the foreground of the source.</p>
<dt><i>width</i></p>
<dd>
<dt><i>height</i></p>
<dd>Specify the width and height of the cursor that you want the size information for.</p>
<dt><i>width_return</i></p>
<dd>
<dt><i>height_return</i></p>
<dd>Return the best width and height that is closest to the specified width and height.</dl>
<h2>Description</h2>
<p>The <code>XRecolorCursor</code> function changes the color of the specified cursor, and if the cursor is being displayed on a screen, the change is visible immediately. The pixel members of the <code>XColor</code> structures are ignored; only the RGB values are used. </p>
<p> <code>XRecolorCursor</code> can generate a <code>BadCursor</code> error. </p>
<p> The <code>XFreeCursor</code> function deletes the association between the cursor resource ID and the specified cursor. The cursor storage is freed when no other resource references it. The specified cursor ID should not be referred to again. </p>
<p> <code>XFreeCursor</code> can generate a <code>BadCursor</code> error. </p>
<p> Some displays allow larger cursors than other displays. The <code>XQueryBestCursor</code> function provides a way to find out what size cursors are actually possible on the display. It returns the largest size that can be displayed. Applications should be prepared to use smaller cursors on displays that cannot support large ones. </p>
<p> <code>XQueryBestCursor</code> can generate a <code>BadDrawable</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadCursor</code></p>
<dd>A value for a Cursor argument does not name a defined Cursor.</p>
<dt><code>BadDrawable</code></p>
<dd>A value for a Drawable argument does not name a defined Window or Pixmap.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreatecolormap/">XCreateColormap</a>(3), <a href="/docs/linux/man/3-xcreatefontcursor/">XCreateFontCursor</a>(3), <a href="/docs/linux/man/3-xdefinecursor/">XDefineCursor</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
