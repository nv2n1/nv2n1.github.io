---
title: "vpnormalindex(3)"
name: "vpnormalindex"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpnormalindex/"
description: "vpNormalIndex, vpNormal – encode/decode a surface normal vector"
---

<p>vpNormalIndex, vpNormal &#8211; encode/decode a surface normal vector</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;

int

vpNormalIndex(nx, ny, nz)

double nx, ny, nz;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpNormal(</code><i>n, nx_ptr, ny_ptr, nz_ptr</i><code>)</code></p>
<dd>
<dd>int <i>n;</i></p>
<dd>double *<i>nx_ptr,</i> *<i>ny_ptr,</i> *<i>nz_ptr;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>nx</i></p>
<dd>X component of surface normal vector.</p>
<dt><i>ny</i></p>
<dd>Y component of surface normal vector.</p>
<dt><i>nz</i></p>
<dd>Z component of surface normal vector.</p>
<dt><i>n</i></p>
<dd>Encoded surface normal vector.</p>
<dt><i>nx_ptr</i></p>
<dd>Pointer to storage for returning X component of surface normal vector.</p>
<dt><i>ny_ptr</i></p>
<dd>Pointer to storage for returning Y component of surface normal vector.</p>
<dt><i>nz_ptr</i></p>
<dd>Pointer to storage for returning Z component of surface normal vector.</dl>
<h2>Description</h2>
<p>These two routines are used to convert surface normal vectors between encoded and unencoded forms. An unencoded vector is described by its three components (stored as double-precision floating point numbers) in an orthogonal coordinate system. An encoded vector is described by a single integer that is suitable for use as an index in a shading lookup table. VolPack&#8217;s built-in shading routines require the use of surface normal vectors encoded using <code>vpNormalIndex</code> (or one of the higher-level normal vector computation routines, <code>vpVolumeNormals</code> or <code>vpScanlineNormals</code>). User-defined shading routines or lookup tables are not required to use encoded normal vectors. </p>
<p> <code>vpNormalIndex</code> computes an encoded vector from the components of an unencoded vector. The vector must be normalized (<i>nx*nx + ny*ny + nz*nz = 1</i>). The maximum possible value of an encoded normal is given by the constant VP_NORM_MAX. </p>
<p> <code>vpNormal</code> computes the components of a vector from the encoded integer form. The encoded normal has less resolution than the unencoded form, so the vector computed by <code>vpNormal</code> may not be equal to the original vector passed to <code>vpNormalIndex</code>.</p>
<h2>Errors</h2>
<p><code>vpNormalIndex</code> always returns a valid encoded normal vector. </p>
<p> <code>vpNormal</code> normally returns the value VP_OK. The following return value is possible:</p>
<dl>
<dt>VPERROR_BAD_VALUE</p>
<dd>The encoded normal vector is invalid.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpvolumenormals/">vpVolumeNormals</a>(3), <a href="/docs/linux/man/3-vpscanlinenormals/">vpScanlineNormals</a>(3) </p>
