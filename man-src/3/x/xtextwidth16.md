---
title: "xtextwidth16(3)"
name: "xtextwidth16"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtextwidth16/"
description: "XTextWidth, XTextWidth16 – compute text width"
---

<p>XTextWidth, XTextWidth16 &#8211; compute text width </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XTextWidth(XFontStruct *<i>font_struct</i>, char *<i>string</i>, int <i>count</i>);</p>
<dd>int XTextWidth16(XFontStruct *<i>font_struct</i>, XChar2b *<i>string</i>, int <i>count</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>count</i></p>
<dd>Specifies the character count in the specified string.</p>
<dt><i>font_struct</i></p>
<dd>Specifies the font used for the width computation.</p>
<dt><i>string</i></p>
<dd>Specifies the character string.</dl>
<h2>Description</h2>
<p>The <code>XTextWidth</code> and <code>XTextWidth16</code> functions return the width of the specified 8-bit or 2-byte character strings.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xloadfont/">XLoadFont</a>(3), <a href="/docs/linux/man/3-xtextextents/">XTextExtents</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
