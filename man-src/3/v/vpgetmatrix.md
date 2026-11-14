---
title: "vpgetmatrix(3)"
name: "vpgetmatrix"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpgetmatrix/"
description: "vpGetMatrix – retrieve the contents of a transformation matrix"
---

<p>vpGetMatrix &#8211; retrieve the contents of a transformation matrix</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpGetMatrix(</code><i>vpc, matrix_code, matrix</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>matrix_code;</i></p>
<dd>vpMatrix4 <i>matrix;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>matrix_code</i></p>
<dd>A code specifying one of the VolPack transformation matrices (VP_MODEL, VP_VIEW, VP_PROJECT or VP_SCREEN).</p>
<dt><i>matrix</i></p>
<dd>Matrix for storing the result.</dl>
<h2>Description</h2>
<p><code>vpGetMatrix</code> retrieves the contents of one of the transformation matrices (see <a href="/docs/linux/man/3-vpcurrentmatrix/">vpCurrentMatrix</a>(3)). The special code VP_SCREEN causes the function to compute the transformation from object coordinates to image coordinates and return a matrix describing this transformation.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return value is possible:</p>
<dl>
<dt>VPERROR_BAD_OPTION</p>
<dd>The <i>matrix_code</i> argument is invalid.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpcurrentmatrix/">vpCurrentMatrix</a>(3) </p>
