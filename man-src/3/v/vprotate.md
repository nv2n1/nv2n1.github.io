---
title: "vprotate(3)"
name: "vprotate"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vprotate/"
description: "vpRotate – multiply the current transformation matrix by a rotation matrix"
---

<p>vpRotate &#8211; multiply the current transformation matrix by a rotation matrix</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpRotate(</code><i>vpc, axis, degrees</i><code>)</code></p>
<dd>
<dd>vpContext <i>*vpc;</i></p>
<dd>int <i>axis;</i></p>
<dd>double <i>degrees;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>axis</i></p>
<dd>Rotation axis code (VP_X_AXIS, VP_Y_AXIS or VP_Z_AXIS).</p>
<dt><i>degrees</i></p>
<dd>Number of degrees to rotate.</dl>
<h2>Description</h2>
<p><code>vpRotate</code> is used to multiply the current transformation matrix by a 4-by-4 rotation matrix. The rotation axis must be one of the three principal viewing axes and is specified with one of the following codes: VP_X_AXIS<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>X axis</p>
<p> VP_Y_AXIS<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Y axis</p>
<p> VP_Z_AXIS<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Z axis</p>
<p> The rotation angle is specified in degrees. A positive angle indicates a clockwise rotation when looking towards the positive direction along the axis. For an X-axis rotation, the rotation matrix is:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cos(d)<tt>&nbsp;<wbr>&nbsp;<wbr></tt>sin(d)<tt>&nbsp;<wbr>&nbsp;<wbr></tt>0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-sin(d)<tt>&nbsp;<wbr></tt>cos(d)<tt>&nbsp;<wbr>&nbsp;<wbr></tt>0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1
</dl>
<p> where d stands for the <i>degrees</i> argument. For a Y-axis rotation, the rotation matrix is:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cos(d)<tt>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-sin(d)<tt>&nbsp;<wbr></tt>0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>sin(d)<tt>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cos(d)<tt>&nbsp;<wbr>&nbsp;<wbr></tt>0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1
</dl>
<p> For a Z-axis rotation, the rotation matrix is:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>cos(d)<tt>&nbsp;<wbr>&nbsp;<wbr></tt>sin(d)<tt>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>-sin(d)<tt>&nbsp;<wbr></tt>cos(d)<tt>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1
</dl>
<p> Use <code>vpCurrentMatrix</code> to set the current transformation matrix. By default, the rotation matrix is post-multiplied (M = M*R where M is the current matrix and R is the rotation matrix). The VP_CONCAT_MODE option to <code>vpSeti</code> can be used to select pre-multiplication.</p>
<h2>State Variables</h2>
<p>The current matrix concatenation parameters can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_CURRENT_MATRIX, VP_CONCAT_MODE.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return value is possible:</p>
<dl>
<dt>VPERROR_BAD_OPTION</p>
<dd>The <i>axis</i> argument is invalid.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpcurrentmatrix/">vpCurrentMatrix</a>(3) </p>
