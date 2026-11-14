---
title: "zla_syrpvgrw(3)"
name: "zla_syrpvgrw"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zla_syrpvgrw/"
description: "zla_syrpvgrw.f –"
---

<p>zla_syrpvgrw.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>DOUBLE PRECISION function <code>zla_syrpvgrw</code> (UPLO, N, INFO, A, LDA, AF, LDAF, IPIV, WORK)<br />
 <i></i><code>ZLA_SYRPVGRW</code> computes the reciprocal pivot growth factor norm(A)/norm(U) for a symmetric indefinite matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function zla_syrpvgrw (character*1UPLO, integerN, integerINFO, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldaf, * )AF, integerLDAF, integer, dimension( * )IPIV, double precision, dimension( * )WORK)</h3>
<p><code>ZLA_SYRPVGRW</code> computes the reciprocal pivot growth factor norm(A)/norm(U) for a symmetric indefinite matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLA_SYRPVGRW computes the reciprocal pivot growth factor
 norm(A)/norm(U). The &quot;max absolute element&quot; norm is used. If this is
 much less than 1, the stability of the LU factorization of the
 (equilibrated) matrix A could be poor. This also means that the
 solution X, estimated condition numbers, and error bounds could be
 unreliable.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
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
 The value of INFO returned from ZSYTRF, .i.e., the pivot in
 column INFO is exactly 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the N-by-N matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>AF</i> </p>
<pre> AF is COMPLEX*16 array, dimension (LDAF,N)
 The block diagonal matrix D and the multipliers used to
 obtain the factor U or L as computed by ZSYTRF.</pre>
<p><i>LDAF</i> </p>
<pre> LDAF is INTEGER
 The leading dimension of the array AF. LDAF &gt;= max(1,N).</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 Details of the interchanges and the block structure of D
 as determined by ZSYTRF.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (2*N)</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> Definition at line 123 of file zla_syrpvgrw.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
