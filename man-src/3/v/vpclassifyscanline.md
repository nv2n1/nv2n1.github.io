---
title: "vpclassifyscanline(3)"
name: "vpclassifyscanline"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpclassifyscanline/"
description: "vpClassifyScanline – incrementally create a preclassified volume from scanlines of scalar data"
---

<p>vpClassifyScanline &#8211; incrementally create a preclassified volume from scanlines of scalar data</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpClassifyScanline(</code><i>vpc, voxels</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>void *<i>voxels;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>voxels</i></p>
<dd>1D array of voxel data.</dl>
<h2>Description</h2>
<p><code>vpClassifyScanline</code> is used to incrementally compute a preclassified volume by classifying one scanline of voxels and storing the result in the current preclassified volume. </p>
<p> The <i>voxels</i> argument is a 1D array containing voxels in the format previously specified with <code>vpSetVoxelSize</code> and <code>vpSetVoxelField</code>. <code>vpVolumeSize</code> must be called to declare the size of the volume before the first call to <code>vpClassifyScanline</code>, and the length of the 1D voxel array must be equal to the length of the X dimension of the volume. The 1D voxel array may be initialized with <code>vpScanlineNormals</code> or a user-defined function. </p>
<p> The voxels in the array are classified using the current opacity transfer function (see <a href="/docs/linux/man/3-vpsetclassifiertable/">vpSetClassifierTable</a>(3)) and appended to the preclassified volume (see <a href="/docs/linux/man/3-vpclassifyvolume/">vpClassifyVolume</a>(3)). Scanlines must be processed in Z-major order: all of the scanlines in the Z=0 slice are processed from Y=0 onward, then the Z=1 slice is processed, and so on. When the last scanline in the volume has been processed the preclassified data structure is ready to be used for rendering. Rendering is not possible until all scanlines have been processed. </p>
<p> When the first scanline of a volume is passed to <code>vpClassifyScanline</code>, any existing preclassified volume data is destroyed.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_VOXEL</p>
<dd>The voxel size or the voxel fields have not been specified or have been incorrectly specified.</p>
<dt>VPERROR_BAD_CLASSIFIER</p>
<dd>The opacity transfer function tables have invalid sizes or are associated with invalid voxel fields or have been incorrectly specified.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpsetclassifiertable/">vpSetClassifierTable</a>(3), <a href="/docs/linux/man/3-vpclassifyvolume/">vpClassifyVolume</a>(3), <a href="/docs/linux/man/3-vpclassifyscalars/">vpClassifyScalars</a>(3) </p>
