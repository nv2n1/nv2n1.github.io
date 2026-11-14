---
title: "displaywidthmm(3)"
name: "displaywidthmm"
section: "3"
letter: "d"
url: "/docs/linux/man/3-displaywidthmm/"
description: "ImageByteOrder, BitmapBitOrder, BitmapPad, BitmapUnit, DisplayHeight, DisplayHeightMM, DisplayWidth, DisplayWidthMM, XListPixmapFormats, XPixmapFormatValues – image format functions and macros"
---

<p>ImageByteOrder, BitmapBitOrder, BitmapPad, BitmapUnit, DisplayHeight, DisplayHeightMM, DisplayWidth, DisplayWidthMM, XListPixmapFormats, XPixmapFormatValues &#8211; image format functions and macros </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>XPixmapFormatValues *XListPixmapFormats(Display *<i>display</i>, int *<i>count_return</i>);</p>
<dd>int ImageByteOrder(Display *<i>display</i>);</p>
<dd>int BitmapBitOrder(Display *<i>display</i>);</p>
<dd>int BitmapPad(Display *<i>display</i>);</p>
<dd>int BitmapUnit(Display *<i>display</i>);</p>
<dd>int DisplayHeight(Display *<i>display</i>, int <i>screen_number</i>);</p>
<dd>int DisplayHeightMM(Display *<i>display</i>, int <i>screen_number</i>);</p>
<dd>int DisplayWidth(Display *<i>display</i>, int <i>screen_number</i>);</p>
<dd>int DisplayWidthMM(Display *<i>display</i>, int <i>screen_number</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>count_return</i></p>
<dd>Returns the number of pixmap formats that are supported by the display.</p>
<dt><i>screen_number</i></p>
<dd>Specifies the appropriate screen number on the host server.</dl>
<h2>Description</h2>
<p>The <code>XListPixmapFormats</code> function returns an array of <code>XPixmapFormatValues</code> structures that describe the types of Z format images supported by the specified display. If insufficient memory is available, <code>XListPixmapFormats</code> returns NULL. To free the allocated storage for the <code>XPixmapFormatValues</code> structures, use <code>XFree</code>. </p>
<p> The <code>ImageByteOrder</code> macro specifies the required byte order for images for each scanline unit in XY format (bitmap) or for each pixel value in Z format. </p>
<p> The <code>BitmapBitOrder</code> macro returns <code>LSBFirst</code> or <code>MSBFirst</code> to indicate whether the leftmost bit in the bitmap as displayed on the screen is the least or most significant bit in the unit. </p>
<p> The <code>BitmapPad</code> macro returns the number of bits that each scanline must be padded. </p>
<p> The <code>BitmapUnit</code> macro returns the size of a bitmap&#8217;s scanline unit in bits. </p>
<p> The <code>DisplayHeight</code> macro returns the height of the specified screen in pixels. </p>
<p> The <code>DisplayHeightMM</code> macro returns the height of the specified screen in millimeters. </p>
<p> The <code>DisplayWidth</code> macro returns the width of the screen in pixels. </p>
<p> The <code>DisplayWidthMM</code> macro returns the width of the specified screen in millimeters.</p>
<h2>Structures</h2>
<p>The <code>XPixmapFormatValues</code> structure provides an interface to the pixmap format information that is returned at the time of a connection setup. It contains: typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int depth;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int bits_per_pixel;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int scanline_pad; } XPixmapFormatValues;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-allplanes/">AllPlanes</a>(3), <a href="/docs/linux/man/3-blackpixelofscreen/">BlackPixelOfScreen</a>(3), <a href="/docs/linux/man/3-iscursorkey/">IsCursorKey</a>(3), <a href="/docs/linux/man/3-xfree/">XFree</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
