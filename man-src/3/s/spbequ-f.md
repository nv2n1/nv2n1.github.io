---
title: "spbequ-f(3)"
name: "spbequ-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spbequ-f/"
description: "spbequ.f –"
---

<p>spbequ.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>spbequ</code> (UPLO, N, KD, AB, LDAB, S, SCOND, AMAX, INFO)<br />
 <i></i><code>SPBEQU</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine spbequ (characterUPLO, integerN, integerKD, real, dimension( ldab, * )AB, integerLDAB, real, dimension( * )S, realSCOND, realAMAX, integerINFO)</h3>
<p><code>SPBEQU</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SPBEQU computes row and column scalings intended to equilibrate a
 symmetric positive definite band matrix A and reduce its condition
 number (with respect to the two-norm). S contains the scale factors,
 S(i) = 1/sqrt(A(i,i)), chosen so that the scaled matrix B with
 elements B(i,j) = S(i)*A(i,j)*S(j) has ones on the diagonal. This
 choice of S puts the condition number of B within a factor N of the
 smallest possible condition number over all possible diagonal
 scalings.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangular of A is stored;
 = 'L': Lower triangular of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>KD</i> </p>
<pre> KD is INTEGER
 The number of superdiagonals of the matrix A if UPLO = 'U',
 or the number of subdiagonals if UPLO = 'L'. KD &gt;= 0.</pre>
<p><i>AB</i> </p>
<pre> AB is REAL array, dimension (LDAB,N)
 The upper or lower triangle of the symmetric band matrix A,
 stored in the first KD+1 rows of the array. The j-th column
 of A is stored in the j-th column of the array AB as follows:
 if UPLO = 'U', AB(kd+1+i-j,j) = A(i,j) for max(1,j-kd)&lt;=i&lt;=j;
 if UPLO = 'L', AB(1+i-j,j) = A(i,j) for j&lt;=i&lt;=min(n,j+kd).</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array A. LDAB &gt;= KD+1.</pre>
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
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
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
<p> Definition at line 130 of file spbequ.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
