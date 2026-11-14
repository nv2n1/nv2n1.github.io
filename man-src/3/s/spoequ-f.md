---
title: "spoequ-f(3)"
name: "spoequ-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spoequ-f/"
description: "spoequ.f –"
---

<p>spoequ.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>spoequ</code> (N, A, LDA, S, SCOND, AMAX, INFO)<br />
 <i></i><code>SPOEQU</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine spoequ (integerN, real, dimension( lda, * )A, integerLDA, real, dimension( * )S, realSCOND, realAMAX, integerINFO)</h3>
<p><code>SPOEQU</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SPOEQU computes row and column scalings intended to equilibrate a
 symmetric positive definite matrix A and reduce its condition number
 (with respect to the two-norm). S contains the scale factors,
 S(i) = 1/sqrt(A(i,i)), chosen so that the scaled matrix B with
 elements B(i,j) = S(i)*A(i,j)*S(j) has ones on the diagonal. This
 choice of S puts the condition number of B within a factor N of the
 smallest possible condition number over all possible diagonal
 scalings.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,N)
 The N-by-N symmetric positive definite matrix whose scaling
 factors are to be computed. Only the diagonal elements of A
 are referenced.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>S</i> </p>
<pre> S is REAL array, dimension (N)
 If INFO = 0, S contains the scale factors for A.</pre>
<p><i>SCOND</i> </p>
<pre> SCOND is REAL
 If INFO = 0, S contains the ratio of the smallest S(i) to
 the largest S(i). If SCOND &gt;= 0.1 and AMAX is neither too
 large nor too small, it is not worth scaling by S.</pre>
<p><i>AMAX</i> </p>
<pre> AMAX is REAL
 Absolute value of largest matrix element. If AMAX is very
 close to overflow or very close to underflow, the matrix
 should be scaled.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, the i-th diagonal element is nonpositive.</pre>
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
<p> Definition at line 113 of file spoequ.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
