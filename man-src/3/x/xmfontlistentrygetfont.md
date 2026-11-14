---
title: "xmfontlistentrygetfont(3)"
name: "xmfontlistentrygetfont"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfontlistentrygetfont/"
description: "XmFontListEntryGetFont — A font list function that retrieves font information from a font list entry"
---

<p><code>XmFontListEntryGetFont</code> &#8212; A font list function that retrieves font information from a font list entry</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XtPointer XmFontListEntryGetFont</code>(
<code>XmFontListEntry entry</code>,
<code>XmFontType *type_return</code>);</pre>
<h2>Description</h2>
<p><code>XmFontListEntryGetFont</code> retrieves font information for a specified font list entry. If the font list entry contains a font, <i>type_return</i> returns <code>XmFONT_IS_FONT</code> and the function returns a pointer to an <code>XFontStruct</code>. If the font list entry contains a font set, <i>type_return</i> returns <code>XmFONT_IS_FONTSET</code> and the function returns the <code>XFontSet</code>.</p>
<dl COMPACT>
<dt><i>entry</i></p>
<dd>Specifies the font list entry.</p>
<dt><i>type_return</i></p>
<dd>Specifies a pointer to the type of the font element for the current entry. Valid values are <code>XmFONT_IS_FONT</code> and <code>XmFONT_IS_FONTSET</code>.</dl>
<p> The returned <code>XFontSet</code> or <code>XFontStruct</code> is not a copy of the toolkit data and must not be freed.</p>
<h2>Return</h2>
<p>Returns an <code>XFontSet</code> or a pointer to an <code>XFontStruct</code> structure.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentrycreate/">XmFontListEntryCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentrygettag/">XmFontListEntryGetTag</a></code>(3) <code><a href="/docs/linux/man/3-xmfontlistentryload/">XmFontListEntryLoad</a></code>(3), and <code><a href="/docs/linux/man/3-xmfontlistnextentry/">XmFontListNextEntry</a></code>(3).</p>
