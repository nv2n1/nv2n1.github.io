---
title: "vpoctreemask(3)"
name: "vpoctreemask"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpoctreemask/"
description: "vpOctreeMask – compute a mask representing one level of a min-max octree"
---

<p>vpOctreeMask &#8211; compute a mask representing one level of a min-max octree</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpOctreeMask(</code><i>vpc, array, array_size, max_level</i><code>)</code></p>
<dd>
<dd>vpContext <i>*vpc;</i></p>
<dd>unsigned char *<i>array;</i></p>
<dd>int <i>array_size;</i></p>
<dd>int <i>max_level;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>array</i></p>
<dd>A 3D array for storing the mask.</p>
<dt><i>array_size</i></p>
<dd>Size of <i>array</i> in bytes.</p>
<dt><i>max_level</i></p>
<dd>Maximum octree level to descend to.</dl>
<h2>Description</h2>
<p><code>vpOctreeMask</code> is used for performance debugging when rendering volumes with a min-max octree. During rendering the min-max octree is used to help determine which voxels are transparent. The time required to make this determination can be minimized by an appropriate choice for the range parameters for <code>vpMinMaxOctreeThreshold</code> and the node size parameters for <code>vpCreateMinMaxOctree</code>. <code>vpOctreeMask</code> provides information that can help to determine whether a set of parameters works effectively or not. </p>
<p> The output of the routine is stored in a 3D array of bytes that has the same dimensions as the volume (although each element is only one byte, regardless of the size of a voxel). For each voxel in the volume the corresponding byte in the output array is set by <code>vpOctreeMask</code> to one of three values: 0 if the voxel is definitely transparent, 255 if the voxel may be non-transparent, or 128 if the voxel may be non-transparent and there is more detailed information available at unvisited levels of the octree. The <i>max_level</i> argument specifies the deepest level of the octree to be visited (the root level is level 0). </p>
<p> A suggested way to use this routine is to compute an octree using a particular set of parameters and then call <code>vpOctreeMask</code> with several different values for <i>max_level.</i> For each resulting mask array, look at slices (or create a volume rendering!) and see how accurately the mask captures the general shape of the data in the original volume. The best set of parameters results in a mask that captures the general shape without an excessively small value for the minimum octree node size (which would result in a very large data structure and a lot of traversal overhead).</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_SIZE</p>
<dd>There is no octree or the output array has the wrong size.</p>
<dt>VPERROR_BAD_VOXEL</p>
<dd>The voxel size or the voxel fields have not been specified or have been incorrectly specified.</p>
<dt>VPERROR_BAD_CLASSIFIER</p>
<dd>The opacity transfer function tables have invalid sizes or are associated with invalid voxel fields or have been incorrectly specified.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpcreateminmaxoctree/">vpCreateMinMaxOctree</a>(3) </p>
