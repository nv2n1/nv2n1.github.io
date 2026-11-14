---
title: "dgelsx-f(3)"
name: "dgelsx-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgelsx-f/"
description: "dgelsx.f –"
---

<p>dgelsx.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dgelsx</code> (M, N, NRHS, A, LDA, B, LDB, JPVT, RCOND, RANK, WORK, INFO)<br />
 <i></i><code> DGELSX solves overdetermined or underdetermined systems for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgelsx (integerM, integerN, integerNRHS, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldb, * )B, integerLDB, integer, dimension( * )JPVT, double precisionRCOND, integerRANK, double precision, dimension( * )WORK, integerINFO)</h3>
<p><code> DGELSX solves overdetermined or underdetermined systems for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> This routine is deprecated and has been replaced by routine DGELSY.
 DGELSX computes the minimum-norm solution to a real linear least
 squares problem:
 minimize || A * X - B ||
 using a complete orthogonal factorization of A. A is an M-by-N
 matrix which may be rank-deficient.
 Several right hand side vectors b and solution vectors x can be
 handled in a single call; they are stored as the columns of the
 M-by-NRHS right hand side matrix B and the N-by-NRHS solution
 matrix X.
 The routine first computes a QR factorization with column pivoting:
 A * P = Q * [ R11 R12 ]
 [ 0 R22 ]
 with R11 defined as the largest leading submatrix whose estimated
 condition number is less than 1/RCOND. The order of R11, RANK,
 is the effective rank of A.
 Then, R22 is considered to be negligible, and R12 is annihilated
 by orthogonal transformations from the right, arriving at the
 complete orthogonal factorization:
 A * P = Q * [ T11 0 ] * Z
 [ 0 0 ]
 The minimum-norm solution is then
 X = P * Z**T [ inv(T11)*Q1**T*B ]
 [ 0 ]
 where Q1 consists of the first RANK columns of Q.</pre>
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
 The number of right hand sides, i.e., the number of
 columns of matrices B and X. NRHS &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA,N)
 On entry, the M-by-N matrix A.
 On exit, A has been overwritten by details of its
 complete orthogonal factorization.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>B</i> </p>
<pre> B is DOUBLE PRECISION array, dimension (LDB,NRHS)
 On entry, the M-by-NRHS right hand side matrix B.
 On exit, the N-by-NRHS solution matrix X.
 If m &gt;= n and RANK = n, the residual sum-of-squares for
 the solution in the i-th column is given by the sum of
 squares of elements N+1:M in that column.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,M,N).</pre>
<p><i>JPVT</i> </p>
<pre> JPVT is INTEGER array, dimension (N)
 On entry, if JPVT(i) .ne. 0, the i-th column of A is an
 initial column, otherwise it is a free column. Before
 the QR factorization of A, all initial columns are
 permuted to the leading positions; only the remaining
 free columns are moved as a result of column pivoting
 during the factorization.
 On exit, if JPVT(i) = k, then the i-th column of A*P
 was the k-th column of A.</pre>
<p><i>RCOND</i> </p>
<pre> RCOND is DOUBLE PRECISION
 RCOND is used to determine the effective rank of A, which
 is defined as the order of the largest leading triangular
 submatrix R11 in the QR factorization with pivoting of A,
 whose estimated condition number &lt; 1/RCOND.</pre>
<p><i>RANK</i> </p>
<pre> RANK is INTEGER
 The effective rank of A, i.e., the order of the submatrix
 R11. This is the same as the order of the submatrix T11
 in the complete orthogonal factorization of A.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension
 (max( min(M,N)+3*N, 2*min(M,N)+NRHS )),</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
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
<p> Definition at line 178 of file dgelsx.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
