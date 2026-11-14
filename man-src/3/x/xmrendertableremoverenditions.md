---
title: "xmrendertableremoverenditions(3)"
name: "xmrendertableremoverenditions"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmrendertableremoverenditions/"
description: "XmRenderTableRemoveRenditions — A convenience function that removes renditions"
---

<p><code>XmRenderTableRemoveRenditions</code> &#8212; A convenience function that removes renditions</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmRenderTable XmRenderTableRemoveRenditions</code>(
<code>XmRenderTable oldtable</code>,
<code>XmStringTag *tags</code>,
<code>int tag_count</code>);</pre>
<h2>Description</h2>
<p><code>XmRenderTableRemoveRenditions</code> removes from <i>oldtable</i> the renditions whose tags match the tags specified in <i>tags</i>, then places the remaining renditions in a newly created render table.</p>
<dl COMPACT>
<dt><i>oldtable</i></p>
<dd>Specifies the render table from which renditions are to be removed. This function deallocates the original render table and the matching renditions after extracting the required information.</p>
<dt><i>tags</i></p>
<dd>Specifies an array of tags, whose corresponding renditions are to be removed from <i>oldtable</i>.</p>
<dt><i>tag_count</i></p>
<dd>Specifies the number of tags in <i>tags</i>.</dl>
<h2>Return</h2>
<p>If <i>oldtable</i> or <i>tags</i> is NULL, or <i>tag_count</i> is 0 (zero), or no renditions are removed from <i>oldtable</i>, this function returns <i>oldtable</i>. Otherwise, it returns a newly allocated <code>XmRenderTable</code>. The application is responsible for managing this allocated render table. The application can recover this allocated space by calling <code>XmRenderTableFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmrendition/">XmRendition</a></code>(3) and <code><a href="/docs/linux/man/3-xmrendertablefree/">XmRenderTableFree</a></code>(3).</p>
