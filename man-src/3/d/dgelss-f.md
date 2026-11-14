---
title: "dgelss-f(3)"
name: "dgelss-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgelss-f/"
description: "dgelss.f –"
---

<p>dgelss.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dgelss</code> (M, N, NRHS, A, LDA, B, LDB, S, RCOND, RANK, WORK, LWORK, INFO)<br />
 <i></i><code> DGELSS solves overdetermined or underdetermined systems for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgelss (integerM, integerN, integerNRHS, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldb, * )B, integerLDB, double precision, dimension( * )S, double precisionRCOND, integerRANK, double precision, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code> DGELSS solves overdetermined or underdetermined systems for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DGELSS computes the minimum norm solution to a real linear least
 squares problem:
 Minimize 2-norm(| b - A*x |).
 using the singular value decomposition (SVD) of A. A is an M-by-N
 matrix which may be rank-deficient.
 Several right hand side vectors b and solution vectors x can be
 handled in a single call; they are stored as the columns of the
 M-by-NRHS right hand side matrix B and the N-by-NRHS solution matrix
 X.
 The effective rank of A is determined by treating as zero those
 singular values which are less than RCOND times the largest singular
 value.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of columns
 of the matrices B and X. NRHS &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA,N)
 On entry, the M-by-N matrix A.
 On exit, the first min(m,n) rows of A are overwritten with
 its right singular vectors, stored rowwise.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>B</i> </p>
<pre> B is DOUBLE PRECISION array, dimension (LDB,NRHS)
 On entry, the M-by-NRHS right hand side matrix B.
 On exit, B is overwritten by the N-by-NRHS solution
 matrix X. If m &gt;= n and RANK = n, the residual
 sum-of-squares for the solution in the i-th column is given
 by the sum of squares of elements n+1:m in that column.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,max(M,N)).</pre>
<p><i>S</i> </p>
<pre> S is DOUBLE PRECISION array, dimension (min(M,N))
 The singular values of A in decreasing order.
 The condition number of A in the 2-norm = <a href="//www.systutorials.com/docs/linux/man/1-S/">S</a>(1)/S(min(m,n)).</pre>
<p><i>RCOND</i> </p>
<pre> RCOND is DOUBLE PRECISION
 RCOND is used to determine the effective rank of A.
 Singular values S(i) &lt;= RCOND*<a href="//www.systutorials.com/docs/linux/man/1-S/">S</a>(1) are treated as zero.
 If RCOND &lt; 0, machine precision is used instead.</pre>
<p><i>RANK</i> </p>
<pre> RANK is INTEGER
 The effective rank of A, i.e., the number of singular values
 which are greater than RCOND*<a href="//www.systutorials.com/docs/linux/man/1-S/">S</a>(1).</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= 1, and also:
 LWORK &gt;= 3*min(M,N) + max( 2*min(M,N), max(M,N), NRHS )
 For good performance, LWORK should generally be larger.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: the algorithm for computing the SVD failed to converge;
 if INFO = i, i off-diagonal elements of an intermediate
 bidiagonal form did not converge to zero.</pre>
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
<p> Definition at line 172 of file dgelss.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
