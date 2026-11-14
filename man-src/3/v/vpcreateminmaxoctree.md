---
title: "vpcreateminmaxoctree(3)"
name: "vpcreateminmaxoctree"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpcreateminmaxoctree/"
description: "vpCreateMinMaxOctree, vpMinMaxOctreeThreshold, vpDestroyMinMaxOctree – create/destroy a min-max octree for optimized rendering"
---

<p>vpCreateMinMaxOctree, vpMinMaxOctreeThreshold, vpDestroyMinMaxOctree &#8211; create/destroy a min-max octree for optimized rendering</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpCreateMinMaxOctree(</code><i>vpc, root_node_size, base_node_size</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>root_node_size, base_node_size;</i>  vpResult</p>
<dl>
<dt> <code>vpMinMaxOctreeThreshold(</code><i>vpc, param_num, range</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>param_num, range;</i>  vpResult</p>
<dl>
<dt> <code>vpDestroyMinMaxOctree(</code><i>vpc</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>root_node_size</i></p>
<dd>Number of voxels per side in the top level (largest nodes) of the octree. Not currently used.</p>
<dt><i>base_node_size</i></p>
<dd>Number of voxels per side in the bottom level (smallest nodes) of the octree. Must be a power of 2.</p>
<dt><i>param_num</i></p>
<dd>Identifying number of one parameter of the opacity transfer function.</p>
<dt><i>range</i></p>
<dd>Range threshold for one parameter of the opacity transfer function. If an octree node spans a larger range then it is subdivided.</dl>
<h2>Description</h2>
<p>These routines are used to create and destroy a min-max octree, an internal data structure that is used to accelerate classifying and rendering volume data in a 3D voxel array. The octree is a hierarchical data structure that contains minimum and maximum values for each voxel field. It does not duplicate the data in the voxel array. The octree is not used with preclassified volumes (see <a href="/docs/linux/man/3-vpclassifyvolume/">vpClassifyVolume</a>(3)). </p>
<p> Before creating an octree, declare a 3D voxel array using <code>vpSetVolumeSize, vpSetVoxelSize, vpSetVoxelField</code> and <code>vpSetRawVoxels,</code> and initialize parameters for the opacity transfer function by calling <code>vpSetClassifierTable</code>. Then initialize the voxel data in the array. The lookup tables for the opacity transfer function do not need to be initialized. </p>
<p> Now call <code>vpMinMaxOctreeThreshold</code> once for each parameter to the opacity transfer function. The parameter number is the same number as the parameter number you would pass to <code>vpClassifierTable.</code> The <i>range</i> argument specifies a &quot;small&quot; range of values for the corresponding parameter. The opacity of a voxel should not vary much for voxels within this range of parameter space. Choosing a value which is too small or too large may result in a reduced performance benefit during rendering. The function <code>vpOctreeMask</code> can be used to visualize the effectiveness of various parameter ranges. Note that you must choose the voxel field associated with each opacity transfer function parameter in advance of creating the octree (by calling <code>vpSetClassiferTable</code>), but the opacity transfer function itself does not need to be known since the lookup tables do not need to be initialized. In the current implementation all of the parameters must be one or two-byte voxel fields; four-byte fields are not allowed. </p>
<p> Finally, call <code>vpCreateMinMaxOctree</code> to actually compute the octree. The arguments specify the largest and smallest node size. These values can be used to trade off storage size of the octree for increased resolution. The octree is stored in the rendering context and is used automatically in subsequent calls to <code>vpClassifyVolume</code> and <code>vpRenderRawVolume.</code> Only one octree may be stored in a context at a time. If an octree already exists when <code>vpCreateMinMaxOctree</code> is called then the old octree is destroyed. </p>
<p> If the data in the voxel array changes then the min-max octree must be explicitly recomputed by calling <code>vpCreateMinMaxOctree</code> again before the next call to <code>vpClassifyVolume</code> or <code>vpRenderRawVolume.</code> </p>
<p> <code>vpDestroyMinMaxOctree</code> destroys the current min-max octree and frees the associated storage.</p>
<h2>State Variables</h2>
<p>The current octree parameters can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_CLASSIFY_FIELD_COUNT, VP_CLASSIFY_FIELDS, VP_MMOCTREE_THRESHOLDS, VP_MMOCTREE_SIZE.</p>
<h2>Errors</h2>
<p>The normal return value for all three functions is VP_OK. <code>vpMinMaxOctreeThreshold</code> can return the following error value:</p>
<dl>
<dt>VPERROR_BAD_VALUE</p>
<dd>The parameter number is invalid.</dl>
<p> <code>vpCreateMinMaxOctree</code> can return the following error values:</p>
<dl>
<dt>VPERROR_BAD_VALUE</p>
<dd>The node size arguments are not a power of two.</p>
<dt>VPERROR_BAD_VOXEL</p>
<dd>The voxel size or the voxel fields have not been specified or have been incorrectly specified, or the number of parameters to the opacity transfer function has been incorrectly specified.</p>
<dt>VPERROR_BAD_VOLUME</p>
<dd>The volume array or volume dimensions have not been specified, or the size of the volume array does not match the volume dimensions.</p>
<dt>VPERROR_BAD_CLASSIFIER</p>
<dd>The fields specified as parameters to the opacity transfer function are invalid or do not have valid sizes.</p>
<dt>VPERROR_LIMIT_EXCEEDED</p>
<dd>The volume is too large, so the maximum size of the octree has been exceeded. Change the constant VP_MAX_OCTREE_LEVELS in volpack.h and recompile the VolPack library.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpclassifyvolume/">vpClassifyVolume</a>(3), <a href="/docs/linux/man/3-vpoctreemask/">vpOctreeMask</a>(3), <a href="/docs/linux/man/3-vprenderrawvolume/">vpRenderRawVolume</a>(3) </p>
