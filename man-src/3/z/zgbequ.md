---
title: "zgbequ(3)"
name: "zgbequ"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zgbequ/"
description: "zgbequ.f –"
---

<p>zgbequ.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zgbequ</code> (M, N, KL, KU, AB, LDAB, R, C, ROWCND, COLCND, AMAX, INFO)<br />
 <i></i><code>ZGBEQU</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zgbequ (integerM, integerN, integerKL, integerKU, complex*16, dimension( ldab, * )AB, integerLDAB, double precision, dimension( * )R, double precision, dimension( * )C, double precisionROWCND, double precisionCOLCND, double precisionAMAX, integerINFO)</h3>
<p><code>ZGBEQU</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZGBEQU computes row and column scalings intended to equilibrate an
 M-by-N band matrix A and reduce its condition number. R returns the
 row scale factors and C the column scale factors, chosen to try to
 make the largest element in each row and column of the matrix B with
 elements B(i,j)=R(i)*A(i,j)*C(j) have absolute value 1.
 R(i) and C(j) are restricted to be between SMLNUM = smallest safe
 number and BIGNUM = largest safe number. Use of these scaling
 factors is not guaranteed to reduce the condition number of A but
 works well in practice.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0.</pre>
<p><i>KL</i> </p>
<pre> KL is INTEGER
 The number of subdiagonals within the band of A. KL &gt;= 0.</pre>
<p><i>KU</i> </p>
<pre> KU is INTEGER
 The number of superdiagonals within the band of A. KU &gt;= 0.</pre>
<p><i>AB</i> </p>
<pre> AB is COMPLEX*16 array, dimension (LDAB,N)
 The band matrix A, stored in rows 1 to KL+KU+1. The j-th
 column of A is stored in the j-th column of the array AB as
 follows:
 AB(ku+1+i-j,j) = A(i,j) for max(1,j-ku)&lt;=i&lt;=min(m,j+kl).</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array AB. LDAB &gt;= KL+KU+1.</pre>
<p><i>R</i> </p>
<pre> R is DOUBLE PRECISION array, dimension (M)
 If INFO = 0, or INFO &gt; M, R contains the row scale factors
 for A.</pre>
<p><i>C</i> </p>
<pre> C is DOUBLE PRECISION array, dimension (N)
 If INFO = 0, C contains the column scale factors for A.</pre>
<p><i>ROWCND</i> </p>
<pre> ROWCND is DOUBLE PRECISION
 If INFO = 0 or INFO &gt; M, ROWCND contains the ratio of the
 smallest R(i) to the largest R(i). If ROWCND &gt;= 0.1 and
 AMAX is neither too large nor too small, it is not worth
 scaling by R.</pre>
<p><i>COLCND</i> </p>
<pre> COLCND is DOUBLE PRECISION
 If INFO = 0, COLCND contains the ratio of the smallest
 C(i) to the largest C(i). If COLCND &gt;= 0.1, it is not
 worth scaling by C.</pre>
<p><i>AMAX</i> </p>
<pre> AMAX is DOUBLE PRECISION
 Absolute value of largest matrix element. If AMAX is very
 close to overflow or very close to underflow, the matrix
 should be scaled.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, and i is
 &lt;= M: the i-th row of A is exactly zero
 &gt; M: the (i-M)-th column of A is exactly zero</pre>
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
<p> Definition at line 154 of file zgbequ.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
