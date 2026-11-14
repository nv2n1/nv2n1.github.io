---
title: "xmfontlistcopy(3)"
name: "xmfontlistcopy"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfontlistcopy/"
description: "XmFontListCopy — A font list function that copies a font list"
---

<p><code>XmFontListCopy</code> &#8212; A font list function that copies a font list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmFontList XmFontListCopy</code>(
<code>XmFontList fontlist</code>);</pre>
<h2>Description</h2>
<p><code>XmFontListCopy</code> creates a new font list consisting of the contents of the <i>fontlist</i> argument.</p>
<dl COMPACT>
<dt><i>fontlist</i></p>
<dd>Specifies a font list to be copied</dl>
<h2>Return</h2>
<p>Returns NULL if <i>fontlist</i> is NULL; otherwise, returns a new font list and allocates space to hold the font list. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmFontListFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3) and <code><a href="/docs/linux/man/3-xmfontlistfree/">XmFontListFree</a></code>(3).</p>
