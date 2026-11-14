---
title: "vpsetvoxelsize(3)"
name: "vpsetvoxelsize"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpsetvoxelsize/"
description: "vpSetVoxelSize – define the size of a voxel"
---

<p>vpSetVoxelSize &#8211; define the size of a voxel</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpSetVoxelSize(</code><i>vpc, bytes_per_voxel, num_voxel_fields,</p>
<dd>num_shade_fields, num_classify_fields</i><code>)</code></p>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>bytes_per_voxel;</i></p>
<dd>int <i>num_voxel_fields;</i></p>
<dd>int <i>num_shade_fields;</i></p>
<dd>int <i>num_classify_fields;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>bytes_per_voxel</i></p>
<dd>Size of one voxel in bytes.</p>
<dt><i>num_voxel_fields</i></p>
<dd>Number of fields in a voxel.</p>
<dt><i>num_shade_fields</i></p>
<dd>Number of voxel fields that are arguments to the shading function.</p>
<dt><i>num_classify_fields</i></p>
<dd>Number of voxel fields that are arguments to the opacity transfer function.</dl>
<h2>Description</h2>
<p><code>vpSetVoxelSize</code> is used to define the size in bytes and the number of fields in a voxel. Each voxel field is analogous to a field in a C structure and the contents of each field is user-defined. See the <code>vpSetVoxelField</code> function (<a href="/docs/linux/man/3-vpsetvoxelfield/">vpSetVoxelField</a>(3)) for setting the size and offset of each field. <code>vpSetVoxelSize</code> should be called before <code>vpSetVoxelField</code> and before any functions that access the contents of a voxel. </p>
<p> Typically, some of the voxel fields are used as arguments to a shading function and some (possibly the same) fields are used as arguments to an opacity transfer function (for classification). The fields that are used for shading should come first, i.e. they should have the smallest offsets, followed by any fields that are only used for classification. The classification fields can then be stripped off to save space during the precomputation stage for the fast rendering algorithm. The parameter <i>num_shade_fields</i> indicates the number of fields (starting from the first) that must not be stripped off. </p>
<p> The parameter <i>num_clsfy_fields</i> indicates the total number of fields that are used as parameters to the opacity transfer function. These fields do not necessarily have to be contiguous, although any fields that are not also used for shading should be the last fields in the voxel. </p>
<p> If the call to <code>vpSetVoxelSize</code> succeeds, any existing precomputed volume data structures in the context are destroyed.</p>
<h2>State Variables</h2>
<p>The current voxel size parameters can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_BYTES_PER_VOXEL, VP_VOXEL_FIELD_COUNT, VP_SHADE_FIELD_COUNT, VP_CLASSIFY_FIELD_COUNT.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_LIMIT_EXCEEDED</p>
<dd>The number of voxel fields exceeds the implementation limit. This limit can be increased by editing volpack.h and recompiling the library.</p>
<dt>VPERROR_BAD_VALUE</p>
<dd>Either <i>num_clsfy_fields</i> or <i>num_shade_fields</i> is out of range.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpsetvoxelfield/">vpSetVoxelField</a>(3) </p>
