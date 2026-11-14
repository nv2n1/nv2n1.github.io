---
title: "zggbal(3)"
name: "zggbal"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zggbal/"
description: "zggbal.f –"
---

<p>zggbal.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zggbal</code> (JOB, N, A, LDA, B, LDB, ILO, IHI, LSCALE, RSCALE, WORK, INFO)<br />
 <i></i><code>ZGGBAL</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zggbal (characterJOB, integerN, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldb, * )B, integerLDB, integerILO, integerIHI, double precision, dimension( * )LSCALE, double precision, dimension( * )RSCALE, double precision, dimension( * )WORK, integerINFO)</h3>
<p><code>ZGGBAL</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZGGBAL balances a pair of general complex matrices (A,B). This
 involves, first, permuting A and B by similarity transformations to
 isolate eigenvalues in the first 1 to ILO$-$1 and last IHI+1 to N
 elements on the diagonal; and second, applying a diagonal similarity
 transformation to rows and columns ILO to IHI to make the rows
 and columns as close in norm as possible. Both steps are optional.
 Balancing may reduce the 1-norm of the matrices, and improve the
 accuracy of the computed eigenvalues and/or eigenvectors in the
 generalized eigenvalue problem A*x = lambda*B*x.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>JOB</i> </p>
<pre> JOB is CHARACTER*1
 Specifies the operations to be performed on A and B:
 = 'N': none: simply set ILO = 1, IHI = N, LSCALE(I) = 1.0
 and RSCALE(I) = 1.0 for i=1,...,N;
 = 'P': permute only;
 = 'S': scale only;
 = 'B': both permute and scale.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrices A and B. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the input matrix A.
 On exit, A is overwritten by the balanced matrix.
 If JOB = 'N', A is not referenced.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB,N)
 On entry, the input matrix B.
 On exit, B is overwritten by the balanced matrix.
 If JOB = 'N', B is not referenced.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>ILO</i> </p>
<pre> ILO is INTEGER</pre>
<p><i>IHI</i> </p>
<pre> IHI is INTEGER
 ILO and IHI are set to integers such that on exit
 A(i,j) = 0 and B(i,j) = 0 if i &gt; j and
 j = 1,...,ILO-1 or i = IHI+1,...,N.
 If JOB = 'N' or 'S', ILO = 1 and IHI = N.</pre>
<p><i>LSCALE</i> </p>
<pre> LSCALE is DOUBLE PRECISION array, dimension (N)
 Details of the permutations and scaling factors applied
 to the left side of A and B. If P(j) is the index of the
 row interchanged with row j, and D(j) is the scaling factor
 applied to row j, then
 LSCALE(j) = P(j) for J = 1,...,ILO-1
 = D(j) for J = ILO,...,IHI
 = P(j) for J = IHI+1,...,N.
 The order in which the interchanges are made is N to IHI+1,
 then 1 to ILO-1.</pre>
<p><i>RSCALE</i> </p>
<pre> RSCALE is DOUBLE PRECISION array, dimension (N)
 Details of the permutations and scaling factors applied
 to the right side of A and B. If P(j) is the index of the
 column interchanged with column j, and D(j) is the scaling
 factor applied to column j, then
 RSCALE(j) = P(j) for J = 1,...,ILO-1
 = D(j) for J = ILO,...,IHI
 = P(j) for J = IHI+1,...,N.
 The order in which the interchanges are made is N to IHI+1,
 then 1 to ILO-1.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (lwork)
 lwork must be at least max(1,6*N) when JOB = 'S' or 'B', and
 at least 1 when JOB = 'N' or 'P'.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
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
<pre> See R.C. WARD, Balancing the generalized eigenvalue problem,
 SIAM J. Sci. Stat. Comp. 2 (1981), 141-152.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 177 of file zggbal.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
