---
title: "vpsetlookupshader(3)"
name: "vpsetlookupshader"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpsetlookupshader/"
description: "vpSetLookupShader – specify shading lookup tables"
---

<p>vpSetLookupShader &#8211; specify shading lookup tables</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpSetLookupShader(</code><i>vpc, color_channels, num_materials,</p>
<dd>color_field, color_table, color_table_size, weight_field, weight_table, weight_table_size</i><code>)</code></p>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>color_channels, num_materials;</i></p>
<dd>int <i>color_field;</i></p>
<dd>float *<i>color_table;</i></p>
<dd>int <i>color_table_size;</i></p>
<dd>int <i>weight_field;</i></p>
<dd>float *<i>weight_table;</i></p>
<dd>int <i>weight_table_size;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>color_channels</i></p>
<dd>The number of color channels per pixel (1 or 3).</p>
<dt><i>num_materials</i></p>
<dd>The number of material types.</p>
<dt><i>color_field</i></p>
<dd>Field number for voxel field containing color lookup table index.</p>
<dt><i>color_table</i></p>
<dd>Color lookup table.</p>
<dt><i>color_table_size</i></p>
<dd>Size of color lookup table in bytes.</p>
<dt><i>weight_field</i></p>
<dd>Field number for voxel field containing material weight lookup table index.</p>
<dt><i>weight_table</i></p>
<dd>Material weight lookup table.</p>
<dt><i>weight_table_size</i></p>
<dd>Size of material weight lookup table in bytes.</dl>
<h2>Description</h2>
<p><code>vpSetLookupShader</code> is used to specify lookup tables that define a shading function. The lookup-table shading algorithm provided by VolPack is designed to support the following shading model. Each voxel is assumed to contain a mixture of some set of basic material types. Each material type has its own shading parameters for the Phong shading equation (for example, the diffuse color components and the shinyness). The color of a voxel is found by computing a color for each material type and then combining the colors in proportion to the fraction of each material in the voxel. The shading model also supports directional (infinite-distance) light sources. </p>
<p> This shading model is implemented using lookup tables. The tables can be precomputed so that the shading equation does not have to be evaluated for every voxel. VolPack provides routines to compute the lookup tables (see <a href="/docs/linux/man/3-vpshadetable/">vpShadeTable</a>(3)). The lookup tables can also be used to implement other shading models by using a user-supplied routine to compute the contents of the tables. See <a href="/docs/linux/man/3-vpsetdepthcueing/">vpSetDepthCueing</a>(3) for information about depth cueing. </p>
<p> It is also possible to define a callback function that will be called to shade each voxel during rendering, instead of using a lookup table. This method allows more general shading models but slows down rendering. To define a callback shader, call <code>vpSetCallback</code> with the VP_GRAY_SHADE_FUNC or VP_RGB_SHADE_FUNC option code (see <a href="/docs/linux/man/3-vpsetcallback/">vpSetCallback</a>(3)). The lookup tables are used if the last successful call to <code>vpSetLookupShader</code> occurred after the last successful call to <code>vpSetCallback</code> with one of the VP_*_SHADE_FUNC options. </p>
<p> The <i>color_channels</i> argument determines whether the shading table will contain grayscale (1 channel) or RGB (3 channel) pixels. The <i>num_materials</i> argument specifies the number of basic material types out of which each voxel can be composed (at least 1). The <i>color_table</i> and <i>weight_table</i> arguments specify two lookup tables, and the <i>color_field</i> and <i>weight_field</i> arguments specify two voxel fields that are used to index the tables. The size of the <i>color_table</i> array must be:</p>
<dl>
<dd>float <i>color_table[n][num_materials][color_channels];</i></dl>
<p> where <i>n</i> is the number of possible values in the <i>color_field</i> field of the voxel (the maximum value plus one). The size of the <i>weight_table</i> argument must be:</p>
<dl>
<dd>float <i>weight_table[m][num_materials];</i></dl>
<p> where <i>m</i> is the number of possible values in the <i>weight_field</i> field of the voxel (the maximum value plus one). If there is only one material then <i>weight_table</i> is not used and may be a NULL pointer. </p>
<p> During rendering the shading lookup tables are accessed as follows. Suppose a particular voxel to be shaded has the value <i>color_index</i> in the field specified by <i>color_field</i> and the value <i>weight_index</i> in the field specified by <i>weight_field</i>. For each material number <i>material_index,</i> a weighted color is computed from the formula:</p>
<dl>
<dd>color = color_table[color_index][material_index] *<br />
 weight_table[weight_index][material_index]</dl>
<p> Then the weighted colors for each material type are added up to give the voxel color. If <i>color_table</i> contains RGB values then each component is treated separately using the above formula. If there is only one material type then the constant 1.0 is substituted for the <i>weight_table</i> value. </p>
<p> The suggested way to use the tables is as follows. The voxel field specified by <i>color_field</i> should contain an encoded surface normal vector; this should be the same field as the <i>norm_field</i> argument to <code>vpVolumeNormals</code> or <code>vpClassifyScalars</code>. In the <i>color_table</i> array, for each possible encoded surface normal (the <i>color</i> index) and material type (the <i>material</i> index) the array should contain the color of the material given the current viewing direction and lighting arrangement. The color is independent of the voxel location because the light sources are assumed to be infinitely distant. The function <code>vpShadeTable</code> initializes the contents of <i>color_table</i> in this way. </p>
<p> The voxel field specified by <i>weight_field</i> should contain some quantity that determines the material composition of the voxel. For example, a field containing the scalar value could be used. In the <i>weight_table</i> array, for each possible value of <i>weight_field</i> there should be one row of material occupancy fractions. Each entry should be a number in the range 0.0-1.0 that specifies the fraction of the voxel occupied by the corresponding material. For example, if there are two material types and a voxel&#8217;s <i>weight_field</i> contains the value 62, then <i>weight_table</i>[62][0] gives the fraction of the voxel occupied by material 0, and <i>weight_table</i>[62][1] gives the fraction of the voxel occupied by material 1. Normally, the numbers in a given row of <i>weight_table</i> should add up to 1.0 (although special effects can be achieved by bending the rules). The function <code>vpRamp</code> is useful for initializing the weight table with piece-wise linear ramps. </p>
<p> The values in the shading lookup tables may be initialized before or after calling <code>vpSetLookupShader.</code> Typically <code>vpSetLookupShader</code> is called once at the beginning of a rendering session, and then the values in the shading tables are modified as the user changes the lighting and shading parameters or the viewing direction.</p>
<h2>State Variables</h2>
<p>Information about the current shading table parameters can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_COLOR_CHANNELS, VP_SHADE_COLOR_TABLE, VP_SHADE_COLOR_SIZE, VP_SHADE_WEIGHT_TABLE, VP_SHADE_WEIGHT_SIZE, VP_SHADE_COLOR_FIELD, VP_SHADE_WEIGHT_FIELD, VP_MATERIAL_COUNT</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_VALUE</p>
<dd>One or more of the arguments has an invalid value or is out of range.</p>
<dt>VPERROR_LIMIT_EXCEEDED</p>
<dd>The <i>num_materials</i> argument has exceeded an internal limit. Change the value of VP_MAX_MATERIAL in volpack.h and recompile the VolPack library.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpshadetable/">vpShadeTable</a>(3), <a href="/docs/linux/man/3-vpsetcallback/">vpSetCallback</a>(3), <a href="/docs/linux/man/3-vpramp/">vpRamp</a>(3), <a href="/docs/linux/man/3-vpvolumenormals/">vpVolumeNormals</a>(3), <a href="/docs/linux/man/3-vpclassifyscalars/">vpClassifyScalars</a>(3), <a href="/docs/linux/man/3-vpsetdepthcueing/">vpSetDepthCueing</a>(3) </p>
