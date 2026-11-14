---
title: "vpsetmaterial(3)"
name: "vpsetmaterial"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpsetmaterial/"
description: "vpSetMaterial – set material properties"
---

<p>vpSetMaterial &#8211; set material properties</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpSetMaterial(</code><i>vpc, material, property, surface_side, r, g, b</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>material;</i></p>
<dd>int <i>property;</i></p>
<dd>int <i>surface_side;</i></p>
<dd>double <i>r, g, b;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>material</i></p>
<dd>A constant specifying a particular material number (VP_MATERIAL0, VP_MATERIAL1, &#8230;, VP_MATERIAL5).</p>
<dt><i>property</i></p>
<dd>A constant specifying one material property (VP_AMBIENT, VP_DIFFUSE, VP_SPECULAR or VP_SHINYNESS).</p>
<dt><i>surface_side</i></p>
<dd>A constant specifying which side of the material surface the properties apply to (VP_EXTERIOR, VP_INTERIOR or VP_BOTH_SIDES).</p>
<dt><i>r, g, b</i></p>
<dd>RGB components of the color associated with the property. For VP_SHINYNESS, <i>g</i> and <i>b</i> are not used.</dl>
<h2>Description</h2>
<p><code>vpSetMaterial</code> is used to set the properties of a material type. Each voxel may be composed of a mixture of several different material types, as described in <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3). Each material type has its own color and light reflection properties. The properties are used as parameters to the Phong shading equation for computing the color of the material given a set of light sources and a viewing direction (see <a href="/docs/linux/man/3-vpshadetable/">vpShadeTable</a>(3)). </p>
<p> To initialize the material parameters, call <code>vpSetMaterial</code> for each property of each material type to be used. The total number of materials is specified as an argument to <code>vpSetLookupShader</code>. The first material is specified by the constant VP_MATERIAL0, the second is VP_MATERIAL1, and so on. </p>
<p> The VP_AMBIENT property specifies the RGB ambient light coefficients of the material. This term represents the intensity of background light reflected by the material. Each of the RGB components specifies the coefficient for the corresponding light basis function. The values of the coefficients should be in the range 0.0-1.0. Default: 0.1 </p>
<p> The VP_DIFFUSE property specifies the RGB diffuse light coefficients of the material. This term represents the fraction of incident light intensity that is reflected diffusely (with a dull, matte appearance). The values of the coefficients should be in the range 0.0-1.0. Default: 0.4 </p>
<p> The VP_SPECULAR property specifies the RGB specular light coefficients of the material. This term represents the fraction of incident light intensity that is reflected specularly (with a shiny, mirror-like appearance). The values of the coefficients should be in the range 0.0-1.0. Default: 0.5 </p>
<p> The VP_SHINYNESS property specifies a single exponent that modifies the spread of specular highlights. The higher the number, the smaller and more intense the specular highlights. The exponent is specified with the <i>r</i> argument and can have any value; the generally-useful range is 1.0 to 100.0. The <i>g</i> and <i>b</i> arguments are ignored for this property. Default: 10.0 </p>
<p> The <i>surface_side</i> argument specifies which side of the material surface the properties apply to. By default, the &quot;interior&quot; side of a voxel is the side in the direction of the surface normal. During rendering, if the normal points closer to the direction of the viewer than the opposite of the normal then the viewer is looking at the exterior side of the voxel rather than the interior. Different material parameters can be applied to the two surface sides by calling <code>vpSetMaterial</code> separately for each side. The option VP_BOTH_SIDES allows the same property to be set for both sides with only one function call. It is possible to reverse the definition of interior and exterior sides by calling <code>vpEnable</code> with the VP_REVERSE_SURFACE_SIDES option. </p>
<p> Voxels are shaded using the following equation:</p>
<dl>
<dd>I = A + L * (D * n_dot_l + S * pow(n_dot_h, E)) </p>
<p> I<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>intensity for one color channel</p>
<p> A<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ambient intensity coefficient</p>
<p> D<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>diffuse reflection coefficient</p>
<p> S<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>specular reflection coefficient</p>
<p> E<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>shinyness</p>
<p> L<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>light intensity</p>
<p> n_dot_l<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>dot product of normal and light vectors</p>
<p> n_dot_h<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>dot product of normal and highlight vectors
</dl>
<p> This equation is evaluated separately for each color channel. If multiple light sources are enabled an additional term identical to the second term above is added for each light source (with different values for L, n_dot_l and n_dot_h corresponding to the particular light source).</p>
<h2>State Variables</h2>
<p>Information about the current material properties can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_MATERIAL_COUNT, VP_REVERSE_SURFACE_SIDES</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_VALUE</p>
<dd>Either the material number or the RGB components are invalid.</p>
<dt>VPERROR_BAD_OPTION</p>
<dd>Either the <i>surface_side</i> or <i>property</i> arguments are invalid.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpsetlookupshader/">vpSetLookupShader</a>(3), <a href="/docs/linux/man/3-vpshadetable/">vpShadeTable</a>(3), <a href="/docs/linux/man/3-vpgetmaterial/">vpGetMaterial</a>(3) </p>
