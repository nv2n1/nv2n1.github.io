---
title: "dtrtri(3)"
name: "dtrtri"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dtrtri/"
description: "dtrtri.f –"
---

<h2 class="name">NAME</h2>
<p> dtrtri.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dtrtri</code> (UPLO, DIAG, N, A, LDA, INFO)<br />
 <i></i><code>DTRTRI</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dtrtri (characterUPLO, characterDIAG, integerN, double precision, dimension( lda, * )A, integerLDA, integerINFO)</h3>
<p> <code>DTRTRI</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DTRTRI computes the inverse of a real upper or lower triangular
 matrix A.
 This is the Level 3 BLAS version of the algorithm.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
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
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
          On entry, the triangular matrix A.  If UPLO = 'U', the
          leading N-by-N upper triangular part of the array A contains
          the upper triangular matrix, and the strictly lower
          triangular part of A is not referenced.  If UPLO = 'L', the
          leading N-by-N lower triangular part of the array A contains
          the lower triangular matrix, and the strictly upper
          triangular part of A is not referenced.  If DIAG = 'U', the
          diagonal elements of A are also not referenced and are
          assumed to be 1.
          On exit, the (triangular) inverse of the original matrix, in
          the same storage format.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -i, the i-th argument had an illegal value
          &gt; 0: if INFO = i, A(i,i) is exactly zero.  The triangular
               matrix is singular and its inverse can not be computed.
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
<p> Definition at line 110 of file dtrtri.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
