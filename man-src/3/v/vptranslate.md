---
title: "vptranslate(3)"
name: "vptranslate"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vptranslate/"
description: "vpTranslate – multiply the current transformation matrix by a translation matrix"
---

<p>vpTranslate &#8211; multiply the current transformation matrix by a translation matrix</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpTranslate(</code><i>vpc, tx, ty, tz</i><code>)</code></p>
<dd>
<dd>vpContext <i>*vpc;</i></p>
<dd>double *<i>tx,</i> *<i>ty,</i> *<i>tz;</i></dl>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>tx</i></p>
<dd>X component of translation vector.</p>
<dt><i>ty</i></p>
<dd>Y component of translation vector.</p>
<dt><i>tz</i></p>
<dd>Z component of translation vector.</dl>
<h2>Description</h2>
<p><code>vpTranslate</code> is used to multiply the current transformation matrix by a 4-by-4 translation matrix. The translation matrix is:</p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr></tt>1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>tx</p>
<p> <tt>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ty</p>
<p> <tt>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>tz</p>
<p> <tt>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>0<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>1
</dl>
<p> Use <code>vpCurrentMatrix</code> to set the current transformation matrix. By default, the transformation matrix is post-multiplied (M = M*T where M is the current matrix and T is the translation matrix). The VP_CONCAT_MODE option to <code>vpSeti</code> can be used to select pre-multiplication.</p>
<h2>State Variables</h2>
<p>The current matrix concatenation parameters can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_CURRENT_MATRIX, VP_CONCAT_MODE.</p>
<h2>Errors</h2>
<p>The return value is always VP_OK.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpcurrentmatrix/">vpCurrentMatrix</a>(3) </p>
