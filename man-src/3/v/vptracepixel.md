---
title: "vptracepixel(3)"
name: "vptracepixel"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vptracepixel/"
description: "vpTracePixel – print a trace of the voxels composited into a pixel"
---

<p>vpTracePixel &#8211; print a trace of the voxels composited into a pixel</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpTracePixel(</code><i>vpc, trace_u, trace_v</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>trace_u, trace_v;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>trace_u, trace_v</i></p>
<dd>Intermediate image coordinates of the pixel to trace.</dl>
<h2>Description</h2>
<p>This routine is for debugging the rendering algorithms. If <i>(trace_u, trace_v)</i> is a valid set of coordinates in the intermediate image then a printout appears during rendering showing a trace of all of the voxels that contribute to the pixel. The intermediate image is not the same as the final image; see <a href="/docs/linux/man/3-vpgetvpsetimage/">vpGetvpSetImage</a>(3). </p>
<p> The VolPack library must be compiled with the -DDEBUG compiler option for this function to have any effect.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3) </p>
