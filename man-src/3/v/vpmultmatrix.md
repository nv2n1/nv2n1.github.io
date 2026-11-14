---
title: "vpmultmatrix(3)"
name: "vpmultmatrix"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpmultmatrix/"
description: "vpMultMatrix – multiply the current transformation matrix by another matrix"
---

<p>vpMultMatrix &#8211; multiply the current transformation matrix by another matrix</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpMultMatrix(</code><i>vpc, m</i><code>)</code></p>
<dd>
<dd>vpContext *<i>vpc;</i></p>
<dd>vpMatrix4 <i>m;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>m</i></p>
<dd>Input matrix.</dl>
<h2>Description</h2>
<p><code>vpMultMatrix</code> is used to multiply the current transformation matrix by an arbitrary 4-by-4 transformation matrix. Use <code>vpCurrentMatrix</code> to set the current transformation matrix. By default, the matrix is post-multiplied (N = N*<i>m</i> where N is the current matrix and <i>m</i> is the argument to <code>vpMultMatrix</code>). The VP_CONCAT_MODE option to <code>vpSeti</code> can be used to select pre-multiplication.</p>
<h2>State Variables</h2>
<p>The current matrix concatenation parameters can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_CURRENT_MATRIX, VP_CONCAT_MODE.</p>
<h2>Errors</h2>
<p>The return value is always VP_OK.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpcurrentmatrix/">vpCurrentMatrix</a>(3) </p>
