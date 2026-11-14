---
title: "vpclassifyscalars(3)"
name: "vpclassifyscalars"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpclassifyscalars/"
description: "vpClassifyScalars – create a preclassified volume from scalar data"
---

<p>vpClassifyScalars &#8211; create a preclassified volume from scalar data</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpClassifyScalars(</code><i>vpc, scalar_data, length, scalar_field,</p>
<dd>gradient_field, norm_field</i><code>)</code></p>
<dd>vpContext *<i>vpc;</i></p>
<dd>unsigned char *<i>scalars;</i></p>
<dd>int <i>size;</i></p>
<dd>int <i>scalar_field, gradient_field, norm_field;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>scalar_data</i></p>
<dd>A 3D array containing one 8-bit scalar value for each voxel in the volume.</p>
<dt><i>length</i></p>
<dd>Size of <i>scalar_data</i> in bytes.</p>
<dt><i>scalar_field</i></p>
<dd>Field number identifying a voxel field for storing the scalar value.</p>
<dt><i>gradient_field</i></p>
<dd>Field number identifying a voxel field for storing the gradient magnitude of the scalar value.</p>
<dt><i>norm_field</i></p>
<dd>Field number identifying a voxel field for storing the surface normal vector for the voxel.</dl>
<h2>Description</h2>
<p><code>vpClassifyScalars</code> combines the functionality of <code>vpVolumeNormals</code> and <code>vpClassifyVolume</code> to produce a preclassified volume directly from a 3D array of scalar values without creating a 3D voxel array. This routine is useful for preparing large data sets for rendering with a fixed classification function, especially if the 3D voxel array would be too large to fit in main memory. The primary limitation is that the only fields each voxel may contain are the fields produced by <code>vpVolumeNormals</code>: an 8-bit scalar value, and 8-bit gradient and/or a 16-bit surface normal vector. See also <code>vpClassifyScanline</code> for processing one scanline of a scalar array at a time. </p>
<p> To use the function, first define the volume size, voxel size, and voxel fields as you would before calling <code>vpVolumeNormals</code>. However, there is no need to call <code>vpSetRawVoxels.</code> Also define the opacity transfer function (see <a href="/docs/linux/man/3-vpsetclassifiertable/">vpSetClassifierTable</a>(3)). Then call <code>vpClassifyScalars</code> with the same arguments you would use for <code>vpVolumeNormals;</code> see <a href="/docs/linux/man/3-vpvolumenormals/">vpVolumeNormals</a>(3) for more details. The result is a preclassified volume, as described in <a href="/docs/linux/man/3-vpclassifyvolume/">vpClassifyVolume</a>(3). If a voxel array has been declared it is not used or modified. </p>
<p> Any existing preclassified volume data is destroyed.</p>
<h2>State Variables</h2>
<p>Information about the current preclassified volume can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_VIEW_X_SIZE, VP_VIEW_Y_SIZE, VP_VIEW_Z_SIZE, VP_VIEW_X_AXIS, VP_VIEW_Y_AXIS, VP_VIEW_Z_AXIS.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_VOXEL</p>
<dd>The voxel size or the voxel fields have not been specified or have been incorrectly specified.</p>
<dt>VPERROR_BAD_CLASSIFIER</p>
<dd>The opacity transfer function tables have invalid sizes or are associated with invalid voxel fields or have been incorrectly specified.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpvolumenormals/">vpVolumeNormals</a>(3), <a href="/docs/linux/man/3-vpsetclassifiertable/">vpSetClassifierTable</a>(3), <a href="/docs/linux/man/3-vpclassifyvolume/">vpClassifyVolume</a>(3), <a href="/docs/linux/man/3-vpclassifyscanline/">vpClassifyScanline</a>(3) </p>
