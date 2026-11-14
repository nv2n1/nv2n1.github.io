---
title: "xmbdrawstring(3)"
name: "xmbdrawstring"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmbdrawstring/"
description: "XmbDrawString, XwcDrawString, Xutf8DrawString – draw text using a single font set"
---

<p>XmbDrawString, XwcDrawString, Xutf8DrawString &#8211; draw text using a single font set </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>void XmbDrawString(Display *<i>display</i>, Drawable <i>d</i>, XFontSet <i>font_set</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, char *<i>string</i>, int <i>num_bytes</i>);</p>
<dd>void XwcDrawString(Display *<i>display</i>, Drawable <i>d</i>, XFontSet <i>font_set</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, wchar_t *<i>string</i>, int <i>num_wchars</i>);</p>
<dd>void Xutf8DrawString(Display *<i>display</i>, Drawable <i>d</i>, XFontSet <i>font_set</i>, GC <i>gc</i>, int <i>x</i>, int <i>y</i>, char *<i>string</i>, int <i>num_bytes</i>);</dl>
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
<p>The <code>XmbDrawString</code>, <code>XwcDrawString</code> and <code>Xutf8DrawString</code> functions draw the specified text with the foreground pixel. When the <code>XFontSet</code> has missing charsets, each unavailable character is drawn with the default string returned by <code>XCreateFontSet</code>. The behavior for an invalid codepoint is undefined. </p>
<p> The function <code>Xutf8DrawString</code> is an extension introduced by The XFree86 Project, Inc., in their 4.0.2 release. Its presence is indicated by the macro <code>X_HAVE_UTF8_STRING</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xdrawimagestring/">XDrawImageString</a>(3), <a href="/docs/linux/man/3-xdrawstring/">XDrawString</a>(3), <a href="/docs/linux/man/3-xdrawtext/">XDrawText</a>(3), <a href="/docs/linux/man/3-xmbdrawimagestring/">XmbDrawImageString</a>(3), <a href="/docs/linux/man/3-xmbdrawtext/">XmbDrawText</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
