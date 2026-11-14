---
title: "xsetbackground(3)"
name: "xsetbackground"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xsetbackground/"
description: "XSetState, XSetFunction, XSetPlaneMask, XSetForeground, XSetBackground – GC convenience routines"
---

<p>XSetState, XSetFunction, XSetPlaneMask, XSetForeground, XSetBackground &#8211; GC convenience routines </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XSetState(Display *<i>display</i>, GC <i>gc</i>, unsigned long <i>foreground</i>, unsigned int <i>background</i>, int <i>function</i>, unsigned long <i>plane_mask</i>);</p>
<dd>int XSetFunction(Display *<i>display</i>, GC <i>gc</i>, int <i>function</i>);</p>
<dd>int XSetPlaneMask(Display *<i>display</i>, GC <i>gc</i>, unsigned long <i>plane_mask</i>);</p>
<dd>int XSetForeground(Display *<i>display</i>, GC <i>gc</i>, unsigned long <i>foreground</i>);</p>
<dd>int XSetBackground(Display *<i>display</i>, GC <i>gc</i>, unsigned long <i>background</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>background</i></p>
<dd>Specifies the background you want to set for the specified GC.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>foreground</i></p>
<dd>Specifies the foreground you want to set for the specified GC.</p>
<dt><i>function</i></p>
<dd>Specifies the function you want to set for the specified GC.</p>
<dt><i>gc</i></p>
<dd>Specifies the GC.</p>
<dt><i>plane_mask</i></p>
<dd>Specifies the plane mask.</dl>
<h2>Description</h2>
<p>The <code>XSetState</code> function sets the foreground, background, plane mask, and function components for the specified GC. </p>
<p> <code>XSetState</code> can generate <code>BadAlloc</code>, <code>BadGC</code>, and <code>BadValue</code> errors. </p>
<p> <code>XSetFunction</code> sets a specified value in the specified GC. </p>
<p> <code>XSetFunction</code> can generate <code>BadAlloc</code>, <code>BadGC</code>, and <code>BadValue</code> errors. </p>
<p> The <code>XSetPlaneMask</code> function sets the plane mask in the specified GC. </p>
<p> <code>XSetPlaneMask</code> can generate <code>BadAlloc</code> and <code>BadGC</code> errors. </p>
<p> The <code>XSetForeground</code> function sets the foreground in the specified GC. </p>
<p> <code>XSetForeground</code> can generate <code>BadAlloc</code> and <code>BadGC</code> errors. </p>
<p> The <code>XSetBackground</code> function sets the background in the specified GC. </p>
<p> <code>XSetBackground</code> can generate <code>BadAlloc</code> and <code>BadGC</code> errors.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadGC</code></p>
<dd>A value for a GContext argument does not name a defined GContext.</p>
<dt><code>BadValue</code></p>
<dd>Some numeric value falls outside the range of values accepted by the request. Unless a specific range is specified for an argument, the full range defined by the argument&#8217;s type is accepted. Any argument defined as a set of alternatives can generate this error.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreategc/">XCreateGC</a>(3), <a href="/docs/linux/man/3-xquerybestsize/">XQueryBestSize</a>(3), <a href="/docs/linux/man/3-xsetarcmode/">XSetArcMode</a>(3), <a href="/docs/linux/man/3-xsetcliporigin/">XSetClipOrigin</a>(3), <a href="/docs/linux/man/3-xsetfillstyle/">XSetFillStyle</a>(3), <a href="/docs/linux/man/3-xsetfont/">XSetFont</a>(3), <a href="/docs/linux/man/3-xsetlineattributes/">XSetLineAttributes</a>(3), <a href="/docs/linux/man/3-xsettile/">XSetTile</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
