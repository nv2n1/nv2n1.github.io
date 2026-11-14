---
title: "zptcon-f(3)"
name: "zptcon-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zptcon-f/"
description: "zptcon.f –"
---

<p>zptcon.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zptcon</code> (N, D, E, ANORM, RCOND, RWORK, INFO)<br />
 <i></i><code>ZPTCON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zptcon (integerN, double precision, dimension( * )D, complex*16, dimension( * )E, double precisionANORM, double precisionRCOND, double precision, dimension( * )RWORK, integerINFO)</h3>
<p><code>ZPTCON</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZPTCON computes the reciprocal of the condition number (in the
 1-norm) of a complex Hermitian positive definite tridiagonal matrix
 using the factorization A = L*D*L**H or A = U**H*D*U computed by
 ZPTTRF.
 Norm(inv(A)) is computed by a direct method, and the reciprocal of
 the condition number is computed as
 RCOND = 1 / (ANORM * norm(inv(A))).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 The n diagonal elements of the diagonal matrix D from the
 factorization of A, as computed by ZPTTRF.</pre>
<p><i>E</i> </p>
<pre> E is COMPLEX*16 array, dimension (N-1)
 The (n-1) off-diagonal elements of the unit bidiagonal factor
 U or L from the factorization of A, as computed by ZPTTRF.</pre>
<p><i>ANORM</i> </p>
<pre> ANORM is DOUBLE PRECISION
 The 1-norm of the original matrix A.</pre>
<p><i>RCOND</i> </p>
<pre> RCOND is DOUBLE PRECISION
 The reciprocal of the condition number of the matrix A,
 computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is the
 1-norm of inv(A) computed in this routine.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
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
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> The method used is described in Nicholas J. Higham, &quot;Efficient
 Algorithms for Computing the Condition Number of a Tridiagonal
 Matrix&quot;, SIAM J. Sci. Stat. Comput., Vol. 7, No. 1, January 1986.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 120 of file zptcon.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
