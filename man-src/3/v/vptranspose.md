---
title: "vptranspose(3)"
name: "vptranspose"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vptranspose/"
description: "vpTranspose – transpose a volume"
---

<p>vpTranspose &#8211; transpose a volume</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpTranspose(</code><i>vpc, axis</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>axis;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>axis</i></p>
<dd>Axis which should have the smallest stride after transposing (VP_X_AXIS, VP_Y_AXIS or VP_Z_AXIS).</dl>
<h2>Description</h2>
<p><code>vpTranspose</code> is used to transpose the 3D voxel array to optimize the memory stride for a particular principal viewing axis. The intended way to use this function is to set the viewing transformation, call <code>vpGeti</code> with the VP_VIEW_AXIS argument to find the corresponding viewing axis, and then call <code>vpTranspose</code> with that axis. Transposing the data changes the arrangement of the data stored in the 3D voxel array. The voxel stride state variables are updated to reflect this change, so the viewing transformation does not need to be changed after transposing. If the volume is already transposed for the requested axis then it returns immediately without modifying the voxel array. </p>
<p> This function is useful only for rendering large 3D voxel arrays. This function has no affect on the preclassified volume data.</p>
<h2>State Variables</h2>
<p>Relevant variables may be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_VIEW_AXIS, VP_VOXEL_XSTRIDE, VP_VOXEL_YSTRIDE, VP_VOXEL_ZSTRIDE.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_OPTION</p>
<dd>The <i>axis</i> argument is invalid.</p>
<dt>VPERROR_BAD_VOLUME</p>
<dd>The 3D voxel array is missing or invalid.</p>
<dt>VPERROR_BAD_VOXEL</p>
<dd>The voxel fields are incorrectly specified.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3) </p>
