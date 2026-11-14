---
title: "xmfontlistcreate(3)"
name: "xmfontlistcreate"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfontlistcreate/"
description: "XmFontListCreate — A font list function that creates a font list"
---

<p><code>XmFontListCreate</code> &#8212; A font list function that creates a font list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmFontList XmFontListCreate</code>(
<code>XFontStruct * font</code>,
<code>XmStringCharSet charset</code>);</pre>
<h2>Description</h2>
<p><code>XmFontListCreate</code> creates a new font list with a single element specified by the provided font and character set. It also allocates the space for the font list. </p>
<p> <code>NOTE:</code> This function is obsolete and exists for compatibility with previous releases. It is replaced by <code>XmFontListAppendEntry</code>.</p>
<dl COMPACT>
<dt><i>font</i></p>
<dd>Specifies a pointer to a font structure for which the new font list is generated. This is the structure returned by the XLib <code>XLoadQueryFont</code> function.</p>
<dt><i>charset</i></p>
<dd>Specifies the character set identifier for the font. This can be <code>XmSTRING_DEFAULT_CHARSET</code>, but this value does not comply with the AES, and it may be removed in future versions of Motif. If the value is <code>XmSTRING_DEFAULT_CHARSET</code>, the routine derives the character set from the current language environment.</dl>
<h2>Return</h2>
<p>Returns NULL if <i>font</i> or <i>charset</i> is NULL; otherwise, returns a new font list.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3) and <code><a href="/docs/linux/man/3-xmfontlistappendentry/">XmFontListAppendEntry</a></code>(3).</p>
