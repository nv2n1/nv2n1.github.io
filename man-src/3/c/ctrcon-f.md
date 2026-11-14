---
title: "ctrcon-f(3)"
name: "ctrcon-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ctrcon-f/"
description: "ctrcon.f –"
---

<p>ctrcon.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ctrcon</code> (NORM, UPLO, DIAG, N, A, LDA, RCOND, WORK, RWORK, INFO)<br />
 <i></i><code>CTRCON</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ctrcon (characterNORM, characterUPLO, characterDIAG, integerN, complex, dimension( lda, * )A, integerLDA, realRCOND, complex, dimension( * )WORK, real, dimension( * )RWORK, integerINFO)</h3>
<p><code>CTRCON</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CTRCON estimates the reciprocal of the condition number of a
 triangular matrix A, in either the 1-norm or the infinity-norm.
 The norm of A is computed and an estimate is obtained for
 norm(inv(A)), then the reciprocal of the condition number is
 computed as
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
<p><i>A</i> </p>
<pre> A is COMPLEX array, dimension (LDA,N)
 The triangular matrix A. If UPLO = 'U', the leading N-by-N
 upper triangular part of the array A contains the upper
 triangular matrix, and the strictly lower triangular part of
 A is not referenced. If UPLO = 'L', the leading N-by-N lower
 triangular part of the array A contains the lower triangular
 matrix, and the strictly upper triangular part of A is not
 referenced. If DIAG = 'U', the diagonal elements of A are
 also not referenced and are assumed to be 1.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
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
<p> Definition at line 137 of file ctrcon.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
