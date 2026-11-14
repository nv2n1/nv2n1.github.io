---
title: "cgbbrd-f(3)"
name: "cgbbrd-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgbbrd-f/"
description: "cgbbrd.f –"
---

<p>cgbbrd.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cgbbrd</code> (VECT, M, N, NCC, KL, KU, AB, LDAB, D, E, Q, LDQ, PT, LDPT, C, LDC, WORK, RWORK, INFO)<br />
 <i></i><code>CGBBRD</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgbbrd (characterVECT, integerM, integerN, integerNCC, integerKL, integerKU, complex, dimension( ldab, * )AB, integerLDAB, real, dimension( * )D, real, dimension( * )E, complex, dimension( ldq, * )Q, integerLDQ, complex, dimension( ldpt, * )PT, integerLDPT, complex, dimension( ldc, * )C, integerLDC, complex, dimension( * )WORK, real, dimension( * )RWORK, integerINFO)</h3>
<p><code>CGBBRD</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CGBBRD reduces a complex general m-by-n band matrix A to real upper
 bidiagonal form B by a unitary transformation: Q**H * A * P = B.
 The routine computes B, and optionally forms Q or P**H, or computes
 Q**H*C for a given matrix C.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>VECT</i> </p>
<pre> VECT is CHARACTER*1
 Specifies whether or not the matrices Q and P**H are to be
 formed.
 = 'N': do not form Q or P**H;
 = 'Q': form Q only;
 = 'P': form P**H only;
 = 'B': form both.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0.</pre>
<p><i>NCC</i> </p>
<pre> NCC is INTEGER
 The number of columns of the matrix C. NCC &gt;= 0.</pre>
<p><i>KL</i> </p>
<pre> KL is INTEGER
 The number of subdiagonals of the matrix A. KL &gt;= 0.</pre>
<p><i>KU</i> </p>
<pre> KU is INTEGER
 The number of superdiagonals of the matrix A. KU &gt;= 0.</pre>
<p><i>AB</i> </p>
<pre> AB is COMPLEX array, dimension (LDAB,N)
 On entry, the m-by-n band matrix A, stored in rows 1 to
 KL+KU+1. The j-th column of A is stored in the j-th column of
 the array AB as follows:
 AB(ku+1+i-j,j) = A(i,j) for max(1,j-ku)&lt;=i&lt;=min(m,j+kl).
 On exit, A is overwritten by values generated during the
 reduction.</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array A. LDAB &gt;= KL+KU+1.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (min(M,N))
 The diagonal elements of the bidiagonal matrix B.</pre>
<p><i>E</i> </p>
<pre> E is REAL array, dimension (min(M,N)-1)
 The superdiagonal elements of the bidiagonal matrix B.</pre>
<p><i>Q</i> </p>
<pre> Q is COMPLEX array, dimension (LDQ,M)
 If VECT = 'Q' or 'B', the m-by-m unitary matrix Q.
 If VECT = 'N' or 'P', the array Q is not referenced.</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q.
 LDQ &gt;= max(1,M) if VECT = 'Q' or 'B'; LDQ &gt;= 1 otherwise.</pre>
<p><i>PT</i> </p>
<pre> PT is COMPLEX array, dimension (LDPT,N)
 If VECT = 'P' or 'B', the n-by-n unitary matrix P'.
 If VECT = 'N' or 'Q', the array PT is not referenced.</pre>
<p><i>LDPT</i> </p>
<pre> LDPT is INTEGER
 The leading dimension of the array PT.
 LDPT &gt;= max(1,N) if VECT = 'P' or 'B'; LDPT &gt;= 1 otherwise.</pre>
<p><i>C</i> </p>
<pre> C is COMPLEX array, dimension (LDC,NCC)
 On entry, an m-by-ncc matrix C.
 On exit, C is overwritten by Q**H*C.
 C is not referenced if NCC = 0.</pre>
<p><i>LDC</i> </p>
<pre> LDC is INTEGER
 The leading dimension of the array C.
 LDC &gt;= max(1,M) if NCC &gt; 0; LDC &gt;= 1 if NCC = 0.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (max(M,N))</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is REAL array, dimension (max(M,N))</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.</pre>
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
<p> Definition at line 193 of file cgbbrd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
