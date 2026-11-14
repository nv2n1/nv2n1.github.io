---
title: "ctpcon(3)"
name: "ctpcon"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ctpcon/"
description: "ctpcon.f –"
---

<h2 class="name">NAME</h2>
<p> ctpcon.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>ctpcon</code> (NORM, UPLO, DIAG, N, AP, RCOND, WORK, RWORK, INFO)<br />
 <i></i><code>CTPCON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ctpcon (characterNORM, characterUPLO, characterDIAG, integerN, complex, dimension( * )AP, realRCOND, complex, dimension( * )WORK, real, dimension( * )RWORK, integerINFO)</h3>
<p> <code>CTPCON</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CTPCON estimates the reciprocal of the condition number of a packed
 triangular matrix A, in either the 1-norm or the infinity-norm.
 The norm of A is computed and an estimate is obtained for
 norm(inv(A)), then the reciprocal of the condition number is
 computed as
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
<p> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  A is upper triangular;
          = 'L':  A is lower triangular.
</pre>
<p> <i>DIAG</i> </p>
<pre>
          DIAG is CHARACTER*1
          = 'N':  A is non-unit triangular;
          = 'U':  A is unit triangular.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>AP</i> </p>
<pre><code>
          AP is COMPLEX array, dimension (N*(N+1)/2)
          The upper or lower triangular matrix A, packed columnwise in
          a linear array.  The j-th column of A is stored in the array
          AP as follows:
          if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
          if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
          If DIAG = 'U', the diagonal elements of A are not referenced
          and are assumed to be 1.
</code></pre>
<p> <i>RCOND</i> </p>
<pre>
          RCOND is REAL
          The reciprocal of the condition number of the matrix A,
          computed as RCOND = 1/(norm(A) * norm(inv(A))).
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
<p> Definition at line 130 of file ctpcon.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
