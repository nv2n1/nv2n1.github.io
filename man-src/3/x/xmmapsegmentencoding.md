---
title: "xmmapsegmentencoding(3)"
name: "xmmapsegmentencoding"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmmapsegmentencoding/"
description: "XmMapSegmentEncoding — A compound string function that returns the compound text encoding format associated with the specified font list tag"
---

<p><code>XmMapSegmentEncoding</code> &#8212; A compound string function that returns the compound text encoding format associated with the specified font list tag</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>char * XmMapSegmentEncoding</code>(
<code>char *fontlist_tag</code>);</pre>
<h2>Description</h2>
<p><code>XmMapSegmentEncoding</code> searches the segment encoding registry for an entry that matches the specified font list tag and returns a copy of the associated compound text encoding format. The application is responsible for freeing the storage associated with the returned data by calling <code>XtFree</code>.</p>
<dl COMPACT>
<dt><i>fontlist_tag</i></p>
<dd>Specifies the compound string font list tag</dl>
<h2>Return</h2>
<p>Returns a copy of the associated compound text encoding format if the font list tag is found in the registry; otherwise, returns NULL.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmcvtxmstringtoct/">XmCvtXmStringToCT</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3), <code><a href="/docs/linux/man/3-xmregistersegmentencoding/">XmRegisterSegmentEncoding</a></code>(3), and <code><a href="/docs/linux/man/3-xmstring/">XmString</a></code>(3).</p>
