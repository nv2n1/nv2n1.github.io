---
title: "vpshadetable(3)"
name: "vpshadetable"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpshadetable/"
description: "vpShadeTable – compute the contents of the shading lookup table"
---

<p>vpShadeTable &#8211; compute the contents of the shading lookup table</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpShadeTable(</code><i>vpc</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></dl>
<h2>Description</h2>
<p><code>vpShadeTable</code> computes the contents of the shading lookup table previously specified with <code>vpLookupShader</code>. For each entry in the table, the Phong shading equation is evaluated using the current lighting properties (as specified with <code>vpSetLight</code>), material properties (as specified with <code>vpSetMaterial</code>), and viewing parameters (as specified with the view transformation commands). See <a href="/docs/linux/man/3-vpsetmaterial/">vpSetMaterial</a>(3) for a description of the shading calculation. </p>
<p> This function should be called before rendering a volume if any of the lighting or material properties have changed or if the viewpoint has changed since the last call to <code>vpShadeTable</code>. It should not be called if shading is performed using a callback function or if the shading lookup tables are initialized by a user-defined routine. </p>
<p> There is one state variable that affects the operation of <code>vpShadeTable</code>. If VP_CLAMP_SHADE_TABLE is enabled (see <a href="/docs/linux/man/3-vpenable/">vpEnable</a>(3)), then values are clamped to the range 0.0-255.0 before they are stored in the table. If this option is not enabled then no clamping is performed. Clamping is enabled by default, but can be turned off to achieve special effects. For example, if all of the voxels in a data set have very low opacity then the rendered image may be very dark. To brighten it, multiply all of the material parameter coefficients by a constant, possibly making the values exceed 1.0, and turn off clamping.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_SINGULAR</p>
<dd>One of the current view transformation matrices is singular.</p>
<dt>VPERROR_BAD_SHADER</p>
<dd>The shading lookup tables are sized incorrectly, or one of the voxel fields used to index the tables is invalid, or the number of material types is invalid.</p>
<dt>VPERROR_BAD_SHADOW</p>
<dd>The angle between the shadow light vector and the viewing direction is too large (must be less than 45 degrees). Either change the light direction or disable shadows (see vpSetShadowLookupShader).</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpcurrentmatrix/">vpCurrentMatrix</a>(3), <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3), <a href="/docs/linux/man/3-vpsetlight/">vpSetLight</a>(3), <a href="/docs/linux/man/3-vpsetmaterial/">vpSetMaterial</a>(3) </p>
