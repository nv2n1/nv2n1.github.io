---
title: "ssytf2_rook(3)"
name: "ssytf2_rook"
section: "3"
letter: "s"
url: "/docs/linux/man/3-ssytf2_rook/"
description: "ssytf2_rook.f –"
---

<p>ssytf2_rook.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ssytf2_rook</code> (UPLO, N, A, LDA, IPIV, INFO)<br />
 <i></i><code>SSYTF2_ROOK</code> computes the factorization of a real symmetric indefinite matrix using the bounded Bunch-Kaufman (&#8216;rook&#8217;) diagonal pivoting method (unblocked algorithm).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ssytf2_rook (characterUPLO, integerN, real, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, integerINFO)</h3>
<p><code>SSYTF2_ROOK</code> computes the factorization of a real symmetric indefinite matrix using the bounded Bunch-Kaufman (&#8216;rook&#8217;) diagonal pivoting method (unblocked algorithm). </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SSYTF2_ROOK computes the factorization of a real symmetric matrix A
 using the bounded Bunch-Kaufman (&quot;rook&quot;) diagonal pivoting method:
 A = U*D*U**T or A = L*D*L**T
 where U (or L) is a product of permutation and unit upper (lower)
 triangular matrices, U**T is the transpose of U, and D is symmetric and
 block diagonal with 1-by-1 and 2-by-2 diagonal blocks.
 This is the unblocked version of the algorithm, calling Level 2 BLAS.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the upper or lower triangular part of the
 symmetric matrix A is stored:
 = 'U': Upper triangular
 = 'L': Lower triangular</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,N)
 On entry, the symmetric matrix A. If UPLO = 'U', the leading
 n-by-n upper triangular part of A contains the upper
 triangular part of the matrix A, and the strictly lower
 triangular part of A is not referenced. If UPLO = 'L', the
 leading n-by-n lower triangular part of A contains the lower
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
 If UPLO = 'U':
 If IPIV(k) &gt; 0, then rows and columns k and IPIV(k)
 were interchanged and D(k,k) is a 1-by-1 diagonal block.
 If IPIV(k) &lt; 0 and IPIV(k-1) &lt; 0, then rows and
 columns k and -IPIV(k) were interchanged and rows and
 columns k-1 and -IPIV(k-1) were inerchaged,
 D(k-1:k,k-1:k) is a 2-by-2 diagonal block.
 If UPLO = 'L':
 If IPIV(k) &gt; 0, then rows and columns k and IPIV(k)
 were interchanged and D(k,k) is a 1-by-1 diagonal block.
 If IPIV(k) &lt; 0 and IPIV(k+1) &lt; 0, then rows and
 columns k and -IPIV(k) were interchanged and rows and
 columns k+1 and -IPIV(k+1) were inerchaged,
 D(k:k+1,k:k+1) is a 2-by-2 diagonal block.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -k, the k-th argument had an illegal value
 &gt; 0: if INFO = k, D(k,k) is exactly zero. The factorization
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
<dd>November 2013</dl>
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> If UPLO = 'U', then A = U*D*U**T, where
 U = H(n)*H(n)* ... *P(k)U(k)* ...,
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
 L = <a href="//www.systutorials.com/docs/linux/man/1-P/">P</a>(1)*<a href="//www.systutorials.com/docs/linux/man/1-L/">L</a>(1)* ... *P(k)*L(k)* ...,
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
<p> <code>Contributors: </code></p>
<dl>
<dd>
<pre> November 2013, Igor Kozachenko,
 Computer Science Division,
 University of California, Berkeley
 September 2007, Sven Hammarling, Nicholas J. Higham, Craig Lucas,
 School of Mathematics,
 University of Manchester
 01-01-96 - Based on modifications by
 J. Lewis, Boeing Computer Services Company
 A. Petitet, Computer Science Dept., Univ. of Tenn., Knoxville abd , USA</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 195 of file ssytf2_rook.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
