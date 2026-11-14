---
title: "xsetfillstyle(3)"
name: "xsetfillstyle"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetfillstyle/"
description: "XSetFillStyle, XSetFillRule – GC convenience routines"
---

<p>XSetFillStyle, XSetFillRule &#8211; GC convenience routines </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XSetFillStyle(Display *<i>display</i>, GC <i>gc</i>, int <i>fill_style</i>);</p>
<dd>int XSetFillRule(Display *<i>display</i>, GC <i>gc</i>, int <i>fill_rule</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>fill_rule</i></p>
<dd>Specifies the fill-rule you want to set for the specified GC. You can pass <code>EvenOddRule</code> or <code>WindingRule</code>.</p>
<dt><i>fill_style</i></p>
<dd>Specifies the fill-style you want to set for the specified GC. You can pass <code>FillSolid</code>, <code>FillTiled</code>, <code>FillStippled</code>, or <code>FillOpaqueStippled</code>.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</dl>
<h2>Description</h2>
<p>The <code>XSetFillStyle</code> function sets the fill-style in the specified GC. </p>
<p> <code>XSetFillStyle</code> can generate <code>BadAlloc</code>, <code>BadGC</code>, and <code>BadValue</code> errors. </p>
<p> The <code>XSetFillRule</code> function sets the fill-rule in the specified GC. </p>
<p> <code>XSetFillRule</code> can generate <code>BadAlloc</code>, <code>BadGC</code>, and <code>BadValue</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadGC</code></p>
<dd>A value for a GContext argument does not name a defined GContext.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreategc/">XCreateGC</a>(3), <a href="/docs/linux/man/3-xquerybestsize/">XQueryBestSize</a>(3), <a href="/docs/linux/man/3-xsetarcmode/">XSetArcMode</a>(3), <a href="/docs/linux/man/3-xsetcliporigin/">XSetClipOrigin</a>(3), <a href="/docs/linux/man/3-xsetfont/">XSetFont</a>(3), <a href="/docs/linux/man/3-xsetlineattributes/">XSetLineAttributes</a>(3), <a href="/docs/linux/man/3-xsetstate/">XSetState</a>(3), <a href="/docs/linux/man/3-xsettile/">XSetTile</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
