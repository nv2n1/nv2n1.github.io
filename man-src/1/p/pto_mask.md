---
title: "pto_mask(1)"
name: "pto_mask"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pto_mask/"
description: "pto_mask – Apply a mask"
---

<h2 class="name">NAME</h2>
<p> pto_mask &#8211; Apply a mask </p>
<h2>SYNOPSIS</h2>
<p> <code>pto_mask</code> [options] input.pto</p>
<h2>DESCRIPTION</h2>
<p> <code>pto_mask</code> applies a mask to nominated images</p>
<h2>USAGE</h2>
<pre>
   pto_mask --mask=maskfile
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code> | &#8211;output=file.pto</p>
<dd> Output Hugin <font SIZE="-1">PTO</font> file. Default: &lt;filename&gt;_mask.pto</p>
<dt><code>&#8211;mask=filename [at] imgNr</code></p>
<dd> Read the mask from the file and assign to given image</p>
<dt><code>&#8211;rotate=CLOCKWISE|90|COUNTERCLOCKWISE|-90</code></p>
<dd> Rotates the mask clock- or counterclockwise</p>
<dt><code>&#8211;process=CLIP|SCALE|PROP_SCALE</code></p>
<dd> Specify how the mask should be modified if the mask is created for an image with different size </p>
<pre>
   * CLIP: clipping (Default)
   * SCALE: Scaling width and height individually
   * PROP_SCALE: Proportional scale
</pre>
<dt><code>-h</code> | &#8211;help</p>
<dd> Shows this help</dl>
<h2>AUTHORS</h2>
<p> Thomas Modes </p>
<h2>Index</h2>
