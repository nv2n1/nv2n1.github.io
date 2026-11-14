---
title: "csyswapr-f(3)"
name: "csyswapr-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-csyswapr-f/"
description: "csyswapr.f –"
---

<p>csyswapr.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>csyswapr</code> (UPLO, N, A, LDA, I1, I2)<br />
 <i></i><code>CSYSWAPR</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine csyswapr (characterUPLO, integerN, complex, dimension( lda, n )A, integerLDA, integerI1, integerI2)</h3>
<p><code>CSYSWAPR</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CSYSWAPR applies an elementary permutation on the rows and the columns of
 a symmetric matrix.</pre>
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
<dd>November 2011</dl>
<p> Definition at line 103 of file csyswapr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
