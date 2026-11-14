---
title: "dla_syrpvgrw-f(3)"
name: "dla_syrpvgrw-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dla_syrpvgrw-f/"
description: "dla_syrpvgrw.f –"
---

<p>dla_syrpvgrw.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>DOUBLE PRECISION function <code>dla_syrpvgrw</code> (UPLO, N, INFO, A, LDA, AF, LDAF, IPIV, WORK)<br />
 <i></i><code>DLA_SYRPVGRW</code> computes the reciprocal pivot growth factor norm(A)/norm(U) for a symmetric indefinite matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function dla_syrpvgrw (character*1UPLO, integerN, integerINFO, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldaf, * )AF, integerLDAF, integer, dimension( * )IPIV, double precision, dimension( * )WORK)</h3>
<p><code>DLA_SYRPVGRW</code> computes the reciprocal pivot growth factor norm(A)/norm(U) for a symmetric indefinite matrix. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLA_SYRPVGRW computes the reciprocal pivot growth factor
 norm(A)/norm(U). The &quot;max absolute element&quot; norm is used. If this is
 much less than 1, the stability of the LU factorization of the
 (equilibrated) matrix A could be poor. This also means that the
 solution X, estimated condition numbers, and error bounds could be
 unreliable.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of linear equations, i.e., the order of the
 matrix A. N &gt;= 0.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 The value of INFO returned from DSYTRF, .i.e., the pivot in
 column INFO is exactly 0.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA,N)
 On entry, the N-by-N matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>AF</i> </p>
<pre> AF is DOUBLE PRECISION array, dimension (LDAF,N)
 The block diagonal matrix D and the multipliers used to
 obtain the factor U or L as computed by DSYTRF.</pre>
<p><i>LDAF</i> </p>
<pre> LDAF is INTEGER
 The leading dimension of the array AF. LDAF &gt;= max(1,N).</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 Details of the interchanges and the block structure of D
 as determined by DSYTRF.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (2*N)</pre>
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
<p> Definition at line 122 of file dla_syrpvgrw.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
