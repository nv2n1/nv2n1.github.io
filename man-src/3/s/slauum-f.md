---
title: "slauum-f(3)"
name: "slauum-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slauum-f/"
description: "slauum.f –"
---

<p>slauum.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slauum</code> (UPLO, N, A, LDA, INFO)<br />
 <i></i><code>SLAUUM</code> computes the product UUH or LHL, where U and L are upper or lower triangular matrices (blocked algorithm).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slauum (characterUPLO, integerN, real, dimension( lda, * )A, integerLDA, integerINFO)</h3>
<p><code>SLAUUM</code> computes the product UUH or LHL, where U and L are upper or lower triangular matrices (blocked algorithm). </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLAUUM computes the product U * U**T or L**T * L, where the triangular
 factor U or L is stored in the upper or lower triangular part of
 the array A.
 If UPLO = 'U' or 'u' then the upper triangle of the result is stored,
 overwriting the factor U in A.
 If UPLO = 'L' or 'l' then the lower triangle of the result is stored,
 overwriting the factor L in A.
 This is the blocked form of the algorithm, calling Level 3 BLAS.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the triangular factor stored in the array A
 is upper or lower triangular:
 = 'U': Upper triangular
 = 'L': Lower triangular</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the triangular factor U or L. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,N)
 On entry, the triangular factor U or L.
 On exit, if UPLO = 'U', the upper triangle of A is
 overwritten with the upper triangle of the product U * U**T;
 if UPLO = 'L', the lower triangle of A is overwritten with
 the lower triangle of the product L**T * L.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -k, the k-th argument had an illegal value</pre>
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
<p> Definition at line 103 of file slauum.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
