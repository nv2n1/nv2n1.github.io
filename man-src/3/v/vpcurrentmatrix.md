---
title: "vpcurrentmatrix(3)"
name: "vpcurrentmatrix"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpcurrentmatrix/"
description: "vpCurrentMatrix – choose the current transformation matrix"
---

<p>vpCurrentMatrix &#8211; choose the current transformation matrix</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpCurrentMatrix(</code><i>vpc, option</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>option;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>option</i></p>
<dd>A code specifying one of the VolPack transformation matrices (VP_MODEL, VP_VIEW or VP_PROJECT).</dl>
<h2>Description</h2>
<p><code>vpCurrentMatrix</code> is used to choose the current transformation matrix. The <i>option</i> parameter must be one of the following:</p>
<dl>
<dd>VP_MODEL<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>modeling transformation</p>
<p> VP_VIEW<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>viewing transformation</p>
<p> VP_PROJECT<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>projection transformation
</dl>
<p> Subsequent calls to the matrix transformation functions (<code>vpIdentityMatrix, vpTranslate, vpRotate, vpScale, vpMultMatrix</code> and <code>vpSetMatrix</code>) are applied to the new current transformation matrix. </p>
<p> Typically the modeling transformation is used to specify a transformation from object coordinates to world coordinates. In object coordinates the volume data is located inside a unit cube centered at the origin (corners at (-0.5, -0.5, -0.5) and (0.5, 0.5, 0.5)). The default modeling transformation is the identity, so the volume is initially located inside the unit cube in world coordinates. By default, the current matrix is VP_MODEL. The modeling transformation is also applied to light direction vectors (see <a href="/docs/linux/man/3-vpsetlight/">vpSetLight</a>(3)). </p>
<p> The viewing transformation is used for transforming world coordinates into eye coordinates. In eye coordinates the viewer is looking down the Z axis in the negative direction. The default value of the matrix is also the identity, so the viewer is looking down the Z axis in world coordinates as well. Typically this transformation matrix is used to specify the location and direction of the viewer. It is also possible to combine the modeling and viewing matrices (as in the OpenGL viewing model), in which case you can store the composite transformation in either the model or the view matrix set the other matrix to the identity. </p>
<p> The projection transformation specifies the transformation from eye coordinates to clip coordinates. In the clip coordinate system the entire viewing frustum lies inside a cube defined by the planes X=1, X=-1, Y=1, Y=-1, Z=1 and Z=-1. This transformation also specifies the type of projection used to produce a 2D image. The 2D image is computed by projecting along the Z axis in the clip coordinate system and then scaling in the X and Y dimensions to the final image size. The routines <code>vpWindow</code> and <code>vpWindowPHIGS</code> are useful for computing projection transformations.</p>
<h2>State Variables</h2>
<p>The current transformation matrix code can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_CURRENT_MATRIX.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return value is possible:</p>
<dl>
<dt>VPERROR_BAD_OPTION</p>
<dd>The <i>option</i> argument is invalid.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpgetmatrix/">vpGetMatrix</a>(3) </p>
