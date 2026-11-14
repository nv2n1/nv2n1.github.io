---
title: "claed7-f(3)"
name: "claed7-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-claed7-f/"
description: "claed7.f –"
---

<p>claed7.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>claed7</code> (N, CUTPNT, QSIZ, TLVLS, CURLVL, CURPBM, D, Q, LDQ, RHO, INDXQ, QSTORE, QPTR, PRMPTR, PERM, GIVPTR, GIVCOL, GIVNUM, WORK, RWORK, IWORK, INFO)<br />
 <i></i><code>CLAED7</code> used by sstedc. Computes the updated eigensystem of a diagonal matrix after modification by a rank-one symmetric matrix. Used when the original matrix is dense.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine claed7 (integerN, integerCUTPNT, integerQSIZ, integerTLVLS, integerCURLVL, integerCURPBM, real, dimension( * )D, complex, dimension( ldq, * )Q, integerLDQ, realRHO, integer, dimension( * )INDXQ, real, dimension( * )QSTORE, integer, dimension( * )QPTR, integer, dimension( * )PRMPTR, integer, dimension( * )PERM, integer, dimension( * )GIVPTR, integer, dimension( 2, * )GIVCOL, real, dimension( 2, * )GIVNUM, complex, dimension( * )WORK, real, dimension( * )RWORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p><code>CLAED7</code> used by sstedc. Computes the updated eigensystem of a diagonal matrix after modification by a rank-one symmetric matrix. Used when the original matrix is dense. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CLAED7 computes the updated eigensystem of a diagonal
 matrix after modification by a rank-one symmetric matrix. This
 routine is used only for the eigenproblem which requires all
 eigenvalues and optionally eigenvectors of a dense or banded
 Hermitian matrix that has been reduced to tridiagonal form.
 T = Q(in) ( D(in) + RHO * Z*Z**H ) Q**H(in) = Q(out) * D(out) * Q**H(out)
 where Z = Q**Hu, u is a vector of length N with ones in the
 CUTPNT and CUTPNT + 1 th elements and zeros elsewhere.
 The eigenvectors of the original matrix are stored in Q, and the
 eigenvalues are in D. The algorithm consists of three stages:
 The first stage consists of deflating the size of the problem
 when there are multiple eigenvalues or if there is a zero in
 the Z vector. For each such occurence the dimension of the
 secular equation problem is reduced by one. This stage is
 performed by the routine SLAED2.
 The second stage consists of calculating the updated
 eigenvalues. This is done by finding the roots of the secular
 equation via the routine SLAED4 (as called by SLAED3).
 This routine also calculates the eigenvectors of the current
 problem.
 The final stage consists of computing the updated eigenvectors
 directly using the updated eigenvalues. The eigenvectors for
 the current problem are multiplied with the eigenvectors from
 the overall problem.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The dimension of the symmetric tridiagonal matrix. N &gt;= 0.</pre>
<p><i>CUTPNT</i> </p>
<pre> CUTPNT is INTEGER
 Contains the location of the last eigenvalue in the leading
 sub-matrix. min(1,N) &lt;= CUTPNT &lt;= N.</pre>
<p><i>QSIZ</i> </p>
<pre> QSIZ is INTEGER
 The dimension of the unitary matrix used to reduce
 the full matrix to tridiagonal form. QSIZ &gt;= N.</pre>
<p><i>TLVLS</i> </p>
<pre> TLVLS is INTEGER
 The total number of merging levels in the overall divide and
 conquer tree.</pre>
<p><i>CURLVL</i> </p>
<pre> CURLVL is INTEGER
 The current level in the overall merge routine,
 0 &lt;= curlvl &lt;= tlvls.</pre>
<p><i>CURPBM</i> </p>
<pre> CURPBM is INTEGER
 The current problem in the current level in the overall
 merge routine (counting from upper left to lower right).</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (N)
 On entry, the eigenvalues of the rank-1-perturbed matrix.
 On exit, the eigenvalues of the repaired matrix.</pre>
<p><i>Q</i> </p>
<pre> Q is COMPLEX array, dimension (LDQ,N)
 On entry, the eigenvectors of the rank-1-perturbed matrix.
 On exit, the eigenvectors of the repaired tridiagonal matrix.</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q. LDQ &gt;= max(1,N).</pre>
<p><i>RHO</i> </p>
<pre> RHO is REAL
 Contains the subdiagonal element used to create the rank-1
 modification.</pre>
<p><i>INDXQ</i> </p>
<pre> INDXQ is INTEGER array, dimension (N)
 This contains the permutation which will reintegrate the
 subproblem just solved back into sorted order,
 ie. D( INDXQ( I = 1, N ) ) will be in ascending order.</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (4*N)</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is REAL array,
 dimension (3*N+2*QSIZ*N)</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (QSIZ*N)</pre>
<p><i>QSTORE</i> </p>
<pre> QSTORE is REAL array, dimension (N**2+1)
 Stores eigenvectors of submatrices encountered during
 divide and conquer, packed together. QPTR points to
 beginning of the submatrices.</pre>
<p><i>QPTR</i> </p>
<pre> QPTR is INTEGER array, dimension (N+2)
 List of indices pointing to beginning of submatrices stored
 in QSTORE. The submatrices are numbered starting at the
 bottom left of the divide and conquer tree, from left to
 right and bottom to top.</pre>
<p><i>PRMPTR</i> </p>
<pre> PRMPTR is INTEGER array, dimension (N lg N)
 Contains a list of pointers which indicate where in PERM a
 level's permutation is stored. PRMPTR(i+1) - PRMPTR(i)
 indicates the size of the permutation and also the size of
 the full, non-deflated problem.</pre>
<p><i>PERM</i> </p>
<pre> PERM is INTEGER array, dimension (N lg N)
 Contains the permutations (from deflation and sorting) to be
 applied to each eigenblock.</pre>
<p><i>GIVPTR</i> </p>
<pre> GIVPTR is INTEGER array, dimension (N lg N)
 Contains a list of pointers which indicate where in GIVCOL a
 level's Givens rotations are stored. GIVPTR(i+1) - GIVPTR(i)
 indicates the number of Givens rotations.</pre>
<p><i>GIVCOL</i> </p>
<pre> GIVCOL is INTEGER array, dimension (2, N lg N)
 Each pair of numbers indicates a pair of columns to take place
 in a Givens rotation.</pre>
<p><i>GIVNUM</i> </p>
<pre> GIVNUM is REAL array, dimension (2, N lg N)
 Each number indicates the S value to be used in the
 corresponding Givens rotation.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: if INFO = 1, an eigenvalue did not converge</pre>
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
<p> Definition at line 247 of file claed7.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
