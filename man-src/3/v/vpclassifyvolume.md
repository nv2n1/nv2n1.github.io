---
title: "vpclassifyvolume(3)"
name: "vpclassifyvolume"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpclassifyvolume/"
description: "vpClassifyVolume, vpDestroyClassifiedVolume – create/destroy a preclassified volume for fast rendering"
---

<p>vpClassifyVolume, vpDestroyClassifiedVolume &#8211; create/destroy a preclassified volume for fast rendering</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpClassifyVolume(</code><i>vpc</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i>  vpResult</p>
<dl>
<dt> <code>vpDestroyClassifyVolume(</code><i>vpc</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></dl>
<h2>Description</h2>
<p><code>vpClassifyVolume</code> is used to compute a preclassified volume for the fast rendering algorithm. The preclassified volume is an internal data structure optimized for rendering speed. <code>vpClassifyVolume</code> should be called after a voxel array has been defined (with <code>vpSetVolumeSize, vpSetVoxelSize, vpSetVoxelField,</code> and <code>vpSetRawVoxels</code>) and initialized (with <code>vpVolumeNormals</code> or a user-defined routine). An opacity transfer function must also be defined with <code>vpSetClassifierTable,</code> and the minimum opacity threshold should be set with the VP_MIN_VOXEL_OPACITY parameter to <code>vpSeti</code>. Two alternative routines are provided to compute a preclassified volume directly from a 3D scalar array or a sequence of scalar scanlines in order to avoid allocating a large 3D voxel array (see <a href="/docs/linux/man/3-vpclassifyscalars/">vpClassifyScalars</a>(3) and <a href="/docs/linux/man/3-vpclassifyscanline/">vpClassifyScanline</a>(3)). </p>
<p> <code>vpClassifyVolume</code> classifies and processes the data in the voxel array and creates a separate preclassified volume. The preclassified data is stored in a run-length encoded format, and voxels that have opacities less than or equal to the minimum opacity threshold are discarded. Normally, three copies of the preclassified volume are created, one for each of the three principal viewing axis. If only one or two copies are necessary for the required range of viewpoints then <code>vpSeti</code> may be called with one or more of the following parameters to specify which copies are required: VP_VIEW_X_AXIS, VP_VIEW_Y_AXIS, VP_VIEW_Z_AXIS. Using these parameters is not recommended unless swap space is lacking. </p>
<p> If a min-max octree is present in the rendering context (see <a href="/docs/linux/man/3-vpcreateminmaxoctree/">vpCreateMinMaxOctree</a>(3)) then it is used to accelerate computation of the preclassified volume. It is advantageous to create a min-max octree if the same volume data will be classified multiple times (with different opacity transfer functions). </p>
<p> Once <code>vpClassifyVolume</code> is finished, the original voxel array is no longer necessary for rendering as long as the opacity transfer function and the volume data do not change. If any changes are made, then the preclassified volume must be explicitly recomputed by calling <code>vpClassifyVolume</code> again. Only one preclassified volume may be stored in a rendering context at a time. Calling <code>vpClassifyVolume</code> causes any existing preclassified volume to be destroyed. </p>
<p> <code>vpDestroyClassifiedVolume</code> destroys the current preclassified volume and frees the associated space.</p>
<h2>State Variables</h2>
<p>Information about the current preclassified volume can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_VIEW_X_SIZE, VP_VIEW_Y_SIZE, VP_VIEW_Z_SIZE, VP_VIEW_X_AXIS, VP_VIEW_Y_AXIS, VP_VIEW_Z_AXIS.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_VOXEL</p>
<dd>The voxel size or the voxel fields have not been specified or have been incorrectly specified.</p>
<dt>VPERROR_BAD_VOLUME</p>
<dd>The volume array or volume dimensions have not been specified, or the size of the volume array does not match the volume dimensions.</p>
<dt>VPERROR_BAD_CLASSIFIER</p>
<dd>The opacity transfer function tables have invalid sizes or are associated with invalid voxel fields or have been incorrectly specified.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpsetclassifiertable/">vpSetClassifierTable</a>(3), <a href="/docs/linux/man/3-vpclassifyscalars/">vpClassifyScalars</a>(3), <a href="/docs/linux/man/3-vpclassifyscanline/">vpClassifyScanline</a>(3) </p>
