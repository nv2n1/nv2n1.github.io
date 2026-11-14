---
title: "xmbdrawtext(3)"
name: "xmbdrawtext"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmbdrawtext/"
description: "XmbDrawText, XwcDrawText, Xutf8DrawText – draw text using multiple font sets"
---

<p>XmbDrawText, XwcDrawText, Xutf8DrawText &#8211; draw text using multiple font sets </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>void XmbDrawText(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, XmbTextItem *<i>items</i>, int <i>nitems</i>);</p>
<dd>void XwcDrawText(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, XwcTextItem *<i>items</i>, int <i>nitems</i>);</p>
<dd>void Xutf8DrawText(Display *<i>display</i>, Drawable <i>d</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, XmbTextItem *<i>items</i>, int <i>nitems</i>);</dl>
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
<dd>Specify the x and y coordinates.</dl>
<h2>Description</h2>
<p>The <code>XmbDrawText</code>, <code>XwcDrawText</code> and <code>Xutf8DrawText</code> functions allow complex spacing and font set shifts between text strings. Each text item is processed in turn, with the origin of a text element advanced in the primary draw direction by the escapement of the previous text item. A text item delta specifies an additional escapement of the text item drawing origin in the primary draw direction. A font_set member other than <code>None</code> in an item causes the font set to be used for this and subsequent text items in the text_items list. Leading text items with a font_set member set to <code>None</code> will not be drawn. </p>
<p> <code>XmbDrawText</code>, <code>XwcDrawText</code> and <code>Xutf8DrawText</code> do not perform any context-dependent rendering between text segments. Clients may compute the drawing metrics by passing each text segment to <code>XmbTextExtents</code>, <code>XwcTextExtents</code>, <code>Xutf8TextExtents</code> or <code>XmbTextPerCharExtents</code>, <code>XwcTextPerCharExtents</code>. <code>Xutf8TextPerCharExtents</code>. When the <code>XFontSet</code> has missing charsets, each unavailable character is drawn with the default string returned by <code>XCreateFontSet</code>. The behavior for an invalid codepoint is undefined. </p>
<p> The function <code>Xutf8DrawText</code> is an extension introduced by The XFree86 Project, Inc., in their 4.0.2 release. Its presence is indicated by the macro <code>X_HAVE_UTF8_STRING</code>.</p>
<h2>Structures</h2>
<p>The <code>XmbTextItem</code> structure contains: typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*chars;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;pointer to string&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int nchars;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;number of bytes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int delta;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;pixel delta between strings&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XFontSet font_set;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;fonts, None means don&#8217;t change&nbsp;*/ } XmbTextItem; The <code>XwcTextItem</code> structure contains: typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;wchar_t&nbsp;*chars;&nbsp;/*&nbsp;pointer to wide char string&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int nchars;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;number of wide characters&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int delta;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;pixel delta between strings&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;XFontSet font_set;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;fonts, None means don&#8217;t change&nbsp;*/ } XwcTextItem;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xdrawimagestring/">XDrawImageString</a>(3), <a href="/docs/linux/man/3-xdrawstring/">XDrawString</a>(3), <a href="/docs/linux/man/3-xdrawtext/">XDrawText</a>(3), <a href="/docs/linux/man/3-xmbdrawimagestring/">XmbDrawImageString</a>(3), <a href="/docs/linux/man/3-xmbdrawstring/">XmbDrawString</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
