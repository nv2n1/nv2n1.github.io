---
title: "zla_porpvgrw(3)"
name: "zla_porpvgrw"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zla_porpvgrw/"
description: "zla_porpvgrw.f –"
---

<p>zla_porpvgrw.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>DOUBLE PRECISION function <code>zla_porpvgrw</code> (UPLO, NCOLS, A, LDA, AF, LDAF, WORK)<br />
 <i></i><code>ZLA_PORPVGRW</code> computes the reciprocal pivot growth factor norm(A)/norm(U) for a symmetric or Hermitian positive-definite matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function zla_porpvgrw (character*1UPLO, integerNCOLS, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldaf, * )AF, integerLDAF, double precision, dimension( * )WORK)</h3>
<p><code>ZLA_PORPVGRW</code> computes the reciprocal pivot growth factor norm(A)/norm(U) for a symmetric or Hermitian positive-definite matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLA_PORPVGRW computes the reciprocal pivot growth factor
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
<p><i>NCOLS</i> </p>
<pre> NCOLS is INTEGER
 The number of columns of the matrix A. NCOLS &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the N-by-N matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>AF</i> </p>
<pre> AF is COMPLEX*16 array, dimension (LDAF,N)
 The triangular factor U or L from the Cholesky factorization
 A = U**T*U or A = L*L**T, as computed by ZPOTRF.</pre>
<p><i>LDAF</i> </p>
<pre> LDAF is INTEGER
 The leading dimension of the array AF. LDAF &gt;= max(1,N).</pre>
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
<p> Definition at line 107 of file zla_porpvgrw.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
