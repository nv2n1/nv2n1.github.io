---
title: "dlaed1-f(3)"
name: "dlaed1-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlaed1-f/"
description: "dlaed1.f –"
---

<p>dlaed1.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlaed1</code> (N, D, Q, LDQ, INDXQ, RHO, CUTPNT, WORK, IWORK, INFO)<br />
 <i></i><code>DLAED1</code> used by sstedc. Computes the updated eigensystem of a diagonal matrix after modification by a rank-one symmetric matrix. Used when the original matrix is tridiagonal.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlaed1 (integerN, double precision, dimension( * )D, double precision, dimension( ldq, * )Q, integerLDQ, integer, dimension( * )INDXQ, double precisionRHO, integerCUTPNT, double precision, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p><code>DLAED1</code> used by sstedc. Computes the updated eigensystem of a diagonal matrix after modification by a rank-one symmetric matrix. Used when the original matrix is tridiagonal. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLAED1 computes the updated eigensystem of a diagonal
 matrix after modification by a rank-one symmetric matrix. This
 routine is used only for the eigenproblem which requires all
 eigenvalues and eigenvectors of a tridiagonal matrix. DLAED7 handles
 the case in which eigenvalues only or eigenvalues and eigenvectors
 of a full symmetric matrix (which was reduced to tridiagonal form)
 are desired.
 T = Q(in) ( D(in) + RHO * Z*Z**T ) Q**T(in) = Q(out) * D(out) * Q**T(out)
 where Z = Q**T*u, u is a vector of length N with ones in the
 CUTPNT and CUTPNT + 1 th elements and zeros elsewhere.
 The eigenvectors of the original matrix are stored in Q, and the
 eigenvalues are in D. The algorithm consists of three stages:
 The first stage consists of deflating the size of the problem
 when there are multiple eigenvalues or if there is a zero in
 the Z vector. For each such occurence the dimension of the
 secular equation problem is reduced by one. This stage is
 performed by the routine DLAED2.
 The second stage consists of calculating the updated
 eigenvalues. This is done by finding the roots of the secular
 equation via the routine DLAED4 (as called by DLAED3).
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
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 On entry, the eigenvalues of the rank-1-perturbed matrix.
 On exit, the eigenvalues of the repaired matrix.</pre>
<p><i>Q</i> </p>
<pre> Q is DOUBLE PRECISION array, dimension (LDQ,N)
 On entry, the eigenvectors of the rank-1-perturbed matrix.
 On exit, the eigenvectors of the repaired tridiagonal matrix.</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q. LDQ &gt;= max(1,N).</pre>
<p><i>INDXQ</i> </p>
<pre> INDXQ is INTEGER array, dimension (N)
 On entry, the permutation which separately sorts the two
 subproblems in D into ascending order.
 On exit, the permutation which will reintegrate the
 subproblems back into sorted order,
 i.e. D( INDXQ( I = 1, N ) ) will be in ascending order.</pre>
<p><i>RHO</i> </p>
<pre> RHO is DOUBLE PRECISION
 The subdiagonal entry used to create the rank-1 modification.</pre>
<p><i>CUTPNT</i> </p>
<pre> CUTPNT is INTEGER
 The location of the last eigenvalue in the leading sub-matrix.
 min(1,N) &lt;= CUTPNT &lt;= N/2.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (4*N + N**2)</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (4*N)</pre>
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
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>Jeff Rutter, Computer Science Division, University of California at Berkeley, USA </p>
<p>&nbsp;<wbr>Modified by Francoise Tisseur, University of Tennessee&nbsp;<wbr></dl>
<p> Definition at line 163 of file dlaed1.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
