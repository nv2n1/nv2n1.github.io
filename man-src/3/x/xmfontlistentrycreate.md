---
title: "xmfontlistentrycreate(3)"
name: "xmfontlistentrycreate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfontlistentrycreate/"
description: "XmFontListEntryCreate — A font list function that creates a font list entry"
---

<p><code>XmFontListEntryCreate</code> &#8212; A font list function that creates a font list entry</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmFontListEntry XmFontListEntryCreate</code>(
<code>char *tag</code>,
<code>XmFontType type</code>,
<code>XtPointer font</code>);</pre>
<h2>Description</h2>
<p><code>XmFontListEntryCreate</code> creates a font list entry that contains either a font or font set and is identified by a tag.</p>
<dl COMPACT>
<dt><i>tag</i></p>
<dd>Specifies a NULL terminated string for the tag of the font list entry. The tag may be specified as <code>XmFONTLIST_DEFAULT_TAG</code>, which is used to identify the default font list element in a font list.</p>
<dt><i>type</i></p>
<dd>Specifies whether the <i>font</i> argument is a font structure or a font set. Valid values are <code>XmFONT_IS_FONT</code> and <code>XmFONT_IS_FONTSET</code>.</p>
<dt><i>font</i></p>
<dd>Specifies either an <code>XFontSet</code> returned by <code>XCreateFontSet</code> or a pointer to an <code>XFontStruct</code> returned by <code>XLoadQueryFont</code>.</dl>
<p> The toolkit does not copy the X Font structure specified by the <i>font</i> argument. Therefore, an application programmer must not free <code>XFontStruct</code> or <code>XFontSet</code> until all font lists and/or font entries that reference it have been freed.</p>
<h2>Return</h2>
<p>Returns a font list entry. The function allocates space to hold the returned font list entry. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmFontListEntryFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistappendentry/">XmFontListAppendEntry</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentryfree/">XmFontListEntryFree</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentrygetfont/">XmFontListEntryGetFont</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentrygettag/">XmFontListEntryGetTag</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentryload/">XmFontListEntryLoad</a></code>(3), and <code><a href="/docs/linux/man/3-xmfontlistremoveentry/">XmFontListRemoveEntry</a></code>(3).</p>
