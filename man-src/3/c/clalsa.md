---
title: "clalsa(3)"
name: "clalsa"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clalsa/"
description: "clalsa.f –"
---

<h2 class="name">NAME</h2>
<p> clalsa.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>clalsa</code> (ICOMPQ, SMLSIZ, N, NRHS, B, LDB, BX, LDBX, U, LDU, VT, K, DIFL, DIFR, Z, POLES, GIVPTR, GIVCOL, LDGCOL, PERM, GIVNUM, C, S, RWORK, IWORK, INFO)<br />
 <i></i><code>CLALSA</code> computes the SVD of the coefficient matrix in compact form. Used by sgelsd.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clalsa (integerICOMPQ, integerSMLSIZ, integerN, integerNRHS, complex, dimension( ldb, * )B, integerLDB, complex, dimension( ldbx, * )BX, integerLDBX, real, dimension( ldu, * )U, integerLDU, real, dimension( ldu, * )VT, integer, dimension( * )K, real, dimension( ldu, * )DIFL, real, dimension( ldu, * )DIFR, real, dimension( ldu, * )Z, real, dimension( ldu, * )POLES, integer, dimension( * )GIVPTR, integer, dimension( ldgcol, * )GIVCOL, integerLDGCOL, integer, dimension( ldgcol, * )PERM, real, dimension( ldu, * )GIVNUM, real, dimension( * )C, real, dimension( * )S, real, dimension( * )RWORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>CLALSA</code> computes the SVD of the coefficient matrix in compact form. Used by sgelsd. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLALSA is an itermediate step in solving the least squares problem
 by computing the SVD of the coefficient matrix in compact form (The
 singular vectors are computed as products of simple orthorgonal
 matrices.).
 If ICOMPQ = 0, CLALSA applies the inverse of the left singular vector
 matrix of an upper bidiagonal matrix to the right hand side; and if
 ICOMPQ = 1, CLALSA applies the right singular vector matrix to the
 right hand side. The singular vector matrices were generated in
 compact form by CLALSA.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ICOMPQ</i> </p>
<pre>
          ICOMPQ is INTEGER
         Specifies whether the left or the right singular vector
         matrix is involved.
         = 0: Left singular vector matrix
         = 1: Right singular vector matrix
</pre>
<p> <i>SMLSIZ</i> </p>
<pre>
          SMLSIZ is INTEGER
         The maximum size of the subproblems at the bottom of the
         computation tree.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
         The row and column dimensions of the upper bidiagonal matrix.
</pre>
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
         The number of columns of B and BX. NRHS must be at least 1.
</pre>
<p> <i>B</i> </p>
<pre>
          B is COMPLEX array, dimension ( LDB, NRHS )
         On input, B contains the right hand sides of the least
         squares problem in rows 1 through M.
         On output, B contains the solution X in rows 1 through N.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
         The leading dimension of B in the calling subprogram.
         LDB must be at least max(1,MAX( M, N ) ).
</pre>
<p> <i>BX</i> </p>
<pre>
          BX is COMPLEX array, dimension ( LDBX, NRHS )
         On exit, the result of applying the left or right singular
         vector matrix to B.
</pre>
<p> <i>LDBX</i> </p>
<pre>
          LDBX is INTEGER
         The leading dimension of BX.
</pre>
<p> <i>U</i> </p>
<pre>
          U is REAL array, dimension ( LDU, SMLSIZ ).
         On entry, U contains the left singular vector matrices of all
         subproblems at the bottom level.
</pre>
<p> <i>LDU</i> </p>
<pre>
          LDU is INTEGER, LDU = &gt; N.
         The leading dimension of arrays U, VT, DIFL, DIFR,
         POLES, GIVNUM, and Z.
</pre>
<p> <i>VT</i> </p>
<pre>
          VT is REAL array, dimension ( LDU, SMLSIZ+1 ).
         On entry, VT**H contains the right singular vector matrices of
         all subproblems at the bottom level.
</pre>
<p> <i>K</i> </p>
<pre>
          K is INTEGER array, dimension ( N ).
</pre>
<p> <i>DIFL</i> </p>
<pre>
          DIFL is REAL array, dimension ( LDU, NLVL ).
         where NLVL = INT(log_2 (N/(SMLSIZ+1))) + 1.
</pre>
<p> <i>DIFR</i> </p>
<pre>
          DIFR is REAL array, dimension ( LDU, 2 * NLVL ).
         On entry, DIFL(*, I) and DIFR(*, 2 * I -1) record
         distances between singular values on the I-th level and
         singular values on the (I -1)-th level, and DIFR(*, 2 * I)
         record the normalizing factors of the right singular vectors
         matrices of subproblems on I-th level.
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is REAL array, dimension ( LDU, NLVL ).
         On entry, Z(1, I) contains the components of the deflation-
         adjusted updating row vector for subproblems on the I-th
         level.
</pre>
<p> <i>POLES</i> </p>
<pre>
          POLES is REAL array, dimension ( LDU, 2 * NLVL ).
         On entry, POLES(*, 2 * I -1: 2 * I) contains the new and old
         singular values involved in the secular equations on the I-th
         level.
</pre>
<p> <i>GIVPTR</i> </p>
<pre>
          GIVPTR is INTEGER array, dimension ( N ).
         On entry, GIVPTR( I ) records the number of Givens
         rotations performed on the I-th problem on the computation
         tree.
</pre>
<p> <i>GIVCOL</i> </p>
<pre>
          GIVCOL is INTEGER array, dimension ( LDGCOL, 2 * NLVL ).
         On entry, for each I, GIVCOL(*, 2 * I - 1: 2 * I) records the
         locations of Givens rotations performed on the I-th level on
         the computation tree.
</pre>
<p> <i>LDGCOL</i> </p>
<pre>
          LDGCOL is INTEGER, LDGCOL = &gt; N.
         The leading dimension of arrays GIVCOL and PERM.
</pre>
<p> <i>PERM</i> </p>
<pre>
          PERM is INTEGER array, dimension ( LDGCOL, NLVL ).
         On entry, PERM(*, I) records permutations done on the I-th
         level of the computation tree.
</pre>
<p> <i>GIVNUM</i> </p>
<pre>
          GIVNUM is REAL array, dimension ( LDU, 2 * NLVL ).
         On entry, GIVNUM(*, 2 *I -1 : 2 * I) records the C- and S-
         values of Givens rotations performed on the I-th level on the
         computation tree.
</pre>
<p> <i>C</i> </p>
<pre>
          C is REAL array, dimension ( N ).
         On entry, if the I-th subproblem is not square,
         C( I ) contains the C-value of a Givens rotation related to
         the right null space of the I-th subproblem.
</pre>
<p> <i>S</i> </p>
<pre>
          S is REAL array, dimension ( N ).
         On entry, if the I-th subproblem is not square,
         S( I ) contains the S-value of a Givens rotation related to
         the right null space of the I-th subproblem.
</pre>
<p> <i>RWORK</i> </p>
<pre>
          RWORK is REAL array, dimension at least
         MAX( (SMLSZ+1)*NRHS*3, N*(1+NRHS) + 2*NRHS ).
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array.
         The dimension must be at least 3 * N
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit.
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
<dd> September 2012</dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Ming Gu and Ren-Cang Li, Computer Science Division, University of California at Berkeley, USA </p>
<p>&nbsp;<wbr>Osni Marques, LBNL/NERSC, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr></dl>
<p> Definition at line 266 of file clalsa.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
