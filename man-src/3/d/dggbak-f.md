---
title: "dggbak-f(3)"
name: "dggbak-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dggbak-f/"
description: "dggbak.f –"
---

<p>dggbak.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dggbak</code> (JOB, SIDE, N, ILO, IHI, LSCALE, RSCALE, M, V, LDV, INFO)<br />
 <i></i><code>DGGBAK</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dggbak (characterJOB, characterSIDE, integerN, integerILO, integerIHI, double precision, dimension( * )LSCALE, double precision, dimension( * )RSCALE, integerM, double precision, dimension( ldv, * )V, integerLDV, integerINFO)</h3>
<p><code>DGGBAK</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DGGBAK forms the right or left eigenvectors of a real generalized
 eigenvalue problem A*x = lambda*B*x, by backward transformation on
 the computed eigenvectors of the balanced pair of matrices output by
 DGGBAL.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>JOB</i> </p>
<pre> JOB is CHARACTER*1
 Specifies the type of backward transformation required:
 = 'N': do nothing, return immediately;
 = 'P': do backward transformation for permutation only;
 = 'S': do backward transformation for scaling only;
 = 'B': do backward transformations for both permutation and
 scaling.
 JOB must be the same as the argument JOB supplied to DGGBAL.</pre>
<p><i>SIDE</i> </p>
<pre> SIDE is CHARACTER*1
 = 'R': V contains right eigenvectors;
 = 'L': V contains left eigenvectors.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of rows of the matrix V. N &gt;= 0.</pre>
<p><i>ILO</i> </p>
<pre> ILO is INTEGER</pre>
<p><i>IHI</i> </p>
<pre> IHI is INTEGER
 The integers ILO and IHI determined by DGGBAL.
 1 &lt;= ILO &lt;= IHI &lt;= N, if N &gt; 0; ILO=1 and IHI=0, if N=0.</pre>
<p><i>LSCALE</i> </p>
<pre> LSCALE is DOUBLE PRECISION array, dimension (N)
 Details of the permutations and/or scaling factors applied
 to the left side of A and B, as returned by DGGBAL.</pre>
<p><i>RSCALE</i> </p>
<pre> RSCALE is DOUBLE PRECISION array, dimension (N)
 Details of the permutations and/or scaling factors applied
 to the right side of A and B, as returned by DGGBAL.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of columns of the matrix V. M &gt;= 0.</pre>
<p><i>V</i> </p>
<pre> V is DOUBLE PRECISION array, dimension (LDV,M)
 On entry, the matrix of right or left eigenvectors to be
 transformed, as returned by DTGEVC.
 On exit, V is overwritten by the transformed eigenvectors.</pre>
<p><i>LDV</i> </p>
<pre> LDV is INTEGER
 The leading dimension of the matrix V. LDV &gt;= max(1,N).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> See R.C. Ward, Balancing the generalized eigenvalue problem,
 SIAM J. Sci. Stat. Comp. 2 (1981), 141-152.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 147 of file dggbak.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
