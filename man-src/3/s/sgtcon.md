---
title: "sgtcon(3)"
name: "sgtcon"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgtcon/"
description: "sgtcon.f –"
---

<h2 class="name">NAME</h2>
<p> sgtcon.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sgtcon</code> (NORM, N, DL, D, DU, DU2, IPIV, ANORM, RCOND, WORK, IWORK, INFO)<br />
 <i></i><code>SGTCON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sgtcon (characterNORM, integerN, real, dimension( * )DL, real, dimension( * )D, real, dimension( * )DU, real, dimension( * )DU2, integer, dimension( * )IPIV, realANORM, realRCOND, real, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>SGTCON</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SGTCON estimates the reciprocal of the condition number of a real
 tridiagonal matrix A using the LU factorization as computed by
 SGTTRF.
 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>NORM</i> </p>
<pre>
          NORM is CHARACTER*1
          Specifies whether the 1-norm condition number or the
          infinity-norm condition number is required:
          = '1' or 'O':  1-norm;
          = 'I':         Infinity-norm.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>DL</i> </p>
<pre>
          DL is REAL array, dimension (N-1)
          The (n-1) multipliers that define the matrix L from the
          LU factorization of A as computed by SGTTRF.
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (N)
          The n diagonal elements of the upper triangular matrix U from
          the LU factorization of A.
</pre>
<p> <i>DU</i> </p>
<pre>
          DU is REAL array, dimension (N-1)
          The (n-1) elements of the first superdiagonal of U.
</pre>
<p> <i>DU2</i> </p>
<pre>
          DU2 is REAL array, dimension (N-2)
          The (n-2) elements of the second superdiagonal of U.
</pre>
<p> <i>IPIV</i> </p>
<pre><code>
IPIV is INTEGER array, dimension(N)
                           The pivot indices; for
    1 &lt;= i &lt;= n, row i of the matrix was
                         interchanged with row IPIV(i)
                             .IPIV(i) will always be either
                     i
                     or i + 1;
IPIV(i) = i indicates a row interchange was not required.
</code></pre>
<p> <i>ANORM</i> </p>
<pre>
          ANORM is REAL
          If NORM = '1' or 'O', the 1-norm of the original matrix A.
          If NORM = 'I', the infinity-norm of the original matrix A.
</pre>
<p> <i>RCOND</i> </p>
<pre>
          RCOND is REAL
          The reciprocal of the condition number of the matrix A,
          computed as RCOND = 1/(ANORM * AINVNM), where AINVNM is an
          estimate of the 1-norm of inv(A) computed in this routine.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (2*N)
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
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
<p> Definition at line 146 of file sgtcon.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
