---
title: "xcreatefontset(3)"
name: "xcreatefontset"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcreatefontset/"
description: "XCreateFontSet, XFreeFontSet – create and free an international text drawing font set"
---

<p>XCreateFontSet, XFreeFontSet &#8211; create and free an international text drawing font set </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>XFontSet XCreateFontSet(Display *<i>display</i>, char *<i>base_font_name_list</i>, char ***<i>missing_charset_list_return</i>, int *<i>missing_charset_count_return</i>, char **<i>def_string_return</i>);</p>
<dd>void XFreeFontSet(Display *<i>display</i>, XFontSet <i>font_set</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>base_font_name_list</i></p>
<dd>Specifies the base font names.</p>
<dt><i>def_string_return</i></p>
<dd>Returns the string drawn for missing charsets.</p>
<dt><i>font_set</i></p>
<dd>Specifies the font set.</p>
<dt><i>missing_charset_count_return</i></p>
<dd>Returns the number of missing charsets.</p>
<dt><i>missing_charset_list_return</i></p>
<dd>Returns the missing charsets.</dl>
<h2>Description</h2>
<p>The <code>XCreateFontSet</code> function creates a font set for the specified display. The font set is bound to the current locale when <code>XCreateFontSet</code> is called. The font set may be used in subsequent calls to obtain font and character information and to image text in the locale of the font set. </p>
<p> The base_font_name_list argument is a list of base font names that Xlib uses to load the fonts needed for the locale. The base font names are a comma-separated list. The string is null-terminated and is assumed to be in the Host Portable Character Encoding; otherwise, the result is implementation-dependent. White space immediately on either side of a separating comma is ignored. </p>
<p> Use of XLFD font names permits Xlib to obtain the fonts needed for a variety of locales from a single locale-independent base font name. The single base font name should name a family of fonts whose members are encoded in the various charsets needed by the locales of interest. </p>
<p> An XLFD base font name can explicitly name a charset needed for the locale. This allows the user to specify an exact font for use with a charset required by a locale, fully controlling the font selection. </p>
<p> If a base font name is not an XLFD name, Xlib will attempt to obtain an XLFD name from the font properties for the font. If this action is successful in obtaining an XLFD name, the <code>XBaseFontNameListOfFontSet</code> function will return this XLFD name instead of the client-supplied name. </p>
<p> Xlib uses the following algorithm to select the fonts that will be used to display text with the <code>XFontSet</code>. </p>
<p> For each font charset required by the locale, the base font name list is searched for the first appearance of one of the following cases that names a set of fonts that exist at the server:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd>The first XLFD-conforming base font name that specifies the required charset or a superset of the required charset in its <code>CharSetRegistry</code> and <code>CharSetEncoding</code> fields. The implementation may use a base font name whose specified charset is a superset of the required charset, for example, an ISO8859-1 font for an ASCII charset.</p>
<dt>&bull;</p>
<dd>The first set of one or more XLFD-conforming base font names that specify one or more charsets that can be remapped to support the required charset. The Xlib implementation may recognize various mappings from a required charset to one or more other charsets and use the fonts for those charsets. For example, JIS Roman is ASCII with tilde and backslash replaced by yen and overbar; Xlib may load an ISO8859-1 font to support this character set if a JIS Roman font is not available.</p>
<dt>&bull;</p>
<dd>The first XLFD-conforming font name or the first non-XLFD font name for which an XLFD font name can be obtained, combined with the required charset (replacing the <code>CharSetRegistry</code> and <code>CharSetEncoding</code> fields in the XLFD font name). As in case 1, the implementation may use a charset that is a superset of the required charset.</p>
<dt>&bull;</p>
<dd>The first font name that can be mapped in some implementation-dependent manner to one or more fonts that support imaging text in the charset.</dl>
<p> For example, assume that a locale required the charsets: </p>
<p> ISO8859-1 JISX0208.1983 JISX0201.1976 GB2312-1980.0 </p>
<p> The user could supply a base_font_name_list that explicitly specifies the charsets, ensuring that specific fonts are used if they exist. For example: </p>
<p> &quot;-JIS-Fixed-Medium-R-Normal&#8211;26-180-100-100-C-240-JISX0208.1983-0,\ -JIS-Fixed-Medium-R-Normal&#8211;26-180-100-100-C-120-JISX0201.1976-0,\ -GB-Fixed-Medium-R-Normal&#8211;26-180-100-100-C-240-GB2312-1980.0,\ -Adobe-Courier-Bold-R-Normal&#8211;25-180-75-75-M-150-ISO8859-1&quot; </p>
<p> Alternatively, the user could supply a base_font_name_list that omits the charsets, letting Xlib select font charsets required for the locale. For example: </p>
<p> &quot;-JIS-Fixed-Medium-R-Normal&#8211;26-180-100-100-C-240,\ -JIS-Fixed-Medium-R-Normal&#8211;26-180-100-100-C-120,\ -GB-Fixed-Medium-R-Normal&#8211;26-180-100-100-C-240,\ -Adobe-Courier-Bold-R-Normal&#8211;25-180-100-100-M-150&quot; </p>
<p> Alternatively, the user could simply supply a single base font name that allows Xlib to select from all available fonts that meet certain minimum XLFD property requirements. For example: </p>
<p> &quot;-*-*-*-R-Normal&#8211;*-180-100-100-*-*&quot; </p>
<p> If <code>XCreateFontSet</code> is unable to create the font set, either because there is insufficient memory or because the current locale is not supported, <code>XCreateFontSet</code> returns NULL, missing_charset_list_return is set to NULL, and missing_charset_count_return is set to zero. If fonts exist for all of the charsets required by the current locale, <code>XCreateFontSet</code> returns a valid <code>XFontSet</code>, missing_charset_list_return is set to NULL, and missing_charset_count_return is set to zero. </p>
<p> If no font exists for one or more of the required charsets, <code>XCreateFontSet</code> sets missing_charset_list_return to a list of one or more null-terminated charset names for which no font exists and sets missing_charset_count_return to the number of missing fonts. The charsets are from the list of the required charsets for the encoding of the locale and do not include any charsets to which Xlib may be able to remap a required charset. </p>
<p> If no font exists for any of the required charsets or if the locale definition in Xlib requires that a font exist for a particular charset and a font is not found for that charset, <code>XCreateFontSet</code> returns NULL. Otherwise, <code>XCreateFontSet</code> returns a valid <code>XFontSet</code> to font_set. </p>
<p> When an Xmb/wc drawing or measuring function is called with an <code>XFontSet</code> that has missing charsets, some characters in the locale will not be drawable. If def_string_return is non-NULL, <code>XCreateFontSet</code> returns a pointer to a string that represents the glyphs that are drawn with this <code>XFontSet</code> when the charsets of the available fonts do not include all font glyphs required to draw a codepoint. The string does not necessarily consist of valid characters in the current locale and is not necessarily drawn with the fonts loaded for the font set, but the client can draw and measure the default glyphs by including this string in a string being drawn or measured with the <code>XFontSet</code>. </p>
<p> If the string returned to def_string_return is the empty string (&quot;&quot;), no glyphs are drawn, and the escapement is zero. The returned string is null-terminated. It is owned by Xlib and should not be modified or freed by the client. It will be freed by a call to <code>XFreeFontSet</code> with the associated <code>XFontSet</code>. Until freed, its contents will not be modified by Xlib. </p>
<p> The client is responsible for constructing an error message from the missing charset and default string information and may choose to continue operation in the case that some fonts did not exist. </p>
<p> The returned <code>XFontSet</code> and missing charset list should be freed with <code>XFreeFontSet</code> and <code>XFreeStringList</code>, respectively. The client-supplied base_font_name_list may be freed by the client after calling <code>XCreateFontSet</code>. </p>
<p> The <code>XFreeFontSet</code> function frees the specified font set. The associated base font name list, font name list, <code>XFontStruct</code> list, and <code>XFontSetExtents</code>, if any, are freed.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xextentsoffontset/">XExtentsofFontSet</a>(3), <a href="/docs/linux/man/3-xfontsoffontset/">XFontsOfFontSet</a>(3), <a href="/docs/linux/man/3-xfontsetextents/">XFontSetExtents</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
