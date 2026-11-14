---
title: "vpvolumenormals(3)"
name: "vpvolumenormals"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpvolumenormals/"
description: "vpVolumeNormals – compute surface normal vectors and gradient magnitudes for a volume"
---

<p>vpVolumeNormals &#8211; compute surface normal vectors and gradient magnitudes for a volume</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpVolumeNormals(</code><i>vpc, scalar_data, length, scalar_field,</p>
<dd>grad_field, norm_field</i><code>)</code></p>
<dd>vpContext *<i>vpc;</i></p>
<dd>unsigned char *<i>scalar_data;</i></p>
<dd>int <i>length;</i></p>
<dd>int <i>scalar_field;</i></p>
<dd>int <i>grad_field;</i></p>
<dd>int <i>norm_field;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>scalar_data</i></p>
<dd>3D array of scalar samples.</p>
<dt><i>length</i></p>
<dd>Size of <i>scalar_data</i> array in bytes.</p>
<dt><i>scalar_field</i></p>
<dd>Voxel field number indicating the field in which to store the scalar samples.</p>
<dt><i>grad_field</i></p>
<dd>Voxel field number indicating the field in which to store the gradient magnitudes of the scalar samples.</p>
<dt><i>norm_field</i></p>
<dd>Voxel field number indicating the field in which to store encoded surface normal vectors.</dl>
<h2>Description</h2>
<p><code>vpVolumeNormals</code> is used to precompute values for voxel fields used in classification and shading algorithms. The input is a 3D array of scalar values; a separate routine is provided for processing scanlines of voxel data (see <a href="/docs/linux/man/3-vpscanlinenormals/">vpScanlineNormals</a>(3)). For each voxel, the routine computes an approximation for the gradient of the scalar field (using a central-difference operator). From this vector the routine can compute the magnitude of the gradient, which is useful for some classification schemes (see <a href="/docs/linux/man/3-vpsetclassifiertable/">vpSetClassifierTable</a>(3)), and a surface normal vector in the direction of the gradient vector, which is used to implement lighting models (see <a href="/docs/linux/man/3-vpshadetable/">vpShadeTable</a>(3)). The scalar value, gradient magnitude and surface normal vector are then stored into the fields of the voxel array, which is separate from the array of scalar values. </p>
<p> The scalar array must be an array of 8-bit values (other sizes are not currently supported). The dimensions of the array must match the volume dimensions previously specified with <code>vpSetVolumeSize</code>. The <i>size</i> argument is used to make sure the array has the correct size. The voxel array must also be initialized by calling <code>vpSetRawVoxels</code> prior to calling <code>vpVolumeNormals</code>. </p>
<p> The three voxel field number arguments indicate which voxel fields the computed information should be stored into, and which field the scalar samples should be copied to. The field numbers must correspond to appropriately-sized voxel fields previously specified with <code>vpSetVoxelField</code>. Any of these arguments can be the constant VP_SKIP_FIELD, in which case the corresponding quantity is not computed or copied. The voxel fields for the scalar value and the gradient magnitude must be one-byte fields, and the field for the surface normal vector must be a two-byte field. The constants VP_SCALAR_MAX, VP_GRAD_MAX and VP_NORM_MAX give the maximum value that might be stored in each field, respectively. The value stored in the surface normal vector field is actually an encoded surface normal; see <a href="/docs/linux/man/3-vpnormalindex/">vpNormalIndex</a>(3).</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_SIZE</p>
<dd>The size of the scalar array does not match the volume dimensions.</p>
<dt>VPERROR_BAD_VALUE</p>
<dd>One or more of the voxel fields specified is invalid, or the corresponding voxel field has the wrong size.</p>
<dt>VPERROR_BAD_VOXEL</p>
<dd>The voxel size or the voxel fields have not been specified or have been incorrectly specified.</p>
<dt>VPERROR_BAD_VOLUME</p>
<dd>The volume array or volume dimensions have not been specified, or the size of the volume array does not match the volume dimensions.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpnormalindex/">vpNormalIndex</a>(3), <a href="/docs/linux/man/3-vpscanlinenormals/">vpScanlineNormals</a>(3), <a href="/docs/linux/man/3-vpsetclassifiertable/">vpSetClassifierTable</a>(3), <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3) </p>
