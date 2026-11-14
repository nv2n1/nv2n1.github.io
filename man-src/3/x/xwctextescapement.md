---
title: "xwctextescapement(3)"
name: "xwctextescapement"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xwctextescapement/"
description: "XmbTextEscapement, XwcTextEscapement, Xutf8TextEscapement – obtain the escapement of text"
---

<p>XmbTextEscapement, XwcTextEscapement, Xutf8TextEscapement &#8211; obtain the escapement of text </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XmbTextEscapement(XFontSet <i>font_set</i>, char *<i>string</i>, int <i>num_bytes</i>);</p>
<dd>int XwcTextEscapement(XFontSet <i>font_set</i>, wchar_t *<i>string</i>, int <i>num_wchars</i>);</p>
<dd>int Xutf8TextEscapement(XFontSet <i>font_set</i>, char *<i>string</i>, int <i>num_bytes</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>font_set</i></p>
<dd>Specifies the font set.</p>
<dt><i>num_bytes</i></p>
<dd>Specifies the number of bytes in the string argument.</p>
<dt><i>num_wchars</i></p>
<dd>Specifies the number of characters in the string argument.</p>
<dt><i>string</i></p>
<dd>Specifies the character string.</dl>
<h2>Description</h2>
<p>The <code>XmbTextEscapement</code>, <code>XwcTextEscapement</code> and <code>Xutf8TextEscapement</code> functions return the escapement in pixels of the specified string as a value, using the fonts loaded for the specified font set. The escapement is the distance in pixels in the primary draw direction from the drawing origin to the origin of the next character to be drawn, assuming that the rendering of the next character is not dependent on the supplied string. </p>
<p> Regardless of the character rendering order, the escapement is always positive. </p>
<p> The function <code>Xutf8TextEscapement</code> is an extension introduced by The XFree86 Project, Inc., in their 4.0.2 release. Its presence is indicated by the macro <code>X_HAVE_UTF8_STRING</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xmbtextextents/">XmbTextExtents</a>(3), <a href="/docs/linux/man/3-xmbtextpercharextents/">XmbTextPerCharExtents</a>(3) <i>Xlib &#8211; C Language X Interface</i></p>
