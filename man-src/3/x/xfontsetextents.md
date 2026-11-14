---
title: "xfontsetextents(3)"
name: "xfontsetextents"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xfontsetextents/"
description: "XFontSetExtents – XFontSetExtents structure"
---

<p>XFontSetExtents &#8211; XFontSetExtents structure </p>
<h2>Structures</h2>
<p>The <code>XFontSetExtents</code> structure contains: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XRectangle max_ink_extent;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;over all drawable characters&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XRectangle max_logical_extent;&nbsp;<wbr>&nbsp;/*&nbsp;over all drawable characters&nbsp;*/ } XFontSetExtents; </p>
<p> The <code>XRectangle</code> structures used to return font set metrics are the usual Xlib screen-oriented rectangles with x, y giving the upper left corner, and width and height always positive. </p>
<p> The max_ink_extent member gives the maximum extent, over all drawable characters, of the rectangles that bound the character glyph image drawn in the foreground color, relative to a constant origin. See <code>XmbTextExtents</code> and <code>XwcTextExtents</code> for detailed semantics. </p>
<p> The max_logical_extent member gives the maximum extent, over all drawable characters, of the rectangles that specify minimum spacing to other graphical features, relative to a constant origin. Other graphical features drawn by the client, for example, a border surrounding the text, should not intersect this rectangle. The max_logical_extent member should be used to compute minimum interline spacing and the minimum area that must be allowed in a text field to draw a given number of arbitrary characters. </p>
<p> Due to context-dependent rendering, appending a given character to a string may change the string&#8217;s extent by an amount other than that character&#8217;s individual extent.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreatefontset/">XCreateFontSet</a>(3), <a href="/docs/linux/man/3-xextentsoffontset/">XExtentsOfFontSet</a>(3), <a href="/docs/linux/man/3-xfontsoffontset/">XFontsOfFontSet</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
