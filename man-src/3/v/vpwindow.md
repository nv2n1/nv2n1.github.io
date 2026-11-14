---
title: "vpwindow(3)"
name: "vpwindow"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpwindow/"
description: "vpWindow – multiply the projection matrix by a perspective or orthographic matrix"
---

<p>vpWindow &#8211; multiply the projection matrix by a perspective or orthographic matrix</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpWindow(</code><i>vpc, type, left, right, bottom, top, near, far</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>type;</i></p>
<dd>double <i>left, right;</i></p>
<dd>double <i>bottom, top;</i></p>
<dd>double <i>near, far;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>type</i></p>
<dd>Projection type code. Currently, must be VP_PARALLEL.</p>
<dt><i>left</i></p>
<dd>Coordinate of the left vertical clipping plane.</p>
<dt><i>right</i></p>
<dd>Coordinate of the right vertical clipping plane.</p>
<dt><i>bottom</i></p>
<dd>Coordinate of the bottom horizontal clipping plane.</p>
<dt><i>top</i></p>
<dd>Coordinate of the top horizontal clipping plane.</p>
<dt><i>near</i></p>
<dd>Coordinate of the near depth clipping plane.</p>
<dt><i>far</i></p>
<dd>Coordinate of the far depth clipping plane.</dl>
<h2>Description</h2>
<p><code>vpWindow</code> is used to multiply the current projection matrix by a perspective or orthographic projection matrix. The new projection matrix is defined by the coordinates of six clipping planes in the eye coordinate system (see <a href="/docs/linux/man/3-vpcurrentmatrix/">vpCurrentMatrix</a>(3)). The matrix maps the points <i>(left, bottom, near)</i> and <i>(right, top, near)</i> to the lower left and upper right corners of the clipping window. For an alternative means of specifying the projection matrix, see <a href="/docs/linux/man/3-vpwindowphigs/">vpWindowPHIGS</a>(3). </p>
<p> Currently, only orthographic projections are supported. Perspective projections will be added in a future release. </p>
<p> The matrix for parallel projections is:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr></tt>A<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>D</p>
<p> <tt>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>B<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>E</p>
<p> <tt>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>C<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>F</p>
<p> <tt>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1</p>
<p> A = 2 / <i>(right &#8211; left)</i><br />
 B = 2 / <i>(top &#8211; bottom)</i><br />
 C = 2 / <i>(far &#8211; near)</i><br />
 D = <i>(left + right) / (left &#8211; right)</i><br />
 E = <i>(bottom + top) / (bottom &#8211; top)</i><br />
 F = <i>(near + far) / (near &#8211; far)</i></dl>
<p> The matrix is multiplied into the projection matrix, even if the projection matrix is not the current matrix. By default, the matrix is post-multiplied (N = N*<i>m</i> where N is the current matrix and <i>m</i> is the argument to <code>vpMultMatrix</code>). The VP_CONCAT_MODE option to <code>vpSeti</code> can be used to select pre-multiplication. The default window is a parallel projection with left = bottom = near = -0.5, and right = top = far = 0.5.</p>
<h2>State Variables</h2>
<p>The current matrix concatenation parameters can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_CONCAT_MODE.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_VALUE</p>
<dd>The clipping plane coordinates are invalid (<i>left &gt;= right</i>, etc.).</p>
<dt>VPERROR_BAD_OPTION</p>
<dd>The <i>type</i> argument is invalid.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpcurrentmatrix/">vpCurrentMatrix</a>(3), <a href="/docs/linux/man/3-vpwindowphigs/">vpWindowPHIGS</a>(3) </p>
