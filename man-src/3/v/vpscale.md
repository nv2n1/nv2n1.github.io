---
title: "vpscale(3)"
name: "vpscale"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpscale/"
description: "vpScale – multiply the current transformation matrix by a scaling matrix"
---

<p>vpScale &#8211; multiply the current transformation matrix by a scaling matrix</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpScale(</code><i>vpc, sx, sy, sz</i><code>)</code></p>
<dd>
<dd>vpContext <i>*vpc;</i></p>
<dd>double <i>sxR;</p>
<dd>double syR;</p>
<dd>double szR;</dl>
<p> </i></p>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>sx</i></p>
<dd>Scale factor for the X dimension.</p>
<dt><i>sy</i></p>
<dd>Scale factor for the Y dimension.</p>
<dt><i>sz</i></p>
<dd>Scale factor for the Z dimension.</dl>
<h2>Description</h2>
<p><code>vpScale</code> is used to multiply the current transformation matrix by a 4-by-4 scaling matrix. The arguments specify independent scale factors for each of the three cartesian axes. The scaling matrix is:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr></tt>sx<tt>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0</p>
<p> <tt>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>sy<tt>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0</p>
<p> <tt>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>sz<tt>&nbsp;<wbr>&nbsp;<wbr></tt>0</p>
<p> <tt>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1
</dl>
<p> Use <code>vpCurrentMatrix</code> to set the current transformation matrix. By default, the scaling matrix is post-multiplied (M = M*S where M is the current matrix and S is the scaling matrix). The VP_CONCAT_MODE option to <code>vpSeti</code> can be used to select pre-multiplication.</p>
<h2>State Variables</h2>
<p>The current matrix concatenation parameters can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_CURRENT_MATRIX, VP_CONCAT_MODE.</p>
<h2>Errors</h2>
<p>The return value is always VP_OK.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpcurrentmatrix/">vpCurrentMatrix</a>(3) </p>
