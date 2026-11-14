---
title: "sdisna-f(3)"
name: "sdisna-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sdisna-f/"
description: "sdisna.f –"
---

<p>sdisna.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sdisna</code> (JOB, M, N, D, SEP, INFO)<br />
 <i></i><code>SDISNA</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sdisna (characterJOB, integerM, integerN, real, dimension( * )D, real, dimension( * )SEP, integerINFO)</h3>
<p><code>SDISNA</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SDISNA computes the reciprocal condition numbers for the eigenvectors
 of a real symmetric or complex Hermitian matrix or for the left or
 right singular vectors of a general m-by-n matrix. The reciprocal
 condition number is the 'gap' between the corresponding eigenvalue or
 singular value and the nearest other one.
 The bound on the error, measured by angle in radians, in the I-th
 computed vector is given by
 SLAMCH( 'E' ) * ( ANORM / SEP( I ) )
 where ANORM = 2-norm(A) = max( abs( D(j) ) ). SEP(I) is not allowed
 to be smaller than SLAMCH( 'E' )*ANORM in order to limit the size of
 the error bound.
 SDISNA may also be used to compute error bounds for eigenvectors of
 the generalized symmetric definite eigenproblem.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>JOB</i> </p>
<pre> JOB is CHARACTER*1
 Specifies for which problem the reciprocal condition numbers
 should be computed:
 = 'E': the eigenvectors of a symmetric/Hermitian matrix;
 = 'L': the left singular vectors of a general matrix;
 = 'R': the right singular vectors of a general matrix.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 If JOB = 'L' or 'R', the number of columns of the matrix,
 in which case N &gt;= 0. Ignored if JOB = 'E'.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (M) if JOB = 'E'
 dimension (min(M,N)) if JOB = 'L' or 'R'
 The eigenvalues (if JOB = 'E') or singular values (if JOB =
 'L' or 'R') of the matrix, in either increasing or decreasing
 order. If singular values, they must be non-negative.</pre>
<p><i>SEP</i> </p>
<pre> SEP is REAL array, dimension (M) if JOB = 'E'
 dimension (min(M,N)) if JOB = 'L' or 'R'
 The reciprocal condition numbers of the vectors.</pre>
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
<dd>November 2011</dl>
<p> Definition at line 118 of file sdisna.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
