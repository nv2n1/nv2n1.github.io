---
title: "vpwindowphigs(3)"
name: "vpwindowphigs"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpwindowphigs/"
description: "vpWindowPHIGS – multiply the projection matrix by a PHIGS viewing matrix"
---

<p>vpWindowPHIGS &#8211; multiply the projection matrix by a PHIGS viewing matrix</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpWindowPHIGS(</code><i>vpc, vrp, vpn, vup, prp, umin, umax, vmin, vmax,</p>
<dd>front, back, projection_type</i><code>)</code></p>
<dd>vpContext *<i>vpc;</i></p>
<dd>vpVector3 <i>vrp, vpn, vup;</i></p>
<dd>vpVector3 <i>prp;</i></p>
<dd>double <i>umin, umax, vmin, vmax, front, back;</i></p>
<dd>int <i>projection_type;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>vrp</i></p>
<dd>Point specifying the view reference point.</p>
<dt><i>vpn</i></p>
<dd>Vector specifying the view plane normal.</p>
<dt><i>vup</i></p>
<dd>Vector specifying the view up vector.</p>
<dt><i>prp</i></p>
<dd>Point specifying the projection reference point (in view reference coordinates).</p>
<dt><i>umin</i></p>
<dd>Left coordinate of clipping window (in view reference coordinates).</p>
<dt><i>umax</i></p>
<dd>Right coordinate of clipping window (in view reference coordinates).</p>
<dt><i>vmin</i></p>
<dd>Bottom coordinate of clipping window (in view reference coordinates).</p>
<dt><i>vmax</i></p>
<dd>Top coordinate of clipping window (in view reference coordinates).</p>
<dt><i>front</i></p>
<dd>Coordinate of the near depth clipping plane (in view reference coordinates).</p>
<dt><i>back</i></p>
<dd>Coordinate of the far depth clipping plane (in view reference coordinates).</p>
<dt><i>projection_type</i></p>
<dd>Projection type code. Currently, must be VP_PARALLEL.</dl>
<h2>Description</h2>
<p><code>vpWindowPHIGS</code> is used to multiply the current projection matrix by a viewing and projection matrix specified by means of the PHIGS viewing model. This model combines specification of the viewpoint, projection and clipping parameters. The resulting matrix is stored in the projection transformation matrix. Since both the view and the projection are specified in this one matrix, normally the view transformation matrix is not used in conjunction with <code>vpWindowPHIGS</code> (it should be set to the identity). Currently, only parallel projections may be specified. For an alternative view specification model, see <a href="/docs/linux/man/3-vpwindow/">vpWindow</a>(3). </p>
<p> Assuming that the view transformation matrix is the identity, the matrix produced by <code>vpWindowPHIGS</code> should transform world coordinates into clip coordinates. This transformation is specified as follows. First, the projection plane (called the view plane) is defined by a point on the plane (the view reference point, <i>vrp</i>) and a vector normal to the plane (the view plane normal, <i>vpn</i>). Next, a coordinate system called the view reference coordinate (VRC) system is specified by means of the view plane normal and the view up vector, <i>vup.</i> The origin of VRC coordinates is the view reference point. The basis vectors of VRC coordinates are:</p>
<dl>
<dd><code>u</code> = v cross n<br />
 <code>v</code> = the projection of <i>vup</i> parallel to <i>vpn</i> onto the view plane<br />
 <code>n</code> = <i>vpn</i></dl>
<p> This coordinate system is used to specify the direction of projection and the clipping window. The clipping window bounds in the projection plane are given by <i>umin, umax, vmin</i> and <i>vmax.</i> The direction of projection is the vector from the center of the clipping window to the projection reference point <i>(prp),</i> which is also specified in VRC coordinates. Finally, the front and back clipping planes are given by n=<i>front</i> and n=<i>back</i> in VRC coordinates. </p>
<p> For a more detailed explanation of this view specification model, see <i>Computer Graphics: Principles and Practice</i> by Foley, vanDam, Feiner and Hughes.</p>
<h2>State Variables</h2>
<p>The current matrix concatenation parameters can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_CONCAT_MODE.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return values are possible:</p>
<dl>
<dt>VPERROR_BAD_VALUE</p>
<dd>The clipping plane coordinates are invalid (<i>umin &gt;= umax</i>, etc.).</p>
<dt>VPERROR_BAD_OPTION</p>
<dd>The <i>type</i> argument is invalid.</p>
<dt>VPERROR_SINGULAR</p>
<dd>The vectors defining view reference coordinates are not mutually orthogonal, or the projection reference point lies in the view plane.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpcurrentmatrix/">vpCurrentMatrix</a>(3), <a href="/docs/linux/man/3-vpwindow/">vpWindow</a>(3) </p>
