---
title: "xsetfont(3)"
name: "xsetfont"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetfont/"
description: "XSetFont – GC convenience routines"
---

<p>XSetFont &#8211; GC convenience routines </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XSetFont(Display *<i>display</i>, GC <i>gc</i>, Font <i>font</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>font</i></p>
<dd>Specifies the font.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</dl>
<h2>Description</h2>
<p>The <code>XSetFont</code> function sets the current font in the specified GC. </p>
<p> <code>XSetFont</code> can generate <code>BadAlloc</code>, <code>BadFont</code>, and <code>BadGC</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadFont</code></p>
<dd>A value for a Font or GContext argument does not name a defined Font.</p>
<dt><code>BadGC</code></p>
<dd>A value for a GContext argument does not name a defined GContext.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreategc/">XCreateGC</a>(3), <a href="/docs/linux/man/3-xquerybestsize/">XQueryBestSize</a>(3), <a href="/docs/linux/man/3-xsetarcmode/">XSetArcMode</a>(3), <a href="/docs/linux/man/3-xsetcliporigin/">XSetClipOrigin</a>(3), <a href="/docs/linux/man/3-xsetfillstyle/">XSetFillStyle</a>(3), <a href="/docs/linux/man/3-xsetlineattributes/">XSetLineAttributes</a>(3), <a href="/docs/linux/man/3-xsetstate/">XSetState</a>(3), <a href="/docs/linux/man/3-xsettile/">XSetTile</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
