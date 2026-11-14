---
title: "xmfontlistentrygettag(3)"
name: "xmfontlistentrygettag"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfontlistentrygettag/"
description: "XmFontListEntryGetTag — A font list function that retrieves the tag of a font list entry"
---

<p><code>XmFontListEntryGetTag</code> &#8212; A font list function that retrieves the tag of a font list entry</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>char* XmFontListEntryGetTag</code>(
<code>XmFontListEntry entry</code>);</pre>
<h2>Description</h2>
<p><code>XmFontListEntryGetTag</code> retrieves a copy of the tag of the specified font list entry. This routine allocates memory for the tag string that must be freed by the application.</p>
<dl COMPACT>
<dt><i>entry</i></p>
<dd>Specifies the font list entry</dl>
<h2>Return</h2>
<p>Returns the tag for the font list entry. The function allocates space to hold the returned tag. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XtFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentrycreate/">XmFontListEntryCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentrygetfont/">XmFontListEntryGetFont</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentryload/">XmFontListEntryLoad</a></code>(3), and <code><a href="/docs/linux/man/3-xmfontlistnextentry/">XmFontListNextEntry</a></code>(3).</p>
