---
title: "vpgetmaterial(3)"
name: "vpgetmaterial"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpgetmaterial/"
description: "vpGetMaterial – get material properties"
---

<p>vpGetMaterial &#8211; get material properties</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpGetMaterial(</code><i>vpc, material, property, surface_side, r_ptr,</p>
<dd>g_ptr, b_ptr</i><code>)</code></p>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>material;</i></p>
<dd>int <i>property;</i></p>
<dd>int <i>surface_side;</i></p>
<dd>double *<i>r_ptr,</i> *<i>g_ptr,</i> *<i>b_ptr;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>material</i></p>
<dd>A constant specifying a particular material number (VP_MATERIAL0, VP_MATERIAL1, &#8230;, VP_MATERIAL5).</p>
<dt><i>property</i></p>
<dd>A constant specifying one material property (VP_AMBIENT, VP_DIFFUSE, VP_SPECULAR or VP_SHINYNESS).</p>
<dt><i>surface_side</i></p>
<dd>A constant specifying one side of the material surface (VP_EXTERIOR or VP_INTERIOR).</p>
<dt><i>r_ptr, g_ptr, b_ptr</i></p>
<dd>Locations to store the RGB components of the color associated with the property. For VP_SHINYNESS, <i>g_ptr</i> and <i>b_ptr</i> are not used.</dl>
<h2>Description</h2>
<p><code>vpGetMaterial</code> is used to get the properties of a material type. The arguments are exactly analogous to <code>vpSetMaterial</code> except that the <i>surface_side</i> argument may not be VP_BOTH_SIDES, and the final three arguments are pointers to locations for storing the material properties.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_VALUE</p>
<dd>The material number is invalid.</p>
<dt>VPERROR_BAD_OPTION</p>
<dd>Either the <i>surface_side</i> or <i>property</i> arguments are invalid.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpsetmaterial/">vpSetMaterial</a>(3) </p>
