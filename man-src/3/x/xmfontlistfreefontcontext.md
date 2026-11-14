---
title: "xmfontlistfreefontcontext(3)"
name: "xmfontlistfreefontcontext"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfontlistfreefontcontext/"
description: "XmFontListFreeFontContext — A font list function that instructs the toolkit that the font list context is no longer needed"
---

<p><code>XmFontListFreeFontContext</code> &#8212; A font list function that instructs the toolkit that the font list context is no longer needed</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmFontListFreeFontContext</code>(
<code>XmFontContext context</code>);</pre>
<h2>Description</h2>
<p><code>XmFontListFreeFontContext</code> instructs the toolkit that the context is no longer needed and will not be used without reinitialization.</p>
<dl COMPACT>
<dt><i>context</i></p>
<dd>Specifies the font list context structure that was allocated by the <code>XmFontListInitFontContext</code> function</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfontlistinitfontcontext/">XmFontListInitFontContext</a></code>(3) and <code><a href="/docs/linux/man/3-xmfontlistnextentry/">XmFontListNextEntry</a></code>(3).</p>
