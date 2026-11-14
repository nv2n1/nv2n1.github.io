---
title: "xdrawtext(3)"
name: "xdrawtext"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdrawtext/"
description: "XDrawText, XDrawText16, XTextItem, XTextItem16 – draw polytext text and text drawing structures"
---

<p>XDrawText, XDrawText16, XTextItem, XTextItem16 &#8211; draw polytext text and text drawing structures </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XDrawText(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, XTextItem *<i>items</i>, int <i>nitems</i>);</p>
<dd>int XDrawText16(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, XTextItem16 *<i>items</i>, int <i>nitems</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>d</i></p>
<dd>Specifies the drawable.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</p>
<dt><i>items</i></p>
<dd>Specifies an array of text items.</p>
<dt><i>nitems</i></p>
<dd>Specifies the number of text items in the array.</p>
<dt><i>x</i></p>
<dd>
<dt><i>y</i></p>
<dd>Specify the x and y coordinates, which are relative to the origin of the specified drawable and define the origin of the first character.</dl>
<h2>Description</h2>
<p>The <code>XDrawText16</code> function is similar to <code>XDrawText</code> except that it uses 2-byte or 16-bit characters. Both functions allow complex spacing and font shifts between counted strings. </p>
<p> Each text item is processed in turn. A font member other than <code>None</code> in an item causes the font to be stored in the GC and used for subsequent text. A text element delta specifies an additional change in the position along the x axis before the string is drawn. The delta is always added to the character origin and is not dependent on any characteristics of the font. Each character image, as defined by the font in the GC, is treated as an additional mask for a fill operation on the drawable. The drawable is modified only where the font character has a bit set to 1. If a text item generates a <code>BadFont</code> error, the previous text items may have been drawn. </p>
<p> For fonts defined with linear indexing rather than 2-byte matrix indexing, each <code>XChar2b</code> structure is interpreted as a 16-bit number with byte1 as the most significant byte. </p>
<p> Both functions use these GC components: function, plane-mask, fill-style, font, subwindow-mode, clip-x-origin, clip-y-origin, and clip-mask. They also use these GC mode-dependent components: foreground, background, tile, stipple, tile-stipple-x-origin, and tile-stipple-y-origin. </p>
<p> <code>XDrawText</code> and <code>XDrawText16</code> can generate <code>BadDrawable</code>, <code>BadFont</code>, <code>BadGC</code>, and <code>BadMatch</code> errors.</p>
<h2>Structures</h2>
<p>The <code>XTextItem</code> and <code>XTextItem16</code> structures contain: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*chars;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;pointer to string&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int nchars;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;number of characters&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int delta;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;delta between strings&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Font font;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Font to print it in, None don&#8217;t change&nbsp;*/ } XTextItem; </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XChar2b&nbsp;*chars;&nbsp;/*&nbsp;pointer to two-byte characters&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int nchars;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;number of characters&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int delta;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;delta between strings&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Font font;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;font to print it in, None don&#8217;t change&nbsp;*/ } XTextItem16; </p>
<p> If the font member is not <code>None</code>, the font is changed before printing and also is stored in the GC. If an error was generated during text drawing, the previous items may have been drawn. The baseline of the characters are drawn starting at the x and y coordinates that you pass in the text drawing functions. </p>
<p> For example, consider the background rectangle drawn by <code>XDrawImageString</code>. If you want the upper-left corner of the background rectangle to be at pixel coordinate (x,y), pass the (x,y + ascent) as the baseline origin coordinates to the text functions. The ascent is the font ascent, as given in the <code>XFontStruct</code> structure. If you want the lower-left corner of the background rectangle to be at pixel coordinate (x,y), pass the (x,y &#8211; descent + 1) as the baseline origin coordinates to the text functions. The descent is the font descent, as given in the <code>XFontStruct</code> structure.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadDrawable</code></p>
<dd>A value for a Drawable argument does not name a defined Window or Pixmap.</p>
<dt><code>BadFont</code></p>
<dd>A value for a Font or GContext argument does not name a defined Font.</p>
<dt><code>BadGC</code></p>
<dd>A value for a GContext argument does not name a defined GContext.</p>
<dt><code>BadMatch</code></p>
<dd>An <code>InputOnly</code> window is used as a Drawable.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xdrawimagestring/">XDrawImageString</a>(3), <a href="/docs/linux/man/3-xdrawstring/">XDrawString</a>(3), <a href="/docs/linux/man/3-xloadfont/">XLoadFont</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
