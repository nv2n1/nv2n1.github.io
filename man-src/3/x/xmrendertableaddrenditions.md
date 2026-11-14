---
title: "xmrendertableaddrenditions(3)"
name: "xmrendertableaddrenditions"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmrendertableaddrenditions/"
description: "XmRenderTableAddRenditions — Creates a new render table"
---

<p><code>XmRenderTableAddRenditions</code> &#8212; Creates a new render table</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>XmRenderTable XmRenderTableAddRenditions</code>(
<code>XmRenderTable oldtable</code>,
<code>XmRendition *renditions</code>,
<code>Cardinal rendition_count</code>,
<code>XmMergeMode merge_mode</code>);</pre>
<h2>Description</h2>
<p><code>XmRenderTableAddRenditions</code> is a function to create a new render table that includes the renditions listed in <i>oldtable</i>, if there is one. This function also copies specified renditions (<i>renditions</i>) to the new render table. The first <i>rendition_count</i> renditions of the <i>renditions</i> array are added to the new table. If a rendition is tagged with a tag that matches a tag already in <i>oldtable</i>, then the existing rendition using that tag is either modified or freed and replaced with the new rendition, depending on the value of <i>merge_mode</i>. If <i>oldtable</i> is NULL, <code>XmRenderTableAddRenditions</code> creates a new render table containing only the specified renditions. </p>
<p> This function deallocates the original render table after extracting the required information. It is the responsibility of the caller to free the renditions of the <i>renditions</i> array by calling the <code>XmRenditionFree</code> function.</p>
<dl COMPACT>
<dt><i>oldtable</i></p>
<dd>Specifies the render table to be added to.</p>
<dt><i>renditions</i></p>
<dd>Specifies an array of renditions to be added.</p>
<dt><i>rendition_count</i></p>
<dd>Specifies the number of renditions from <i>renditions</i> to be added.</p>
<dt><i>merge_mode</i></p>
<dd>Specifies what to do if the <code>XmNtag</code> of a rendition matches that of one that already exists in <i>oldtable</i>. The possible values are as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmMERGE_REPLACE</code></p>
<dd>Completely replaces the old rendition with the new one.</p>
<dt><code>XmMERGE_OLD</code></p>
<dd>Replaces any unspecified values of the old rendition with the corresponding values from the new rendition.</p>
<dt><code>XmMERGE_NEW</code></p>
<dd>Replaces the old rendition with the new rendition, replacing any unspecified values of the new rendition with the corresponding values from the old rendition.</p>
<dt><code>XmSKIP</code></p>
<dd>Skips over the new rendition, leaving the old rendition intact.</dl>
</dl>
</dl>
<h2>Return</h2>
<p>If <i>renditions</i> is NULL or <i>rendition_count</i> is 0 (zero), this function returns <i>oldtable</i>. Otherwise, the function returns a new <code>XmRenderTable</code>. The function allocates space to hold this new render table. The application is responsible for managing this allocated space. The application can recover the allocated space by calling <code>XmRenderTableFree</code>.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmrendition/">XmRendition</a></code>(3) and <code><a href="/docs/linux/man/3-xmrendertablefree/">XmRenderTableFree</a></code>(3).</p>
