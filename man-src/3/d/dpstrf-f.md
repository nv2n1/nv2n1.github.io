---
title: "dpstrf-f(3)"
name: "dpstrf-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpstrf-f/"
description: "dpstrf.f –"
---

<p>dpstrf.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dpstrf</code> (UPLO, N, A, LDA, PIV, RANK, TOL, WORK, INFO)<br />
 <i></i><code>DPSTRF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dpstrf (characterUPLO, integerN, double precision, dimension( lda, * )A, integerLDA, integer, dimension( n )PIV, integerRANK, double precisionTOL, double precision, dimension( 2*n )WORK, integerINFO)</h3>
<p><code>DPSTRF</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DPSTRF computes the Cholesky factorization with complete
 pivoting of a real symmetric positive semidefinite matrix A.
 The factorization has the form
 P**T * A * P = U**T * U , if UPLO = 'U',
 P**T * A * P = L * L**T, if UPLO = 'L',
 where U is an upper triangular matrix and L is lower triangular, and
 P is stored as vector PIV.
 This algorithm does not attempt to check that A is positive
 semidefinite. This version of the algorithm calls level 3 BLAS.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the upper or lower triangular part of the
 symmetric matrix A is stored.
 = 'U': Upper triangular
 = 'L': Lower triangular</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA,N)
 On entry, the symmetric matrix A. If UPLO = 'U', the leading
 n by n upper triangular part of A contains the upper
 triangular part of the matrix A, and the strictly lower
 triangular part of A is not referenced. If UPLO = 'L', the
 leading n by n lower triangular part of A contains the lower
 triangular part of the matrix A, and the strictly upper
 triangular part of A is not referenced.
 On exit, if INFO = 0, the factor U or L from the Cholesky
 factorization as above.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>PIV</i> </p>
<pre> PIV is INTEGER array, dimension (N)
 PIV is such that the nonzero entries are P( PIV(K), K ) = 1.</pre>
<p><i>RANK</i> </p>
<pre> RANK is INTEGER
 The rank of A given by the number of steps the algorithm
 completed.</pre>
<p><i>TOL</i> </p>
<pre> TOL is DOUBLE PRECISION
 User defined tolerance. If TOL &lt; 0, then N*U*MAX( A(K,K) )
 will be used. The algorithm terminates at the (K-1)st step
 if the pivot &lt;= TOL.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (2*N)
 Work space.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 &lt; 0: If INFO = -K, the K-th argument had an illegal value,
 = 0: algorithm completed successfully, and
 &gt; 0: the matrix A is either rank deficient with computed rank
 as returned in RANK, or is indefinite. See Section 7 of
 LAPACK Working Note #161 for further information.</pre>
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
<p> Definition at line 141 of file dpstrf.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
