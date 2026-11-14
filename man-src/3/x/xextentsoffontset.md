---
title: "xextentsoffontset(3)"
name: "xextentsoffontset"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xextentsoffontset/"
description: "XExtentsOfFontSet – obtain the maximum extents structure for a font set"
---

<p>XExtentsOfFontSet &#8211; obtain the maximum extents structure for a font set </p>
<h2>Syntax</h2>
<dl COMPACT>
<dd>XFontSetExtents *XExtentsOfFontSet(XFontSet <i>font_set</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>font_set</i></p>
<dd>Specifies the font set.</dl>
<h2>Description</h2>
<p>The <code>XExtentsOfFontSet</code> function returns an <code>XFontSetExtents</code> structure for the fonts used by the Xmb and Xwc layers for the given font set. </p>
<p> The <code>XFontSetExtents</code> structure is owned by Xlib and should not be modified or freed by the client. It will be freed by a call to <code>XFreeFontSet</code> with the associated <code>XFontSet</code>. Until freed, its contents will not be modified by Xlib.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-xcreatefontset/">XCreateFontSet</a>(3), <a href="/docs/linux/man/3-xfontsoffontset/">XFontsOfFontSet</a>(3), <a href="/docs/linux/man/3-xfontsetextents/">XFontSetExtents</a>(3)<br />
 <i>Xlib &#8211; C Language X Interface</i></p>
