---
title: "dgemm-f(3)"
name: "dgemm-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgemm-f/"
description: "dgemm.f –"
---

<p>dgemm.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dgemm</code> (TRANSA, TRANSB, M, N, K, ALPHA, A, LDA, B, LDB, BETA, C, LDC)<br />
 <i></i><code>DGEMM</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgemm (characterTRANSA, characterTRANSB, integerM, integerN, integerK, double precisionALPHA, double precision, dimension(lda,*)A, integerLDA, double precision, dimension(ldb,*)B, integerLDB, double precisionBETA, double precision, dimension(ldc,*)C, integerLDC)</h3>
<p><code>DGEMM</code> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DGEMM performs one of the matrix-matrix operations
 C := alpha*op( A )*op( B ) + beta*C,
 where op( X ) is one of
 op( X ) = X or op( X ) = X**T,
 alpha and beta are scalars, and A, B and C are matrices, with op( A )
 an m by k matrix, op( B ) a k by n matrix and C an m by n matrix.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>TRANSA</i> </p>
<pre> TRANSA is CHARACTER*1
 On entry, TRANSA specifies the form of op( A ) to be used in
 the matrix multiplication as follows:
 TRANSA = 'N' or 'n', op( A ) = A.
 TRANSA = 'T' or 't', op( A ) = A**T.
 TRANSA = 'C' or 'c', op( A ) = A**T.</pre>
<p><i>TRANSB</i> </p>
<pre> TRANSB is CHARACTER*1
 On entry, TRANSB specifies the form of op( B ) to be used in
 the matrix multiplication as follows:
 TRANSB = 'N' or 'n', op( B ) = B.
 TRANSB = 'T' or 't', op( B ) = B**T.
 TRANSB = 'C' or 'c', op( B ) = B**T.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 On entry, M specifies the number of rows of the matrix
 op( A ) and of the matrix C. M must be at least zero.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 On entry, N specifies the number of columns of the matrix
 op( B ) and the number of columns of the matrix C. N must be
 at least zero.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER
 On entry, K specifies the number of columns of the matrix
 op( A ) and the number of rows of the matrix op( B ). K must
 be at least zero.</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is DOUBLE PRECISION.
 On entry, ALPHA specifies the scalar alpha.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array of DIMENSION ( LDA, ka ), where ka is
 k when TRANSA = 'N' or 'n', and is m otherwise.
 Before entry with TRANSA = 'N' or 'n', the leading m by k
 part of the array A must contain the matrix A, otherwise
 the leading k by m part of the array A must contain the
 matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 On entry, LDA specifies the first dimension of A as declared
 in the calling (sub) program. When TRANSA = 'N' or 'n' then
 LDA must be at least max( 1, m ), otherwise LDA must be at
 least max( 1, k ).</pre>
<p><i>B</i> </p>
<pre> B is DOUBLE PRECISION array of DIMENSION ( LDB, kb ), where kb is
 n when TRANSB = 'N' or 'n', and is k otherwise.
 Before entry with TRANSB = 'N' or 'n', the leading k by n
 part of the array B must contain the matrix B, otherwise
 the leading n by k part of the array B must contain the
 matrix B.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 On entry, LDB specifies the first dimension of B as declared
 in the calling (sub) program. When TRANSB = 'N' or 'n' then
 LDB must be at least max( 1, k ), otherwise LDB must be at
 least max( 1, n ).</pre>
<p><i>BETA</i> </p>
<pre> BETA is DOUBLE PRECISION.
 On entry, BETA specifies the scalar beta. When BETA is
 supplied as zero then C need not be set on input.</pre>
<p><i>C</i> </p>
<pre> C is DOUBLE PRECISION array of DIMENSION ( LDC, n ).
 Before entry, the leading m by n part of the array C must
 contain the matrix C, except when beta is zero, in which
 case C need not be set on entry.
 On exit, the array C is overwritten by the m by n matrix
 ( alpha*op( A )*op( B ) + beta*C ).</pre>
<p><i>LDC</i> </p>
<pre> LDC is INTEGER
 On entry, LDC specifies the first dimension of C as declared
 in the calling (sub) program. LDC must be at least
 max( 1, m ).</pre>
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
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> Level 3 Blas routine.
 -- Written on 8-February-1989.
 Jack Dongarra, Argonne National Laboratory.
 Iain Duff, AERE Harwell.
 Jeremy Du Croz, Numerical Algorithms Group Ltd.
 Sven Hammarling, Numerical Algorithms Group Ltd.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 188 of file dgemm.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
