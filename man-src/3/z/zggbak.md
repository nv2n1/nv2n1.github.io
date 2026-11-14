---
title: "zggbak(3)"
name: "zggbak"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zggbak/"
description: "zggbak.f –"
---

<p>zggbak.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zggbak</code> (JOB, SIDE, N, ILO, IHI, LSCALE, RSCALE, M, V, LDV, INFO)<br />
 <i></i><code>ZGGBAK</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zggbak (characterJOB, characterSIDE, integerN, integerILO, integerIHI, double precision, dimension( * )LSCALE, double precision, dimension( * )RSCALE, integerM, complex*16, dimension( ldv, * )V, integerLDV, integerINFO)</h3>
<p><code>ZGGBAK</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZGGBAK forms the right or left eigenvectors of a complex generalized
 eigenvalue problem A*x = lambda*B*x, by backward transformation on
 the computed eigenvectors of the balanced pair of matrices output by
 ZGGBAL.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>JOB</i> </p>
<pre> JOB is CHARACTER*1
 Specifies the type of backward transformation required:
 = 'N': do nothing, return immediately;
 = 'P': do backward transformation for permutation only;
 = 'S': do backward transformation for scaling only;
 = 'B': do backward transformations for both permutation and
 scaling.
 JOB must be the same as the argument JOB supplied to ZGGBAL.</pre>
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
 The integers ILO and IHI determined by ZGGBAL.
 1 &lt;= ILO &lt;= IHI &lt;= N, if N &gt; 0; ILO=1 and IHI=0, if N=0.</pre>
<p><i>LSCALE</i> </p>
<pre> LSCALE is DOUBLE PRECISION array, dimension (N)
 Details of the permutations and/or scaling factors applied
 to the left side of A and B, as returned by ZGGBAL.</pre>
<p><i>RSCALE</i> </p>
<pre> RSCALE is DOUBLE PRECISION array, dimension (N)
 Details of the permutations and/or scaling factors applied
 to the right side of A and B, as returned by ZGGBAL.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of columns of the matrix V. M &gt;= 0.</pre>
<p><i>V</i> </p>
<pre> V is COMPLEX*16 array, dimension (LDV,M)
 On entry, the matrix of right or left eigenvectors to be
 transformed, as returned by ZTGEVC.
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
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> See R.C. Ward, Balancing the generalized eigenvalue problem,
 SIAM J. Sci. Stat. Comp. 2 (1981), 141-152.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 148 of file zggbak.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
