---
title: "slasda(3)"
name: "slasda"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slasda/"
description: "slasda.f –"
---

<h2 class="name">NAME</h2>
<p> slasda.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slasda</code> (ICOMPQ, SMLSIZ, N, SQRE, D, E, U, LDU, VT, K, DIFL, DIFR, Z, POLES, GIVPTR, GIVCOL, LDGCOL, PERM, GIVNUM, C, S, WORK, IWORK, INFO)<br />
 <i></i><code>SLASDA</code> computes the singular value decomposition (SVD) of a real upper bidiagonal matrix with diagonal d and off-diagonal e. Used by sbdsdc.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slasda (integerICOMPQ, integerSMLSIZ, integerN, integerSQRE, real, dimension( * )D, real, dimension( * )E, real, dimension( ldu, * )U, integerLDU, real, dimension( ldu, * )VT, integer, dimension( * )K, real, dimension( ldu, * )DIFL, real, dimension( ldu, * )DIFR, real, dimension( ldu, * )Z, real, dimension( ldu, * )POLES, integer, dimension( * )GIVPTR, integer, dimension( ldgcol, * )GIVCOL, integerLDGCOL, integer, dimension( ldgcol, * )PERM, real, dimension( ldu, * )GIVNUM, real, dimension( * )C, real, dimension( * )S, real, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>SLASDA</code> computes the singular value decomposition (SVD) of a real upper bidiagonal matrix with diagonal d and off-diagonal e. Used by sbdsdc. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 Using a divide and conquer approach, SLASDA computes the singular
 value decomposition (SVD) of a real upper bidiagonal N-by-M matrix
 B with diagonal D and offdiagonal E, where M = N + SQRE. The
 algorithm computes the singular values in the SVD B = U * S * VT.
 The orthogonal matrices U and VT are optionally computed in
 compact form.
 A related subroutine, SLASD0, computes the singular values and
 the singular vectors in explicit form.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ICOMPQ</i> </p>
<pre>
          ICOMPQ is INTEGER
         Specifies whether singular vectors are to be computed
         in compact form, as follows
         = 0: Compute singular values only.
         = 1: Compute singular vectors of upper bidiagonal
              matrix in compact form.
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
         The row dimension of the upper bidiagonal matrix. This is
         also the dimension of the main diagonal array D.
</pre>
<p> <i>SQRE</i> </p>
<pre>
          SQRE is INTEGER
         Specifies the column dimension of the bidiagonal matrix.
         = 0: The bidiagonal matrix has column dimension M = N;
         = 1: The bidiagonal matrix has column dimension M = N + 1.
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension ( N )
         On entry D contains the main diagonal of the bidiagonal
         matrix. On exit D, if INFO = 0, contains its singular values.
</pre>
<p> <i>E</i> </p>
<pre>
          E is REAL array, dimension ( M-1 )
         Contains the subdiagonal entries of the bidiagonal matrix.
         On exit, E has been destroyed.
</pre>
<p> <i>U</i> </p>
<pre>
          U is REAL array,
         dimension ( LDU, SMLSIZ ) if ICOMPQ = 1, and not referenced
         if ICOMPQ = 0. If ICOMPQ = 1, on exit, U contains the left
         singular vector matrices of all subproblems at the bottom
         level.
</pre>
<p> <i>LDU</i> </p>
<pre>
          LDU is INTEGER, LDU = &gt; N.
         The leading dimension of arrays U, VT, DIFL, DIFR, POLES,
         GIVNUM, and Z.
</pre>
<p> <i>VT</i> </p>
<pre>
          VT is REAL array,
         dimension ( LDU, SMLSIZ+1 ) if ICOMPQ = 1, and not referenced
         if ICOMPQ = 0. If ICOMPQ = 1, on exit, VT**T contains the right
         singular vector matrices of all subproblems at the bottom
         level.
</pre>
<p> <i>K</i> </p>
<pre>
          K is INTEGER array, dimension ( N )
         if ICOMPQ = 1 and dimension 1 if ICOMPQ = 0.
         If ICOMPQ = 1, on exit, K(I) is the dimension of the I-th
         secular equation on the computation tree.
</pre>
<p> <i>DIFL</i> </p>
<pre>
          DIFL is REAL array, dimension ( LDU, NLVL ),
         where NLVL = floor(log_2 (N/SMLSIZ))).
</pre>
<p> <i>DIFR</i> </p>
<pre><code>
          DIFR is REAL array,
                  dimension ( LDU, 2 * NLVL ) if ICOMPQ = 1 and
                  dimension ( N ) if ICOMPQ = 0.
         If ICOMPQ = 1, on exit, DIFL(1:N, I) and DIFR(1:N, 2 * I - 1)
         record distances between singular values on the I-th
         level and singular values on the (I -1)-th level, and
         DIFR(1:N, 2 * I ) contains the normalizing factors for
         the right singular vector matrix. See SLASD8 for details.
</code></pre>
<p> <i>Z</i> </p>
<pre>
          Z is REAL array,
                  dimension ( LDU, NLVL ) if ICOMPQ = 1 and
                  dimension ( N ) if ICOMPQ = 0.
         The first K elements of Z(1, I) contain the components of
         the deflation-adjusted updating row vector for subproblems
         on the I-th level.
</pre>
<p> <i>POLES</i> </p>
<pre>
          POLES is REAL array,
         dimension ( LDU, 2 * NLVL ) if ICOMPQ = 1, and not referenced
         if ICOMPQ = 0. If ICOMPQ = 1, on exit, POLES(1, 2*I - 1) and
         POLES(1, 2*I) contain  the new and old singular values
         involved in the secular equations on the I-th level.
</pre>
<p> <i>GIVPTR</i> </p>
<pre>
          GIVPTR is INTEGER array,
         dimension ( N ) if ICOMPQ = 1, and not referenced if
         ICOMPQ = 0. If ICOMPQ = 1, on exit, GIVPTR( I ) records
         the number of Givens rotations performed on the I-th
         problem on the computation tree.
</pre>
<p> <i>GIVCOL</i> </p>
<pre>
          GIVCOL is INTEGER array,
         dimension ( LDGCOL, 2 * NLVL ) if ICOMPQ = 1, and not
         referenced if ICOMPQ = 0. If ICOMPQ = 1, on exit, for each I,
         GIVCOL(1, 2 *I - 1) and GIVCOL(1, 2 *I) record the locations
         of Givens rotations performed on the I-th level on the
         computation tree.
</pre>
<p> <i>LDGCOL</i> </p>
<pre>
          LDGCOL is INTEGER, LDGCOL = &gt; N.
         The leading dimension of arrays GIVCOL and PERM.
</pre>
<p> <i>PERM</i> </p>
<pre>
          PERM is INTEGER array, dimension ( LDGCOL, NLVL )
         if ICOMPQ = 1, and not referenced
         if ICOMPQ = 0. If ICOMPQ = 1, on exit, PERM(1, I) records
         permutations done on the I-th level of the computation tree.
</pre>
<p> <i>GIVNUM</i> </p>
<pre>
          GIVNUM is REAL array,
         dimension ( LDU,  2 * NLVL ) if ICOMPQ = 1, and not
         referenced if ICOMPQ = 0. If ICOMPQ = 1, on exit, for each I,
         GIVNUM(1, 2 *I - 1) and GIVNUM(1, 2 *I) record the C- and S-
         values of Givens rotations performed on the I-th level on
         the computation tree.
</pre>
<p> <i>C</i> </p>
<pre>
          C is REAL array,
         dimension ( N ) if ICOMPQ = 1, and dimension 1 if ICOMPQ = 0.
         If ICOMPQ = 1 and the I-th subproblem is not square, on exit,
         C( I ) contains the C-value of a Givens rotation related to
         the right null space of the I-th subproblem.
</pre>
<p> <i>S</i> </p>
<pre>
          S is REAL array, dimension ( N ) if
         ICOMPQ = 1, and dimension 1 if ICOMPQ = 0. If ICOMPQ = 1
         and the I-th subproblem is not square, on exit, S( I )
         contains the S-value of a Givens rotation related to
         the right null space of the I-th subproblem.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension
         (6 * N + (SMLSIZ + 1)*(SMLSIZ + 1)).
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (7*N).
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit.
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
          &gt; 0:  if INFO = 1, a singular value did not converge
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
<dd> Ming Gu and Huan Ren, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 272 of file slasda.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
