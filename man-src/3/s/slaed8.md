---
title: "slaed8(3)"
name: "slaed8"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slaed8/"
description: "slaed8.f –"
---

<h2 class="name">NAME</h2>
<p> slaed8.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slaed8</code> (ICOMPQ, K, N, QSIZ, D, Q, LDQ, INDXQ, RHO, CUTPNT, Z, DLAMDA, Q2, LDQ2, W, PERM, GIVPTR, GIVCOL, GIVNUM, INDXP, INDX, INFO)<br />
 <i></i><code>SLAED8</code> used by sstedc. Merges eigenvalues and deflates secular equation. Used when the original matrix is dense.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slaed8 (integerICOMPQ, integerK, integerN, integerQSIZ, real, dimension( * )D, real, dimension( ldq, * )Q, integerLDQ, integer, dimension( * )INDXQ, realRHO, integerCUTPNT, real, dimension( * )Z, real, dimension( * )DLAMDA, real, dimension( ldq2, * )Q2, integerLDQ2, real, dimension( * )W, integer, dimension( * )PERM, integerGIVPTR, integer, dimension( 2, * )GIVCOL, real, dimension( 2, * )GIVNUM, integer, dimension( * )INDXP, integer, dimension( * )INDX, integerINFO)</h3>
<p> <code>SLAED8</code> used by sstedc. Merges eigenvalues and deflates secular equation. Used when the original matrix is dense. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLAED8 merges the two sets of eigenvalues together into a single
 sorted set.  Then it tries to deflate the size of the problem.
 There are two ways in which deflation can occur:  when two or more
 eigenvalues are close together or if there is a tiny element in the
 Z vector.  For each such occurrence the order of the related secular
 equation problem is reduced by one.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ICOMPQ</i> </p>
<pre>
          ICOMPQ is INTEGER
          = 0:  Compute eigenvalues only.
          = 1:  Compute eigenvectors of original dense symmetric matrix
                also.  On entry, Q contains the orthogonal matrix used
                to reduce the original matrix to tridiagonal form.
</pre>
<p> <i>K</i> </p>
<pre>
          K is INTEGER
         The number of non-deflated eigenvalues, and the order of the
         related secular equation.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
         The dimension of the symmetric tridiagonal matrix.  N &gt;= 0.
</pre>
<p> <i>QSIZ</i> </p>
<pre>
          QSIZ is INTEGER
         The dimension of the orthogonal matrix used to reduce
         the full matrix to tridiagonal form.  QSIZ &gt;= N if ICOMPQ = 1.
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (N)
         On entry, the eigenvalues of the two submatrices to be
         combined.  On exit, the trailing (N-K) updated eigenvalues
         (those which were deflated) sorted into increasing order.
</pre>
<p> <i>Q</i> </p>
<pre>
          Q is REAL array, dimension (LDQ,N)
         If ICOMPQ = 0, Q is not referenced.  Otherwise,
         on entry, Q contains the eigenvectors of the partially solved
         system which has been previously updated in matrix
         multiplies with other partially solved eigensystems.
         On exit, Q contains the trailing (N-K) updated eigenvectors
         (those which were deflated) in its last N-K columns.
</pre>
<p> <i>LDQ</i> </p>
<pre>
          LDQ is INTEGER
         The leading dimension of the array Q.  LDQ &gt;= max(1,N).
</pre>
<p> <i>INDXQ</i> </p>
<pre>
          INDXQ is INTEGER array, dimension (N)
         The permutation which separately sorts the two sub-problems
         in D into ascending order.  Note that elements in the second
         half of this permutation must first have CUTPNT added to
         their values in order to be accurate.
</pre>
<p> <i>RHO</i> </p>
<pre>
          RHO is REAL
         On entry, the off-diagonal element associated with the rank-1
         cut which originally split the two submatrices which are now
         being recombined.
         On exit, RHO has been modified to the value required by
         SLAED3.
</pre>
<p> <i>CUTPNT</i> </p>
<pre>
          CUTPNT is INTEGER
         The location of the last eigenvalue in the leading
         sub-matrix.  min(1,N) &lt;= CUTPNT &lt;= N.
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is REAL array, dimension (N)
         On entry, Z contains the updating vector (the last row of
         the first sub-eigenvector matrix and the first row of the
         second sub-eigenvector matrix).
         On exit, the contents of Z are destroyed by the updating
         process.
</pre>
<p> <i>DLAMDA</i> </p>
<pre>
          DLAMDA is REAL array, dimension (N)
         A copy of the first K eigenvalues which will be used by
         SLAED3 to form the secular equation.
</pre>
<p> <i>Q2</i> </p>
<pre>
          Q2 is REAL array, dimension (LDQ2,N)
         If ICOMPQ = 0, Q2 is not referenced.  Otherwise,
         a copy of the first K eigenvectors which will be used by
         SLAED7 in a matrix multiply (SGEMM) to update the new
         eigenvectors.
</pre>
<p> <i>LDQ2</i> </p>
<pre>
          LDQ2 is INTEGER
         The leading dimension of the array Q2.  LDQ2 &gt;= max(1,N).
</pre>
<p> <i>W</i> </p>
<pre>
          W is REAL array, dimension (N)
         The first k values of the final deflation-altered z-vector and
         will be passed to SLAED3.
</pre>
<p> <i>PERM</i> </p>
<pre>
          PERM is INTEGER array, dimension (N)
         The permutations (from deflation and sorting) to be applied
         to each eigenblock.
</pre>
<p> <i>GIVPTR</i> </p>
<pre>
          GIVPTR is INTEGER
         The number of Givens rotations which took place in this
         subproblem.
</pre>
<p> <i>GIVCOL</i> </p>
<pre>
          GIVCOL is INTEGER array, dimension (2, N)
         Each pair of numbers indicates a pair of columns to take place
         in a Givens rotation.
</pre>
<p> <i>GIVNUM</i> </p>
<pre>
          GIVNUM is REAL array, dimension (2, N)
         Each number indicates the S value to be used in the
         corresponding Givens rotation.
</pre>
<p> <i>INDXP</i> </p>
<pre>
          INDXP is INTEGER array, dimension (N)
         The permutation used to place deflated values of D at the end
         of the array.  INDXP(1:K) points to the nondeflated D-values
         and INDXP(K+1:N) points to the deflated eigenvalues.
</pre>
<p> <i>INDX</i> </p>
<pre>
          INDX is INTEGER array, dimension (N)
         The permutation used to sort the contents of D into ascending
         order.
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
<dd> Jeff Rutter, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 242 of file slaed8.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
