---
title: "xwctextpercharextents(3)"
name: "xwctextpercharextents"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xwctextpercharextents/"
description: "XmbTextPerCharExtents, XwcTextPerCharExtents, Xutf8TextPerCharExtents – obtain per-character information for a text string"
---

<p>XmbTextPerCharExtents, XwcTextPerCharExtents, Xutf8TextPerCharExtents &#8211; obtain per-character information for a text string </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>Status XmbTextPerCharExtents(XFontSet <i>font_set</i>, char *<i>string</i>, int <i>num_bytes</i>, XRectangle *<i>ink_array_return</i>, XRectangle *<i>logical_array_return</i>, int <i>array_size</i>, int *<i>num_chars_return</i>, XRectangle *<i>overall_ink_return</i>, XRectangle *<i>overall_logical_return</i>);</p>
<dd>Status XwcTextPerCharExtents(XFontSet <i>font_set</i>, wchar_t *<i>string</i>, int <i>num_wchars</i>, XRectangle *<i>ink_array_return</i>, XRectangle *<i>logical_array_return</i>, int <i>array_size</i>, int *<i>num_chars_return</i>, XRectangle *<i>overall_ink_return</i>, XRectangle *<i>overall_logical_return</i>);</p>
<dd>Status Xutf8TextPerCharExtents(XFontSet <i>font_set</i>, char *<i>string</i>, int <i>num_bytes</i>, XRectangle *<i>ink_array_return</i>, XRectangle *<i>logical_array_return</i>, int <i>array_size</i>, int *<i>num_chars_return</i>, XRectangle *<i>overall_ink_return</i>, XRectangle *<i>overall_logical_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>array_size</i></p>
<dd>Specifies the size of ink_array_return and logical_array_return. The caller must pass in arrays of this size.</p>
<dt><i>font_set</i></p>
<dd>Specifies the font set.</p>
<dt><i>ink_array_return</i></p>
<dd>Returns the ink dimensions for each character.</p>
<dt><i>logical_array_return</i></p>
<dd>Returns the logical dimensions for each character.</p>
<dt><i>num_bytes</i></p>
<dd>Specifies the number of bytes in the string argument.</p>
<dt><i>num_chars_return</i></p>
<dd>Returns the number of characters in the string argument.</p>
<dt><i>num_wchars</i></p>
<dd>Specifies the number of characters in the string argument.</p>
<dt><i>overall_ink_return</i></p>
<dd>Returns the overall ink extents of the entire string.</p>
<dt><i>overall_logical_return</i></p>
<dd>Returns the overall logical extents of the entire string.</p>
<dt><i>string</i></p>
<dd>Specifies the character string.</dl>
<h2>Description</h2>
<p>The <code>XmbTextPerCharExtents</code>, <code>XwcTextPerCharExtents</code> and <code>Xutf8TextPerCharExtents</code> functions return the text dimensions of each character of the specified text, using the fonts loaded for the specified font set. Each successive element of ink_array_return and logical_array_return is set to the successive character&#8217;s drawn metrics, relative to the drawing origin of the string and one rectangle for each character in the supplied text string. The number of elements of ink_array_return and logical_array_return that have been set is returned to num_chars_return. </p>
<p> Each element of ink_array_return is set to the bounding box of the corresponding character&#8217;s drawn foreground color. Each element of logical_array_return is set to the bounding box that provides minimum spacing to other graphical features for the corresponding character. Other graphical features should not intersect any of the logical_array_return rectangles. </p>
<p> Note that an <code>XRectangle</code> represents the effective drawing dimensions of the character, regardless of the number of font glyphs that are used to draw the character or the direction in which the character is drawn. If multiple characters map to a single character glyph, the dimensions of all the <code>XRectangles</code> of those characters are the same. </p>
<p> When the <code>XFontSet</code> has missing charsets, metrics for each unavailable character are taken from the default string returned by <code>XCreateFontSet</code> so that the metrics represent the text as it will actually be drawn. The behavior for an invalid codepoint is undefined. </p>
<p> If the array_size is too small for the number of characters in the supplied text, the functions return zero and num_chars_return is set to the number of rectangles required. Otherwise, the functions return a nonzero value. </p>
<p> If the overall_ink_return or overall_logical_return argument is non-NULL, <code>XmbTextPerCharExtents</code>, <code>XwcTextPerCharExtents</code> and <code>Xutf8TextPerCharExtents</code> return the maximum extent of the string&#8217;s metrics to overall_ink_return or overall_logical_return, as returned by <code>XmbTextExtents</code>, <code>XwcTextExtents</code> or <code>Xutf8TextExtents</code>. </p>
<p> The function <code>Xutf8TextPerCharExtents</code> is an extension introduced by The XFree86 Project, Inc., in their 4.0.2 release. Its presence is indicated by the macro <code>X_HAVE_UTF8_STRING</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xmbtextescapement/">XmbTextEscapement</a>(3), <a href="/docs/linux/man/3-xmbtextextents/">XmbTextExtents</a>(3) <i>Xlib &#8211; C Language X Interface</i></p>
