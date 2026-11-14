---
title: "xtextextents(3)"
name: "xtextextents"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtextextents/"
description: "XTextExtents, XTextExtents16, XQueryTextExtents, XQueryTextExtents16 – compute or query text extents"
---

<p>XTextExtents, XTextExtents16, XQueryTextExtents, XQueryTextExtents16 &#8211; compute or query text extents </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XTextExtents(XFontStruct *<i>font_struct</i>, char *<i>string</i>, int <i>nchars</i>, int *<i>direction_return</i>, int *<i>font_ascent_return</i>, int *<i>font_descent_return</i>, XCharStruct *<i>overall_return</i>);</p>
<dd>int XTextExtents16(XFontStruct *<i>font_struct</i>, XChar2b *<i>string</i>, int <i>nchars</i>, int *<i>direction_return</i>, int *<i>font_ascent_return</i>, int *<i>font_descent_return</i>, XCharStruct *<i>overall_return</i>);</p>
<dd>int XQueryTextExtents(Display *<i>display</i>, XID <i>font_ID</i>, char *<i>string</i>, int <i>nchars</i>, int *<i>direction_return</i>, int *<i>font_ascent_return</i>, int *<i>font_descent_return</i>, XCharStruct *<i>overall_return</i>);</p>
<dd>int XQueryTextExtents16(Display *<i>display</i>, XID <i>font_ID</i>, XChar2b *<i>string</i>, int <i>nchars</i>, int *<i>direction_return</i>, int *<i>font_ascent_return</i>, int *<i>font_descent_return</i>, XCharStruct *<i>overall_return</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>direction_return</i></p>
<dd>Returns the value of the direction hint or <code>FontRightToLeft</code>).</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>font_ID</i></p>
<dd>Specifies either the font ID or the <code>GContext</code> ID that contains the font.</p>
<dt><i>font_ascent_return</i></p>
<dd>Returns the font ascent.</p>
<dt><i>font_descent_return</i></p>
<dd>Returns the font descent.</p>
<dt><i>font_struct</i></p>
<dd>Specifies the <code>XFontStruct</code> structure.</p>
<dt><i>nchars</i></p>
<dd>Specifies the number of characters in the character string.</p>
<dt><i>string</i></p>
<dd>Specifies the character string.</p>
<dt><i>overall_return</i></p>
<dd>Returns the overall size in the specified <code>XCharStruct</code> structure.</dl>
<h2>Description</h2>
<p>The <code>XTextExtents</code> and <code>XTextExtents16</code> functions perform the size computation locally and, thereby, avoid the round-trip overhead of <code>XQueryTextExtents</code> and <code>XQueryTextExtents16</code>. Both functions return an <code>XCharStruct</code> structure, whose members are set to the values as follows. </p>
<p> The ascent member is set to the maximum of the ascent metrics of all characters in the string. The descent member is set to the maximum of the descent metrics. The width member is set to the sum of the character-width metrics of all characters in the string. For each character in the string, let W be the sum of the character-width metrics of all characters preceding it in the string. Let L be the left-side-bearing metric of the character plus W. Let R be the right-side-bearing metric of the character plus W. The lbearing member is set to the minimum L of all characters in the string. The rbearing member is set to the maximum R. </p>
<p> For fonts defined with linear indexing rather than 2-byte matrix indexing, each <code>XChar2b</code> structure is interpreted as a 16-bit number with byte1 as the most significant byte. If the font has no defined default character, undefined characters in the string are taken to have all zero metrics. </p>
<p> The <code>XQueryTextExtents</code> and <code>XQueryTextExtents16</code> functions return the bounding box of the specified 8-bit and 16-bit character string in the specified font or the font contained in the specified GC. These functions query the X server and, therefore, suffer the round-trip overhead that is avoided by <code>XTextExtents</code> and <code>XTextExtents16</code>. Both functions return a <code>XCharStruct</code> structure, whose members are set to the values as follows. </p>
<p> The ascent member is set to the maximum of the ascent metrics of all characters in the string. The descent member is set to the maximum of the descent metrics. The width member is set to the sum of the character-width metrics of all characters in the string. For each character in the string, let W be the sum of the character-width metrics of all characters preceding it in the string. Let L be the left-side-bearing metric of the character plus W. Let R be the right-side-bearing metric of the character plus W. The lbearing member is set to the minimum L of all characters in the string. The rbearing member is set to the maximum R. </p>
<p> For fonts defined with linear indexing rather than 2-byte matrix indexing, each <code>XChar2b</code> structure is interpreted as a 16-bit number with byte1 as the most significant byte. If the font has no defined default character, undefined characters in the string are taken to have all zero metrics. </p>
<p> Characters with all zero metrics are ignored. If the font has no defined default_char, the undefined characters in the string are also ignored. </p>
<p> <code>XQueryTextExtents</code> and <code>XQueryTextExtents16</code> can generate <code>BadFont</code> and <code>BadGC</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadFont</code></p>
<dd>A value for a Font or GContext argument does not name a defined Font.</p>
<dt><code>BadGC</code></p>
<dd>A value for a GContext argument does not name a defined GContext.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xloadfont/">XLoadFont</a>(3), <a href="/docs/linux/man/3-xtextwidth/">XTextWidth</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
