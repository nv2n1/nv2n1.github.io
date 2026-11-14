---
title: "zhfrk(3)"
name: "zhfrk"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zhfrk/"
description: "zhfrk.f –"
---

<p>zhfrk.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zhfrk</code> (TRANSR, UPLO, TRANS, N, K, ALPHA, A, LDA, BETA, C)<br />
 <i></i><code>ZHFRK</code> performs a Hermitian rank-k operation for matrix in RFP format.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zhfrk (characterTRANSR, characterUPLO, characterTRANS, integerN, integerK, double precisionALPHA, complex*16, dimension( lda, * )A, integerLDA, double precisionBETA, complex*16, dimension( * )C)</h3>
<p><code>ZHFRK</code> performs a Hermitian rank-k operation for matrix in RFP format. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> Level 3 BLAS like routine for C in RFP Format.
 ZHFRK performs one of the Hermitian rank--k operations
 C := alpha*A*A**H + beta*C,
 or
 C := alpha*A**H*A + beta*C,
 where alpha and beta are real scalars, C is an n--by--n Hermitian
 matrix and A is an n--by--k matrix in the first case and a k--by--n
 matrix in the second case.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>TRANSR</i> </p>
<pre> TRANSR is CHARACTER*1
 = 'N': The Normal Form of RFP A is stored;
 = 'C': The Conjugate-transpose Form of RFP A is stored.</pre>
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 On entry, UPLO specifies whether the upper or lower
 triangular part of the array C is to be referenced as
 follows:
 UPLO = 'U' or 'u' Only the upper triangular part of C
 is to be referenced.
 UPLO = 'L' or 'l' Only the lower triangular part of C
 is to be referenced.
 Unchanged on exit.</pre>
<p><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 On entry, TRANS specifies the operation to be performed as
 follows:
 TRANS = 'N' or 'n' C := alpha*A*A**H + beta*C.
 TRANS = 'C' or 'c' C := alpha*A**H*A + beta*C.
 Unchanged on exit.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 On entry, N specifies the order of the matrix C. N must be
 at least zero.
 Unchanged on exit.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER
 On entry with TRANS = 'N' or 'n', K specifies the number
 of columns of the matrix A, and on entry with
 TRANS = 'C' or 'c', K specifies the number of rows of the
 matrix A. K must be at least zero.
 Unchanged on exit.</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is DOUBLE PRECISION
 On entry, ALPHA specifies the scalar alpha.
 Unchanged on exit.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array of DIMENSION (LDA,ka)
 where KA
 is K when TRANS = 'N' or 'n', and is N otherwise. Before
 entry with TRANS = 'N' or 'n', the leading N--by--K part of
 the array A must contain the matrix A, otherwise the leading
 K--by--N part of the array A must contain the matrix A.
 Unchanged on exit.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 On entry, LDA specifies the first dimension of A as declared
 in the calling (sub) program. When TRANS = 'N' or 'n'
 then LDA must be at least max( 1, n ), otherwise LDA must
 be at least max( 1, k ).
 Unchanged on exit.</pre>
<p><i>BETA</i> </p>
<pre> BETA is DOUBLE PRECISION
 On entry, BETA specifies the scalar beta.
 Unchanged on exit.</pre>
<p><i>C</i> </p>
<pre> C is COMPLEX*16 array, dimension (N*(N+1)/2)
 On entry, the matrix A in RFP Format. RFP Format is
 described by TRANSR, UPLO and N. Note that the imaginary
 parts of the diagonal elements need not be set, they are
 assumed to be zero, and on exit they are set to zero.</pre>
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
<p> Definition at line 168 of file zhfrk.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
