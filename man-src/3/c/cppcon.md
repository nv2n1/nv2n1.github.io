---
title: "cppcon(3)"
name: "cppcon"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cppcon/"
description: "cppcon.f –"
---

<h2 class="name">NAME</h2>
<p> cppcon.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cppcon</code> (UPLO, N, AP, ANORM, RCOND, WORK, RWORK, INFO)<br />
 <i></i><code>CPPCON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cppcon (characterUPLO, integerN, complex, dimension( * )AP, realANORM, realRCOND, complex, dimension( * )WORK, real, dimension( * )RWORK, integerINFO)</h3>
<p> <code>CPPCON</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CPPCON estimates the reciprocal of the condition number (in the 
 1-norm) of a complex Hermitian positive definite packed matrix using
 the Cholesky factorization A = U**H*U or A = L*L**H computed by
 CPPTRF.
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
          = 'U':  Upper triangle of A is stored;
          = 'L':  Lower triangle of A is stored.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>AP</i> </p>
<pre><code>
          AP is COMPLEX array, dimension (N*(N+1)/2)
          The triangular factor U or L from the Cholesky factorization
          A = U**H*U or A = L*L**H, packed columnwise in a linear
          array.  The j-th column of U or L is stored in the array AP
          as follows:
          if UPLO = 'U', AP(i + (j-1)*j/2) = U(i,j) for 1&lt;=i&lt;=j;
          if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = L(i,j) for j&lt;=i&lt;=n.
</code></pre>
<p> <i>ANORM</i> </p>
<pre>
          ANORM is REAL
          The 1-norm (or infinity-norm) of the Hermitian matrix A.
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
          WORK is COMPLEX array, dimension (2*N)
</pre>
<p> <i>RWORK</i> </p>
<pre>
          RWORK is REAL array, dimension (N)
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
<p> Definition at line 119 of file cppcon.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
