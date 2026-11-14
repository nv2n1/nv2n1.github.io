---
title: "xmfontlistadd(3)"
name: "xmfontlistadd"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfontlistadd/"
description: "XmFontListAdd — A font list function that creates a new font list"
---

<p><code>XmFontListAdd</code> &#8212; A font list function that creates a new font list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmFontList XmFontListAdd</code>(
<code>XmFontList oldlist</code>,
<code>XFontStruct *font</code>,
<code>XmStringCharSet charset</code>);</pre>
<h2>Description</h2>
<p><code>XmFontListAdd</code> creates a new font list consisting of the contents of <i>oldlist</i> and the new font list element being added. This function deallocates <i>oldlist</i> after extracting the required information; therefore, do not reference <i>oldlist</i> thereafter. </p>
<p> <code>NOTE:</code> This function is obsolete and exists for compatibility with previous releases. It has been replaced by <code>XmFontListAppendEntry</code>.</p>
<dl COMPACT>
<dt><i>oldlist</i></p>
<dd>Specifies a pointer to the font list to which an entry will be added.</p>
<dt><i>font</i></p>
<dd>Specifies a pointer to a font structure for which the new font list is generated. This is the structure returned by the XLib <code>XLoadQueryFont</code> function.</p>
<dt><i>charset</i></p>
<dd>Specifies the character set identifier for the font. This can be <code>XmSTRING_DEFAULT_CHARSET</code>, but this value does not comply with the AES, and it may be removed in future versions of Motif. If the value is <code>XmSTRING_DEFAULT_CHARSET</code>, the routine derives the character set from the current language environment.</dl>
<h2>Return</h2>
<p>Returns NULL if <i>oldlist</i> is NULL; returns <i>oldlist</i> if <i>font</i> or <i>charset</i> is NULL; otherwise, returns a new font list.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3) and <code><a href="/docs/linux/man/3-xmfontlistappendentry/">XmFontListAppendEntry</a></code>(3).</p>
