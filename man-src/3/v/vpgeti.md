---
title: "vpgeti(3)"
name: "vpgeti"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpgeti/"
description: "vpGeti, vpGetd, vpGetp – get the value of an option"
---

<p>vpGeti, vpGetd, vpGetp &#8211; get the value of an option</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpGeti(</code><i>vpc, option, iptr</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>option;</i></p>
<dd>int *<i>iptr;</i>  vpResult</p>
<dl>
<dt> <code>vpGetd(</code><i>vpc, option, dptr</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>option;</i></p>
<dd>double *<i>dptr;</i>  vpResult</p>
<dl>
<dt> <code>vpGetp(</code><i>vpc, option, pptr</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>option;</i></p>
<dd>void *<i>pptr;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>option</i></p>
<dd>Constant that specifies the option to be retrieved.</p>
<dt><i>iptr</i></p>
<dd>Location to store an integer result.</p>
<dt><i>dptr</i></p>
<dd>Location to store a double result.</p>
<dt><i>pptr</i></p>
<dd>Location to store a pointer result.</dl>
<h2>Description</h2>
<p>These functions are used the get the values of integer-, double- or pointer-valued state variables in a rendering context. The following list summarizes the integer-valued options that can be retrieved with <code>vpGeti</code>. The value of the option is stored in the location given by <i>iptr;</i> the return value of <code>vpGeti</code> is not the value of the option. Unless otherwise noted, the result is a single integer and <i>iptr</i> should point to a single integer location.</p>
<dl>
<dt>VP_XLEN</p>
<dd>Get the length of the X dimension of the volume in voxels.</p>
<dt>VP_YLEN</p>
<dd>Get the length of the Y dimension of the volume in voxels.</p>
<dt>VP_ZLEN</p>
<dd>Get the length of the Y dimension of the volume in voxels.</p>
<dt>VP_BYTES_PER_VOXEL</p>
<dd>Get the size of a voxel in bytes.</p>
<dt>VP_VOXEL_FIELD_COUNT</p>
<dd>Get the number of fields in a voxel.</p>
<dt>VP_SHADE_FIELD_COUNT</p>
<dd>Get the number of fields in a voxel used as parameters for shading the voxel.</p>
<dt>VP_FIELD_SIZES</p>
<dd>Get the size of each voxel field in bytes. <i>iptr</i> must point to an array of integers containing one entry for each voxel field (use VP_VOXEL_FIELD_COUNT to determine the number of fields).</p>
<dt>VP_FIELD_OFFSETS</p>
<dd>Get the byte offset from the beginning of a voxel for each voxel field. <i>iptr</i> must point to an array of integers containing one entry for each voxel field (use VP_VOXEL_FIELD_COUNT to determine the number of fields).</p>
<dt>VP_FIELD_MAXES</p>
<dd>Get the maximum value of the quantity stored in each voxel field. <i>iptr</i> must point to an array of integers containing one entry for each voxel field (use VP_VOXEL_FIELD_COUNT to determine the number of fields).</p>
<dt>VP_VOXEL_DATA_SIZE</p>
<dd>Get the size (in bytes) of the 3D voxel array.</p>
<dt>VP_VOXEL_XSTRIDE</p>
<dd>Get the stride (in bytes) for the X dimension of the 3D voxel array.</p>
<dt>VP_VOXEL_YSTRIDE</p>
<dd>Get the stride (in bytes) for the Y dimension of the 3D voxel array.</p>
<dt>VP_VOXEL_ZSTRIDE</p>
<dd>Get the stride (in bytes) for the Z dimension of the 3D voxel array.</p>
<dt>VP_CLASSIFY_FIELD_COUNT</p>
<dd>Get the number of fields in a voxel used as parameters for classifying the voxel (the number of arguments to the opacity transfer function).</p>
<dt>VP_CLASSIFY_FIELDS</p>
<dd>Get the field numbers for the arguments to the opacity transfer function. <i>iptr</i> must point to an array of integers containing one entry for each argument (use VP_CLASSIFY_FIELD_COUNT to determine the number of arguments).</p>
<dt>VP_CLASSIFY_TABLE_SIZES</p>
<dd>Get the size (in bytes) of each lookup table used for the opacity transfer function. <i>iptr</i> must point to an array of integers containing one entry for each lookup table (use VP_CLASSIFY_FIELD_COUNT to determine the number of lookup tables, which equals the number of arguments to the opacity transfer function).</p>
<dt>VP_COLOR_CHANNELS</p>
<dd>Get the number of color channels that the current shading lookup tables or shading callback function will produce.</p>
<dt>VP_SHADE_COLOR_SIZE</p>
<dd>Get the size of the shading lookup table for color values (see <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3)).</p>
<dt>VP_SHADE_WEIGHT_SIZE</p>
<dd>Get the size of the shading lookup table for weight values (see <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3)).</p>
<dt>VP_MATERIAL_COUNT</p>
<dd>Get the number of material types used by the current lookup shader (see <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3)).</p>
<dt>VP_SHADE_COLOR_FIELD</p>
<dd>Get the field number used for indexing the shading lookup table for color values (see <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3)).</p>
<dt>VP_SHADE_WEIGHT_FIELD</p>
<dd>Get the field number used for indexing the shading lookup table for weight values (see <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3)).</p>
<dt>VP_LIGHT0</p>
<dd>
<dt>VP_LIGHT1</p>
<dd>
<dt>VP_LIGHT2</p>
<dd>
<dt>VP_LIGHT3</p>
<dd>
<dt>VP_LIGHT4</p>
<dd>
<dt>VP_LIGHT5</p>
<dd>The retrieved value is nonzero if the corresponding light is enabled, or 0 if it is disabled.</p>
<dt>VP_LIGHT_BOTH_SIDES</p>
<dd>The retrieved value is nonzero if two-sided lighting is enabled (see <a href="/docs/linux/man/3-vpsetlight/">vpSetLight</a>(3)), or 0 if it is disabled.</p>
<dt>VP_REVERSE_SURFACE_SIDES</p>
<dd>The retrieved value is nonzero if the definitions of interior and exterior surfaces have been reversed (see <a href="/docs/linux/man/3-vpsetmaterial/">vpSetMaterial</a>(3)), or 0 if they have not.</p>
<dt>VP_DEPTH_CUE</p>
<dd>The retrieved value is nonzero if depth cueing is enabled, or 0 if it is disabled.</p>
<dt>VP_DEPTH_CUE_TABLE_SIZE</p>
<dd>Get the current number of entries in the depth cueing table (see <a href="/docs/linux/man/3-vpsetdepthcueing/">vpSetDepthCueing</a>(3)).</p>
<dt>VP_DEPTH_CUE_SIZE_HINT</p>
<dd>Get the current hint for the number of entries in the depth cueing table (see <a href="/docs/linux/man/3-vpsetdepthcueing/">vpSetDepthCueing</a>(3)).</p>
<dt>VP_CURRENT_MATRIX</p>
<dd>Get the identifier for the current transformation matrix (VP_MODEL, VP_VIEW or VP_PROJECT).</p>
<dt>VP_CONCAT_MODE</p>
<dd>Get the identifier for the current matrix concatenation mode (VP_CONCAT_LEFT or VP_CONCAT_RIGHT).</p>
<dt>VP_IMAGE_WIDTH</p>
<dd>Get the width (in pixels) of the output image array.</p>
<dt>VP_IMAGE_HEIGHT</p>
<dd>Get the height (in pixels) of the output image array.</p>
<dt>VP_IMAGE_SCAN_SIZE</p>
<dd>Get the number bytes per scanline in the output image array.</p>
<dt>VP_VIEW_AXIS</p>
<dd>Get the identifier for the current major viewing axis in the object coordinate system (VP_X_AXIS, VP_Y_AXIS or VP_Z_AXIS). The axis depends on the viewing transformation.</p>
<dt>VP_INTERMEDIATE_WIDTH</p>
<dd>Get the width (in pixels) of the intermediate image required to render the current volume with the current viewing transformation (see <a href="/docs/linux/man/3-vprenderrawvolume/">vpRenderRawVolume</a>(3)).</p>
<dt>VP_INTERMEDIATE_HEIGHT</p>
<dd>Get the height (in pixels) of the intermediate image required to render the current volume with the current viewing transformation (see <a href="/docs/linux/man/3-vprenderrawvolume/">vpRenderRawVolume</a>(3)).</p>
<dt>VP_INTERMEDIATE_COLOR</p>
<dd>Get the number of color channels in the intermediate image (see <a href="/docs/linux/man/3-vprenderrawvolume/">vpRenderRawVolume</a>(3)).</p>
<dt>VP_INT_WIDTH_HINT</p>
<dd>Get the current hint for the width (in pixels) of the intermediate image (see <a href="/docs/linux/man/3-vprenderrawvolume/">vpRenderRawVolume</a>(3)).</p>
<dt>VP_INT_HEIGHT_HINT</p>
<dd>Get the current hint for the height (in pixels) of the intermediate image (see <a href="/docs/linux/man/3-vprenderrawvolume/">vpRenderRawVolume</a>(3)).</p>
<dt>VP_VIEW_X_AXIS</p>
<dd>
<dt>VP_VIEW_Y_AXIS</p>
<dd>
<dt>VP_VIEW_Z_AXIS</p>
<dd>The retrieved value is non-zero if computing a preclassified volume for the corresponding major viewing axis is enabled (see <a href="/docs/linux/man/3-vpclassifyvolume/">vpClassifyVolume</a>(3)).</p>
<dt>VP_VIEW_X_SIZE</p>
<dd>
<dt>VP_VIEW_Y_SIZE</p>
<dd>
<dt>VP_VIEW_Z_SIZE</p>
<dd>Get the size (in bytes) of the preclassified volume for the corresponding major viewing axis.</p>
<dt>VP_MMOCTREE_THRESHOLDS</p>
<dd>Get the current min-max octree range thresholds. <i>iptr</i> must point to an array of integers containing one entry for each threshold (use VP_CLASSIFY_FIELD_COUNT to determine the number of thresholds, which equals the number of arguments to the opacity transfer function).</p>
<dt>VP_MMOCTREE_SIZE</p>
<dd>Get the size (in bytes) of the min-max octree.</p>
<dt>VP_SHADOW</p>
<dd>The retrieved value is nonzero if shadows are enabled (see <a href="/docs/linux/man/3-vpsetshadowlookupshader/">vpSetShadowLookupShader</a>(3)).</p>
<dt>VP_SHADOW_LIGHT</p>
<dd>Get the constant (e.g. VP_LIGHT0) associated with the current shadow light (see <a href="/docs/linux/man/3-vpsetshadowlookupshader/">vpSetShadowLookupShader</a>(3)).</p>
<dt>VP_SHADOW_WIDTH_HINT</p>
<dd>Get the current hint for the width (in pixels) of the shadow buffer (see <a href="/docs/linux/man/3-vpsetshadowlookupshader/">vpSetShadowLookupShader</a>(3)).</p>
<dt>VP_SHADOW_HEIGHT_HINT</p>
<dd>Get the current hint for the height (in pixels) of the shadow buffer (see <a href="/docs/linux/man/3-vpsetshadowlookupshader/">vpSetShadowLookupShader</a>(3)).</p>
<dt>VP_SHADOW_COLOR_SIZE</p>
<dd>Get the size of the shading lookup table for shadowed color values (see <a href="/docs/linux/man/3-vpsetshadowlookupshader/">vpSetShadowLookupShader</a>(3)).</p>
<dt>VP_SHADOW_BIAS</p>
<dd>Get the current shadow bias value (see <a href="/docs/linux/man/3-vpsetshadowlookupshader/">vpSetShadowLookupShader</a>(3)).</p>
<dt>VP_PIXEL_TYPE</p>
<dd>Get the current image pixel type (see <a href="/docs/linux/man/3-vpsetimage/">vpSetImage</a>(3)).</p>
<dt>VP_CLAMP_SHADE_TABLE</p>
<dd>The retrieved value is nonzero if clamping is enabled for shade table entries, or 0 if it is disabled (see <a href="/docs/linux/man/3-vpshadetable/">vpShadeTable</a>(3)).</p>
<dt>VP_COMPOSITE_ORDER</p>
<dd>This value is used for debugging only. It returns 1 if the current major viewing axis (VP_VIEW_AXIS) points in the same direction as the viewing direction, or -1 if they point in opposite directions.</dl>
<p> The following list summarizes the double-valued options that can be retrieved with <code>vpGetd</code>. The result is always a single double and <i>dptr</i> should point to a single double location.</p>
<dl>
<dt>VP_MIN_VOXEL_OPACITY</p>
<dd>Get the minimum opacity threshold (see <a href="/docs/linux/man/3-vpseti/">vpSeti</a>(3)).</p>
<dt>VP_DEPTH_CUE_FRONT</p>
<dd>Get the front depth cueing factor (see <a href="/docs/linux/man/3-vpsetdepthcueing/">vpSetDepthCueing</a>(3)).</p>
<dt>VP_DEPTH_CUE_DENSITY</p>
<dd>Get the depth cueing density (see <a href="/docs/linux/man/3-vpsetdepthcueing/">vpSetDepthCueing</a>(3)).</p>
<dt>VP_DEPTH_CUE_QUANTIZATION</p>
<dd>Get the depth cueing quantization (see <a href="/docs/linux/man/3-vpsetdepthcueing/">vpSetDepthCueing</a>(3)).</p>
<dt>VP_MAX_RAY_OPACITY</p>
<dd>Get the maximum opacity threshold (see <a href="/docs/linux/man/3-vpseti/">vpSeti</a>(3)).</dl>
<p> The following list summarizes the pointer-valued options that can be retrieved with <code>vpGetp</code>. Unless otherwise noted, the result is a single pointer and <i>pptr</i> should point to a single pointer location.</p>
<dl>
<dt>VP_VOXEL_DATA</p>
<dd>Get a pointer to the 3D voxel array.</p>
<dt>VP_CLASSIFY_TABLES</p>
<dd>Get pointers to each of the lookup tables for the opacity transfer function. <i>pptr</i> must point to an array of pointers containing one entry for each table (use VP_CLASSIFY_FIELD_COUNT to determine the number of tables, which is equal to the number of arguments to the opacity transfer function).</p>
<dt>VP_SHADE_FUNC</p>
<dd>Get the shading callback function (see <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3)).</p>
<dt>VP_SHADE_COLOR_TABLE</p>
<dd>Get a pointer to the shading lookup table for colors (see <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3)).</p>
<dt>VP_SHADE_WEIGHT_TABLE</p>
<dd>Get a pointer to the shading lookup table for weights (see <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3)).</p>
<dt>VP_IMAGE</p>
<dd>Get a pointer to the output image array (see <a href="/docs/linux/man/3-vpsetimage/">vpSetImage</a>(3)).</p>
<dt>VP_LOG_ALLOC_FUNC</p>
<dd>Get a pointer to the memory allocator logging function (see <a href="/docs/linux/man/3-vpsetcallback/">vpSetCallback</a>(3)).</p>
<dt>VP_LOG_FREE_FUNC</p>
<dd>Get a pointer to the memory deallocator logging function (see <a href="/docs/linux/man/3-vpsetcallback/">vpSetCallback</a>(3)).</p>
<dt>VP_STATUS_FUNC</p>
<dd>Get a pointer to the status reporting function (see <a href="/docs/linux/man/3-vpsetcallback/">vpSetCallback</a>(3)).</p>
<dt>VP_READ_FUNC</p>
<dd>Get a pointer to the file I/O read function (see <a href="/docs/linux/man/3-vpsetcallback/">vpSetCallback</a>(3)).</p>
<dt>VP_WRITE_FUNC</p>
<dd>Get a pointer to the file I/O write function (see <a href="/docs/linux/man/3-vpsetcallback/">vpSetCallback</a>(3)).</p>
<dt>VP_MMAP_FUNC</p>
<dd>Get a pointer to the file I/O memory mapping function (see <a href="/docs/linux/man/3-vpsetcallback/">vpSetCallback</a>(3)).</p>
<dt>VP_CLIENT_DATA</p>
<dd>Get a pointer to the client data (see <a href="/docs/linux/man/3-vpsetclientdata/">vpSetClientData</a>(3)).</p>
<dt>VP_SHADOW_COLOR_TABLE</p>
<dd>Get a pointer to the shading lookup table for shadowed color values (see <a href="/docs/linux/man/3-vpsetshadowlookupshader/">vpSetShadowLookupShader</a>(3)).</dl>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_OPTION</p>
<dd>The <i>option</i> argument is invalid.</p>
<dt>VPERROR_SINGULAR</p>
<dd>One of the current view transformation matrices is singular. (Only possible for options that depend on the current view transformation).</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpseti/">vpSeti</a>(3) </p>
