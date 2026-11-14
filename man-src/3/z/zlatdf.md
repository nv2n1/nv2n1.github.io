---
title: "zlatdf(3)"
name: "zlatdf"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlatdf/"
description: "zlatdf.f –"
---

<p>zlatdf.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlatdf</code> (IJOB, N, Z, LDZ, RHS, RDSUM, RDSCAL, IPIV, JPIV)<br />
 <i></i><code>ZLATDF</code> uses the LU factorization of the n-by-n matrix computed by sgetc2 and computes a contribution to the reciprocal Dif-estimate.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlatdf (integerIJOB, integerN, complex*16, dimension( ldz, * )Z, integerLDZ, complex*16, dimension( * )RHS, double precisionRDSUM, double precisionRDSCAL, integer, dimension( * )IPIV, integer, dimension( * )JPIV)</h3>
<p><code>ZLATDF</code> uses the LU factorization of the n-by-n matrix computed by sgetc2 and computes a contribution to the reciprocal Dif-estimate. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLATDF computes the contribution to the reciprocal Dif-estimate
 by solving for x in Z * x = b, where b is chosen such that the norm
 of x is as large as possible. It is assumed that LU decomposition
 of Z has been computed by ZGETC2. On entry RHS = f holds the
 contribution from earlier solved sub-systems, and on return RHS = x.
 The factorization of Z returned by ZGETC2 has the form
 Z = P * L * U * Q, where P and Q are permutation matrices. L is lower
 triangular with unit diagonal elements and U is upper triangular.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>IJOB</i> </p>
<pre> IJOB is INTEGER
 IJOB = 2: First compute an approximative null-vector e
 of Z using ZGECON, e is normalized and solve for
 Zx = +-e - f with the sign giving the greater value of
 2-norm(x). About 5 times as expensive as Default.
 IJOB .ne. 2: Local look ahead strategy where
 all entries of the r.h.s. b is choosen as either +1 or
 -1. Default.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix Z.</pre>
<p><i>Z</i> </p>
<pre> Z is DOUBLE PRECISION array, dimension (LDZ, N)
 On entry, the LU part of the factorization of the n-by-n
 matrix Z computed by ZGETC2: Z = P * L * U * Q</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDA &gt;= max(1, N).</pre>
<p><i>RHS</i> </p>
<pre> RHS is DOUBLE PRECISION array, dimension (N).
 On entry, RHS contains contributions from other subsystems.
 On exit, RHS contains the solution of the subsystem with
 entries according to the value of IJOB (see above).</pre>
<p><i>RDSUM</i> </p>
<pre> RDSUM is DOUBLE PRECISION
 On entry, the sum of squares of computed contributions to
 the Dif-estimate under computation by ZTGSYL, where the
 scaling factor RDSCAL (see below) has been factored out.
 On exit, the corresponding sum of squares updated with the
 contributions from the current sub-system.
 If TRANS = 'T' RDSUM is not touched.
 NOTE: RDSUM only makes sense when ZTGSY2 is called by CTGSYL.</pre>
<p><i>RDSCAL</i> </p>
<pre> RDSCAL is DOUBLE PRECISION
 On entry, scaling factor used to prevent overflow in RDSUM.
 On exit, RDSCAL is updated w.r.t. the current contributions
 in RDSUM.
 If TRANS = 'T', RDSCAL is not touched.
 NOTE: RDSCAL only makes sense when ZTGSY2 is called by
 ZTGSYL.</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N).
 The pivot indices; for 1 &lt;= i &lt;= N, row i of the
 matrix has been interchanged with row IPIV(i).</pre>
<p><i>JPIV</i> </p>
<pre> JPIV is INTEGER array, dimension (N).
 The pivot indices; for 1 &lt;= j &lt;= N, column j of the
 matrix has been interchanged with column JPIV(j).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> <code>Further Details: </code></p>
<dl>
<dd>This routine is a further developed implementation of algorithm BSOLVE in [1] using complete pivoting in the LU factorization.</dl>
<p> <code>Contributors: </code></p>
<dl>
<dd>Bo Kagstrom and Peter Poromaa, Department of Computing Science, Umea University, S-901 87 Umea, Sweden.</dl>
<p> <code>References: </code></p>
<dl>
<dd>[1] Bo Kagstrom and Lars Westin, Generalized Schur Methods with Condition Estimators for Solving the Generalized Sylvester Equation, IEEE Transactions on Automatic Control, Vol. 34, No. 7, July 1989, pp 745-751. </p>
<p>&nbsp;<wbr>[2]&nbsp;<wbr>Peter Poromaa, On Efficient and Robust Estimators for the Separation between two Regular Matrix Pairs with Applications in Condition Estimation. Report UMINF-95.05, Department of Computing Science, Umea University, S-901 87 Umea, Sweden,</p>
<dl>
<dt>1995.</p>
<dd></dl>
</dl>
<p> Definition at line 169 of file zlatdf.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
