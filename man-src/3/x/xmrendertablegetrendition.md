---
title: "xmrendertablegetrendition(3)"
name: "xmrendertablegetrendition"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmrendertablegetrendition/"
description: "XmRenderTableGetRendition — A convenience function that matches a rendition tag"
---

<p><code>XmRenderTableGetRendition</code> &#8212; A convenience function that matches a rendition tag</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmRendition XmRenderTableGetRendition</code>(
<code>XmRenderTable table</code>,
<code>XmStringTag tag</code>);</pre>
<h2>Description</h2>
<p><code>XmRenderTableGetRendition</code> searches <i>table</i> and returns a copy of the rendition whose <code>XmNtag</code> resource matches <i>tag</i>. If no rendition matches, then NULL is returned. This function is to be used for just one rendition match. </p>
<p> It is the responsibility of the caller to free the returned rendition with the <code>XmRenditionFree</code> function.</p>
<dl COMPACT>
<dt><i>table</i></p>
<dd>Specifies the table containing renditions to be searched.</p>
<dt><i>tag</i></p>
<dd>Specifies the tag to search for.</dl>
<h2>Return</h2>
<p>Returns NULL if there is no match; otherwise, this function returns a new <code>XmRendition</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmrendertablegetrenditions/">XmRenderTableGetRenditions</a></code>(3), <code><a href="/docs/linux/man/3-xmrendertablegettags/">XmRenderTableGetTags</a></code>(3), and <code><a href="/docs/linux/man/3-xmrendition/">XmRendition</a></code>(3).</p>
