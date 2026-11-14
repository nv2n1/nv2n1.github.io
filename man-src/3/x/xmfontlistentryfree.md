---
title: "xmfontlistentryfree(3)"
name: "xmfontlistentryfree"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfontlistentryfree/"
description: "XmFontListEntryFree — A font list function that recovers memory used by a font list entry"
---

<p><code>XmFontListEntryFree</code> &#8212; A font list function that recovers memory used by a font list entry</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmFontListEntryFree</code>(
<code>XmFontListEntry *entry</code>);</pre>
<h2>Description</h2>
<p><code>XmFontListEntryFree</code> recovers memory used by a font list entry. This routine does not free the <code>XFontSet</code> or <code>XFontStruct</code> associated with the font list entry.</p>
<dl COMPACT>
<dt><i>entry</i></p>
<dd>Specifies a pointer to the font list entry to be freed. In addition, it may be necessary to take the address of the font list entry (via the <code>&amp;</code> operator) before passing it to this function.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistappendentry/">XmFontListAppendEntry</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentrycreate/">XmFontListEntryCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentryload/">XmFontListEntryLoad</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistnextentry/">XmFontListNextEntry</a></code>(3), and <code><a href="/docs/linux/man/3-xmfontlistremoveentry/">XmFontListRemoveEntry</a></code>(3).</p>
