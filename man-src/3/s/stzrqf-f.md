---
title: "stzrqf-f(3)"
name: "stzrqf-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stzrqf-f/"
description: "stzrqf.f –"
---

<p>stzrqf.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>stzrqf</code> (M, N, A, LDA, TAU, INFO)<br />
 <i></i><code>STZRQF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine stzrqf (integerM, integerN, real, dimension( lda, * )A, integerLDA, real, dimension( * )TAU, integerINFO)</h3>
<p><code>STZRQF</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> This routine is deprecated and has been replaced by routine STZRZF.
 STZRQF reduces the M-by-N ( M&lt;=N ) real upper trapezoidal matrix A
 to upper triangular form by means of orthogonal transformations.
 The upper trapezoidal matrix A is factored as
 A = ( R 0 ) * Z,
 where Z is an N-by-N orthogonal matrix and R is an M-by-M upper
 triangular matrix.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= M.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,N)
 On entry, the leading M-by-N upper trapezoidal part of the
 array A must contain the matrix to be factorized.
 On exit, the leading M-by-M upper triangular part of A
 contains the upper triangular matrix R, and elements M+1 to
 N of the first M rows of A, with the array TAU, represent the
 orthogonal matrix Z as a product of M elementary reflectors.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>TAU</i> </p>
<pre> TAU is REAL array, dimension (M)
 The scalar factors of the elementary reflectors.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
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
<pre> The factorization is obtained by Householder's method. The kth
 transformation matrix, Z( k ), which is used to introduce zeros into
 the ( m - k + 1 )th row of A, is given in the form
 Z( k ) = ( I 0 ),
 ( 0 T( k ) )
 where
 T( k ) = I - tau*u( k )*u( k )**T, u( k ) = ( 1 ),
 ( 0 )
 ( z( k ) )
 tau is a scalar and z( k ) is an ( n - m ) element vector.
 tau and z( k ) are chosen to annihilate the elements of the kth row
 of X.
 The scalar tau is returned in the kth element of TAU and the vector
 u( k ) in the kth row of A, such that the elements of z( k ) are
 in a( k, m + 1 ), ..., a( k, n ). The elements of R are returned in
 the upper triangular part of A.
 Z is given by
 Z = Z( 1 ) * Z( 2 ) * ... * Z( m ).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 139 of file stzrqf.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
