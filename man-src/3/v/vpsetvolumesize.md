---
title: "vpsetvolumesize(3)"
name: "vpsetvolumesize"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpsetvolumesize/"
description: "vpSetVolumeSize – define the dimensions of a volume"
---

<p>vpSetVolumeSize &#8211; define the dimensions of a volume</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpSetVolumeSize(</code><i>vpc, xlen, ylen, zlen</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>xlen, ylen, zlen;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>xlen</i></p>
<dd>Size of first dimension of the volume in voxels.</p>
<dt><i>ylen</i></p>
<dd>Size of the second dimension of the volume in voxels.</p>
<dt><i>zlen</i></p>
<dd>Size of the third dimension of the volume in voxels.</dl>
<h2>Description</h2>
<p><code>vpSetVolumeSize</code> is used to define the dimensions of a volume. It must be called before volume data is loaded into a rendering context. Any existing precomputed volume data structures in the context are destroyed.</p>
<h2>State Variables</h2>
<p>The current volume dimensions may be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_XLEN, VP_YLEN, VP_ZLEN.</p>
<h2>Errors</h2>
<p>The return value is always VP_OK.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3) </p>
