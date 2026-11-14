---
title: "xmfontlistinitfontcontext(3)"
name: "xmfontlistinitfontcontext"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmfontlistinitfontcontext/"
description: "XmFontListInitFontContext — A font list function that allows applications to access the entries in a font list"
---

<p><code>XmFontListInitFontContext</code> &#8212; A font list function that allows applications to access the entries in a font list</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>Boolean XmFontListInitFontContext</code>(
<code>XmFontContext *context</code>,
<code>XmFontList fontlist</code>);</pre>
<h2>Description</h2>
<p><code>XmFontListInitFontContext</code> establishes a context to allow applications to access the contents of a font list. This context is used when reading the font list entry tag, font, or font set associated with each entry in the font list. A Boolean status is returned to indicate whether or not the font list is valid. </p>
<p> If an application deallocates the font list passed to <code>XmFontListInitFontContext</code> as the fontlist argument, the context established by this function is rendered no longer valid.</p>
<dl COMPACT>
<dt><i>context</i></p>
<dd>Specifies a pointer to the allocated context</p>
<dt><i>fontlist</i></p>
<dd>Specifies the font list</dl>
<h2>Return</h2>
<p>Returns True if the context was allocated; otherwise, returns False. If the function allocated a context, the application is responsible for managing the allocated space. The application can recover the allocated space by calling <code>XmFontListFreeFontContext</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmfontlist/">XmFontList</a></code>(3), <code><a href="/docs/linux/man/3-xmfontlistfreefontcontext/">XmFontListFreeFontContext</a></code>(3), and <code><a href="/docs/linux/man/3-xmfontlistnextentry/">XmFontListNextEntry</a></code>(3).</p>
