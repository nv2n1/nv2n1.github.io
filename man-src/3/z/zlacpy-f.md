---
title: "zlacpy-f(3)"
name: "zlacpy-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlacpy-f/"
description: "zlacpy.f –"
---

<p>zlacpy.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlacpy</code> (UPLO, M, N, A, LDA, B, LDB)<br />
 <i></i><code>ZLACPY</code> copies all or part of one two-dimensional array to another.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlacpy (characterUPLO, integerM, integerN, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldb, * )B, integerLDB)</h3>
<p><code>ZLACPY</code> copies all or part of one two-dimensional array to another. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLACPY copies all or part of a two-dimensional matrix A to another
 matrix B.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies the part of the matrix A to be copied to B.
 = 'U': Upper triangular part
 = 'L': Lower triangular part
 Otherwise: All of the matrix A</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 The m by n matrix A. If UPLO = 'U', only the upper trapezium
 is accessed; if UPLO = 'L', only the lower trapezium is
 accessed.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB,N)
 On exit, B = A in the locations specified by UPLO.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,M).</pre>
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
<p> Definition at line 104 of file zlacpy.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
