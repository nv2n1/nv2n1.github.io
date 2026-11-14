---
title: "ctrti2-f(3)"
name: "ctrti2-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ctrti2-f/"
description: "ctrti2.f –"
---

<p>ctrti2.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ctrti2</code> (UPLO, DIAG, N, A, LDA, INFO)<br />
 <i></i><code>CTRTI2</code> computes the inverse of a triangular matrix (unblocked algorithm).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ctrti2 (characterUPLO, characterDIAG, integerN, complex, dimension( lda, * )A, integerLDA, integerINFO)</h3>
<p><code>CTRTI2</code> computes the inverse of a triangular matrix (unblocked algorithm). </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CTRTI2 computes the inverse of a complex upper or lower triangular
 matrix.
 This is the Level 2 BLAS version of the algorithm.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the matrix A is upper or lower triangular.
 = 'U': Upper triangular
 = 'L': Lower triangular</pre>
<p><i>DIAG</i> </p>
<pre> DIAG is CHARACTER*1
 Specifies whether or not the matrix A is unit triangular.
 = 'N': Non-unit triangular
 = 'U': Unit triangular</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX array, dimension (LDA,N)
 On entry, the triangular matrix A. If UPLO = 'U', the
 leading n by n upper triangular part of the array A contains
 the upper triangular matrix, and the strictly lower
 triangular part of A is not referenced. If UPLO = 'L', the
 leading n by n lower triangular part of the array A contains
 the lower triangular matrix, and the strictly upper
 triangular part of A is not referenced. If DIAG = 'U', the
 diagonal elements of A are also not referenced and are
 assumed to be 1.
 On exit, the (triangular) inverse of the original matrix, in
 the same storage format.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -k, the k-th argument had an illegal value</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> Definition at line 111 of file ctrti2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
