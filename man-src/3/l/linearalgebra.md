---
title: "linearalgebra(3)"
name: "linearalgebra"
section: "3"
letter: "l"
url: "/docs/linux/man/3-linearalgebra/"
description: "vpIdentity3, vpIdentity4, vpNormalize3, vpMatrixVectorMult4, vpMatrixMult4, vpCrossProduct, vpSolveSystem4, vpSetVector3, vpSetVector4 – linear algebra routines"
---

<p>vpIdentity3, vpIdentity4, vpNormalize3, vpMatrixVectorMult4, vpMatrixMult4, vpCrossProduct, vpSolveSystem4, vpSetVector3, vpSetVector4 &#8211; linear algebra routines</p>
<h2>Synopsis</h2>
<p>#include &lt;<a href="file:/usr/include/volpack.h">volpack.h</a>&gt; </p>
<p> void</p>
<dl COMPACT>
<dt> <code>vpIdentity3(</code><i>m_dst</i><code>)</code></p>
<dd>
<dd>vpMatrix3 <i>m_dst;</i> </p>
</dl>
<p> void</p>
<dl COMPACT>
<dt> <code>vpIdentity4(</code><i>m_dst</i><code>)</code></p>
<dd>
<dd>vpMatrix4 <i>m_dst;</i> </p>
</dl>
<p> vpResult</p>
<dl COMPACT>
<dt> <code>vpNormalize3(</code><i>v_src1</i><code>)</code></p>
<dd>
<dd>vpVector3 <i>v_src1;</i> </p>
</dl>
<p> void</p>
<dl COMPACT>
<dt> <code>vpMatrixVectorMult4(</code><i>v_dst, m_src1, v_src1</i><code>)</code></p>
<dd>
<dd>vpVector4 <i>v_dst;</i></p>
<dd>vpMatrix4 <i>m_src1;</i></p>
<dd>vpVector4 <i>v_src1;</i> </p>
</dl>
<p> void</p>
<dl COMPACT>
<dt> <code>vpMatrixMult4(</code><i>m_dst, m_src1, m_src2</i><code>)</code></p>
<dd>
<dd>vpVector4 <i>m_dst, m_src1, m_src2;</i> </p>
</dl>
<p> void</p>
<dl COMPACT>
<dt> <code>vpCrossProduct(</code><i>v_dst, v_src1, v_src2</i><code>)</code></p>
<dd>
<dd>vpVector3 <i>v_dst, v_src1, v_src2;</i> </p>
</dl>
<p> vpResult</p>
<dl COMPACT>
<dt> <code>vpSolveSystem4(</code><i>m_src1, b, count</i><code>)</code></p>
<dd>
<dd>vpMatrix4 <i>m_src1;</i></p>
<dd>vpVector4 <i>b[];</i></p>
<dd>int <i>count;</i> </p>
</dl>
<p> void</p>
<dl COMPACT>
<dt> <code>vpSetVector3(</code><i>v_dst, x, y, z</i><code>)</code></p>
<dd>
<dd>vpVector3 <i>v_dst;</i></p>
<dd>double <i>x, y, z;</i> </p>
</dl>
<p> void</p>
<dl COMPACT>
<dt> <code>vpSetVector4(</code><i>v_dst, x, y, z, w</i><code>)</code></p>
<dd>
<dd>vpVector4 <i>v_dst;</i></p>
<dd>double <i>x, y, z, w;</i></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>m_src1, m_src2, m_dst</i></p>
<dd>Source and destination matrices.</p>
<dt><i>v_src1, v_src2, v_dst</i></p>
<dd>Source and destination vectors.</p>
<dt><i>b</i></p>
<dd>Array of right-hand-side vectors.</p>
<dt><i>count</i></p>
<dd>Number of right-hand-side vectors.</p>
<dt><i>x, y, z, w</i></p>
<dd>Vector components.</dl>
<h2>Description</h2>
<p>These routines form a simple linear algebra package used internally by VolPack. The routines are also available as utility routines for use by the application. </p>
<p> <code>vpIdentity3</code> assigns the identity matrix to a 3-by-3 matrix. </p>
<p> <code>vpIdentity4</code> assigns the identity matrix to a 4-by-4 matrix. </p>
<p> <code>vpNormalize3</code> normalizes a 3-element vector (so the magnitude is 1.0). The result overwrites the source vector. </p>
<p> <code>vpMatrixVectorMult4</code> multiplies a 4-by-4 matrix by a 4-element column vector and stores the result in the destination vector <i>(v_dst = m . v_src)</i>. </p>
<p> <code>vpMatrixMult4</code> multiplies two 4-by-4 matrices and stores the result in the destination matrix <i>(m_dst = m_src1 . m_src2)</i>. </p>
<p> <code>vpCrossProduct</code> computes the cross product of two 3-element vectors and stores the result in the destination vector <i>(v_dst = v_src1 x v_src2)</i>. </p>
<p> <code>vpSolveSystem4</code> solves the linear system <i>m . x = b</i> for each right-hand-side vector in the <i>b</i> array. The solution vectors overwrite the vectors in the <i>b</i> array. The solution is computed using Gauss-Jordan elimination with partial pivoting and implicit scaling. </p>
<p> <code>vpSetVector3</code> initializes the components of a 3-element vector <i>(v_dst = [x, y, z]).</i> It is a macro. </p>
<p> <code>vpSetVector4</code> initializes the components of a 4-element vector <i>(v_dst = [x, y, z, w]).</i> It is a macro.</p>
<h2>Errors</h2>
<p><code>vpNormalize3</code> and <code>vpSolveSystem4</code> normally return VP_OK. The following error return value is possible:</p>
<dl COMPACT>
<dt>VPERROR_SINGULAR</p>
<dd>The vector is a 0 vector (<code>vpNormalize3</code> only), or the matrix is singular (<code>vpSolveSystem4</code> only).</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3)</p>
