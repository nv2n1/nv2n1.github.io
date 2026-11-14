---
title: "ctrttp(3)"
name: "ctrttp"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ctrttp/"
description: "ctrttp.f –"
---

<h2 class="name">NAME</h2>
<p> ctrttp.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>ctrttp</code> (UPLO, N, A, LDA, AP, INFO)<br />
 <i></i><code>CTRTTP</code> copies a triangular matrix from the standard full format (TR) to the standard packed format (TP).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ctrttp (characterUPLO, integerN, complex, dimension( lda, * )A, integerLDA, complex, dimension( * )AP, integerINFO)</h3>
<p> <code>CTRTTP</code> copies a triangular matrix from the standard full format (TR) to the standard packed format (TP). </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CTRTTP copies a triangular matrix A from full format (TR) to standard
 packed format (TP).
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
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrices AP and A.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
          On entry, the triangular matrix A.  If UPLO = 'U', the leading
          N-by-N upper triangular part of A contains the upper
          triangular part of the matrix A, and the strictly lower
          triangular part of A is not referenced.  If UPLO = 'L', the
          leading N-by-N lower triangular part of A contains the lower
          triangular part of the matrix A, and the strictly upper
          triangular part of A is not referenced.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>AP</i> </p>
<pre><code>
          AP is COMPLEX array, dimension ( N*(N+1)/2 ),
          On exit, the upper or lower triangular matrix A, packed
          columnwise in a linear array. The j-th column of A is stored
          in the array AP as follows:
          if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
          if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
</code></pre>
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
<p> Definition at line 105 of file ctrttp.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
