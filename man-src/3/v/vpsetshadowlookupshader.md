---
title: "vpsetshadowlookupshader(3)"
name: "vpsetshadowlookupshader"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpsetshadowlookupshader/"
description: "vpSetShadowLookupShader – specify shading lookup tables for rendering shadows"
---

<p>vpSetShadowLookupShader &#8211; specify shading lookup tables for rendering shadows</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpSetShadowLookupShader(</code><i>vpc, color_channels, num_materials,</p>
<dd>color_field, color_table, color_table_size, weight_field, weight_table, weight_table_size, shadow_table, shadow_table_size</i><code>)</code></p>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>color_channels, num_materials;</i></p>
<dd>int <i>color_field;</i></p>
<dd>float *<i>color_table;</i></p>
<dd>int <i>color_table_size;</i></p>
<dd>int <i>weight_field;</i></p>
<dd>float *<i>weight_table;</i></p>
<dd>int <i>weight_table_size;</i></p>
<dd>float *<i>shadow_table;</i></p>
<dd>int <i>shadow_table_size;</i></dl>
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
<dd>Size of material weight lookup table in bytes.</p>
<dt><i>shadow_table</i></p>
<dd>Shadow color lookup table.</p>
<dt><i>shadow_table_size</i></p>
<dd>Size of shadow color lookup table in bytes.</dl>
<h2>Description</h2>
<p><code>vpSetShadowLookupShader</code> is used to specify lookup tables that define a shading function for rendering a volume with shadows. It should be used instead of <code>vpSetLookupShader</code> when shadows are enabled. </p>
<p> VolPack supports a fast, one-pass shadow algorithm. The algorithm computes the fraction of light from a given light source that reaches each voxel. The fraction is then used to attenuate the diffuse and specular shading terms associated with that light source, producing a dark shadow in areas that are hidden from the light source. The implementation uses lookup tables so that most of the shading calculation can be precomputed. </p>
<p> In order to compute the shadows in a single pass the algorithm places a restriction on the direction of the light source: the light casting the shadows must not be more than 45 degrees from the viewing direction. The quality of the shadows may degrade if the angle approaches 45 degrees. The current implementation allows shadows to be cast only from one light source. Additional lights may be enabled, but they will not cast shadows. </p>
<p> To make a rendering with shadows, the following steps must be performed:</p>
<dl>
<dd>Call <code>vpSetShadowLookupShader</code> to define the lookup tables (see discussion below).</p>
<dd>Call <code>vpSeti</code> with the VP_SHADOW_LIGHT option to specify which light will cast shadows. The current implementation only allows one light to be specified.</p>
<dd>Call <code>vpSeti</code> with the VP_SHADOW_BIAS option to set the shadow bias value (see discussion below).</p>
<dd>Call <code>vpEnable</code> with the VP_SHADOW option to enable shadows.</p>
<dd>Call <code>vpShadeTable</code> as usual to initialize the lookup tables.</p>
<dd>Call one of the rendering routines.</dl>
<p> <code>vpSetShadowLookupShader</code> defines the lookup tables required for the shading and shadowing algorithm. The first nine arguments are identical to the arguments for <code>vpSetLookupShader</code> (see the corresponding man page). The remaining two arguments specify an additional color lookup table, <i>shadow_table,</i> with the same dimensions as <i>color_table</i>. The contents of the table will be initialized by <code>vpShadeTable</code>. </p>
<p> The call to <code>vpSeti</code> with the VP_SHADOW_BIAS option specifies an offset to eliminate self-shadowing. Self-shadowing is an intrinsic problem when implementing shadow algorithms for volume rendering. Consider a single voxelized object consisting of an opaque core surrounded by a &quot;halo&quot; of lower-opacity voxels (necessary for the scene to be band-limited). As a light ray pierces the halo its strength is attenuated. By the time the light reaches the high-opacity region a significant fraction of the light may be obscured, resulting in a general darkening of the image even if no shadows should be present. The problem can be corrected by moving the shadow a small distance along the direction of the light rays. VP_SHADOW_BIAS specifies the distance of the bias in units of voxels. The optimal value depends on the data set. Increase the bias until it has no more effect on overall image brightness, but do not increase it too far or small features in the data will no longer produce correct shadows. </p>
<p> <code>vpShadeTable</code> initializes the shading lookup tables. It operates differently when shadows are enabled. Instead of computing one color for each surface normal vector and storing the results in <i>color_table,</i> the routine computes two colors terms. The first term is the portion of the voxel color due to the diffuse and specular components of the shadow light. This value is stored in <i>shadow_table</i>. The second term contains the contribution of all other light source and the ambient light term, and is stored in <i>color_table.</i> During rendering the color of a voxel is computed by extracting a surface normal from the voxel, using the surface normal to index both <i>color_table</i> and <i>shadow_table,</i> attenuating the value from <i>shadow_table</i> by the local strength of the shadow light, and then adding the two terms together. The local strength of the shadow light is found by extracting a value from the shadow buffer, an internal data structure that is updated during rendering. </p>
<p> The values in the shading lookup tables may be initialized before or after calling <code>vpSetShadowLookupShader.</code> Typically <code>vpSetShadowLookupShader</code> is called once at the beginning of a rendering session, and then <code>vpShadeTable</code> is called whenever the user changes the lighting and shading parameters or the viewing direction. </p>
<p> The shadow buffer is an internal 2D array used to maintain state during rendering. There are several state variables that can be used to query its current size in pixels (VP_SHADOW_WIDTH and VP_SHADOW_HEIGHT) and to suggest a size (VP_SHADOW_WIDTH_HINT and VP_SHADOW_HEIGHT_HINT). The required size depends on the volume size and the shadow light&#8217;s direction. Normally the buffer is automatically resized when necessary.</p>
<h2>State Variables</h2>
<p>Information about the current shading table parameters can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_COLOR_CHANNELS, VP_SHADE_COLOR_TABLE, VP_SHADE_COLOR_SIZE, VP_SHADE_WEIGHT_TABLE, VP_SHADE_WEIGHT_SIZE, VP_SHADE_COLOR_FIELD, VP_SHADE_WEIGHT_FIELD, VP_MATERIAL_COUNT, VP_SHADOW, VP_SHADOW_LIGHT, VP_SHADOW_WIDTH_HINT, VP_SHADOW_HEIGHT_HINT, VP_SHADOW_WIDTH, VP_SHADOW_HEIGHT, VP_SHADOW_COLOR_TABLE, VP_SHADOW_COLOR_SIZE, VP_SHADOW_BIAS</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_VALUE</p>
<dd>One or more of the arguments has an invalid value or is out of range.</p>
<dt>VPERROR_LIMIT_EXCEEDED</p>
<dd>The <i>num_materials</i> argument has exceeded an internal limit. Change the value of VP_MAX_MATERIAL in volpack.h and recompile the VolPack library.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpshadetable/">vpShadeTable</a>(3), <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3) </p>
