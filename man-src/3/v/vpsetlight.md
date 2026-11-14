---
title: "vpsetlight(3)"
name: "vpsetlight"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpsetlight/"
description: "vpSetLight – set lighting properties"
---

<p>vpSetLight &#8211; set lighting properties</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpSetLight(</code><i>vpc, light_num, property, n0, n1, n2</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>light_num;</i></p>
<dd>int <i>property;</i></p>
<dd>double <i>n0, n1, n2;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>light_num</i></p>
<dd>A constant specifying a particular light source (VP_LIGHT0, VP_LIGHT1, &#8230;, VP_LIGHT5).</p>
<dt><i>property</i></p>
<dd>A constant specifying one lighting property (VP_COLOR or VP_DIRECTION).</p>
<dt><i>n0, n1, n2</i></p>
<dd>Components of an RGB color (for VP_COLOR) or a direction vector (for VP_DIRECTION).</dl>
<h2>Description</h2>
<p><code>vpSetLight</code> is used to set the properties of a light source. VolPack currently only supports directional light sources: each light is infinitely distant, so it can be fully characterized by a direction vector and a color. The lighting properties are used by <code>vpShadeTable</code> to compute the shading lookup table, which is then used to compute a color for each voxel. </p>
<p> To initialize the lighting environment, call <code>vpSetLight</code> twice for each light source which will be enabled. One call should set the RGB components of the light color (by using the VP_COLOR code for the <i>property</i> parameter), and one call should set the XYZ components of the light direction vector (by using the VP_DIRECTION code for the <i>property</i> parameter). The particular light source is specified with one of the light source codes defined in volpack.h: VP_LIGHT0, VP_LIGHT1, &#8230;, VP_LIGHT5. In the current implementation, at most six light sources may be specified. </p>
<p> The RGB components of a light color should be numbers in the range 0.0 (zero intensity) to 1.0 (full intensity). For grayscale renderings only the first (red) component is used and the other components may be set to any legal value. The default is white light (1.0, 1.0, 1.0). </p>
<p> The light direction vector points from the light source towards the lit object. It is transformed by the current contents of the modeling matrix (see <code>vpCurrentMatrix</code>). This allows the direction vector to be specified in an arbitrary coordinate system, provided the current modeling matrix properly transforms the vector into world coordinates. The default is the vector (1,1,1). </p>
<p> Each light source contributes to the shading computation only if it is enabled by calling <code>vpEnable.</code> By default, VP_LIGHT0 is enabled and all other lights are disabled. The more light sources that are enabled, the longer it takes to precompute the contents of the shading lookup table. </p>
<p> One additional property of the light sources can be set with <code>vpEnable</code>: VP_LIGHT_BOTH_SIDES. With this option enabled each light source shines in two opposing directions, as if there were two light sources facing each other with opposite direction vectors. No additional computation is required when this option is enabled.</p>
<h2>State Variables</h2>
<p>Information about the current lighting properties can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_LIGHT_BOTH_SIDES.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_LIMIT_EXCEEDED</p>
<dd>The light number is invalid or exceeds an implementation limit.</p>
<dt>VPERROR_SINGULAR</p>
<dd>The light direction vector is a zero vector.</p>
<dt>VPERROR_BAD_VALUE</p>
<dd>The RGB color components are out of range.</p>
<dt>VPERROR_BAD_OPTION</p>
<dd>The <i>property</i> argument is invalid.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3), <a href="/docs/linux/man/3-vpshadetable/">vpShadeTable</a>(3), <a href="/docs/linux/man/3-vpgetlight/">vpGetLight</a>(3) </p>
