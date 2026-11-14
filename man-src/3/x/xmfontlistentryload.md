---
title: "xmfontlistentryload(3)"
name: "xmfontlistentryload"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfontlistentryload/"
description: "XmFontListEntryLoad — A font list function that loads a font or creates a font set and creates an accompanying font list entry"
---

<p><code>XmFontListEntryLoad</code> &#8212; A font list function that loads a font or creates a font set and creates an accompanying font list entry</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmFontListEntry XmFontListEntryLoad</code>(
<code>Display *display</code>,
<code>char *font_name</code>,
<code>XmFontType type</code>,
<code>char *tag</code>);</pre>
<h2>Description</h2>
<p><code>XmFontListEntryLoad</code> loads a font or creates a font set based on the value of the <i>type</i> argument. It creates and returns a font list entry that contains the font or font set and the specified tag. </p>
<p> If the value of <i>type</i> is <code>XmFONT_IS_FONT</code>, the function uses the <code>XtCvtStringToFontStruct</code> routine to convert the value of <i>font_name</i> to a font struct. If the value of <i>type</i> is <code>XmFONT_IS_FONTSET</code>, the function uses the <code>XtCvtStringToFontSet</code> converter to create a font set in the current locale. <code>XmFontListEntryLoad</code> creates a font list entry that contains the font or font set derived from the converter. For more information about <code>XtCvtStringToFontStruct</code> and <code>XtCvtStringToFontSet</code>, see <i>X Toolkit Intrinsics&#8212;C Language Interface.</i> </p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the display where the font list will be used.</p>
<dt><i>font_name</i></p>
<dd>Specifies an X Logical Font Description (XLFD) string, which is interpreted either as a font name or as a base font name list. A base font name list is a comma-separated and NULL-terminated string.</p>
<dt><i>type</i></p>
<dd>Specifies whether the <i>font_name</i> argument refers to a font name or to a base font name list. Valid values are <code>XmFONT_IS_FONT</code> and <code>XmFONT_IS_FONTSET</code>.</p>
<dt><i>tag</i></p>
<dd>Specifies the tag of the font list entry to be created. The tag may be specified as <code>XmFONTLIST_DEFAULT_TAG</code>, which is used to identify the default font list element in a font list when specified as part of a resource.</dl>
<h2>Return</h2>
<p>If the specified font is not found, or if the specified font set cannot be created, then either an implementation-defined font will be opened or a font set will be created, and a warning messge will be generated. If no suitable font can be found or a font set cannot be created, then another message will be generated and the function will return NULL; otherwise the function returns a font list entry. If the function returns a font list entry, the function allocates space to hold the font list entry. The application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmFontListEntryFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistappendentry/">XmFontListAppendEntry</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentrycreate/">XmFontListEntryCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentryfree/">XmFontListEntryFree</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentrygetfont/">XmFontListEntryGetFont</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentrygettag/">XmFontListEntryGetTag</a></code>(3), and <code><a href="/docs/linux/man/3-xmfontlistremoveentry/">XmFontListRemoveEntry</a></code>(3).</p>
