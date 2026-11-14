---
title: "cla_gbrpvgrw-f(3)"
name: "cla_gbrpvgrw-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cla_gbrpvgrw-f/"
description: "cla_gbrpvgrw.f –"
---

<p>cla_gbrpvgrw.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>REAL function <code>cla_gbrpvgrw</code> (N, KL, KU, NCOLS, AB, LDAB, AFB, LDAFB)<br />
 <i></i><code>CLA_GBRPVGRW</code> computes the reciprocal pivot growth factor norm(A)/norm(U) for a general banded matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function cla_gbrpvgrw (integerN, integerKL, integerKU, integerNCOLS, complex, dimension( ldab, * )AB, integerLDAB, complex, dimension( ldafb, * )AFB, integerLDAFB)</h3>
<p><code>CLA_GBRPVGRW</code> computes the reciprocal pivot growth factor norm(A)/norm(U) for a general banded matrix. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CLA_GBRPVGRW computes the reciprocal pivot growth factor
 norm(A)/norm(U). The &quot;max absolute element&quot; norm is used. If this is
 much less than 1, the stability of the LU factorization of the
 (equilibrated) matrix A could be poor. This also means that the
 solution X, estimated condition numbers, and error bounds could be
 unreliable.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of linear equations, i.e., the order of the
 matrix A. N &gt;= 0.</pre>
<p><i>KL</i> </p>
<pre> KL is INTEGER
 The number of subdiagonals within the band of A. KL &gt;= 0.</pre>
<p><i>KU</i> </p>
<pre> KU is INTEGER
 The number of superdiagonals within the band of A. KU &gt;= 0.</pre>
<p><i>NCOLS</i> </p>
<pre> NCOLS is INTEGER
 The number of columns of the matrix A. NCOLS &gt;= 0.</pre>
<p><i>AB</i> </p>
<pre> AB is COMPLEX array, dimension (LDAB,N)
 On entry, the matrix A in band storage, in rows 1 to KL+KU+1.
 The j-th column of A is stored in the j-th column of the
 array AB as follows:
 AB(KU+1+i-j,j) = A(i,j) for max(1,j-KU)&lt;=i&lt;=min(N,j+kl)</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array AB. LDAB &gt;= KL+KU+1.</pre>
<p><i>AFB</i> </p>
<pre> AFB is COMPLEX array, dimension (LDAFB,N)
 Details of the LU factorization of the band matrix A, as
 computed by CGBTRF. U is stored as an upper triangular
 band matrix with KL+KU superdiagonals in rows 1 to KL+KU+1,
 and the multipliers used during the factorization are stored
 in rows KL+KU+2 to 2*KL+KU+1.</pre>
<p><i>LDAFB</i> </p>
<pre> LDAFB is INTEGER
 The leading dimension of the array AFB. LDAFB &gt;= 2*KL+KU+1.</pre>
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
<p> Definition at line 117 of file cla_gbrpvgrw.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
