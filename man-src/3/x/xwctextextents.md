---
title: "xwctextextents(3)"
name: "xwctextextents"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xwctextextents/"
description: "XmbTextExtents, XwcTextExtents, Xutf8TextExtents – compute text extents"
---

<p>XmbTextExtents, XwcTextExtents, Xutf8TextExtents &#8211; compute text extents </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XmbTextExtents(XFontSet <i>font_set</i>, char *<i>string</i>, int <i>num_bytes</i>, XRectangle *<i>overall_ink_return</i>, XRectangle *<i>overall_logical_return</i>);</p>
<dd>int XwcTextExtents(XFontSet <i>font_set</i>, wchar_t *<i>string</i>, int <i>num_wchars</i>, XRectangle *<i>overall_ink_return</i>, XRectangle *<i>overall_logical_return</i>);</p>
<dd>int Xutf8TextExtents(XFontSet <i>font_set</i>, char *<i>string</i>, int <i>num_bytes</i>, XRectangle *<i>overall_ink_return</i>, XRectangle *<i>overall_logical_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>font_set</i></p>
<dd>Specifies the font set.</p>
<dt><i>num_bytes</i></p>
<dd>Specifies the number of bytes in the string argument.</p>
<dt><i>num_wchars</i></p>
<dd>Specifies the number of characters in the string argument.</p>
<dt><i>overall_ink_return</i></p>
<dd>Returns the overall ink dimensions.</p>
<dt><i>overall_logical_return</i></p>
<dd>Returns the overall logical dimensions.</p>
<dt><i>string</i></p>
<dd>Specifies the character string.</dl>
<h2>Description</h2>
<p>The <code>XmbTextExtents</code>, <code>XwcTextExtents</code> and <code>Xutf8TextExtents</code> functions set the components of the specified overall_ink_return and overall_logical_return arguments to the overall bounding box of the string&#8217;s image and a logical bounding box for spacing purposes, respectively. They return the value returned by <code>XmbTextEscapement</code>, <code>XwcTextEscapement</code> or <code>Xutf8TextEscapement</code>. These metrics are relative to the drawing origin of the string, using the fonts loaded for the specified font set. </p>
<p> If the overall_ink_return argument is non-NULL, it is set to the bounding box of the string&#8217;s character ink. The overall_ink_return for a nondescending, horizontally drawn Latin character is conventionally entirely above the baseline; that is, overall_ink_return.height &lt;= -overall_ink_return.y. The overall_ink_return for a nonkerned character is entirely at, and to the right of, the origin; that is, overall_ink_return.x &gt;= 0. A character consisting of a single pixel at the origin would set overall_ink_return fields y = 0, x = 0, width = 1, and height = 1. </p>
<p> If the overall_logical_return argument is non-NULL, it is set to the bounding box that provides minimum spacing to other graphical features for the string. Other graphical features, for example, a border surrounding the text, should not intersect this rectangle. </p>
<p> When the <code>XFontSet</code> has missing charsets, metrics for each unavailable character are taken from the default string returned by <code>XCreateFontSet</code> so that the metrics represent the text as it will actually be drawn. The behavior for an invalid codepoint is undefined. </p>
<p> The function <code>Xutf8TextExtents</code> is an extension introduced by The XFree86 Project, Inc., in their 4.0.2 release. Its presence is indicated by the macro <code>X_HAVE_UTF8_STRING</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xmbtextescapement/">XmbTextEscapement</a>(3), <a href="/docs/linux/man/3-xmbtextpercharextents/">XmbTextPerCharExtents</a>(3) <i>Xlib &#8211; C Language X Interface</i></p>
