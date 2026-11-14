---
title: "slaed2-f(3)"
name: "slaed2-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slaed2-f/"
description: "slaed2.f –"
---

<p>slaed2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slaed2</code> (K, N, N1, D, Q, LDQ, INDXQ, RHO, Z, DLAMDA, W, Q2, INDX, INDXC, INDXP, COLTYP, INFO)<br />
 <i></i><code>SLAED2</code> used by sstedc. Merges eigenvalues and deflates secular equation. Used when the original matrix is tridiagonal.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slaed2 (integerK, integerN, integerN1, real, dimension( * )D, real, dimension( ldq, * )Q, integerLDQ, integer, dimension( * )INDXQ, realRHO, real, dimension( * )Z, real, dimension( * )DLAMDA, real, dimension( * )W, real, dimension( * )Q2, integer, dimension( * )INDX, integer, dimension( * )INDXC, integer, dimension( * )INDXP, integer, dimension( * )COLTYP, integerINFO)</h3>
<p><code>SLAED2</code> used by sstedc. Merges eigenvalues and deflates secular equation. Used when the original matrix is tridiagonal. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLAED2 merges the two sets of eigenvalues together into a single
 sorted set. Then it tries to deflate the size of the problem.
 There are two ways in which deflation can occur: when two or more
 eigenvalues are close together or if there is a tiny entry in the
 Z vector. For each such occurrence the order of the related secular
 equation problem is reduced by one.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>K</i> </p>
<pre> K is INTEGER
 The number of non-deflated eigenvalues, and the order of the
 related secular equation. 0 &lt;= K &lt;=N.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The dimension of the symmetric tridiagonal matrix. N &gt;= 0.</pre>
<p><i>N1</i> </p>
<pre> N1 is INTEGER
 The location of the last eigenvalue in the leading sub-matrix.
 min(1,N) &lt;= N1 &lt;= N/2.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (N)
 On entry, D contains the eigenvalues of the two submatrices to
 be combined.
 On exit, D contains the trailing (N-K) updated eigenvalues
 (those which were deflated) sorted into increasing order.</pre>
<p><i>Q</i> </p>
<pre> Q is REAL array, dimension (LDQ, N)
 On entry, Q contains the eigenvectors of two submatrices in
 the two square blocks with corners at (1,1), (N1,N1)
 and (N1+1, N1+1), (N,N).
 On exit, Q contains the trailing (N-K) updated eigenvectors
 (those which were deflated) in its last N-K columns.</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q. LDQ &gt;= max(1,N).</pre>
<p><i>INDXQ</i> </p>
<pre> INDXQ is INTEGER array, dimension (N)
 The permutation which separately sorts the two sub-problems
 in D into ascending order. Note that elements in the second
 half of this permutation must first have N1 added to their
 values. Destroyed on exit.</pre>
<p><i>RHO</i> </p>
<pre> RHO is REAL
 On entry, the off-diagonal element associated with the rank-1
 cut which originally split the two submatrices which are now
 being recombined.
 On exit, RHO has been modified to the value required by
 SLAED3.</pre>
<p><i>Z</i> </p>
<pre> Z is REAL array, dimension (N)
 On entry, Z contains the updating vector (the last
 row of the first sub-eigenvector matrix and the first row of
 the second sub-eigenvector matrix).
 On exit, the contents of Z have been destroyed by the updating
 process.</pre>
<p><i>DLAMDA</i> </p>
<pre> DLAMDA is REAL array, dimension (N)
 A copy of the first K eigenvalues which will be used by
 SLAED3 to form the secular equation.</pre>
<p><i>W</i> </p>
<pre> W is REAL array, dimension (N)
 The first k values of the final deflation-altered z-vector
 which will be passed to SLAED3.</pre>
<p><i>Q2</i> </p>
<pre> Q2 is REAL array, dimension (N1**2+(N-N1)**2)
 A copy of the first K eigenvectors which will be used by
 SLAED3 in a matrix multiply (SGEMM) to solve for the new
 eigenvectors.</pre>
<p><i>INDX</i> </p>
<pre> INDX is INTEGER array, dimension (N)
 The permutation used to sort the contents of DLAMDA into
 ascending order.</pre>
<p><i>INDXC</i> </p>
<pre> INDXC is INTEGER array, dimension (N)
 The permutation used to arrange the columns of the deflated
 Q matrix into three groups: the first group contains non-zero
 elements only at and above N1, the second contains
 non-zero elements only below N1, and the third is dense.</pre>
<p><i>INDXP</i> </p>
<pre> INDXP is INTEGER array, dimension (N)
 The permutation used to place deflated values of D at the end
 of the array. INDXP(1:K) points to the nondeflated D-values
 and INDXP(K+1:N) points to the deflated eigenvalues.</pre>
<p><i>COLTYP</i> </p>
<pre> COLTYP is INTEGER array, dimension (N)
 During execution, a label which will indicate which of the
 following types a column in the Q2 matrix is:
 1 : non-zero in the upper half only;
 2 : dense;
 3 : non-zero in the lower half only;
 4 : deflated.
 On exit, COLTYP(i) is the number of columns of type i,
 for i=1 to 4 only.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> <code>Contributors: </code></p>
<dl>
<dd>Jeff Rutter, Computer Science Division, University of California at Berkeley, USA </p>
<p>&nbsp;<wbr>Modified by Francoise Tisseur, University of Tennessee&nbsp;<wbr></dl>
<p> Definition at line 212 of file slaed2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
