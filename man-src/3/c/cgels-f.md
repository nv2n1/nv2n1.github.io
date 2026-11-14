---
title: "cgels-f(3)"
name: "cgels-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgels-f/"
description: "cgels.f –"
---

<p>cgels.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cgels</code> (TRANS, M, N, NRHS, A, LDA, B, LDB, WORK, LWORK, INFO)<br />
 <i></i><code> CGELS solves overdetermined or underdetermined systems for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgels (characterTRANS, integerM, integerN, integerNRHS, complex, dimension( lda, * )A, integerLDA, complex, dimension( ldb, * )B, integerLDB, complex, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code> CGELS solves overdetermined or underdetermined systems for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CGELS solves overdetermined or underdetermined complex linear systems
 involving an M-by-N matrix A, or its conjugate-transpose, using a QR
 or LQ factorization of A. It is assumed that A has full rank.
 The following options are provided:
 1. If TRANS = 'N' and m &gt;= n: find the least squares solution of
 an overdetermined system, i.e., solve the least squares problem
 minimize || B - A*X ||.
 2. If TRANS = 'N' and m &lt; n: find the minimum norm solution of
 an underdetermined system A * X = B.
 3. If TRANS = 'C' and m &gt;= n: find the minimum norm solution of
 an undetermined system A**H * X = B.
 4. If TRANS = 'C' and m &lt; n: find the least squares solution of
 an overdetermined system, i.e., solve the least squares problem
 minimize || B - A**H * X ||.
 Several right hand side vectors b and solution vectors x can be
 handled in a single call; they are stored as the columns of the
 M-by-NRHS right hand side matrix B and the N-by-NRHS solution
 matrix X.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 = 'N': the linear system involves A;
 = 'C': the linear system involves A**H.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of right hand sides, i.e., the number of
 columns of the matrices B and X. NRHS &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX array, dimension (LDA,N)
 On entry, the M-by-N matrix A.
 if M &gt;= N, A is overwritten by details of its QR
 factorization as returned by CGEQRF;
 if M &lt; N, A is overwritten by details of its LQ
 factorization as returned by CGELQF.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX array, dimension (LDB,NRHS)
 On entry, the matrix B of right hand side vectors, stored
 columnwise; B is M-by-NRHS if TRANS = 'N', or N-by-NRHS
 if TRANS = 'C'.
 On exit, if INFO = 0, B is overwritten by the solution
 vectors, stored columnwise:
 if TRANS = 'N' and m &gt;= n, rows 1 to n of B contain the least
 squares solution vectors; the residual sum of squares for the
 solution in each column is given by the sum of squares of the
 modulus of elements N+1 to M in that column;
 if TRANS = 'N' and m &lt; n, rows 1 to N of B contain the
 minimum norm solution vectors;
 if TRANS = 'C' and m &gt;= n, rows 1 to M of B contain the
 minimum norm solution vectors;
 if TRANS = 'C' and m &lt; n, rows 1 to M of B contain the
 least squares solution vectors; the residual sum of squares
 for the solution in each column is given by the sum of
 squares of the modulus of elements M+1 to N in that column.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= MAX(1,M,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK.
 LWORK &gt;= max( 1, MN + max( MN, NRHS ) ).
 For optimal performance,
 LWORK &gt;= max( 1, MN + max( MN, NRHS )*NB ).
 where MN = min(M,N) and NB is the optimum block size.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, the i-th diagonal element of the
 triangular factor of A is zero, so that A does not have
 full rank; the least squares solution could not be
 computed.</pre>
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
<p> Definition at line 182 of file cgels.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
