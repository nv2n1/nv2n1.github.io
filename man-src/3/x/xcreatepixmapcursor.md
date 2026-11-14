---
title: "xcreatepixmapcursor(3)"
name: "xcreatepixmapcursor"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xcreatepixmapcursor/"
description: "XCreateFontCursor, XCreatePixmapCursor, XCreateGlyphCursor – create cursors"
---

<p>XCreateFontCursor, XCreatePixmapCursor, XCreateGlyphCursor &#8211; create cursors </p>
<h2>Syntax</h2>
<p>#include &lt;X11/cursorfont.h&gt;</p>
<dl COMPACT>
<dd>Cursor XCreateFontCursor(Display *<i>display</i>, unsigned int <i>shape</i>);</p>
<dd>Cursor XCreatePixmapCursor(Display *<i>display</i>, Pixmap <i>source</i>, Pixmap <i>mask</i>, XColor *<i>foreground_color</i>, XColor *<i>background_color</i>, unsigned int <i>x</i>, unsigned int <i>y</i>);</p>
<dd>Cursor XCreateGlyphCursor(Display *<i>display</i>, Font <i>source_font</i>, Font <i>mask_font</i>, unsigned int <i>source_char</i>, unsigned int <i>mask_char</i>, XColor *<i>foreground_color</i>, XColor *<i>background_color</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>background_color</i></p>
<dd>Specifies the RGB values for the background of the source.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>foreground_color</i></p>
<dd>Specifies the RGB values for the foreground of the source.</p>
<dt><i>mask</i></p>
<dd>Specifies the cursor&#8217;s source bits to be displayed or <code>None</code>.</p>
<dt><i>mask_char</i></p>
<dd>Specifies the glyph character for the mask.</p>
<dt><i>mask_font</i></p>
<dd>Specifies the font for the mask glyph or <code>None</code>.</p>
<dt><i>shape</i></p>
<dd>Specifies the shape of the cursor.</p>
<dt><i>source</i></p>
<dd>Specifies the shape of the source cursor.</p>
<dt><i>source_char</i></p>
<dd>Specifies the character glyph for the source.</p>
<dt><i>source_font</i></p>
<dd>Specifies the font for the source glyph.</p>
<dt><i>x</i></p>
<dd>
<dt><i>y</i></p>
<dd>Specify the x and y coordinates, which indicate the hotspot relative to the source&#8217;s origin.</dl>
<h2>Description</h2>
<p>X provides a set of standard cursor shapes in a special font named cursor. Applications are encouraged to use this interface for their cursors because the font can be customized for the individual display type. The shape argument specifies which glyph of the standard fonts to use. </p>
<p> The hotspot comes from the information stored in the cursor font. The initial colors of a cursor are a black foreground and a white background (see <code>XRecolorCursor</code>). </p>
<p> <code>XCreateFontCursor</code> can generate <code>BadAlloc</code> and <code>BadValue</code> errors. </p>
<p> The <code>XCreatePixmapCursor</code> function creates a cursor and returns the cursor ID associated with it. The foreground and background RGB values must be specified using foreground_color and background_color, even if the X server only has a <code>StaticGray</code> or <code>GrayScale</code> screen. The foreground color is used for the pixels set to 1 in the source, and the background color is used for the pixels set to 0. Both source and mask, if specified, must have depth one (or a <code>BadMatch</code> error results) but can have any root. The mask argument defines the shape of the cursor. The pixels set to 1 in the mask define which source pixels are displayed, and the pixels set to 0 define which pixels are ignored. If no mask is given, all pixels of the source are displayed. The mask, if present, must be the same size as the pixmap defined by the source argument, or a <code>BadMatch</code> error results. The hotspot must be a point within the source, or a <code>BadMatch</code> error results. </p>
<p> The components of the cursor can be transformed arbitrarily to meet display limitations. The pixmaps can be freed immediately if no further explicit references to them are to be made. Subsequent drawing in the source or mask pixmap has an undefined effect on the cursor. The X server might or might not make a copy of the pixmap. </p>
<p> <code>XCreatePixmapCursor</code> can generate <code>BadAlloc</code> and <code>BadPixmap</code> errors. </p>
<p> The <code>XCreateGlyphCursor</code> function is similar to <code>XCreatePixmapCursor</code> except that the source and mask bitmaps are obtained from the specified font glyphs. The source_char must be a defined glyph in source_font, or a <code>BadValue</code> error results. If mask_font is given, mask_char must be a defined glyph in mask_font, or a <code>BadValue</code> error results. The mask_font and character are optional. The origins of the source_char and mask_char (if defined) glyphs are positioned coincidently and define the hotspot. The source_char and mask_char need not have the same bounding box metrics, and there is no restriction on the placement of the hotspot relative to the bounding boxes. If no mask_char is given, all pixels of the source are displayed. You can free the fonts immediately by calling <code>XFreeFont</code> if no further explicit references to them are to be made. </p>
<p> For 2-byte matrix fonts, the 16-bit value should be formed with the byte1 member in the most significant byte and the byte2 member in the least significant byte. </p>
<p> <code>XCreateGlyphCursor</code> can generate <code>BadAlloc</code>, <code>BadFont</code>, and <code>BadValue</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadFont</code></p>
<dd>A value for a Font or GContext argument does not name a defined Font.</p>
<dt><code>BadMatch</code></p>
<dd>Some argument or pair of arguments has the correct type and range but fails to match in some other way required by the request.</p>
<dt><code>BadPixmap</code></p>
<dd>A value for a Pixmap argument does not name a defined Pixmap.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xdefinecursor/">XDefineCursor</a>(3), <a href="/docs/linux/man/3-xloadfont/">XLoadFont</a>(3), <a href="/docs/linux/man/3-xrecolorcursor/">XRecolorCursor</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
