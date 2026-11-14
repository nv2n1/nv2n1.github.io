---
title: "tk_getfontmetrics(3)"
name: "tk_getfontmetrics"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tk_getfontmetrics/"
description: "Tk_FontId, Tk_GetFontMetrics, Tk_PostscriptFontName – accessor functions for fonts"
---

<p>Tk_FontId, Tk_GetFontMetrics, Tk_PostscriptFontName &#8211; accessor functions for fonts </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tk.h&gt;</code>
Font
<code>Tk_FontId(</code><i>tkfont</i><code>)</code>
<code>Tk_GetFontMetrics(</code><i>tkfont, fmPtr</i><code>)</code>
int
<code>Tk_PostscriptFontName(</code><i>tkfont, dsPtr</i><code>)</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tk_Font <i>tkfont</i> (in) Opaque font token being queried. Must have been returned by a previous call to <code>Tk_GetFont</code>.</p>
<dd>Tk_FontMetrics <i>*fmPtr</i> (out) Pointer to structure in which the font metrics for <i>tkfont</i> will be stored. See <code>DATA STRUCTURES</code> below for details.</p>
<dd>Tcl_DString <i>*dsPtr</i> (out) Pointer to an initialized <code>Tcl_DString</code> to which the name of the Postscript font that corresponds to <i>tkfont</i> will be appended.
</dl>
<h2>Description</h2>
<p>Given a <i>tkfont</i>, <code>Tk_FontId</code> returns the token that should be selected into an XGCValues structure in order to construct a graphics context that can be used to draw text in the specified font. </p>
<p> <code>Tk_GetFontMetrics</code> computes the ascent, descent, and linespace of the <i>tkfont</i> in pixels and stores those values in the structure pointer to by <i>fmPtr</i>. These values can be used in computations such as to space multiple lines of text, to align the baselines of text in different fonts, and to vertically align text in a given region. See the documentation for the <code>font</code> command for definitions of the terms ascent, descent, and linespace, used in font metrics. </p>
<p> <code>Tk_PostscriptFontName</code> maps a <i>tkfont</i> to the corresponding Postscript font name that should be used when printing. The return value is the size in points of the <i>tkfont</i> and the Postscript font name is appended to <i>dsPtr</i>. <i>DsPtr</i> must refer to an initialized <code>Tcl_DString</code>. Given a &#8220;reasonable&#8221; Postscript printer, the following screen font families should print correctly:</p>
<dl COMPACT>
<dd><code>Avant Garde</code>, <code>Arial</code>, <code>Bookman</code>, <code>Courier</code>, <code>Courier New</code>, <code>Geneva</code>, <code>Helvetica</code>, <code>Monaco</code>, <code>New Century Schoolbook</code>, <code>New York</code>, <code>Palatino</code>, <code>Symbol</code>, <code>Times</code>, <code>Times New Roman</code>, <code>Zapf Chancery</code>, and <code>Zapf Dingbats</code>.</dl>
<p> Any other font families may not print correctly because the computed Postscript font name may be incorrect or not exist on the printer.</p>
<h2>Data Structures</h2>
<p>The <code>Tk_FontMetrics</code> data structure is used by <code>Tk_GetFontMetrics</code> to return information about a font and is defined as follows:</p>
<dl COMPACT>
<dd>
<pre>typedef struct Tk_FontMetrics {
 int <i>ascent</i>;
 int <i>descent</i>;
 int <i>linespace</i>;
} Tk_FontMetrics;</pre>
</dl>
<p> The <i>ascent</i> field is the amount in pixels that the tallest letter sticks up above the baseline, plus any extra blank space added by the designer of the font. </p>
<p> The <i>descent</i> is the largest amount in pixels that any letter sticks below the baseline, plus any extra blank space added by the designer of the font. </p>
<p> The <i>linespace</i> is the sum of the ascent and descent. How far apart two lines of text in the same font should be placed so that none of the characters in one line overlap any of the characters in the other line.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/n-font/">font</a>(n), <a href="/docs/linux/man/3-measurechar/">MeasureChar</a>(3)</p>
<h2>Keywords</h2>
<p>font, measurement, Postscript</p>
