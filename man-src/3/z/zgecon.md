---
title: "zgecon(3)"
name: "zgecon"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zgecon/"
description: "zgecon.f –"
---

<p>zgecon.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zgecon</code> (NORM, N, A, LDA, ANORM, RCOND, WORK, RWORK, INFO)<br />
 <i></i><code>ZGECON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zgecon (characterNORM, integerN, complex*16, dimension( lda, * )A, integerLDA, double precisionANORM, double precisionRCOND, complex*16, dimension( * )WORK, double precision, dimension( * )RWORK, integerINFO)</h3>
<p><code>ZGECON</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZGECON estimates the reciprocal of the condition number of a general
 complex matrix A, in either the 1-norm or the infinity-norm, using
 the LU factorization computed by ZGETRF.
 An estimate is obtained for norm(inv(A)), and the reciprocal of the
 condition number is computed as
 RCOND = 1 / ( norm(A) * norm(inv(A)) ).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>NORM</i> </p>
<pre> NORM is CHARACTER*1
 Specifies whether the 1-norm condition number or the
 infinity-norm condition number is required:
 = '1' or 'O': 1-norm;
 = 'I': Infinity-norm.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 The factors L and U from the factorization A = P*L*U
 as computed by ZGETRF.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>ANORM</i> </p>
<pre> ANORM is DOUBLE PRECISION
 If NORM = '1' or 'O', the 1-norm of the original matrix A.
 If NORM = 'I', the infinity-norm of the original matrix A.</pre>
<p><i>RCOND</i> </p>
<pre> RCOND is DOUBLE PRECISION
 The reciprocal of the condition number of the matrix A,
 computed as RCOND = 1/(norm(A) * norm(inv(A))).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (2*N)</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (2*N)</pre>
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
<p> Definition at line 124 of file zgecon.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
