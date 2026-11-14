---
title: "vpscanlinenormals(3)"
name: "vpscanlinenormals"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpscanlinenormals/"
description: "vpScanlineNormals – compute surface normal vectors and gradient magnitudes for a scanline"
---

<p>vpScanlineNormals &#8211; compute surface normal vectors and gradient magnitudes for a scanline</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpScanlineNormals(</code><i>vpc, length, scalar_data, scalar_minus_y,</p>
<dd>scalar_plus_y, scalar_minus_z, scalar_plus_z, voxel_data, scalar_field, grad_field, norm_field</i><code>)</code></p>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>length;</i></p>
<dd>unsigned char *<i>scalar_data;</i></p>
<dd>unsigned char *<i>scalar_minus_y,</i> *<i>scalar_plus_y;</i></p>
<dd>unsigned char *<i>scalar_minus_z,</i> *<i>scalar_plus_z;</i></p>
<dd>void *<i>voxel_data;</i></p>
<dd>int <i>scalar_field;</i></p>
<dd>int <i>grad_field;</i></p>
<dd>int <i>norm_field;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>length</i></p>
<dd>Size of <i>scalar_data</i> array in bytes.</p>
<dt><i>scalar_data</i></p>
<dd>1D array of scalar samples.</p>
<dt><i>scalar_minus_y</i></p>
<dd>1D array of scalar samples adjacent to <i>scalar_data</i> in the -Y direction.</p>
<dt><i>scalar_plus_y</i></p>
<dd>1D array of scalar samples adjacent to <i>scalar_data</i> in the +Y direction.</p>
<dt><i>scalar_minus_z</i></p>
<dd>1D array of scalar samples adjacent to <i>scalar_data</i> in the -Z direction.</p>
<dt><i>scalar_plus_z</i></p>
<dd>1D array of scalar samples adjacent to <i>scalar_data</i> in the +Z direction.</p>
<dt><i>voxel_data</i></p>
<dd>1D array of voxels for storing results.</p>
<dt><i>scalar_field</i></p>
<dd>Voxel field number indicating the field in which to store the scalar samples.</p>
<dt><i>grad_field</i></p>
<dd>Voxel field number indicating the field in which to store the gradient magnitudes of the scalar samples.</p>
<dt><i>norm_field</i></p>
<dd>Voxel field number indicating the field in which to store encoded surface normal vectors.</dl>
<h2>Description</h2>
<p><code>vpScanlineNormals</code> is used to precompute values for voxel fields used in classification and shading algorithms. The input is a collection of 5 adjacent 1D arrays of scalar values; a separate routine is provided for processing a full 3D array of voxel data (see <a href="/docs/linux/man/3-vpvolumenormals/">vpVolumeNormals</a>(3)). <code>vpScanlineNormals</code> is useful for loading large volumes into memory scanline-by-scanline and precomputing voxel fields incrementally, instead of loading a complete copy of the 3D scalar array in addition to the voxel array. In all other respects this routine is identical in function to <code>vpVolumeNormals</code>. </p>
<p> The 1D scalar arrays must be arrays of 8-bit values (other sizes are not currently supported). The <i>length</i> parameter indicates both the size and the number of elements in each of the scalar arrays. <code>vpScanlineNormals</code> performs the computation described in <a href="/docs/linux/man/3-vpvolumenormals/">vpVolumeNormals</a>(3), but only for the single scanline specified by <i>scalar_data</i>. The other four scanline arguments must be the immediately adjacent scanlines and are used to compute the gradient. </p>
<p> The results are stored in the <i>voxel_data</i> array which must have space for the same number of voxels as the length of one scalar scanline. The size of a voxel must be specified with <code>vpSetVoxelSize</code> before calling <code>vpScanlineNormals,</code> but it is not necessary to call <code>vpSetRawVoxels.</code> The arguments <i>scalar_field, grad_field</i> and <i>norm_field</i> specify which voxel fields the computed quantities should be stored into. The field numbers must correspond to appropriately-sized voxel fields previously specified with <code>vpSetVoxelField</code>. Any of these arguments can be the constant VP_SKIP_FIELD, in which case the corresponding quantity is not computed or copied. The voxel fields for the scalar value and the gradient magnitude must be one-byte fields, and the field for the surface normal vector must be a two-byte field. The constants VP_SCALAR_MAX, VP_GRAD_MAX and VP_NORM_MAX give the maximum value that might be stored in each field, respectively. The value stored in the surface normal vector field is actually an encoded surface normal; see <a href="/docs/linux/man/3-vpnormalindex/">vpNormalIndex</a>(3).</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_VALUE</p>
<dd>One or more of the voxel fields specified is invalid, or the corresponding voxel field has the wrong size.</p>
<dt>VPERROR_BAD_VOXEL</p>
<dd>The voxel size or the voxel fields have not been specified or have been incorrectly specified.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpnormalindex/">vpNormalIndex</a>(3), <a href="/docs/linux/man/3-vpvolumenormals/">vpVolumeNormals</a>(3), <a href="/docs/linux/man/3-vpsetclassifiertable/">vpSetClassifierTable</a>(3), <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3) </p>
