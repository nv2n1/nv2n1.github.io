---
title: "xwcdrawimagestring(3)"
name: "xwcdrawimagestring"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xwcdrawimagestring/"
description: "XmbDrawImageString, XwcDrawImageString, Xutf8DrawImageString – draw image text using a single font set"
---

<p>XmbDrawImageString, XwcDrawImageString, Xutf8DrawImageString &#8211; draw image text using a single font set </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>void XmbDrawImageString(Display *<i>display</i>, Drawable <i>d</i>, XFontSet <i>font_set</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, char *<i>string</i>, int <i>num_bytes</i>);</p>
<dd>void XwcDrawImageString(Display *<i>display</i>, Drawable <i>d</i>, XFontSet <i>font_set</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, wchar_t *<i>string</i>, int <i>num_wchars</i>);</p>
<dd>void Xutf8DrawImageString(Display *<i>display</i>, Drawable <i>d</i>, XFontSet <i>font_set</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, char *<i>string</i>, int <i>num_bytes</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>d</i></p>
<dd>Specifies the drawable.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>font_set</i></p>
<dd>Specifies the font set.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</p>
<dt><i>num_bytes</i></p>
<dd>Specifies the number of bytes in the string argument.</p>
<dt><i>num_wchars</i></p>
<dd>Specifies the number of characters in the string argument.</p>
<dt><i>string</i></p>
<dd>Specifies the character string.</p>
<dt><i>x</i></p>
<dd>
<dt><i>y</i></p>
<dd>Specify the x and y coordinates.</dl>
<h2>Description</h2>
<p>The <code>XmbDrawImageString</code>, <code>XwcDrawImageString</code> and <code>Xutf8DrawImageString</code> functions fill a destination rectangle with the background pixel defined in the GC and then paint the text with the foreground pixel. The filled rectangle is the rectangle returned to overall_logical_return by <code>XmbTextExtents</code>, <code>XwcTextExtents</code> or <code>Xutf8TextExtents</code> for the same text and <code>XFontSet</code>. </p>
<p> When the <code>XFontSet</code> has missing charsets, each unavailable character is drawn with the default string returned by <code>XCreateFontSet</code>. The behavior for an invalid codepoint is undefined. </p>
<p> The function <code>Xutf8TextExtents</code> is an extension introduced by The XFree86 Project, Inc., in their 4.0.2 release. Its presence is indicated by the macro <code>X_HAVE_UTF8_STRING</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xdrawimagestring/">XDrawImageString</a>(3), <a href="/docs/linux/man/3-xdrawstring/">XDrawString</a>(3), <a href="/docs/linux/man/3-xdrawtext/">XDrawText</a>(3), <a href="/docs/linux/man/3-xmbdrawstring/">XmbDrawString</a>(3), <a href="/docs/linux/man/3-xmbdrawtext/">XmbDrawText</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
