---
title: "xft(3)"
name: "xft"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xft/"
description: "Xft – X FreeType interface library"
---

<p>&nbsp;Xft &#8211; X FreeType interface library </p>
<h2>Description</h2>
<p><code>Xft</code> is a simple library designed to interface the FreeType rasterizer with the X Rendering Extension. This manual page barely scratches the surface of this library.</p>
<h2>Header File</h2>
<p><code>#include &lt;X11/Xft/Xft.h&gt;</code></p>
<h2>Constants</h2>
<dl COMPACT>
<dt><code>XFT_MAJOR</code></p>
<dd>is the major version number of <code>Xft</code>.</p>
<dt><code>XFT_MINOR</code></p>
<dd>is the minor version number of <code>Xft</code>.</p>
<dt><code>XFT_REVISION</code></p>
<dd>is the revision number of <code>Xft</code>.</p>
<dt><code>XFT_VERSION</code></p>
<dd>is <code>XFT_MAJOR</code> times 10000 (ten thousand), plus <code>XFT_MINOR</code> times 100, plus <code>XFT_REVISION</code>.</p>
<dt><code>XftVersion</code></p>
<dd>is an alias for <code>XFT_VERSION</code>.</dl>
<p> The following example illustrates how <code>Xft</code>&#8216;s version constants might be used: </p>
<pre> #if (XFT_VERSION &gt;= 20107)
 (void) puts(&quot;Version 2.1.7 or later of the Xft library is in&quot;
 &quot; use.&quot;);
 #else
 (void) printf(&quot;Insufficient version of Xft (%d.%d.%d) installed;
 &quot; need at least version 2.1.7.
&quot;, XFT_MAJOR,
 XFT_MINOR,
 XFT_REVISION);
 #endif</pre>
<h2>Data Types</h2>
<dl COMPACT>
<dt><code>XftFont</code></p>
<dd>
<pre>typedef struct _XftFont {
 int ascent;
 int descent;
 int height;
 int max_advance_width;
 FcCharSet *charset;
 FcPattern *pattern;
} XftFont;</pre>
<p>An <code>XftFont</code> is the primary data structure of interest to programmers using <code>Xft</code>; it contains general font metrics and pointers to the Fontconfig character set and pattern associated with the font. The <code>FcCharSet</code> and <code>FcPattern</code> data types are defined by the Fontconfig library.</p>
<dd><code>XftFont</code>s are populated with any of <code>XftFontOpen</code>(), <code>XftFontOpenName</code>(), <code>XftFontOpenXlfd</code>(), <code>XftFontOpenInfo</code>(), or <code>XftFontOpenPattern</code>(). <code>XftFontCopy</code>() is used to duplicate <code>XftFont</code>s, and <code>XftFontClose</code>() is used to mark an <code>XftFont</code> as unused. <code>XftFont</code>s are internally allocated, reference-counted, and freed by <code>Xft</code>; the programmer does not ordinarily need to allocate or free storage for them.</p>
<dd><code>XftDrawGlyphs</code>(), the <code>XftDrawString</code>*() family, <code>XftDrawCharSpec</code>(), and <code>XftDrawGlyphSpec</code>() use <code>XftFont</code>s to render text to an <code>XftDraw</code> object, which may correspond to either a core X drawable or an X Rendering Extension drawable.</p>
<dd><code>XftGlyphExtents</code>() and the <code>XftTextExtents</code>*() family are used to determine the extents (maximum dimensions) of an <code>XftFont</code>.</p>
<dd>An <code>XftFont</code>&#8216;s glyph or character coverage can be determined with <code>XftFontCheckGlyph</code>() or <code>XftCharExists</code>(). <code>XftCharIndex</code>() returns the <code>XftFont</code>-specific character index corresponding to a given Unicode codepoint.</p>
<dd><code>XftGlyphRender</code>(), <code>XftGlyphSpecRender</code>(), <code>XftCharSpecRender</code>(), and the <code>XftTextRender</code>*() family use <code>XftFont</code>s to draw into X Rendering Extension <code>Picture</code> structures. <code>Note:</code> <code>XftDrawGlyphs</code>(), the <code>XftDrawString</code>*() family, <code>XftDrawCharSpec</code>(), and <code>XftDrawGlyphSpec</code>() provide a means of rendering fonts that is independent of the availability of the X Rendering Extension on the X server.</p>
<dt><code>XftFontInfo</code></p>
<dd>is an opaque object that stores information about a font. <code>XftFontInfo</code> structures are created with <code>XftFontInfoCreate</code>(), freed with <code>XftFontInfoDestroy</code>(), and compared with <code>XftFontInfoEqual</code>(). <code>XftFontInfo</code> objects are internally allocated and freed by <code>Xft</code>; the programmer does not ordinarily need to allocate or free storage for them.</p>
<dd>Each <code>XftFontInfo</code> structure in use is associated with a unique identifier, which can be retrieved with <code>XftFontInfoHash</code>(). An <code>XftFont</code> can be opened based on <code>XftFontInfo</code> data with <code>XftFontOpenInfo</code>().</p>
<dt><code>XftColor</code></p>
<dd>
<pre>typedef struct _XftColor {
 unsigned long pixel;
 XRenderColor color;
} XftColor;</pre>
<p>An <code>XftColor</code> object permits text and other items to be rendered in a particular color (or the closest approximation offered by the X visual in use). The <code>XRenderColor</code> data type is defined by the X Render Extension library.</p>
<dd><code>XftColorAllocName</code>() and <code>XftColorAllocValue</code>() request a color allocation from the X server (if necessary) and initialize the members of <code>XftColor</code>. <code>XftColorFree</code>() instructs the X server to free the color currently allocated for an <code>XftColor</code>.</p>
<dd>One an <code>XftColor</code> has been initialized, <code>XftDrawSrcPicture</code>(), <code>XftDrawGlyphs</code>(), the <code>XftDrawString</code>*() family, <code>XftDrawCharSpec</code>(), <code>XftDrawCharFontSpec</code>(), <code>XftDrawGlyphSpec</code>(), <code>XftDrawGlyphFontSpec</code>(), and <code>XftDrawRect</code>() may be used to draw various objects using it.</p>
<dt><code>XftDraw</code></p>
<dd>is an opaque object which holds information used to render to an X drawable using either the core protocol or the X Rendering extension.</p>
<dd><code>XftDraw</code> objects are created with any of <code>XftDrawCreate</code>() (which associates an <code>XftDraw</code> with an existing X drawable), <code>XftDrawCreateBitmap</code>(), or <code>XftDrawCreateAlpha</code>(), and destroyed with <code>XftDrawDestroy</code>(). The X drawable associated with an <code>XftDraw</code> can be changed with <code>XftDrawChange</code>(). <code>XftDraw</code>s are internally allocated and freed by <code>Xft</code>; the programmer does not ordinarily need to allocate or free storage for them.</p>
<dd>The X <code>Display</code>, <code>Drawable</code>, <code>Colormap</code>, and <code>Visual</code> of an <code>XftDraw</code> can be queried with <code>XftDrawDisplay</code>(), <code>XftDrawDrawable</code>(), <code>XftDrawColormap</code>(), and <code>XftDrawVisual</code>(), respectively. The X Rendering Extension <code>Picture</code> associated with an <code>XftDraw</code> is returned by <code>XftDrawPicture</code>().</p>
<dt><code>XftCharSpec</code></p>
<dd>
<pre>typedef struct _XftCharSpec {
 FcChar32 ucs4;
 short x;
 short y;
} XftCharSpec;</pre>
<dd>The <code>FcChar32</code> data type is defined by the Fontconfig library.</p>
<dt><code>XftCharFontSpec</code></p>
<dd>
<pre>typedef struct _XftCharFontSpec {
 XftFont *font;
 FcChar32 ucs4;
 short x;
 short y;
} XftCharFontSpec;</pre>
<dd>The <code>FcChar32</code> data type is defined by the Fontconfig library.</p>
<dt><code>XftGlyphSpec</code></p>
<dd>
<pre>typedef struct _XftGlyphSpec {
 FT_UInt glyph;
 short x;
 short y;
} XftGlyphSpec;</pre>
<dd>The <code>FT_UInt</code> data type is defined by the FreeType library.</p>
<dt><code>XftGlyphFontSpec</code></p>
<dd>
<pre>typedef struct _XftGlyphFontSpec {
 XftFont *font;
 FT_UInt glyph;
 short x;
 short y;
} XftGlyphFontSpec;</pre>
<dd>The <code>FT_UInt</code> data type is defined by the FreeType library.</dl>
<h2>Functions</h2>
<h3>Opening and Matching Fonts</h3>
<pre><code>XftFont *</code>
<code>XftFontOpen (Display *</code><i>dpy</i><code>,</code>
<code> int </code><i>screen</i><code>,</code>
<code> ...);</code></pre>
<p><code>XftFontOpen</code> takes a list of pattern element triples of the form <i>field</i>,<i> type</i>,<i> value</i> (terminated with a NULL), matches that pattern against the available fonts, and opens the matching font, sizing it correctly for screen number <i>screen</i> on display <i>dpy</i>. The <code>Display</code> data type is defined by the X11 library. Returns NULL if no match is found. </p>
<p> Example: </p>
<pre> font = XftFontOpen (dpy, screen,
 XFT_FAMILY, XftTypeString, &quot;charter&quot;,
 XFT_SIZE, XftTypeDouble, 12.0,
 NULL);</pre>
<p>This opens the &#8220;charter&#8221; font at 12 points. The point size is automatically converted to the correct pixel size based on the resolution of the monitor. </p>
<pre><code>XftFont *</code>
<code>XftFontOpenName (Display *</code><i>dpy</i><code>,</code>
<code> int </code><i>screen</i><code>,</code>
<code> unsigned char *</code><i>name</i><code>);</code></pre>
<p><code>XftFontOpenName</code> behaves as <code>XftFontOpen</code> does, except that it takes a Fontconfig pattern string (which is passed to the Fontconfig library&#8217;s <code>FcNameParse</code>() function). </p>
<pre><code>XftFont *</code>
<code>XftFontOpenXlfd (Display *</code><i>dpy</i><code>,</code>
<code> int </code><i>screen</i><code>,</code>
<code> unsigned char *</code><i>xlfd</i><code>)</code></pre>
<p><code>XftFontOpenXlfd</code> behaves as <code>XftFontOpen</code> does, except that it takes a string containing an X Logical Font Description (XLFD). </p>
<pre><code>FcPattern *</code>
<code>XftFontMatch (Display *</code><i>dpy</i><code>,</code>
<code> int </code><i>screen</i><code>,</code>
<code> FcPattern *</code><i>pattern</i><code>,</code>
<code> FcResult *</code><i>result</i><code>);</code></pre>
<p>Also used internally by the <code>XftFontOpen</code>* functions, <code>XftFontMatch</code> can also be used directly to determine the Fontconfig font pattern resulting from an Xft font open request. The <code>FcPattern</code> and <code>FcResult</code> data types are defined by the Fontconfig library.</p>
<h3>Determining the Pixel Extents of a Text String</h3>
<pre><code>void</code>
<code>XftTextExtents8 (Display *</code><i>dpy</i><code>,</code>
<code> XftFont *</code><i>font</i><code>,</code>
<code> FcChar8 *</code><i>string</i><code>,</code>
<code> int </code><i>len</i><code>,</code>
<code> XGlyphInfo *</code><i>extents</i><code>);</code></pre>
<p><code>XftTextExtents8</code> computes the pixel extents on display <i>dpy</i> of no more than <i>len</i> glyphs of a <i>string</i> consisting of eight-bit characters when drawn with <i>font</i>, storing them in <i>extents</i>. The <code>FcChar8</code> data type is defined by the Fontconfig library, and the <code>XGlyphInfo</code> data type is defined by the X Rendering Extension library. </p>
<pre><code>void</code>
<code>XftTextExtents16 (Display *</code><i>dpy</i><code>,</code>
<code> XftFont *</code><i>font</i><code>,</code>
<code> FcChar16 *</code><i>string</i><code>,</code>
<code> int </code><i>len</i><code>,</code>
<code> XGlyphInfo *</code><i>extents</i><code>);</code></pre>
<p><code>XftTextExtents16</code> computes the pixel extents on display <i>dpy</i> of no more than <i>len</i> glyphs of a <i>string</i> consisting of sixteen-bit characters when drawn with <i>font</i>, storing them in <i>extents</i>. The <code>FcChar16</code> data type is defined by the Fontconfig library, and the <code>XGlyphInfo</code> data type is defined by the X Rendering Extension library. </p>
<pre><code>void</code>
<code>XftTextExtents32 (Display *</code><i>dpy</i><code>,</code>
<code> XftFont *</code><i>font</i><code>,</code>
<code> FcChar32 *</code><i>string</i><code>,</code>
<code> int </code><i>len</i><code>,</code>
<code> XGlyphInfo *</code><i>extents</i><code>);</code></pre>
<p><code>XftTextExtents32</code> computes the pixel extents on display <i>dpy</i> of no more than <i>len</i> glyphs of a <i>string</i> consisting of thirty-two-bit characters when drawn with <i>font</i>, storing them in <i>extents</i>. The <code>FcChar32</code> data type is defined by the Fontconfig library, and the <code>XGlyphInfo</code> data type is defined by the X Rendering Extension library. </p>
<pre><code>void</code>
<code>XftTextExtentsUtf8 (Display *</code><i>dpy</i><code>,</code>
<code> XftFont *</code><i>font</i><code>,</code>
<code> FcChar8 *</code><i>string</i><code>,</code>
<code> int </code><i>len</i><code>,</code>
<code> XGlyphInfo *</code><i>extents</i><code>);</code></pre>
<p><code>XftTextExtentsUtf8</code> computes the pixel extents on display <i>dpy</i> of no more than <i>len</i> bytes of a UTF-8 encoded <i>string</i> when drawn with <i>font</i>, storing them in <i>extents</i>. The <code>XGlyphInfo</code> data type is defined by the X Rendering Extension library. </p>
<pre><code>void</code>
<code>XftTextExtentsUtf16 (Display *</code><i>dpy</i><code>,</code>
<code> XftFont *</code><i>font</i><code>,</code>
<code> FcChar8 *</code><i>string</i><code>,</code>
<code> FcEndian </code><i>endian</i><code>,</code>
<code> int </code><i>len</i><code>,</code>
<code> XGlyphInfo *</code><i>extents</i><code>);</code></pre>
<p><code>XftTextExtentsUtf16</code> computes the pixel extents on display <i>dpy</i> of no more than <i>len</i> bytes of a UTF-16LE- or UTF-16BE-encoded <i>string</i> when drawn with <i>font</i>, storing them in <i>extents</i>. The endianness of <i>string</i> must be specified in <i>endian</i>. The <code>FcEndian</code> data type is defined by the Fontconfig library, and the <code>XGlyphInfo</code> data type is defined by the X Rendering Extension library. </p>
<pre><code>void</code>
<code>XftGlyphExtents (Display *</code><i>dpy</i><code>,</code>
<code> XftFont *</code><i>font</i><code>,</code>
<code> FT_UInt *</code><i>glyphs</i><code>,</code>
<code> int </code><i>nglyphs</i><code>,</code>
<code> XGlyphInfo *</code><i>extents</i><code>);</code></pre>
<p>Also used internally by the <code>XftTextExtents</code>* functions, <code>XftGlyphExtents</code> computes the pixel extents on display <i>dpy</i> of no more than <i>nglyphs</i> in the array <i>glyphs</i> drawn with <i>font</i>, storing them in <i>extents</i>. The <code>FT_UInt</code> data type is defined by the FreeType library, and the <code>XGlyphInfo</code> data type is defined by the X Rendering Extension library.</p>
<h3>Drawing Strings (and Other Things)</h3>
<pre><code>XftDraw *</code>
<code>XftDrawCreate (Display *</code><i>dpy</i><code>,</code>
<code> Drawable </code><i>drawable</i><code>,</code>
<code> Visual *</code><i>visual</i><code>,</code>
<code> Colormap </code><i>colormap</i><code>);</code></pre>
<p><code>XftDrawCreate</code> creates a structure that can be used to render text and rectangles using the specified <i>drawable</i>, <i>visual</i>, and <i>colormap</i> on <i>display</i>. The <code>Drawable</code>, <code>Visual</code>, and <code>Colormap</code> data types are defined by the X11 library. </p>
<pre><code>XftDraw *</code>
<code>XftDrawCreateBitmap (Display *</code><i>dpy</i><code>,</code>
<code> Pixmap </code><i>bitmap</i><code>);</code></pre>
<p><code>XftDrawCreateBitmap</code> behaves as <code>XftDrawCreate</code>, except it uses an X pixmap of color depth 1 instead of an X drawable. The <code>Pixmap</code> data type is defined by the X11 library. </p>
<pre><code>XftDraw *</code>
<code>XftDrawCreateAlpha (Display *</code><i>dpy</i><code>,</code>
<code> Pixmap </code><i>pixmap</i><code>,</code>
<code> int </code><i>depth</i><code>);</code></pre>
<p><code>XftDrawCreateAlpha</code> behaves as <code>XftDrawCreate</code>, except it uses an X pixmap of color depth <i>depth</i> instead of an X drawable. The <code>Pixmap</code> data type is defined by the X11 library. </p>
<pre><code>void</code>
<code>XftDrawChange (XftDraw *</code><i>draw</i><code>,</code>
<code> Drawable </code><i>drawable</i><code>);</code></pre>
<p><code>XftDrawChange</code> changes the X drawable association of the existing Xft draw object <i>draw</i> from its current value to <i>drawable</i>. </p>
<pre><code>Display *</code>
<code>XftDrawDisplay (XftDraw *</code><i>draw</i><code>);</code></pre>
<p><code>XftDrawDisplay</code> returns a pointer to the display associated with the Xft draw object <i>draw</i>. </p>
<pre><code>Drawable</code>
<code>XftDrawDrawable (XftDraw *</code><i>draw</i><code>);</code></pre>
<p><code>XftDrawDrawable</code> returns the X drawable associated with the Xft draw object <i>draw</i>. </p>
<pre><code>Colormap</code>
<code>XftDrawColormap (XftDraw *</code><i>draw</i><code>);</code></pre>
<p><code>XftDrawColormap</code> returns the colormap associatied with the Xft draw object <i>draw</i>. </p>
<pre><code>Visual *</code>
<code>XftDrawVisual (XftDraw *</code><i>draw</i><code>);</code></pre>
<p><code>XftDrawVisual</code> returns a pointer to the visual associated with the Xft draw object <i>draw</i>. </p>
<pre><code>Picture</code>
<code>XftDrawPicture (XftDraw *</code><i>draw</i><code>);</code></pre>
<p><code>XftDrawPicture</code> returns the picture associated with the Xft draw object <i>draw</i>. If the the X server does not support the X Rendering Extension, 0 is returned. </p>
<pre><code>Picture</code>
<code>XftDrawSrcPicture (XftDraw *</code><i>draw</i><code>,</code>
<code> XftColor *</code><i>color</i><code>);</code></pre>
<p>This function is never called if the X server doesn&#8217;t support the X Rendering Extension; instead, <code>XftGlyphCore</code> is used. </p>
<pre><code>void</code>
<code>XftDrawDestroy (XftDraw *</code><i>draw</i><code>);</code></pre>
<p><code>XftDrawDestroy</code> destroys <i>draw</i> (created by one of the <code>XftCreate</code> functions) and frees the memory that was allocated for it. </p>
<pre><code>void</code>
<code>XftDrawString8 (XftDraw *</code><i>d</i><code>,</code>
<code> XftColor *</code><i>color</i><code>,</code>
<code> XftFont *</code><i>font</i><code>,</code>
<code> int </code><i>x</i><code>,</code>
<code> int </code><i>y</i><code>,</code>
<code> unsigned char *</code><i>string</i><code>,</code>
<code> int </code><i>len</i><code>);</code></pre>
<p><code>XftDrawString8</code> draws no more than <i>len</i> glyphs of <i>string</i> to Xft drawable <i>d</i> using <i>font</i> in <i>color</i> at position <i>x</i>,<i> y</i>. </p>
<pre><code>void</code>
<code>XftDrawRect (XftDraw *</code><i>d</i><code>,</code>
<code> XftColor *</code><i>color</i><code>,</code>
<code> int </code><i>x</i><code>,</code>
<code> int </code><i>y</i><code>,</code>
<code> unsigned int </code><i>width</i><code>,</code>
<code> unsigned int </code><i>height</i><code>);</code></pre>
<p><code>XftDrawRect</code> draws a solid rectangle of the specified <i>color</i>, <i>width</i>, and <i>height</i> at position <i>x</i>,<i> y</i> to Xft drawable <i>d</i>.</p>
<h2>Compatibility</h2>
<p>As of version 2, <code>Xft</code> has become relatively stable and is expected to retain source and binary compatibility in future releases. </p>
<p> <code>Xft</code> does provide a compatibility interface to its previous major version, Xft 1.<i>x</i>, described below.</p>
<h3>Xft 1.x Compatibility Header File</h3>
<p><code>#include &lt;X11/Xft/XftCompat.h&gt;</code></p>
<h3>Xft 1.x Compatibility Data Types</h3>
<dl COMPACT>
<dt><code>XftPattern</code></p>
<dd>holds a set of names with associated value lists; each name refers to a property of a font. <code>XftPattern</code>s are used as inputs to the matching code as well as holding information about specific fonts.</p>
<dt><code>XftFontSet</code></p>
<dd>contains a list of <code>XftPattern</code>s. Internally, <code>Xft</code> uses this data structure to hold sets of fonts. Externally, <code>Xft</code> returns the results of listing fonts in this format.</p>
<dt><code>XftObjectSet</code></p>
<dd>holds a set of names and is used to specify which fields from fonts are placed in the the list of returned patterns when listing fonts.</dl>
<h2>Author</h2>
<p>Keith Packard</p>
<h2>See Also</h2>
<p><i>Fontconfig Developers Reference</i><br />
 <i>FreeType API Reference</i><br />
 <i>Xlib &#8211; C Language Interface</i></p>
