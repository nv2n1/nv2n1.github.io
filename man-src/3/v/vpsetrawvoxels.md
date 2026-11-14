---
title: "vpsetrawvoxels(3)"
name: "vpsetrawvoxels"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpsetrawvoxels/"
description: "vpSetRawVoxels – specify an array of volume data"
---

<p>vpSetRawVoxels &#8211; specify an array of volume data</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpSetRawVoxels(</code><i>vpc, voxels, size, xstride, ystride, zstride</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>void *<i>voxels;</i></p>
<dd>int <i>size;</i></p>
<dd>int <i>xstride, ystride, zstride;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>voxels</i></p>
<dd>3D array of voxels.</p>
<dt><i>size</i></p>
<dd>Size of the voxel array in bytes.</p>
<dt><i>xstride</i></p>
<dd>Number of bytes from the beginning of one voxel to the beginning of the next voxel in the first array dimension.</p>
<dt><i>ystride</i></p>
<dd>Number of bytes from the beginning of one voxel to the beginning of the next voxel in the second array dimension.</p>
<dt><i>zstride</i></p>
<dd>Number of bytes from the beginning of one voxel to the beginning of the next voxel in the third array dimension.</dl>
<h2>Description</h2>
<p><code>vpSetRawVoxels</code> is used to specify a 3D array that contains the volume data. The array must be large enough for the volume dimensions specified with <code>vpSetVolumeSize</code> and the voxel size specified with <code>vpSetVoxelSize</code>. The data in the array may be initialized before or after calling <code>vpSetRawVoxels</code>. </p>
<p> Some of the VolPack routines operate faster if the volume is stored in z-major order (<i>xstride &lt; ystride &lt; zstride</i>) but it is not strictly necessary. </p>
<p> The voxel array is not automatically deallocated when the context is destroyed with <code>vpDestroyContext</code>. The application is responsible for managing the memory associated with the volume array. </p>
<p> The voxel array can be a very large data structure, possibly larger than available main memory. It is sometimes possible to precompute the optimized data structures required for the fast rendering algorithm without explicitly allocating a voxel array. See <a href="/docs/linux/man/3-vpclassifyscalars/">vpClassifyScalars</a>(3). </p>
<p> During the call to <code>vpSetRawVoxels</code>, any existing precomputed volume data structures in the context are destroyed.</p>
<h2>State Variables</h2>
<p>The current voxel array parameters can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_VOXEL_DATA, VP_VOXEL_DATA_SIZE, VP_VOXEL_XSTRIDE, VP_VOXEL_YSTRIDE, VP_VOXEL_ZSTRIDE.</p>
<h2>Errors</h2>
<p>The routine always returns VP_OK.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3) </p>
