---
title: "xdrawimagestring16(3)"
name: "xdrawimagestring16"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdrawimagestring16/"
description: "XDrawImageString, XDrawImageString16 – draw image text"
---

<p>XDrawImageString, XDrawImageString16 &#8211; draw image text </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XDrawImageString(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, char *<i>string</i>, int <i>length</i>);</p>
<dd>int XDrawImageString16(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, XChar2b *<i>string</i>, int <i>length</i>);</dl>
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
<p>The <code>XDrawImageString16</code> function is similar to <code>XDrawImageString</code> except that it uses 2-byte or 16-bit characters. Both functions also use both the foreground and background pixels of the GC in the destination. </p>
<p> The effect is first to fill a destination rectangle with the background pixel defined in the GC and then to paint the text with the foreground pixel. The upper-left corner of the filled rectangle is at: </p>
<p> [x, y &#8211; font-ascent] </p>
<p> The width is: </p>
<p> overall-width </p>
<p> The height is: </p>
<p> font-ascent + font-descent </p>
<p> The overall-width, font-ascent, and font-descent are as would be returned by <code>XQueryTextExtents</code> using gc and string. The function and fill-style defined in the GC are ignored for these functions. The effective function is <code>GXcopy</code>, and the effective fill-style is <code>FillSolid</code>. </p>
<p> For fonts defined with 2-byte matrix indexing and used with <code>XDrawImageString</code>, each byte is used as a byte2 with a byte1 of zero. </p>
<p> Both functions use these GC components: plane-mask, foreground, background, font, subwindow-mode, clip-x-origin, clip-y-origin, and clip-mask. </p>
<p> <code>XDrawImageString</code> and <code>XDrawImageString16</code> can generate <code>BadDrawable</code>, <code>BadGC</code>, and <code>BadMatch</code> errors.</p>
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
<p><a href="/docs/linux/man/3-xdrawstring/">XDrawString</a>(3), <a href="/docs/linux/man/3-xdrawtext/">XDrawText</a>(3), <a href="/docs/linux/man/3-xloadfont/">XLoadFont</a>(3), <a href="/docs/linux/man/3-xtextextents/">XTextExtents</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
