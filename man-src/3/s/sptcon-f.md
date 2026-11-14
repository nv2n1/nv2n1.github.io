---
title: "sptcon-f(3)"
name: "sptcon-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sptcon-f/"
description: "sptcon.f –"
---

<p>sptcon.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sptcon</code> (N, D, E, ANORM, RCOND, WORK, INFO)<br />
 <i></i><code>SPTCON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sptcon (integerN, real, dimension( * )D, real, dimension( * )E, realANORM, realRCOND, real, dimension( * )WORK, integerINFO)</h3>
<p> <code>SPTCON</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dt>
<dd>
<pre>
 SPTCON computes the reciprocal of the condition number (in the
 1-norm) of a real symmetric positive definite tridiagonal matrix
 using the factorization A = L*D*L**T or A = U**T*D*U computed by
 SPTTRF.
 Norm(inv(A)) is computed by a direct method, and the reciprocal of
 the condition number is computed as
              RCOND = 1 / (ANORM * norm(inv(A))).
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (N)
          The n diagonal elements of the diagonal matrix D from the
          factorization of A, as computed by SPTTRF.
</pre>
<p> <i>E</i> </p>
<pre>
          E is REAL array, dimension (N-1)
          The (n-1) off-diagonal elements of the unit bidiagonal factor
          U or L from the factorization of A,  as computed by SPTTRF.
</pre>
<p> <i>ANORM</i> </p>
<pre>
          ANORM is REAL
          The 1-norm of the original matrix A.
</pre>
<p> <i>RCOND</i> </p>
<pre>
          RCOND is REAL
          The reciprocal of the condition number of the matrix A,
          computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is the
          1-norm of inv(A) computed in this routine.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dt>
<dd> September 2012</dl>
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dt>
<dd>
<pre>
  The method used is described in Nicholas J. Higham, &quot;Efficient
  Algorithms for Computing the Condition Number of a Tridiagonal
  Matrix&quot;, SIAM J. Sci. Stat. Comput., Vol. 7, No. 1, January 1986.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 119 of file sptcon.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code.</p>
