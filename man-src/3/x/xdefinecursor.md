---
title: "xdefinecursor(3)"
name: "xdefinecursor"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xdefinecursor/"
description: "XDefineCursor, XUndefineCursor – define cursors"
---

<p>XDefineCursor, XUndefineCursor &#8211; define cursors </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>int XDefineCursor(Display *<i>display</i>, Window <i>w</i>, Cursor <i>cursor</i>);</p>
<dd>int XUndefineCursor(Display *<i>display</i>, Window <i>w</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>cursor</i></p>
<dd>Specifies the cursor that is to be displayed or <code>None</code>.</p>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>w</i></p>
<dd>Specifies the window.</dl>
<h2>Description</h2>
<p>If a cursor is set, it will be used when the pointer is in the window. If the cursor is <code>None</code>, it is equivalent to <code>XUndefineCursor</code>. </p>
<p> <code>XDefineCursor</code> can generate <code>BadCursor</code> and <code>BadWindow</code> errors. </p>
<p> The <code>XUndefineCursor</code> function undoes the effect of a previous <code>XDefineCursor</code> for this window. When the pointer is in the window, the parent&#8217;s cursor will now be used. On the root window, the default cursor is restored. </p>
<p> <code>XUndefineCursor</code> can generate a <code>BadWindow</code> error.</p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>The server failed to allocate the requested resource or server memory.</p>
<dt><code>BadCursor</code></p>
<dd>A value for a Cursor argument does not name a defined Cursor.</p>
<dt><code>BadWindow</code></p>
<dd>A value for a Window argument does not name a defined Window.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreatefontcursor/">XCreateFontCursor</a>(3), <a href="/docs/linux/man/3-xrecolorcursor/">XRecolorCursor</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
