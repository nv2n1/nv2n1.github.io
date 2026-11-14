---
title: "sspcon(3)"
name: "sspcon"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sspcon/"
description: "sspcon.f –"
---

<h2 class="name">NAME</h2>
<p> sspcon.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sspcon</code> (UPLO, N, AP, IPIV, ANORM, RCOND, WORK, IWORK, INFO)<br />
 <i></i><code>SSPCON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sspcon (characterUPLO, integerN, real, dimension( * )AP, integer, dimension( * )IPIV, realANORM, realRCOND, real, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>SSPCON</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SSPCON estimates the reciprocal of the condition number (in the
 1-norm) of a real symmetric packed matrix A using the factorization
 A = U*D*U**T or A = L*D*L**T computed by SSPTRF.
 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as RCOND = 1 / (ANORM * norm(inv(A))).
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          Specifies whether the details of the factorization are stored
          as an upper or lower triangular matrix.
          = 'U':  Upper triangular, form is A = U*D*U**T;
          = 'L':  Lower triangular, form is A = L*D*L**T.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>AP</i> </p>
<pre>
          AP is REAL array, dimension (N*(N+1)/2)
          The block diagonal matrix D and the multipliers used to
          obtain the factor U or L as computed by SSPTRF, stored as a
          packed triangular matrix.
</pre>
<p> <i>IPIV</i> </p>
<pre>
          IPIV is INTEGER array, dimension (N)
          Details of the interchanges and the block structure of D
          as determined by SSPTRF.
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
<dd> November 2011</dl>
<p> Definition at line 125 of file sspcon.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
