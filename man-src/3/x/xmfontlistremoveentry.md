---
title: "xmfontlistremoveentry(3)"
name: "xmfontlistremoveentry"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfontlistremoveentry/"
description: "XmFontListRemoveEntry — A font list function that removes a font list entry from a font list"
---

<p><code>XmFontListRemoveEntry</code> &#8212; A font list function that removes a font list entry from a font list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmFontList XmFontListRemoveEntry</code>(
<code>XmFontList oldlist</code>,
<code>XmFontListEntry entry</code>);</pre>
<h2>Description</h2>
<p><code>XmFontListRemoveEntry</code> creates a new font list that contains the contents of <i>oldlist</i> minus those entries specified in <i>entry</i>. The routine removes any entries from <i>oldlist</i> that match the components (tag, type font/font set) of the specified entry. The function deallocates the original font list after extracting the required information. The caller uses <code>XmFontListEntryFree</code> to recover memory allocated for the specified entry. This routine does not free the <code>XFontSet</code> or <code>XFontStruct</code> associated with the font list entry that is removed.</p>
<dl COMPACT>
<dt><i>oldlist</i></p>
<dd>Specifies the font list</p>
<dt><i>entry</i></p>
<dd>Specifies the font list entry to be removed</dl>
<h2>Return</h2>
<p>If <i>oldlist</i> is NULL, the function returns NULL. If <i>entry</i> is NULL or no entries are removed, the function returns <i>oldlist</i>. Otherwise, it returns a new font list. If the function returns a new font list, the function allocates space to hold the new font list. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmFontListFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistappendentry/">XmFontListAppendEntry</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentrycreate/">XmFontListEntryCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentryfree/">XmFontListEntryFree</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentryload/">XmFontListEntryLoad</a></code>(3), and <code><a href="/docs/linux/man/3-xmfontlistfree/">XmFontListFree</a></code>(3).</p>
