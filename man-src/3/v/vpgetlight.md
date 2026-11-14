---
title: "vpgetlight(3)"
name: "vpgetlight"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpgetlight/"
description: "vpGetLight – get lighting properties"
---

<p>vpGetLight &#8211; get lighting properties</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpGetLight(</code><i>vpc, light_num, property, n0_ptr, n1_ptr, n2_ptr</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>light_num;</i></p>
<dd>int <i>property;</i></p>
<dd>double *<i>n0_ptr,</i> *<i>n1_ptr,</i> *<i>n2_ptr;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>light_num</i></p>
<dd>A constant specifying a particular light source (VP_LIGHT0, VP_LIGHT1, &#8230;, VP_LIGHT5).</p>
<dt><i>property</i></p>
<dd>A constant specifying one lighting property (VP_COLOR or VP_DIRECTION).</p>
<dt><i>n0_ptr, n1_ptr, n2_ptr</i></p>
<dd>Locations for storing the result: components of an RGB color (for VP_COLOR) or a direction vector (for VP_DIRECTION).</dl>
<h2>Description</h2>
<p><code>vpGetLight</code> is used to get the properties of a light source. The arguments are exactly analogous to <code>vpSetLight</code> except that the final three arguments are pointers to locations for storing the lighting properties.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_LIMIT_EXCEEDED</p>
<dd>The light number is invalid or exceeds an implementation limit.</p>
<dt>VPERROR_BAD_OPTION</p>
<dd>The <i>property</i> argument is invalid.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpsetlight/">vpSetLight</a>(3) </p>
