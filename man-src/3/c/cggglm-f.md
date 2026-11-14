---
title: "cggglm-f(3)"
name: "cggglm-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cggglm-f/"
description: "cggglm.f –"
---

<p>cggglm.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cggglm</code> (N, M, P, A, LDA, B, LDB, D, X, Y, WORK, LWORK, INFO)<br />
 <i></i><code> CGGEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cggglm (integerN, integerM, integerP, complex, dimension( lda, * )A, integerLDA, complex, dimension( ldb, * )B, integerLDB, complex, dimension( * )D, complex, dimension( * )X, complex, dimension( * )Y, complex, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code> CGGEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CGGGLM solves a general Gauss-Markov linear model (GLM) problem:
 minimize || y ||_2 subject to d = A*x + B*y
 x
 where A is an N-by-M matrix, B is an N-by-P matrix, and d is a
 given N-vector. It is assumed that M &lt;= N &lt;= M+P, and
 rank(A) = M and rank( A B ) = N.
 Under these assumptions, the constrained equation is always
 consistent, and there is a unique solution x and a minimal 2-norm
 solution y, which is obtained using a generalized QR factorization
 of the matrices (A, B) given by
 A = Q*(R), B = Q*T*Z.
 (0)
 In particular, if matrix B is square nonsingular, then the problem
 GLM is equivalent to the following weighted linear least squares
 problem
 minimize || inv(B)*(d-A*x) ||_2
 x
 where inv(B) denotes the inverse of B.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of rows of the matrices A and B. N &gt;= 0.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of columns of the matrix A. 0 &lt;= M &lt;= N.</pre>
<p><i>P</i> </p>
<pre> P is INTEGER
 The number of columns of the matrix B. P &gt;= N-M.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX array, dimension (LDA,M)
 On entry, the N-by-M matrix A.
 On exit, the upper triangular part of the array A contains
 the M-by-M upper triangular matrix R.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX array, dimension (LDB,P)
 On entry, the N-by-P matrix B.
 On exit, if N &lt;= P, the upper triangle of the subarray
 B(1:N,P-N+1:P) contains the N-by-N upper triangular matrix T;
 if N &gt; P, the elements on and above the (N-P)th subdiagonal
 contain the N-by-P upper trapezoidal matrix T.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>D</i> </p>
<pre> D is COMPLEX array, dimension (N)
 On entry, D is the left hand side of the GLM equation.
 On exit, D is destroyed.</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX array, dimension (M)</pre>
<p><i>Y</i> </p>
<pre> Y is COMPLEX array, dimension (P)
 On exit, X and Y are the solutions of the GLM problem.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= max(1,N+M+P).
 For optimum performance, LWORK &gt;= M+min(N,P)+max(N,P)*NB,
 where NB is an upper bound for the optimal blocksizes for
 CGEQRF, CGERQF, CUNMQR and CUNMRQ.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 = 1: the upper triangular factor R associated with A in the
 generalized QR factorization of the pair (A, B) is
 singular, so that rank(A) &lt; M; the least squares
 solution could not be computed.
 = 2: the bottom (N-M) by (N-M) part of the upper trapezoidal
 factor T associated with B in the generalized QR
 factorization of the pair (A, B) is singular, so that
 rank( A B ) &lt; N; the least squares solution could not
 be computed.</pre>
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
<p> Definition at line 185 of file cggglm.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
