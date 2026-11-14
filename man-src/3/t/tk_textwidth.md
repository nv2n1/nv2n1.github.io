---
title: "tk_textwidth(3)"
name: "tk_textwidth"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_textwidth/"
description: "Tk_MeasureChars, Tk_TextWidth, Tk_DrawChars, Tk_UnderlineChars – routines to measure and display simple single-line strings."
---

<p>Tk_MeasureChars, Tk_TextWidth, Tk_DrawChars, Tk_UnderlineChars &#8211; routines to measure and display simple single-line strings. </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
int
<code>Tk_MeasureChars(</code><i>tkfont, string, numBytes, maxPixels, flags, lengthPtr</i><code>)</code>
int
<code>Tk_TextWidth(</code><i>tkfont, string, numBytes</i><code>)</code>
<code>Tk_DrawChars(</code><i>display, drawable, gc, tkfont, string, numBytes, x, y</i><code>)</code>
<code>Tk_UnderlineChars(</code><i>display, drawable, gc, tkfont, string, x, y, firstByte, lastByte</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Font <i>tkfont</i> (in) Token for font in which text is to be drawn or measured. Must have been returned by a previous call to <code>Tk_GetFont</code>.</p>
<dd>const char <i>*string</i> (in) Text to be measured or displayed. Need not be null terminated. Any non-printing meta-characters in the string (such as tabs, newlines, and other control characters) will be measured or displayed in a platform-dependent manner.</p>
<dd>int <i>numBytes</i> (in) The maximum number of bytes to consider when measuring or drawing <i>string</i>. Must be greater than or equal to 0.</p>
<dd>int <i>maxPixels</i> (in) If <i>maxPixels</i> is &gt;= 0, it specifies the longest permissible line length in pixels. Characters from <i>string</i> are processed only until this many pixels have been covered. If <i>maxPixels</i> is &lt; 0, then the line length is unbounded and the <i>flags</i> argument is ignored.</p>
<dd>int <i>flags</i> (in) Various flag bits OR-ed together: <code>TK_PARTIAL_OK</code> means include a character as long as any part of it fits in the length given by <i>maxPixels</i>; otherwise, a character must fit completely to be considered. <code>TK_WHOLE_WORDS</code> means stop on a word boundary, if possible. If <code>TK_AT_LEAST_ONE</code> is set, it means return at least one character even if no characters could fit in the length given by <i>maxPixels</i>. If <code>TK_AT_LEAST_ONE</code> is set and <code>TK_WHOLE_WORDS</code> is also set, it means that if not even one word fits on the line, return the first few letters of the word that did fit; if not even one letter of the word fit, then the first letter will still be returned.</p>
<dd>int <i>*lengthPtr</i> (out) Filled with the number of pixels occupied by the number of characters returned as the result of <code>Tk_MeasureChars</code>.</p>
<dd>Display <i>*display</i> (in) Display on which to draw.</p>
<dd>Drawable <i>drawable</i> (in) Window or pixmap in which to draw.</p>
<dd>GC <i>gc</i> (in) Graphics context for drawing characters. The font selected into this GC must be the same as the <i>tkfont</i>.</p>
<dd>int <i>x, y</i> (in) Coordinates at which to place the left edge of the baseline when displaying <i>string</i>.</p>
<dd>int <i>firstByte</i> (in) The index of the first byte of the first character to underline in the <i>string</i>. Underlining begins at the left edge of this character.</p>
<dd>int <i>lastByte</i> (in) The index of the first byte of the last character up to which the underline will be drawn. The character specified by <i>lastByte</i> will not itself be underlined.
</dl>
<h2>Description</h2>
<p>These routines are for measuring and displaying simple single-font, single-line strings. To measure and display single-font, multi-line, justified text, refer to the documentation for <code>Tk_ComputeTextLayout</code>. There is no programming interface in the core of Tk that supports multi-font, multi-line text; support for that behavior must be built on top of simpler layers. Note that the interfaces described here are byte-oriented not character-oriented, so index values coming from Tcl scripts need to be converted to byte offsets using the <code>Tcl_UtfAtIndex</code> and related routines. </p>
<p> A glyph is the displayable picture of a letter, number, or some other symbol. Not all character codes in a given font have a glyph. Characters such as tabs, newlines/returns, and control characters that have no glyph are measured and displayed by these procedures in a platform-dependent manner; under X, they are replaced with backslashed escape sequences, while under Windows and Macintosh hollow or solid boxes may be substituted. Refer to the documentation for <code>Tk_ComputeTextLayout</code> for a programming interface that supports the platform-independent expansion of tab characters into columns and newlines/returns into multi-line text. </p>
<p> <code>Tk_MeasureChars</code> is used both to compute the length of a given string and to compute how many characters from a string fit in a given amount of space. The return value is the number of bytes from <i>string</i> that fit in the space specified by <i>maxPixels</i> subject to the conditions described by <i>flags</i>. If all characters fit, the return value will be <i>numBytes</i>. <i>*lengthPtr</i> is filled with the computed width, in pixels, of the portion of the string that was measured. For example, if the return value is 5, then <i>*lengthPtr</i> is filled with the distance between the left edge of <i>string</i>[0] and the right edge of <i>string</i>[4]. </p>
<p> <code>Tk_TextWidth</code> is a wrapper function that provides a simpler interface to the <code>Tk_MeasureChars</code> function. The return value is how much space in pixels the given <i>string</i> needs. </p>
<p> <code>Tk_DrawChars</code> draws the <i>string</i> at the given location in the given <i>drawable</i>. </p>
<p> <code>Tk_UnderlineChars</code> underlines the given range of characters in the given <i>string</i>. It does not draw the characters (which are assumed to have been displayed previously by <code>Tk_DrawChars</code>); it just draws the underline. This procedure is used to underline a few characters without having to construct an underlined font. To produce natively underlined text, the appropriate underlined font should be constructed and used.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/n-font/">font</a>(n), <a href="/docs/linux/man/3-fontid/">FontId</a>(3)</p>
<h2>Keywords</h2>
<p>font, measurement</p>
