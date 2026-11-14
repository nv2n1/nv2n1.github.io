---
title: "xmrendertablecopy(3)"
name: "xmrendertablecopy"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmrendertablecopy/"
description: "XmRenderTableCopy — A render table function that copies renditions"
---

<p><code>XmRenderTableCopy</code> &#8212; A render table function that copies renditions</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmRenderTable XmRenderTableCopy</code>(
<code>XmRenderTable table</code>,
<code>XmStringTag *tags</code>,
<code>int tag_count</code>);</pre>
<h2>Description</h2>
<p><code>XmRenderTableCopy</code> creates a new render table which will contain the renditions of the <i>table</i> whose tags match those in <i>tags</i>.</p>
<dl COMPACT>
<dt><i>table</i></p>
<dd>Specifies the table containing the renditions to be copied.</p>
<dt><i>tags</i></p>
<dd>Specifies an array of tags, whose corresponding renditions are to be copied. NULL indicates that the complete table should be copied.</p>
<dt><i>tag_count</i></p>
<dd>Specifies the number of tags in <i>tags</i>.</dl>
<h2>Return</h2>
<p>Returns NULL if <i>table</i> is NULL. Otherwise, this function returns the new render table. This function allocates space to hold the new render table. The application is responsible for managing this allocated space. The application can recover this allocated space by calling <code>XmRenderTableFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmrendition/">XmRendition</a></code>(3) and <code><a href="/docs/linux/man/3-xmrendertablefree/">XmRenderTableFree</a></code>(3).</p>
