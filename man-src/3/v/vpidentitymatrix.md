---
title: "vpidentitymatrix(3)"
name: "vpidentitymatrix"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpidentitymatrix/"
description: "vpIdentityMatrix – load the identity matrix into the current transformation matrix"
---

<p>vpIdentityMatrix &#8211; load the identity matrix into the current transformation matrix</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpIdentityMatrix(</code><i>vpc</i><code>)</code></p>
<dd>
<dd>vpContext <i>*vpc;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></dl>
<h2>Description</h2>
<p><code>vpIdentityMatrix</code> is used to load a 4-by-4 identity matrix into the current transformation matrix. Use <code>vpCurrentMatrix</code> to set the current transformation matrix.</p>
<h2>Errors</h2>
<p>The return value is always VP_OK.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpcurrentmatrix/">vpCurrentMatrix</a>(3), <a href="/docs/linux/man/3-vpgetmatrix/">vpGetMatrix</a>(3) </p>
