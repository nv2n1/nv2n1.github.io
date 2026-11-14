---
title: "csptrs(3)"
name: "csptrs"
section: "3"
letter: "c"
url: "/docs/linux/man/3-csptrs/"
description: "csptrs.f –"
---

<h2 class="name">NAME</h2>
<p> csptrs.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>csptrs</code> (UPLO, N, NRHS, AP, IPIV, B, LDB, INFO)<br />
 <i></i><code>CSPTRS</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine csptrs (characterUPLO, integerN, integerNRHS, complex, dimension( * )AP, integer, dimension( * )IPIV, complex, dimension( ldb, * )B, integerLDB, integerINFO)</h3>
<p> <code>CSPTRS</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CSPTRS solves a system of linear equations A*X = B with a complex
 symmetric matrix A stored in packed format using the factorization
 A = U*D*U**T or A = L*D*L**T computed by CSPTRF.
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
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
          The number of right hand sides, i.e., the number of columns
          of the matrix B.  NRHS &gt;= 0.
</pre>
<p> <i>AP</i> </p>
<pre>
          AP is COMPLEX array, dimension (N*(N+1)/2)
          The block diagonal matrix D and the multipliers used to
          obtain the factor U or L as computed by CSPTRF, stored as a
          packed triangular matrix.
</pre>
<p> <i>IPIV</i> </p>
<pre>
          IPIV is INTEGER array, dimension (N)
          Details of the interchanges and the block structure of D
          as determined by CSPTRF.
</pre>
<p> <i>B</i> </p>
<pre>
          B is COMPLEX array, dimension (LDB,NRHS)
          On entry, the right hand side matrix B.
          On exit, the solution matrix X.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0: if INFO = -i, the i-th argument had an illegal value
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
<p> Definition at line 116 of file csptrs.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
