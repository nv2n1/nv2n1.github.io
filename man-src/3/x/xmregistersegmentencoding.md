---
title: "xmregistersegmentencoding(3)"
name: "xmregistersegmentencoding"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmregistersegmentencoding/"
description: "XmRegisterSegmentEncoding — A compound string function that registers a compound text encoding format for a specified font list element tag"
---

<p><code>XmRegisterSegmentEncoding</code> &#8212; A compound string function that registers a compound text encoding format for a specified font list element tag</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>char * XmRegisterSegmentEncoding</code>(
<code>char *fontlist_tag</code>,
<code>char *ct_encoding</code>);</pre>
<h2>Description</h2>
<p><code>XmRegisterSegmentEncoding</code> registers a compound text encoding format with the specified font list element tag. The <code>XmCvtXmStringToCT</code> function uses this registry to map the font list tags of compound string segments to compound text encoding formats. Registering a font list tag that already exists in the registry overwrites the original entry. You can unregister a font list tag by passing a NULL value for the <i>ct_encoding</i> parameter.</p>
<dl COMPACT>
<dt><i>fontlist_tag</i></p>
<dd>Specifies the font list element tag to be registered. The tag must be a NULL-terminated ISO8859-1 string.</p>
<dt><i>ct_encoding</i></p>
<dd>Specifies the compound text character set to be used for segments with the font list tag. The value must be a NULL-terminated ISO8859-1 string. A value of <code>XmFONTLIST_DEFAULT_TAG</code> maps the specified font list tag to the code set of the locale.</dl>
<h2>Return</h2>
<p>Returns NULL for a new font list tag or the old <i>ct_encoding</i> value for an already registered font list tag. The application is responsible for freeing the storage associated with the returned data (if any) by calling <code>XtFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcvtxmstringtoct/">XmCvtXmStringToCT</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3), <code><a href="/docs/linux/man/3-xmmapsegmentencoding/">XmMapSegmentEncoding</a></code>(3), and <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3).</p>
