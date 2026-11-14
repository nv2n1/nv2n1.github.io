---
title: "cgbcon-f(3)"
name: "cgbcon-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgbcon-f/"
description: "cgbcon.f –"
---

<p>cgbcon.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cgbcon</code> (NORM, N, KL, KU, AB, LDAB, IPIV, ANORM, RCOND, WORK, RWORK, INFO)<br />
 <i></i><code>CGBCON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgbcon (characterNORM, integerN, integerKL, integerKU, complex, dimension( ldab, * )AB, integerLDAB, integer, dimension( * )IPIV, realANORM, realRCOND, complex, dimension( * )WORK, real, dimension( * )RWORK, integerINFO)</h3>
<p><code>CGBCON</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CGBCON estimates the reciprocal of the condition number of a complex
 general band matrix A, in either the 1-norm or the infinity-norm,
 using the LU factorization computed by CGBTRF.
 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as
 RCOND = 1 / ( norm(A) * norm(inv(A)) ).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>NORM</i> </p>
<pre> NORM is CHARACTER*1
 Specifies whether the 1-norm condition number or the
 infinity-norm condition number is required:
 = '1' or 'O': 1-norm;
 = 'I': Infinity-norm.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>KL</i> </p>
<pre> KL is INTEGER
 The number of subdiagonals within the band of A. KL &gt;= 0.</pre>
<p><i>KU</i> </p>
<pre> KU is INTEGER
 The number of superdiagonals within the band of A. KU &gt;= 0.</pre>
<p><i>AB</i> </p>
<pre> AB is COMPLEX array, dimension (LDAB,N)
 Details of the LU factorization of the band matrix A, as
 computed by CGBTRF. U is stored as an upper triangular band
 matrix with KL+KU superdiagonals in rows 1 to KL+KU+1, and
 the multipliers used during the factorization are stored in
 rows KL+KU+2 to 2*KL+KU+1.</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array AB. LDAB &gt;= 2*KL+KU+1.</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 The pivot indices; for 1 &lt;= i &lt;= N, row i of the matrix was
 interchanged with row IPIV(i).</pre>
<p><i>ANORM</i> </p>
<pre> ANORM is REAL
 If NORM = '1' or 'O', the 1-norm of the original matrix A.
 If NORM = 'I', the infinity-norm of the original matrix A.</pre>
<p><i>RCOND</i> </p>
<pre> RCOND is REAL
 The reciprocal of the condition number of the matrix A,
 computed as RCOND = 1/(norm(A) * norm(inv(A))).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (2*N)</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is REAL array, dimension (N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
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
<p> Definition at line 147 of file cgbcon.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
