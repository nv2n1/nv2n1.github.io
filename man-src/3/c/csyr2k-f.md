---
title: "csyr2k-f(3)"
name: "csyr2k-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-csyr2k-f/"
description: "csyr2k.f –"
---

<p>csyr2k.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>csyr2k</code> (UPLO, TRANS, N, K, ALPHA, A, LDA, B, LDB, BETA, C, LDC)<br />
 <i></i><code>CSYR2K</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine csyr2k (characterUPLO, characterTRANS, integerN, integerK, complexALPHA, complex, dimension(lda,*)A, integerLDA, complex, dimension(ldb,*)B, integerLDB, complexBETA, complex, dimension(ldc,*)C, integerLDC)</h3>
<p><code>CSYR2K</code> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CSYR2K performs one of the symmetric rank 2k operations
 C := alpha*A*B**T + alpha*B*A**T + beta*C,
 or
 C := alpha*A**T*B + alpha*B**T*A + beta*C,
 where alpha and beta are scalars, C is an n by n symmetric matrix
 and A and B are n by k matrices in the first case and k by n
 matrices in the second case.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 On entry, UPLO specifies whether the upper or lower
 triangular part of the array C is to be referenced as
 follows:
 UPLO = 'U' or 'u' Only the upper triangular part of C
 is to be referenced.
 UPLO = 'L' or 'l' Only the lower triangular part of C
 is to be referenced.</pre>
<p><i>TRANS</i> </p>
<pre> TRANS is CHARACTER*1
 On entry, TRANS specifies the operation to be performed as
 follows:
 TRANS = 'N' or 'n' C := alpha*A*B**T + alpha*B*A**T +
 beta*C.
 TRANS = 'T' or 't' C := alpha*A**T*B + alpha*B**T*A +
 beta*C.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 On entry, N specifies the order of the matrix C. N must be
 at least zero.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER
 On entry with TRANS = 'N' or 'n', K specifies the number
 of columns of the matrices A and B, and on entry with
 TRANS = 'T' or 't', K specifies the number of rows of the
 matrices A and B. K must be at least zero.</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is COMPLEX
 On entry, ALPHA specifies the scalar alpha.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX array of DIMENSION ( LDA, ka ), where ka is
 k when TRANS = 'N' or 'n', and is n otherwise.
 Before entry with TRANS = 'N' or 'n', the leading n by k
 part of the array A must contain the matrix A, otherwise
 the leading k by n part of the array A must contain the
 matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 On entry, LDA specifies the first dimension of A as declared
 in the calling (sub) program. When TRANS = 'N' or 'n'
 then LDA must be at least max( 1, n ), otherwise LDA must
 be at least max( 1, k ).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX array of DIMENSION ( LDB, kb ), where kb is
 k when TRANS = 'N' or 'n', and is n otherwise.
 Before entry with TRANS = 'N' or 'n', the leading n by k
 part of the array B must contain the matrix B, otherwise
 the leading k by n part of the array B must contain the
 matrix B.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 On entry, LDB specifies the first dimension of B as declared
 in the calling (sub) program. When TRANS = 'N' or 'n'
 then LDB must be at least max( 1, n ), otherwise LDB must
 be at least max( 1, k ).</pre>
<p><i>BETA</i> </p>
<pre> BETA is COMPLEX
 On entry, BETA specifies the scalar beta.</pre>
<p><i>C</i> </p>
<pre> C is COMPLEX array of DIMENSION ( LDC, n ).
 Before entry with UPLO = 'U' or 'u', the leading n by n
 upper triangular part of the array C must contain the upper
 triangular part of the symmetric matrix and the strictly
 lower triangular part of C is not referenced. On exit, the
 upper triangular part of the array C is overwritten by the
 upper triangular part of the updated matrix.
 Before entry with UPLO = 'L' or 'l', the leading n by n
 lower triangular part of the array C must contain the lower
 triangular part of the symmetric matrix and the strictly
 upper triangular part of C is not referenced. On exit, the
 lower triangular part of the array C is overwritten by the
 lower triangular part of the updated matrix.</pre>
<p><i>LDC</i> </p>
<pre> LDC is INTEGER
 On entry, LDC specifies the first dimension of C as declared
 in the calling (sub) program. LDC must be at least
 max( 1, n ).</pre>
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
<p> Definition at line 189 of file csyr2k.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
