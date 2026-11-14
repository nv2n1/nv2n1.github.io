---
title: "xmrendertablegetrenditions(3)"
name: "xmrendertablegetrenditions"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmrendertablegetrenditions/"
description: "XmRenderTableGetRenditions — A convenience function that matches rendition tags"
---

<p><code>XmRenderTableGetRenditions</code> &#8212; A convenience function that matches rendition tags</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmRendition *XmRenderTableGetRenditions</code>(
<code>XmRenderTable table</code>,
<code>XmStringTag *tags</code>,
<code>Cardinal tag_count</code>);</pre>
<h2>Description</h2>
<p><code>XmRenderTableGetRenditions</code> searches <i>table</i> and returns an array of copies of the renditions whose <code>XmNtag</code> resources match a tag in <i>tags</i>. If no renditions match, then NULL is returned. The size of the returned array is <i>tag_count</i>. The <code>XmNtag</code> resource of each rendition will match the corresponding tag in <i>tags</i>. If no match is found for a particular tag, the corresponding slot in the return value will be NULL. </p>
<p> It is the responsibility of the caller to call the <code>XmRenditionFree</code> function to free the new renditions, and the <code>XtFree</code> function to free the array.</p>
<dl COMPACT>
<dt><i>table</i></p>
<dd>Specifies the table containing renditions to be searched.</p>
<dt><i>tags</i></p>
<dd>Specifies the tags to search for.</p>
<dt><i>tag_count</i></p>
<dd>Specifies the number of tags in <i>tags</i>.</dl>
<h2>Return</h2>
<p>Returns NULL if there is no match; otherwise, this function returns an array of new <code>XmRendition</code>s.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmrendertablegetrendition/">XmRenderTableGetRendition</a></code>(3), <code><a href="/docs/linux/man/3-xmrendertablegettags/">XmRenderTableGetTags</a></code>(3), and <code><a href="/docs/linux/man/3-xmrendition/">XmRendition</a></code>(3).</p>
