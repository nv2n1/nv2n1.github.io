---
title: "sspgst(3)"
name: "sspgst"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sspgst/"
description: "sspgst.f –"
---

<h2 class="name">NAME</h2>
<p> sspgst.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sspgst</code> (ITYPE, UPLO, N, AP, BP, INFO)<br />
 <i></i><code>SSPGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sspgst (integerITYPE, characterUPLO, integerN, real, dimension( * )AP, real, dimension( * )BP, integerINFO)</h3>
<p> <code>SSPGST</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SSPGST reduces a real symmetric-definite generalized eigenproblem
 to standard form, using packed storage.
 If ITYPE = 1, the problem is A*x = lambda*B*x,
 and A is overwritten by inv(U**T)*A*inv(U) or inv(L)*A*inv(L**T)
 If ITYPE = 2 or 3, the problem is A*B*x = lambda*x or
 B*A*x = lambda*x, and A is overwritten by U*A*U**T or L**T*A*L.
 B must have been previously factorized as U**T*U or L*L**T by SPPTRF.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ITYPE</i> </p>
<pre>
          ITYPE is INTEGER
          = 1: compute inv(U**T)*A*inv(U) or inv(L)*A*inv(L**T);
          = 2 or 3: compute U*A*U**T or L**T*A*L.
</pre>
<p> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  Upper triangle of A is stored and B is factored as
                  U**T*U;
          = 'L':  Lower triangle of A is stored and B is factored as
                  L*L**T.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrices A and B.  N &gt;= 0.
</pre>
<p> <i>AP</i> </p>
<pre><code>
          AP is REAL array, dimension (N*(N+1)/2)
          On entry, the upper or lower triangle of the symmetric matrix
          A, packed columnwise in a linear array.  The j-th column of A
          is stored in the array AP as follows:
          if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
          if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
          On exit, if INFO = 0, the transformed matrix, stored in the
          same format as A.
</code></pre>
<p> <i>BP</i> </p>
<pre>
          BP is REAL array, dimension (N*(N+1)/2)
          The triangular factor from the Cholesky factorization of B,
          stored in the same format as A, as returned by SPPTRF.
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
<p> Definition at line 114 of file sspgst.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
