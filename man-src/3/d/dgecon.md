---
title: "dgecon(3)"
name: "dgecon"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgecon/"
description: "dgecon.f –"
---

<h2 class="name">NAME</h2>
<p> dgecon.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dgecon</code> (NORM, N, A, LDA, ANORM, RCOND, WORK, IWORK, INFO)<br />
 <i></i><code>DGECON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgecon (characterNORM, integerN, double precision, dimension( lda, * )A, integerLDA, double precisionANORM, double precisionRCOND, double precision, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>DGECON</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DGECON estimates the reciprocal of the condition number of a general
 real matrix A, in either the 1-norm or the infinity-norm, using
 the LU factorization computed by DGETRF.
 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as
    RCOND = 1 / ( norm(A) * norm(inv(A)) ).
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
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
          The factors L and U from the factorization A = P*L*U
          as computed by DGETRF.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>ANORM</i> </p>
<pre>
          ANORM is DOUBLE PRECISION
          If NORM = '1' or 'O', the 1-norm of the original matrix A.
          If NORM = 'I', the infinity-norm of the original matrix A.
</pre>
<p> <i>RCOND</i> </p>
<pre>
          RCOND is DOUBLE PRECISION
          The reciprocal of the condition number of the matrix A,
          computed as RCOND = 1/(norm(A) * norm(inv(A))).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (4*N)
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
<dd> November 2011</dl>
<p> Definition at line 124 of file dgecon.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
