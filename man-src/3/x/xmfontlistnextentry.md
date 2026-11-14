---
title: "xmfontlistnextentry(3)"
name: "xmfontlistnextentry"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfontlistnextentry/"
description: "XmFontListNextEntry — A font list function that returns the next entry in a font list"
---

<p><code>XmFontListNextEntry</code> &#8212; A font list function that returns the next entry in a font list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmFontListEntry XmFontListNextEntry</code>(
<code>XmFontContext context</code>);</pre>
<h2>Description</h2>
<p><code>XmFontListNextEntry</code> returns the next entry in the font list. The application uses the <code>XmFontListInitFontContext</code> routine to create a font list context. The first call to <code>XmFontListNextEntry</code> sets the context to the first entry in the font list. The application then calls <code>XmFontListNextEntry</code> repeatedly with the same context. Each succeeding call accesses the next entry of the font list. When finished, the application calls <code>XmFontListFreeFontContext</code> to free the allocated font list context.</p>
<dl COMPACT>
<dt><i>context</i></p>
<dd>Specifies the font list context</dl>
<h2>Return</h2>
<p>Returns NULL if the context does not refer to a valid entry or if it is at the end of the font list; otherwise, it returns a font list entry. If the function does return a font list entry, the font list entry is not a copy. Therefore, the application should not free the returned font list entry.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentryfree/">XmFontListEntryFree</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentrygetfont/">XmFontListEntryGetFont</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentrygettag/">XmFontListEntryGetTag</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistfreefontcontext/">XmFontListFreeFontContext</a></code>(3), and <code><a href="/docs/linux/man/3-xmfontlistinitfontcontext/">XmFontListInitFontContext</a></code>(3).</p>
