---
title: "xdirectionaldependentdrawing(3)"
name: "xdirectionaldependentdrawing"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdirectionaldependentdrawing/"
description: "XFontsOfFontSet, XBaseFontNameListOfFontSet, XLocaleOfFontSet, XContextDependentDrawing, XContextualDrawing, XDirectionalDependentDrawing – obtain fontset information"
---

<p>XFontsOfFontSet, XBaseFontNameListOfFontSet, XLocaleOfFontSet, XContextDependentDrawing, XContextualDrawing, XDirectionalDependentDrawing &#8211; obtain fontset information </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XFontsOfFontSet(XFontSet <i>font_set</i>, XFontStruct ***<i>font_struct_list_return</i>, char ***<i>font_name_list_return</i>);</p>
<dd>char *XBaseFontNameListOfFontSet(XFontSet <i>font_set</i>);</p>
<dd>char *XLocaleOfFontSet(XFontSet <i>font_set</i>);</p>
<dd>Bool XContextDependentDrawing(XFontSet <i>font_set</i>);</p>
<dd>Bool XContextualDrawing(XFontSet <i>font_set</i>);</p>
<dd>Bool XDirectionalDependentDrawing(XFontSet <i>font_set</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>font_set</i></p>
<dd>Specifies the font set.</p>
<dt><i>font_name_list_return</i></p>
<dd>Returns the list of font names.</p>
<dt><i>font_struct_list_return</i></p>
<dd>Returns the list of font structs.</dl>
<h2>Description</h2>
<p>The <code>XFontsOfFontSet</code> function returns a list of one or more <code>XFontStructs</code> and font names for the fonts used by the Xmb and Xwc layers for the given font set. A list of pointers to the <code>XFontStruct</code> structures is returned to font_struct_list_return. A list of pointers to null-terminated, fully specified font name strings in the locale of the font set is returned to font_name_list_return. The font_name_list order corresponds to the font_struct_list order. The number of <code>XFontStruct</code> structures and font names is returned as the value of the function. </p>
<p> Because it is not guaranteed that a given character will be imaged using a single font glyph, there is no provision for mapping a character or default string to the font properties, font ID, or direction hint for the font for the character. The client may access the <code>XFontStruct</code> list to obtain these values for all the fonts currently in use. </p>
<p> Xlib does not guarantee that fonts are loaded from the server at the creation of an <code>XFontSet</code>. Xlib may choose to cache font data, loading it only as needed to draw text or compute text dimensions. Therefore, existence of the per_char metrics in the <code>XFontStruct</code> structures in the <code>XFontStructSet</code> is undefined. Also, note that all properties in the <code>XFontStruct</code> structures are in the STRING encoding. </p>
<p> The <code>XFontStruct</code> and font name lists are owned by Xlib and should not be modified or freed by the client. They will be freed by a call to <code>XFreeFontSet</code> with the associated <code>XFontSet</code>. Until freed, their contents will not be modified by Xlib. </p>
<p> The <code>XBaseFontNameListOfFontSet</code> function returns the original base font name list supplied by the client when the <code>XFontSet</code> was created. A null-terminated string containing a list of comma-separated font names is returned as the value of the function. White space may appear immediately on either side of separating commas. </p>
<p> If <code>XCreateFontSet</code> obtained an XLFD name from the font properties for the font specified by a non-XLFD base name, the <code>XBaseFontNameListOfFontSet</code> function will return the XLFD name instead of the non-XLFD base name. </p>
<p> The base font name list is owned by Xlib and should not be modified or freed by the client. It will be freed by a call to <code>XFreeFontSet</code> with the associated <code>XFontSet</code>. Until freed, its contents will not be modified by Xlib. </p>
<p> The <code>XLocaleOfFontSet</code> function returns the name of the locale bound to the specified <code>XFontSet</code>, as a null-terminated string. </p>
<p> The returned locale name string is owned by Xlib and should not be modified or freed by the client. It may be freed by a call to <code>XFreeFontSet</code> with the associated <code>XFontSet</code>. Until freed, it will not be modified by Xlib. </p>
<p> The <code>XContextDependentDrawing</code> function returns <code>True</code> if the drawing functions implement implicit text directionality or if text drawn with the font_set might include context-dependent drawing; otherwise, it returns <code>False</code>. </p>
<p> The <code>XContextualDrawing</code> function returns <code>True</code> if text drawn with the font set might include context-dependent drawing; otherwise, it returns <code>False</code>. </p>
<p> The <code>XDirectionalDependentDrawing</code> function returns <code>True</code> if the drawing functions implement implicit text directionality; otherwise, it returns <code>False</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreatefontset/">XCreateFontSet</a>(3), <a href="/docs/linux/man/3-xcreateom/">XCreateOM</a>(3), <a href="/docs/linux/man/3-xcreateoc/">XCreateOC</a>(3), <a href="/docs/linux/man/3-xextentsoffontset/">XExtentsOfFontSet</a>(3), <a href="/docs/linux/man/3-xfontsetextents/">XFontSetExtents</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
