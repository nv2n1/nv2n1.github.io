---
title: "dlals0-f(3)"
name: "dlals0-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlals0-f/"
description: "dlals0.f –"
---

<p>dlals0.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlals0</code> (ICOMPQ, NL, NR, SQRE, NRHS, B, LDB, BX, LDBX, PERM, GIVPTR, GIVCOL, LDGCOL, GIVNUM, LDGNUM, POLES, DIFL, DIFR, Z, K, C, S, WORK, INFO)<br />
 <i></i><code>DLALS0</code> applies back multiplying factors in solving the least squares problem using divide and conquer SVD approach. Used by sgelsd.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlals0 (integerICOMPQ, integerNL, integerNR, integerSQRE, integerNRHS, double precision, dimension( ldb, * )B, integerLDB, double precision, dimension( ldbx, * )BX, integerLDBX, integer, dimension( * )PERM, integerGIVPTR, integer, dimension( ldgcol, * )GIVCOL, integerLDGCOL, double precision, dimension( ldgnum, * )GIVNUM, integerLDGNUM, double precision, dimension( ldgnum, * )POLES, double precision, dimension( * )DIFL, double precision, dimension( ldgnum, * )DIFR, double precision, dimension( * )Z, integerK, double precisionC, double precisionS, double precision, dimension( * )WORK, integerINFO)</h3>
<p><code>DLALS0</code> applies back multiplying factors in solving the least squares problem using divide and conquer SVD approach. Used by sgelsd. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLALS0 applies back the multiplying factors of either the left or the
 right singular vector matrix of a diagonal matrix appended by a row
 to the right hand side matrix B in solving the least squares problem
 using the divide-and-conquer SVD approach.
 For the left singular vector matrix, three types of orthogonal
 matrices are involved:
 (1L) Givens rotations: the number of such rotations is GIVPTR; the
 pairs of columns/rows they were applied to are stored in GIVCOL;
 and the C- and S-values of these rotations are stored in GIVNUM.
 (2L) Permutation. The (NL+1)-st row of B is to be moved to the first
 row, and for J=2:N, PERM(J)-th row of B is to be moved to the
 J-th row.
 (3L) The left singular vector matrix of the remaining matrix.
 For the right singular vector matrix, four types of orthogonal
 matrices are involved:
 (1R) The right singular vector matrix of the remaining matrix.
 (2R) If SQRE = 1, one extra Givens rotation to generate the right
 null space.
 (3R) The inverse transformation of (2L).
 (4R) The inverse transformation of (1L).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ICOMPQ</i> </p>
<pre> ICOMPQ is INTEGER
 Specifies whether singular vectors are to be computed in
 factored form:
 = 0: Left singular vector matrix.
 = 1: Right singular vector matrix.</pre>
<p><i>NL</i> </p>
<pre> NL is INTEGER
 The row dimension of the upper block. NL &gt;= 1.</pre>
<p><i>NR</i> </p>
<pre> NR is INTEGER
 The row dimension of the lower block. NR &gt;= 1.</pre>
<p><i>SQRE</i> </p>
<pre> SQRE is INTEGER
 = 0: the lower block is an NR-by-NR square matrix.
 = 1: the lower block is an NR-by-(NR+1) rectangular matrix.
 The bidiagonal matrix has row dimension N = NL + NR + 1,
 and column dimension M = N + SQRE.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of columns of B and BX. NRHS must be at least 1.</pre>
<p><i>B</i> </p>
<pre> B is DOUBLE PRECISION array, dimension ( LDB, NRHS )
 On input, B contains the right hand sides of the least
 squares problem in rows 1 through M. On output, B contains
 the solution X in rows 1 through N.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of B. LDB must be at least
 max(1,MAX( M, N ) ).</pre>
<p><i>BX</i> </p>
<pre> BX is DOUBLE PRECISION array, dimension ( LDBX, NRHS )</pre>
<p><i>LDBX</i> </p>
<pre> LDBX is INTEGER
 The leading dimension of BX.</pre>
<p><i>PERM</i> </p>
<pre> PERM is INTEGER array, dimension ( N )
 The permutations (from deflation and sorting) applied
 to the two blocks.</pre>
<p><i>GIVPTR</i> </p>
<pre> GIVPTR is INTEGER
 The number of Givens rotations which took place in this
 subproblem.</pre>
<p><i>GIVCOL</i> </p>
<pre> GIVCOL is INTEGER array, dimension ( LDGCOL, 2 )
 Each pair of numbers indicates a pair of rows/columns
 involved in a Givens rotation.</pre>
<p><i>LDGCOL</i> </p>
<pre> LDGCOL is INTEGER
 The leading dimension of GIVCOL, must be at least N.</pre>
<p><i>GIVNUM</i> </p>
<pre> GIVNUM is DOUBLE PRECISION array, dimension ( LDGNUM, 2 )
 Each number indicates the C or S value used in the
 corresponding Givens rotation.</pre>
<p><i>LDGNUM</i> </p>
<pre> LDGNUM is INTEGER
 The leading dimension of arrays DIFR, POLES and
 GIVNUM, must be at least K.</pre>
<p><i>POLES</i> </p>
<pre> POLES is DOUBLE PRECISION array, dimension ( LDGNUM, 2 )
 On entry, POLES(1:K, 1) contains the new singular
 values obtained from solving the secular equation, and
 POLES(1:K, 2) is an array containing the poles in the secular
 equation.</pre>
<p><i>DIFL</i> </p>
<pre> DIFL is DOUBLE PRECISION array, dimension ( K ).
 On entry, DIFL(I) is the distance between I-th updated
 (undeflated) singular value and the I-th (undeflated) old
 singular value.</pre>
<p><i>DIFR</i> </p>
<pre> DIFR is DOUBLE PRECISION array, dimension ( LDGNUM, 2 ).
 On entry, DIFR(I, 1) contains the distances between I-th
 updated (undeflated) singular value and the I+1-th
 (undeflated) old singular value. And DIFR(I, 2) is the
 normalizing factor for the I-th right singular vector.</pre>
<p><i>Z</i> </p>
<pre> Z is DOUBLE PRECISION array, dimension ( K )
 Contain the components of the deflation-adjusted updating row
 vector.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER
 Contains the dimension of the non-deflated matrix,
 This is the order of the related secular equation. 1 &lt;= K &lt;=N.</pre>
<p><i>C</i> </p>
<pre> C is DOUBLE PRECISION
 C contains garbage if SQRE =0 and the C-value of a Givens
 rotation related to the right null space if SQRE = 1.</pre>
<p><i>S</i> </p>
<pre> S is DOUBLE PRECISION
 S contains garbage if SQRE =0 and the S-value of a Givens
 rotation related to the right null space if SQRE = 1.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension ( K )</pre>
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
<dd>September 2012</dl>
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>Ming Gu and Ren-Cang Li, Computer Science Division, University of California at Berkeley, USA </p>
<p>&nbsp;<wbr>Osni Marques, LBNL/NERSC, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr></dl>
<p> Definition at line 267 of file dlals0.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
