---
title: "dgelsy-f(3)"
name: "dgelsy-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgelsy-f/"
description: "dgelsy.f –"
---

<p>dgelsy.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dgelsy</code> (M, N, NRHS, A, LDA, B, LDB, JPVT, RCOND, RANK, WORK, LWORK, INFO)<br />
 <i></i><code> DGELSY solves overdetermined or underdetermined systems for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgelsy (integerM, integerN, integerNRHS, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldb, * )B, integerLDB, integer, dimension( * )JPVT, double precisionRCOND, integerRANK, double precision, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code> DGELSY solves overdetermined or underdetermined systems for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DGELSY computes the minimum-norm solution to a real linear least
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
 where Q1 consists of the first RANK columns of Q.
 This routine is basically identical to the original xGELSX except
 three differences:
 o The call to the subroutine xGEQPF has been substituted by the
 the call to the subroutine xGEQP3. This subroutine is a Blas-3
 version of the QR factorization with column pivoting.
 o Matrix B (the right hand side) is updated with Blas-3.
 o The permutation of matrix B (the right hand side) is faster and
 more simple.</pre>
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
 On exit, the N-by-NRHS solution matrix X.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,M,N).</pre>
<p><i>JPVT</i> </p>
<pre> JPVT is INTEGER array, dimension (N)
 On entry, if JPVT(i) .ne. 0, the i-th column of A is permuted
 to the front of AP, otherwise column i is a free column.
 On exit, if JPVT(i) = k, then the i-th column of AP
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
<pre> WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK.
 The unblocked strategy requires that:
 LWORK &gt;= MAX( MN+3*N+1, 2*MN+NRHS ),
 where MN = min( M, N ).
 The block algorithm requires that:
 LWORK &gt;= MAX( MN+2*N+NB*(N+1), 2*MN+NB*NRHS ),
 where NB is an upper bound on the blocksize returned
 by ILAENV for the routines DGEQP3, DTZRZF, STZRQF, DORMQR,
 and DORMRZ.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: If INFO = -i, the i-th argument had an illegal value.</pre>
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
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>A. Petitet, Computer Science Dept., Univ. of Tenn., Knoxville, USA </p>
<p>&nbsp;<wbr>E. Quintana-Orti, Depto. de Informatica, Universidad Jaime I, Spain&nbsp;<wbr> </p>
<p>&nbsp;<wbr>G. Quintana-Orti, Depto. de Informatica, Universidad Jaime I, Spain&nbsp;<wbr> </p>
<p>&nbsp;<wbr></dl>
<p> Definition at line 204 of file dgelsy.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
