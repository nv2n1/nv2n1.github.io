---
title: "xdrawstring(3)"
name: "xdrawstring"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdrawstring/"
description: "XDrawString, XDrawString16 – draw text characters"
---

<p>XDrawString, XDrawString16 &#8211; draw text characters </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XDrawString(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, char *<i>string</i>, int <i>length</i>);</p>
<dd>int XDrawString16(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, XChar2b *<i>string</i>, int <i>length</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>d</i></p>
<dd>Specifies the drawable.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</p>
<dt><i>length</i></p>
<dd>Specifies the number of characters in the string argument.</p>
<dt><i>string</i></p>
<dd>Specifies the character string.</p>
<dt><i>x</i></p>
<dd>
<dt><i>y</i></p>
<dd>Specify the x and y coordinates, which are relative to the origin of the specified drawable and define the origin of the first character.</dl>
<h2>Description</h2>
<p>Each character image, as defined by the font in the GC, is treated as an additional mask for a fill operation on the drawable. The drawable is modified only where the font character has a bit set to 1. For fonts defined with 2-byte matrix indexing and used with <code>XDrawString16</code>, each byte is used as a byte2 with a byte1 of zero. </p>
<p> Both functions use these GC components: function, plane-mask, fill-style, font, subwindow-mode, clip-x-origin, clip-y-origin, and clip-mask. They also use these GC mode-dependent components: foreground, background, tile, stipple, tile-stipple-x-origin, and tile-stipple-y-origin. </p>
<p> <code>XDrawString</code> and <code>XDrawString16</code> can generate <code>BadDrawable</code>, <code>BadGC</code>, and <code>BadMatch</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadDrawable</code></p>
<dd>A value for a Drawable argument does not name a defined Window or Pixmap.</p>
<dt><code>BadGC</code></p>
<dd>A value for a GContext argument does not name a defined GContext.</p>
<dt><code>BadMatch</code></p>
<dd>An <code>InputOnly</code> window is used as a Drawable.</p>
<dt><code>BadMatch</code></p>
<dd>Some argument or pair of arguments has the correct type and range but fails to match in some other way required by the request.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xdrawimagestring/">XDrawImageString</a>(3), <a href="/docs/linux/man/3-xdrawtext/">XDrawText</a>(3), <a href="/docs/linux/man/3-xloadfont/">XLoadFont</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
