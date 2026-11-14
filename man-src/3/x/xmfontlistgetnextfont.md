---
title: "xmfontlistgetnextfont(3)"
name: "xmfontlistgetnextfont"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfontlistgetnextfont/"
description: "XmFontListGetNextFont — A font list function that allows applications to access the fonts and character sets in a font list"
---

<p><code>XmFontListGetNextFont</code> &#8212; A font list function that allows applications to access the fonts and character sets in a font list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmFontListGetNextFont</code>(
<code>XmFontContext context</code>,
<code>XmStringCharSet *charset</code>,
<code>XFontStruct **font</code>);</pre>
<h2>Description</h2>
<p><code>XmFontListGetNextFont</code> accesses the character set and font for the next entry of the font list. The application first uses the <code>XmFontListInitFontContext</code> routine to create a font list context. The application then calls <code>XmFontListGetNextFont</code> repeatedly with the same context. Each succeeding call accesses the next element of the font list. When finished, the application calls <code>XmFontListFreeFontContext</code> to free the allocated font list context. </p>
<p> This routine allocates memory for the character set string that must be freed by the application. The function allocates memory for <i>charset</i>. The application is responsible for managing the allocated memory. The application can recover the allocated memory by calling <code>XtFree</code>. </p>
<p> This function is obsolete and exists for compatibility with previous releases. It is replaced by <code>XmFontListNextEntry</code>. If <code>XmFontListGetNextFont</code> is passed a context that contains a font set entry, it will return the first font of the font set. The next call to the function will move to the next entry in the font list.</p>
<dl COMPACT>
<dt><i>context</i></p>
<dd>Specifies the font list context</p>
<dt><i>charset</i></p>
<dd>Specifies a pointer to a character set string; the routine returns the character set for the current font list element</p>
<dt><i>font</i></p>
<dd>Specifies a pointer to a pointer to a font structure; the routine returns the font for the current font list element</dl>
<h2>Return</h2>
<p>Returns True if the returned values are valid; otherwise, returns False.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3) and <code><a href="/docs/linux/man/3-xmfontlistnextentry/">XmFontListNextEntry</a></code>(3).</p>
