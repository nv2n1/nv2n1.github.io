---
title: "xmfontlistappendentry(3)"
name: "xmfontlistappendentry"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfontlistappendentry/"
description: "XmFontListAppendEntry — A font list function that appends an entry to a font list"
---

<p><code>XmFontListAppendEntry</code> &#8212; A font list function that appends an entry to a font list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmFontList XmFontListAppendEntry</code>(
<code>XmFontList oldlist</code>,
<code>XmFontListEntry entry</code>);</pre>
<h2>Description</h2>
<p><code>XmFontListAppendEntry</code> creates a new font list that contains the contents of <i>oldlist</i>. This function copies the contents of the font list entry being added into this new font list. If <i>oldlist</i> is NULL, <code>XmFontListAppendEntry</code> creates a new font list containing only the single entry specified. </p>
<p> This function deallocates the original font list after extracting the required information. The caller must free the font list entry by using <code>XmFontListEntryFree</code>.</p>
<dl COMPACT>
<dt><i>oldlist</i></p>
<dd>Specifies the font list to be added to</p>
<dt><i>entry</i></p>
<dd>Specifies the font list entry to be added</dl>
<h2>Return</h2>
<p>If <i>entry</i> is NULL, returns <i>oldlist</i>; otherwise, returns a new font list.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentrycreate/">XmFontListEntryCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentryfree/">XmFontListEntryFree</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentryload/">XmFontListEntryLoad</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistfree/">XmFontListFree</a></code>(3), and <code><a href="/docs/linux/man/3-xmfontlistremoveentry/">XmFontListRemoveEntry</a></code>(3).</p>
