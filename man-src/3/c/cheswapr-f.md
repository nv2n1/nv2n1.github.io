---
title: "cheswapr-f(3)"
name: "cheswapr-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cheswapr-f/"
description: "cheswapr.f –"
---

<p>cheswapr.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cheswapr</code> (UPLO, N, A, LDA, I1, I2)<br />
 <i></i><code>CHESWAPR</code> applies an elementary permutation on the rows and columns of a Hermitian matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cheswapr (characterUPLO, integerN, complex, dimension( lda, n )A, integerLDA, integerI1, integerI2)</h3>
<p><code>CHESWAPR</code> applies an elementary permutation on the rows and columns of a Hermitian matrix. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CHESWAPR applies an elementary permutation on the rows and the columns of
 a hermitian matrix.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the details of the factorization are stored
 as an upper or lower triangular matrix.
 = 'U': Upper triangular, form is A = U*D*U**T;
 = 'L': Lower triangular, form is A = L*D*L**T.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX array, dimension (LDA,N)
 On entry, the NB diagonal matrix D and the multipliers
 used to obtain the factor U or L as computed by CSYTRF.
 On exit, if INFO = 0, the (symmetric) inverse of the original
 matrix. If UPLO = 'U', the upper triangular part of the
 inverse is formed and the part of A below the diagonal is not
 referenced; if UPLO = 'L' the lower triangular part of the
 inverse is formed and the part of A above the diagonal is
 not referenced.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>I1</i> </p>
<pre> I1 is INTEGER
 Index of the first row to swap</pre>
<p><i>I2</i> </p>
<pre> I2 is INTEGER
 Index of the second row to swap</pre>
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
<p> Definition at line 103 of file cheswapr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
