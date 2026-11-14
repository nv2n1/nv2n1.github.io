---
title: "vpextract(3)"
name: "vpextract"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpextract/"
description: "vpExtract – extract one field from a rectangular region of a volume"
---

<p>vpExtract &#8211; extract one field from a rectangular region of a volume</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpExtract(</code><i>vpc, volume_type, x0, y0, z0, x1, y1, z1, field, dst,</p>
<dd>dst_size, dst_xstride, dst_ystride, dst_zstride</i><code>)</code></p>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>volume_type;</i></p>
<dd>int <i>x0, y0, z0;</i></p>
<dd>int <i>x1, y1, z1;</i></p>
<dd>int <i>field;</i></p>
<dd>void *<i>dst;</i></p>
<dd>int <i>dst_size;</i></p>
<dd>int <i>dst_xstride, dst_ystride, dst_zstride;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>volume_type</i></p>
<dd>A code indicating which volume data structure to extract the region from (VP_RAW_VOLUME, VP_CLASSIFIED_VOLUME, VP_CLX_VOLUME, VP_CLY_VOLUME or VP_CLZ_VOLUME)</p>
<dt><i>x0, y0, z0</i></p>
<dd>Origin of the extracted region in the voxel array.</p>
<dt><i>x1, y1, z1</i></p>
<dd>Opposite corner of the extracted region in the voxel array.</p>
<dt><i>field</i></p>
<dd>A voxel field number identifying the field to extract, or one of these special codes: VP_OPACITY_FIELD, VP_CORRECTED_OPAC_FIELD, VP_COLOR_FIELD.</p>
<dt><i>dst</i></p>
<dd>Destination array.</p>
<dt><i>dst_size</i></p>
<dd>Size of destination array in bytes.</p>
<dt><i>dst_xstride, dst_ystride, dst_zstride</i></p>
<dd>Strides (in bytes) for the X, Y and Z dimensions of the destination array.</dl>
<h2>Description</h2>
<p><code>vpExtract</code> is used to extract one field from a rectangular region of the 3D voxel array or the preclassified volume and store the result in a separate array. It is also possible to retrieve computed voxel opacities or colors. </p>
<p> The <i>volume_type</i> argument is used to choose which data structure the region should be extracted from. The choices are:</p>
<dl>
<dt>VP_RAW_VOLUME</p>
<dd>Extract from the 3D voxel array (see <a href="/docs/linux/man/3-vpsetrawvoxels/">vpSetRawVoxels</a>(3)).</p>
<dt>VP_CLASSIFIED_VOLUME</p>
<dd>Extract from the preclassified volume (see <a href="/docs/linux/man/3-vpclassifyvolume/">vpClassifyVolume</a>(3)). The are three copies of the voxel data in the preclassified volume, one for each principal viewing axis. The copy which will result in the fastest access (best memory stride) is selected.</p>
<dt>VP_CLX_VOLUME</p>
<dd>Extract from the preclassified volume used for X-axis viewing.</p>
<dt>VP_CLY_VOLUME</p>
<dd>Extract from the preclassified volume used for Y-axis viewing.</p>
<dt>VP_CLZ_VOLUME</p>
<dd>Extract from the preclassified volume used for Z-axis viewing.</dl>
<p> The last three choices for the <i>volume_type</i> argument are usually used only for debugging. </p>
<p> The next six arguments give the coordinates of the corners of the extracted region in the volume. The coordinates are indexes into the array. </p>
<p> The <i>field</i> argument is used to select which voxel field to extract. Any of the voxel field numbers previously specified with <code>vpVoxelField</code> may be specified. The output array must be sized appropriately for the dimensions of the region and the size of the extracted field. The following special constants may also be used instead of a voxel field number:</p>
<dl>
<dt>VP_OPACITY_FIELD</p>
<dd>Return voxel opacities for voxels in the indicated region. If the 3D voxel array is selected then the opacities are computed on-the-fly using the current opacity transfer function. The minimum opacity threshold is ignored. If the preclassified volume is selected then the precomputed opacities are extracted. Opacities below the minimum opacity threshold at the time the volume was classified are set to 0. The output array should have type unsigned char, and the opacities are stored as number between 0 (transparent) and 255 (opaque).</p>
<dt>VP_CORRECTED_OPAC_FIELD</p>
<dd>This option is the same as the VP_OPACITY_FIELD option, except that voxel opacities are corrected for the current view transformation. The opacity transfer function is assumed to produce the opacity of a voxel viewed perpendicular to one face of the volume with no scale factor. If the voxel has been scaled or rotated with respect to the viewer then the apparent opacity must be corrected.</p>
<dt>VP_COLOR_FIELD</p>
<dd>Return voxel colors for voxels in the indicated region. The colors are computed on-the-fly using the current shading, lighting and material parameters. The output array should have type unsigned char, and each color channel is stored as number between 0 (off) and 255 (full intensity). The number of color channels per pixels is determined by the current shading parameters. (Not currently supported for preclassified volumes.)</dl>
<p> The remaining arguments specify the output array, its size (for error checking), and the stride for each dimension (to allow padding the end of scanlines or storing the result in a higher-dimension array).</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_VALUE</p>
<dd>The volume coordinates are out of bounds or invalid (x0 &gt; x1, etc.), or the field number is invalid.</p>
<dt>VPERROR_BAD_SIZE</p>
<dd>The destination array size is incorrect.</p>
<dt>VPERROR_BAD_VOLUME</p>
<dd>The volume data does not exist.</p>
<dt>VPERROR_BAD_OPTION</p>
<dd>The <i>volume_type</i> argument is invalid.</p>
<dt>VPERROR_BAD_VOLUME</p>
<dd>The volume size or data is missing or invalid.</p>
<dt>VPERROR_BAD_VOXEL</p>
<dd>The voxel fields are incorrectly defined.</p>
<dt>VPERROR_BAD_CLASSIFIER</p>
<dd>The opacity transfer function is incorrectly specified.</p>
<dt>VPERROR_BAD_SHADER</p>
<dd>The shading parameters have been incorrectly specified.</p>
<dt>VPERROR_SINGULAR</p>
<dd>One or more of the view transformation matrices is singular.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3) </p>
