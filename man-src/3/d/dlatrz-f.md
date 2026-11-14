---
title: "dlatrz-f(3)"
name: "dlatrz-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlatrz-f/"
description: "dlatrz.f –"
---

<p>dlatrz.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlatrz</code> (M, N, L, A, LDA, TAU, WORK)<br />
 <i></i><code>DLATRZ</code> factors an upper trapezoidal matrix by means of orthogonal transformations.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlatrz (integerM, integerN, integerL, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )TAU, double precision, dimension( * )WORK)</h3>
<p><code>DLATRZ</code> factors an upper trapezoidal matrix by means of orthogonal transformations. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLATRZ factors the M-by-(M+L) real upper trapezoidal matrix
 [ A1 A2 ] = [ A(1:M,1:M) A(1:M,N-L+1:N) ] as ( R 0 ) * Z, by means
 of orthogonal transformations. Z is an (M+L)-by-(M+L) orthogonal
 matrix and, R and A1 are M-by-M upper triangular matrices.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0.</pre>
<p><i>L</i> </p>
<pre> L is INTEGER
 The number of columns of the matrix A containing the
 meaningful part of the Householder vectors. N-M &gt;= L &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA,N)
 On entry, the leading M-by-N upper trapezoidal part of the
 array A must contain the matrix to be factorized.
 On exit, the leading M-by-M upper triangular part of A
 contains the upper triangular matrix R, and elements N-L+1 to
 N of the first M rows of A, with the array TAU, represent the
 orthogonal matrix Z as a product of M elementary reflectors.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>TAU</i> </p>
<pre> TAU is DOUBLE PRECISION array, dimension (M)
 The scalar factors of the elementary reflectors.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (M)</pre>
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
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>A. Petitet, Computer Science Dept., Univ. of Tenn., Knoxville, USA</dl>
<p> <code>Further Details: </code></p>
<dl COMPACT>
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
 tau is a scalar and z( k ) is an l element vector. tau and z( k )
 are chosen to annihilate the elements of the kth row of A2.
 The scalar tau is returned in the kth element of TAU and the vector
 u( k ) in the kth row of A2, such that the elements of z( k ) are
 in a( k, l + 1 ), ..., a( k, n ). The elements of R are returned in
 the upper triangular part of A1.
 Z is given by
 Z = Z( 1 ) * Z( 2 ) * ... * Z( m ).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 141 of file dlatrz.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
