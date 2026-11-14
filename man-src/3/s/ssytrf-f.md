---
title: "ssytrf-f(3)"
name: "ssytrf-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-ssytrf-f/"
description: "ssytrf.f –"
---

<p>ssytrf.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ssytrf</code> (UPLO, N, A, LDA, IPIV, WORK, LWORK, INFO)<br />
 <i></i><code>SSYTRF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ssytrf (characterUPLO, integerN, real, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, real, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code>SSYTRF</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SSYTRF computes the factorization of a real symmetric matrix A using
 the Bunch-Kaufman diagonal pivoting method. The form of the
 factorization is
 A = U*D*U**T or A = L*D*L**T
 where U (or L) is a product of permutation and unit upper (lower)
 triangular matrices, and D is symmetric and block diagonal with 
 1-by-1 and 2-by-2 diagonal blocks.
 This is the blocked version of the algorithm, calling Level 3 BLAS.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,N)
 On entry, the symmetric matrix A. If UPLO = 'U', the leading
 N-by-N upper triangular part of A contains the upper
 triangular part of the matrix A, and the strictly lower
 triangular part of A is not referenced. If UPLO = 'L', the
 leading N-by-N lower triangular part of A contains the lower
 triangular part of the matrix A, and the strictly upper
 triangular part of A is not referenced.
 On exit, the block diagonal matrix D and the multipliers used
 to obtain the factor U or L (see below for further details).</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 Details of the interchanges and the block structure of D.
 If IPIV(k) &gt; 0, then rows and columns k and IPIV(k) were
 interchanged and D(k,k) is a 1-by-1 diagonal block.
 If UPLO = 'U' and IPIV(k) = IPIV(k-1) &lt; 0, then rows and
 columns k-1 and -IPIV(k) were interchanged and D(k-1:k,k-1:k)
 is a 2-by-2 diagonal block. If UPLO = 'L' and IPIV(k) =
 IPIV(k+1) &lt; 0, then rows and columns k+1 and -IPIV(k) were
 interchanged and D(k:k+1,k:k+1) is a 2-by-2 diagonal block.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The length of WORK. LWORK &gt;=1. For best performance
 LWORK &gt;= N*NB, where NB is the block size returned by ILAENV.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, D(i,i) is exactly zero. The factorization
 has been completed, but the block diagonal matrix D is
 exactly singular, and division by zero will occur if it
 is used to solve a system of equations.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> If UPLO = 'U', then A = U*D*U**T, where
 U = H(n)*H(n)* ... &lt;em&gt;P(k)U(k)&lt;/em&gt; ...,
 i.e., U is a product of terms P(k)*U(k), where k decreases from n to
 1 in steps of 1 or 2, and D is a block diagonal matrix with 1-by-1
 and 2-by-2 diagonal blocks D(k). P(k) is a permutation matrix as
 defined by IPIV(k), and U(k) is a unit upper triangular matrix, such
 that if the diagonal block D(k) is of order s (s = 1 or 2), then
 ( I v 0 ) k-s
 U(k) = ( 0 I 0 ) s
 ( 0 0 I ) n-k
 k-s s n-k
 If s = 1, D(k) overwrites A(k,k), and v overwrites A(1:k-1,k).
 If s = 2, the upper triangle of D(k) overwrites A(k-1,k-1), A(k-1,k),
 and A(k,k), and v overwrites A(1:k-2,k-1:k).
 If UPLO = 'L', then A = L*D*L**T, where
 L = <a href="//www.systutorials.com/docs/linux/man/1-P/">P</a>(1)*<a href="//www.systutorials.com/docs/linux/man/1-L/">L</a>(1)* ... &lt;em&gt;P(k)*L(k)&lt;/em&gt; ...,
 i.e., L is a product of terms P(k)*L(k), where k increases from 1 to
 n in steps of 1 or 2, and D is a block diagonal matrix with 1-by-1
 and 2-by-2 diagonal blocks D(k). P(k) is a permutation matrix as
 defined by IPIV(k), and L(k) is a unit lower triangular matrix, such
 that if the diagonal block D(k) is of order s (s = 1 or 2), then
 ( I 0 0 ) k-1
 L(k) = ( 0 I 0 ) s
 ( 0 v I ) n-k-s+1
 k-1 s n-k-s+1
 If s = 1, D(k) overwrites A(k,k), and v overwrites A(k+1:n,k).
 If s = 2, the lower triangle of D(k) overwrites A(k,k), A(k+1,k),
 and A(k+1,k+1), and v overwrites A(k+2:n,k:k+1).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 183 of file ssytrf.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
