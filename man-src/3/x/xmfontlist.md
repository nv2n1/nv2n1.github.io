---
title: "xmfontlist(3)"
name: "xmfontlist"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfontlist/"
description: "XmFontList — Data type for a font list"
---

<p><code>XmFontList</code> &#8212; Data type for a font list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;</pre>
<h2>Description</h2>
<p><code>XmFontList</code> is the data type for a font list. A font list consists of font list entries. Each entry contains a font or a font set (a group of fonts) and is identified with a tag, which is optional. If this tag is NULL, the tag is set to <code>XmFONTLIST_DEFAULT_TAG</code>. </p>
<p> The value of <code>XmFONTLIST_DEFAULT_TAG</code> is <code>XmFONTLIST_DEFAULT_TAG_STRING</code>. </p>
<p> When a compound string is displayed, the font list element tag of the compound string segment is matched with a font list entry tag in the font list and the matching font list entry is used to display the compound string. A font list entry is chosen as follows:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>The first font list entry whose tag matches the tag of the compound string segment is used.</p>
<dt> &bull;</p>
<dd>If no match has been found and if the tag of the compound string segment is <code>XmFONTLIST_DEFAULT_TAG</code>, the first font list entry whose tag matches the tag that would result from creating an entry with <code>XmSTRING_DEFAULT_CHARSET</code> is used. For example, if creating an entry with <code>XmSTRING_DEFAULT_CHARSET</code> would result in the tag <code>ISO8859-1</code>, the compound string segment tag <code>XmFONTLIST_DEFAULT_TAG</code> matches the font list entry tag <code>ISO8859-1</code>.</p>
<dt> &bull;</p>
<dd>If no match has been found and if the tag of the compound string segment matches the tag that would result from creating a segment with <code>XmSTRING_DEFAULT_CHARSET</code>, the first font list entry whose tag is <code>XmFONTLIST_DEFAULT_TAG</code> is used.</p>
<dt> &bull;</p>
<dd>If no match has been found, the first entry in the font list is used.</dl>
<p> The font list interface consists of the routines listed in <code>Related Information</code>. </p>
<p> Font lists are specified in resource files with the following syntax: </p>
<pre><i>resource_spec</i><code>:</code> <i>font_entry</i> [, <i>font_entry</i> ]+</pre>
<p>The resource value string consists of one or more font list entries separated by commas. Each <i>font_entry</i> identifies a font or font set and an optional font list entry tag. A tag specified for a single font follows the font name and is separated by = (equals sign); otherwise, in a font set the tag is separated by a colon. The colon is required whether a tag is specified or not. A font entry uses the following syntax to specify a single font: </p>
<pre><i>font_name</i> [ '=' <i>tag</i> ]</pre>
<p>For example, the following entry specifies a 10 point Times Italic font without a font list entry tag; </p>
<pre><tt>*fontList: -Adobe-Times-Medium-I-Normal--10*</tt></pre>
<p>A font entry containing a font set is similar, except a semicolon separates multiple font names and the specification ends with a colon followed by an optional tag: </p>
<pre><i>font_name</i> [ ';' <i>font_name</i> ]+ ':' [ <i>tag</i> ]</pre>
<p>A <i>font_name</i> is an X Logical Font Description (XLFD) string and <i>tag</i> is any set of characters from ISO646IRV except space, comma, colon, equal sign and semicolon. Following is an example of a font set entry. It consists of three fonts (except for charsets), and an explicit font list entry tag. </p>
<pre><tt>*fontList: -Adobe-Courier-Bold-R-Normal--25-180-100-100-M-150;-JIS-Fixed-Medium-R-Normal--26-180-100-100-C-240;-JIS-Fixed-Medium-R-Normal--26-180-100-100-C-120:MY_TAG</tt></pre>
<p>Note that the <code>XmRenderTable</code> is another data type that can be used for font lists. Refer to the <code><a href="/docs/linux/man/3-xmrendertable/">XmRenderTable</a></code>(3) for details.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfontlistadd/">XmFontListAdd</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistappendentry/">XmFontListAppendEntry</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistcopy/">XmFontListCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistcreate/">XmFontListCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentrycreate/">XmFontListEntryCreate</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentryfree/">XmFontListEntryFree</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentrygetfont/">XmFontListEntryGetFont</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentrygettag/">XmFontListEntryGetTag</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistentryload/">XmFontListEntryLoad</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistfree/">XmFontListFree</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistfreefontcontext/">XmFontListFreeFontContext</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistgetnextfont/">XmFontListGetNextFont</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistinitfontcontext/">XmFontListInitFontContext</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistnextentry/">XmFontListNextEntry</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistremoveentry/">XmFontListRemoveEntry</a></code>(3), <code><a href="/docs/linux/man/3-xmrendertable/">XmRenderTable</a></code>(3), and <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3).</p>
