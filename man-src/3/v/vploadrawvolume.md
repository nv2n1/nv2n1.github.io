---
title: "vploadrawvolume(3)"
name: "vploadrawvolume"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vploadrawvolume/"
description: "vpLoadRawVolume, vpLoadMinMaxOctree, vpLoadClassifiedVolume, vpLoadContext – load volume data structures from a file"
---

<p>vpLoadRawVolume, vpLoadMinMaxOctree, vpLoadClassifiedVolume, vpLoadContext &#8211; load volume data structures from a file</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpLoadRawVolume(</code><i>vpc, fd</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>fd;</i>  vpResult</p>
<dl>
<dt> <code>vpLoadMinMaxOctree(</code><i>vpc, fd</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>fd;</i>  vpResult</p>
<dl>
<dt> <code>vpLoadClassifiedVolume(</code><i>vpc, fd</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>fd;</i>  vpResult</p>
<dl>
<dt> <code>vpLoadContext(</code><i>vpc, fd</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>fd;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>fd</i></p>
<dd>File descriptor from <code><a href="/docs/linux/man/2-open/">open</a></code>(2), open for reading.</dl>
<h2>Description</h2>
<p>These functions are used to load volume data structures into a rendering context from files in the format written by the VolPack file storing routines (see <a href="/docs/linux/man/3-vpstorerawvolume/">vpStoreRawVolume</a>(3)). </p>
<p> <code>vpLoadRawVolume</code> loads a 3D voxel array file. The file includes information about the size of the volume and the layout of the voxels as well as the volume data itself. A new voxel array is allocated, the data is read into the array, and the array is stored in the rendering context. Note that the array will not be freed automatically when the context is destroyed; the application is responsible for freeing the array when appropriate (by using <code>vpGetp</code> with the VP_VOXEL_DATA state variable code to retrieve the array pointer), or for unmapping the voxel array if it has been memory mapped (see below). </p>
<p> Any existing min-max octree or preclassified volume data is destroyed when <code>vpLoadRawVolume</code> is called. The information loaded from the file includes all of the parameters set with <code>vpSetVolumeSize</code>, <code>vpSetVoxelSize</code>, <code>vpSetVoxelField</code> and <code>vpSetRawVoxels</code>. The data in the file is automatically byte-swapped if the file was written on an architecture with different byte ordering than the current architecture. A magic constant in the file is used to determine if byte-swapping is necessary. Volume fields that have not been explicitly declared (by calling <code>vpSetVoxelField</code> before storing the voxel array file) cannot be byte-swapped. </p>
<p> <code>vpLoadMinMaxOctree</code> loads a min-max octree file. The current 3D voxel array size and voxel layout must match the data in the octree file before the file is loaded; consistency checks are performed. Any existing octree is destroyed and the new octree is stored in the rendering context. Byte-swapping is performed if necessary. </p>
<p> <code>vpLoadClassifiedVolume</code> loads a preclassified volume data file. The file includes information about the size of the volume and the layout of the voxels as well as the volume data itself. If the volume matches the size and layout of any existing volume data in the rendering context then the data in the file replaces only the current preclassified volume; otherwise, the old octree is destroyed, the 3D voxel array parameters are zeroed out, and the new size and layout parameters are loaded. The information loaded from the file includes all of the parameters set with <code>vpSetVolumeSize</code>, <code>vpSetVoxelSize</code> and <code>vpSetVoxelField</code>. Byte-swapping is performed if necessary. </p>
<p> <code>vpLoadContext</code> loads a rendering context file. The file includes all rendering parameters except volume data and callback functions. The contents of any lookup tables for shading and classification are also loaded. Any existing preclassified volume data or octree are destroyed and the 3D voxel array parameters pointer is zeroed out. The lookup tables are loaded into dynamically allocated arrays, and the application is responsible for freeing those array when necessary; the arrays are not automatically freed when <code>vpDestroyContext</code> is called. In the current implementation byte swapping is not performed so context files from other architectures cannot be read. </p>
<p> The function used to read data from the files can be set by calling <code>vpSetCallback</code> with the VP_READ_FUNC option. This could be used to implement a file-compression system, for example. It is also possible to memory-map data from files by setting the VP_MMAP_FUNC option. If this function is set then large data structures are memory mapped from files instead of being copied into memory, when possible. Data that must be byte-swapped cannot be memory mapped. Memory mapping has the advantages that less swap space is required and data is loaded into memory only as it is used.</p>
<h2>State Variables</h2>
<p>The current file I/O parameters can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_READ_FUNC, VP_MMAP_FUNC.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_IO</p>
<dd>The file reading or memory mapping function returned an error value (in which case the external variable <code>errno</code> should contain an operating-system specific error code), or the end of the file was reached prematurely.</p>
<dt>VPERROR_BAD_FILE</p>
<dd>The data in the file is invalid, usually meaning that it isn&#8217;t a file written by the appropriate VolPack function.</p>
<dt>VPERROR_BAD_VOLUME</p>
<dd>The data in a min-max octree file does not match the current volume size (<code>vpLoadMinMaxOctree</code> only).</p>
<dt>VPERROR_BAD_VOXEL</p>
<dd>The data in a min-max octree file does not match the current voxel layout parameters (<code>vpLoadMinMaxOctree</code> only).</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpstorerawvolume/">vpStoreRawVolume</a>(3) </p>
