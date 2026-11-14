---
title: "ztpcon-f(3)"
name: "ztpcon-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-ztpcon-f/"
description: "ztpcon.f –"
---

<p>ztpcon.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ztpcon</code> (NORM, UPLO, DIAG, N, AP, RCOND, WORK, RWORK, INFO)<br />
 <i></i><code>ZTPCON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ztpcon (characterNORM, characterUPLO, characterDIAG, integerN, complex*16, dimension( * )AP, double precisionRCOND, complex*16, dimension( * )WORK, double precision, dimension( * )RWORK, integerINFO)</h3>
<p><code>ZTPCON</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZTPCON estimates the reciprocal of the condition number of a packed
 triangular matrix A, in either the 1-norm or the infinity-norm.
 The norm of A is computed and an estimate is obtained for
 norm(inv(A)), then the reciprocal of the condition number is
 computed as
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
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': A is upper triangular;
 = 'L': A is lower triangular.</pre>
<p><i>DIAG</i> </p>
<pre> DIAG is CHARACTER*1
 = 'N': A is non-unit triangular;
 = 'U': A is unit triangular.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>AP</i> </p>
<pre> AP is COMPLEX*16 array, dimension (N*(N+1)/2)
 The upper or lower triangular matrix A, packed columnwise in
 a linear array. The j-th column of A is stored in the array
 AP as follows:
 if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
 if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
 If DIAG = 'U', the diagonal elements of A are not referenced
 and are assumed to be 1.</pre>
<p><i>RCOND</i> </p>
<pre> RCOND is DOUBLE PRECISION
 The reciprocal of the condition number of the matrix A,
 computed as RCOND = 1/(norm(A) * norm(inv(A))).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (2*N)</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (N)</pre>
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
<p> Definition at line 130 of file ztpcon.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
