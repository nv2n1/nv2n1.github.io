---
title: "xlistfontswithinfo(3)"
name: "xlistfontswithinfo"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xlistfontswithinfo/"
description: "XListFonts, XFreeFontNames, XListFontsWithInfo, XFreeFontInfo – obtain or free font names and information"
---

<p>XListFonts, XFreeFontNames, XListFontsWithInfo, XFreeFontInfo &#8211; obtain or free font names and information </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>char **XListFonts(Display *<i>display</i>, char *<i>pattern</i>, int <i>maxnames</i>, int *<i>actual_count_return</i>);</p>
<dd>int XFreeFontNames(char *<i>list</i>[]);</p>
<dd>char **XListFontsWithInfo(Display *<i>display</i>, char *<i>pattern</i>, int <i>maxnames</i>, int *<i>count_return</i>, XFontStruct **<i>info_return</i>);</p>
<dd>int XFreeFontInfo(char **<i>names</i>, XFontStruct *<i>free_info</i>, int <i>actual_count</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>actual_count</i></p>
<dd>Specifies the actual number of font names. </p>
<dt><i>actual_count_return</i></p>
<dd>Returns the actual number of font names.</p>
<dt><i>count_return</i></p>
<dd>Returns the actual number of matched font names.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>info_return</i></p>
<dd>Returns the font information.</p>
<dt><i>free_info</i></p>
<dd>Specifies the font information. </p>
<dt><i>list</i></p>
<dd>Specifies the array of strings you want to free.</p>
<dt><i>maxnames</i></p>
<dd>Specifies the maximum number of names to be returned.</p>
<dt><i>names</i></p>
<dd>Specifies the list of font names. </p>
<dt><i>pattern</i></p>
<dd>Specifies the null-terminated pattern string that can contain wildcard characters.</dl>
<h2>Description</h2>
<p>The <code>XListFonts</code> function returns an array of available font names (as controlled by the font search path; see <code>XSetFontPath</code>) that match the string you passed to the pattern argument. The pattern string can contain any characters, but each asterisk (*) is a wildcard for any number of characters, and each question mark (?) is a wildcard for a single character. If the pattern string is not in the Host Portable Character Encoding, the result is implementation-dependent. Use of uppercase or lowercase does not matter. Each returned string is null-terminated. If the data returned by the server is in the Latin Portable Character Encoding, then the returned strings are in the Host Portable Character Encoding. Otherwise, the result is implementation-dependent. If there are no matching font names, <code>XListFonts</code> returns NULL. The client should call <code>XFreeFontNames</code> when finished with the result to free the memory. </p>
<p> The <code>XFreeFontNames</code> function frees the array and strings returned by <code>XListFonts</code> or <code>XListFontsWithInfo</code>. </p>
<p> The <code>XListFontsWithInfo</code> function returns a list of font names that match the specified pattern and their associated font information. The list of names is limited to size specified by maxnames. The information returned for each font is identical to what <code>XLoadQueryFont</code> would return except that the per-character metrics are not returned. The pattern string can contain any characters, but each asterisk (*) is a wildcard for any number of characters, and each question mark (?) is a wildcard for a single character. If the pattern string is not in the Host Portable Character Encoding, the result is implementation-dependent. Use of uppercase or lowercase does not matter. Each returned string is null-terminated. If the data returned by the server is in the Latin Portable Character Encoding, then the returned strings are in the Host Portable Character Encoding. Otherwise, the result is implementation-dependent. If there are no matching font names, <code>XListFontsWithInfo</code> returns NULL. </p>
<p> To free only the allocated name array, the client should call <code>XFreeFontNames</code>. To free both the name array and the font information array or to free just the font information array, the client should call <code>XFreeFontInfo</code>. </p>
<p> The <code>XFreeFontInfo</code> function frees a font structure or an array of font structures and optionally an array of font names. If NULL is passed for names, no font names are freed. If a font structure for an open font (returned by <code>XLoadQueryFont</code>) is passed, the structure is freed, but the font is not closed; use <code>XUnloadFont</code> to close the font. </p>
<p> Note that <code>XListFontsWithInfo</code> is not thread-safe. If other threads make X requests on the same <code>Display</code>, then this function&#8217;s behavior is undefined.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xloadfont/">XLoadFont</a>(3), <a href="/docs/linux/man/3-xsetfontpath/">XSetFontPath</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
