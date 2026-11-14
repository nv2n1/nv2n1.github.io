---
title: "chetri-f(3)"
name: "chetri-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chetri-f/"
description: "chetri.f –"
---

<p>chetri.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>chetri</code> (UPLO, N, A, LDA, IPIV, WORK, INFO)<br />
 <i></i><code>CHETRI</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine chetri (characterUPLO, integerN, complex, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, complex, dimension( * )WORK, integerINFO)</h3>
<p><code>CHETRI</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CHETRI computes the inverse of a complex Hermitian indefinite matrix
 A using the factorization A = U*D*U**H or A = L*D*L**H computed by
 CHETRF.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the details of the factorization are stored
 as an upper or lower triangular matrix.
 = 'U': Upper triangular, form is A = U*D*U**H;
 = 'L': Lower triangular, form is A = L*D*L**H.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX array, dimension (LDA,N)
 On entry, the block diagonal matrix D and the multipliers
 used to obtain the factor U or L as computed by CHETRF.
 On exit, if INFO = 0, the (Hermitian) inverse of the original
 matrix. If UPLO = 'U', the upper triangular part of the
 inverse is formed and the part of A below the diagonal is not
 referenced; if UPLO = 'L' the lower triangular part of the
 inverse is formed and the part of A above the diagonal is
 not referenced.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 Details of the interchanges and the block structure of D
 as determined by CHETRF.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, D(i,i) = 0; the matrix is singular and its
 inverse could not be computed.</pre>
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
<p> Definition at line 115 of file chetri.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
