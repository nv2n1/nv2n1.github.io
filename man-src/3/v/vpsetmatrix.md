---
title: "vpsetmatrix(3)"
name: "vpsetmatrix"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpsetmatrix/"
description: "vpSetMatrix – load a matrix into the current transformation matrix"
---

<p>vpSetMatrix &#8211; load a matrix into the current transformation matrix</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpSetMatrix(</code><i>vpc, m</i><code>)</code></p>
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
<p><code>vpSetMatrix</code> is used to load a 4-by-4 transformation matrix into the current transformation matrix. Use <code>vpCurrentMatrix</code> to set the current transformation matrix.</p>
<h2>State Variables</h2>
<p>The current transformation matrix parameters can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_CURRENT_MATRIX.</p>
<h2>Errors</h2>
<p>The return value is always VP_OK.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpcurrentmatrix/">vpCurrentMatrix</a>(3), <a href="/docs/linux/man/3-vpgetmatrix/">vpGetMatrix</a>(3) </p>
