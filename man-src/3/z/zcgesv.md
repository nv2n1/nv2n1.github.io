---
title: "zcgesv(3)"
name: "zcgesv"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zcgesv/"
description: "zcgesv.f –"
---

<p>zcgesv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<pre><code>subroutine zcgesv (N, NRHS, A, LDA, IPIV, B, LDB, X, LDX, WORK, SWORK, RWORK, ITER, INFO)


ZCGESV computes the solution to system of linear equations A * X = B for GE matrices (mixed precision with iterative refinement)</code></pre>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zcgesv (integerN, integerNRHS, complex*16, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, complex*16, dimension( ldb, * )B, integerLDB, complex*16, dimension( ldx, * )X, integerLDX, complex*16, dimension( n, * )WORK, complex, dimension( * )SWORK, double precision, dimension( * )RWORK, integerITER, integerINFO)</h3>
<p><code> ZCGESV computes the solution to system of linear equations A * X = B for GE matrices</code> (mixed precision with iterative refinement) </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZCGESV computes the solution to a complex system of linear equations
 A * X = B,
 where A is an N-by-N matrix and X and B are N-by-NRHS matrices.
 ZCGESV first attempts to factorize the matrix in COMPLEX and use this
 factorization within an iterative refinement procedure to produce a
 solution with COMPLEX*16 normwise backward error quality (see below).
 If the approach fails the method switches to a COMPLEX*16
 factorization and solve.
 The iterative refinement is not going to be a winning strategy if
 the ratio COMPLEX performance over COMPLEX*16 performance is too
 small. A reasonable strategy should take the number of right-hand
 sides and the size of the matrix into account. This might be done
 with a call to ILAENV in the future. Up to now, we always try
 iterative refinement.
 The iterative refinement process is stopped if
 ITER &gt; ITERMAX
 or for all the RHS we have:
 RNRM &lt; SQRT(N)*XNRM*ANRM*EPS*BWDMAX
 where
 o ITER is the number of the current iteration in the iterative
 refinement process
 o RNRM is the infinity-norm of the residual
 o XNRM is the infinity-norm of the solution
 o ANRM is the infinity-operator-norm of the matrix A
 o EPS is the machine epsilon returned by DLAMCH('Epsilon')
 The value ITERMAX and BWDMAX are fixed to 30 and 1.0D+00
 respectively.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of linear equations, i.e., the order of the
 matrix A. N &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrix B. NRHS &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array,
 dimension (LDA,N)
 On entry, the N-by-N coefficient matrix A.
 On exit, if iterative refinement has been successfully used
 (INFO.EQ.0 and ITER.GE.0, see description below), then A is
 unchanged, if double precision factorization has been used
 (INFO.EQ.0 and ITER.LT.0, see description below), then the
 array A contains the factors L and U from the factorization
 A = P*L*U; the unit diagonal elements of L are not stored.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 The pivot indices that define the permutation matrix P;
 row i of the matrix was interchanged with row IPIV(i).
 Corresponds either to the single precision factorization
 (if INFO.EQ.0 and ITER.GE.0) or the double precision
 factorization (if INFO.EQ.0 and ITER.LT.0).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB,NRHS)
 The N-by-NRHS right hand side matrix B.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX*16 array, dimension (LDX,NRHS)
 If INFO = 0, the N-by-NRHS solution matrix X.</pre>
<p><i>LDX</i> </p>
<pre> LDX is INTEGER
 The leading dimension of the array X. LDX &gt;= max(1,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (N*NRHS)
 This array is used to hold the residual vectors.</pre>
<p><i>SWORK</i> </p>
<pre> SWORK is COMPLEX array, dimension (N*(N+NRHS))
 This array is used to use the single precision matrix and the
 right-hand sides or solutions in single precision.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (N)</pre>
<p><i>ITER</i> </p>
<pre> ITER is INTEGER
 &lt; 0: iterative refinement has failed, COMPLEX*16
 factorization has been performed
 -1 : the routine fell back to full precision for
 implementation- or machine-specific reasons
 -2 : narrowing the precision induced an overflow,
 the routine fell back to full precision
 -3 : failure of CGETRF
 -31: stop the iterative refinement after the 30th
 iterations
 &gt; 0: iterative refinement has been sucessfully used.
 Returns the number of iterations</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, U(i,i) computed in COMPLEX*16 is exactly
 zero. The factorization has been completed, but the
 factor U is exactly singular, so the solution
 could not be computed.</pre>
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
<p> Definition at line 201 of file zcgesv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
