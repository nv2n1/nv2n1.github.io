---
title: "ztpttr(3)"
name: "ztpttr"
section: "3"
letter: "z"
url: "/docs/linux/man/3-ztpttr/"
description: "ztpttr.f –"
---

<p>ztpttr.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ztpttr</code> (UPLO, N, AP, A, LDA, INFO)<br />
 <i></i><code>ZTPTTR</code> copies a triangular matrix from the standard packed format (TP) to the standard full format (TR).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ztpttr (characterUPLO, integerN, complex*16, dimension( * )AP, complex*16, dimension( lda, * )A, integerLDA, integerINFO)</h3>
<p><code>ZTPTTR</code> copies a triangular matrix from the standard packed format (TP) to the standard full format (TR). </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZTPTTR copies a triangular matrix A from standard packed format (TP)
 to standard full format (TR).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': A is upper triangular.
 = 'L': A is lower triangular.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>AP</i> </p>
<pre> AP is COMPLEX*16 array, dimension ( N*(N+1)/2 ),
 On entry, the upper or lower triangular matrix A, packed
 columnwise in a linear array. The j-th column of A is stored
 in the array AP as follows:
 if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j&lt;=i&lt;=n.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension ( LDA, N )
 On exit, the triangular matrix A. If UPLO = 'U', the leading
 N-by-N upper triangular part of A contains the upper
 triangular part of the matrix A, and the strictly lower
 triangular part of A is not referenced. If UPLO = 'L', the
 leading N-by-N lower triangular part of A contains the lower
 triangular part of the matrix A, and the strictly upper
 triangular part of A is not referenced.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> Definition at line 105 of file ztpttr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
