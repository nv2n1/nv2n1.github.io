---
title: "vpstorerawvolume(3)"
name: "vpstorerawvolume"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpstorerawvolume/"
description: "vpStoreRawVolume, vpStoreMinMaxOctree, vpStoreClassifiedVolume, vpStoreContext – store volume data structures to a file"
---

<p>vpStoreRawVolume, vpStoreMinMaxOctree, vpStoreClassifiedVolume, vpStoreContext &#8211; store volume data structures to a file</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpStoreRawVolume(</code><i>vpc, fd</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>fd;</i>  vpResult</p>
<dl>
<dt> <code>vpStoreMinMaxOctree(</code><i>vpc, fd</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>fd;</i>  vpResult</p>
<dl>
<dt> <code>vpStoreClassifiedVolume(</code><i>vpc, fd</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>fd;</i>  vpResult</p>
<dl>
<dt> <code>vpStoreContext(</code><i>vpc, fd</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>fd;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>fd</i></p>
<dd>File descriptor from <code><a href="/docs/linux/man/2-open/">open</a></code>(2), open for writing.</dl>
<h2>Description</h2>
<p>These functions are used to store volume data structures from a rendering context into files in the format read by the VolPack file reading routines (see <a href="/docs/linux/man/3-vploadrawvolume/">vpLoadRawVolume</a>(3)). </p>
<p> <code>vpStoreRawVolume</code> creates a 3D voxel array file. The file includes information about the size of the volume and the layout of the voxels as well as the volume data itself. </p>
<p> <code>vpStoreMinMaxOctree</code> creates a min-max octree file. The file includes information about the size of the volume and the layout of the voxels as well as the octree itself. </p>
<p> <code>vpStoreClassifiedVolume</code> creates a preclassified volume data file. The file includes information about the size of the volume and the layout of the voxels as well as the volume data itself. </p>
<p> <code>vpStoreContext</code> creates a rendering context file. The file includes all rendering parameters except volume data and callback functions. The contents of any lookup tables for shading and classification are also stored. </p>
<p> The function used to write data to the files can be set by calling <code>vpSetCallback</code> with the VP_WRITE_FUNC option. This could be used to implement a file-compression system, for example.</p>
<h2>State Variables</h2>
<p>The current file I/O parameters can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_WRITE_FUNC.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_IO</p>
<dd>The file writing function returned an error value (in which case the external variable <code>errno</code> should contain an operating-system specific error code), or the file system is full.</p>
<dt>VPERROR_BAD_VOLUME</p>
<dd>The volume dimensions are invalid, or there is no voxel data in the context.</p>
<dt>VPERROR_BAD_SIZE</p>
<dd>There is no min-max octree in the volume (<code>vpStoreMinMaxOctree</code> only).</p>
<dt>VPERROR_BAD_VOXEL</p>
<dd>The voxel fields in the rendering context have not been properly defined.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vploadrawvolume/">vpLoadRawVolume</a>(3) </p>
