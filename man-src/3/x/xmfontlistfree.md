---
title: "xmfontlistfree(3)"
name: "xmfontlistfree"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfontlistfree/"
description: "XmFontListFree — A font list function that recovers memory used by a font list"
---

<p><code>XmFontListFree</code> &#8212; A font list function that recovers memory used by a font list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>void XmFontListFree</code>(
<code>XmFontList list</code>);</pre>
<h2>Description</h2>
<p><code>XmFontListFree</code> recovers memory used by a font list. This routine does not free the <code>XFontSet</code> or <code>XFontStruct</code> associated with the specified font list.</p>
<dl COMPACT>
<dt><i>list</i></p>
<dd>Specifies the font list to be freed</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistappendentry/">XmFontListAppendEntry</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistcopy/">XmFontListCopy</a></code>(3), and <code><a href="/docs/linux/man/3-xmfontlistremoveentry/">XmFontListRemoveEntry</a></code>(3).</p>
