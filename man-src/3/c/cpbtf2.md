---
title: "cpbtf2(3)"
name: "cpbtf2"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpbtf2/"
description: "cpbtf2.f –"
---

<h2 class="name">NAME</h2>
<p> cpbtf2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cpbtf2</code> (UPLO, N, KD, AB, LDAB, INFO)<br />
 <i></i><code>CPBTF2</code> computes the Cholesky factorization of a symmetric/Hermitian positive definite band matrix (unblocked algorithm).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cpbtf2 (characterUPLO, integerN, integerKD, complex, dimension( ldab, * )AB, integerLDAB, integerINFO)</h3>
<p> <code>CPBTF2</code> computes the Cholesky factorization of a symmetric/Hermitian positive definite band matrix (unblocked algorithm). </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CPBTF2 computes the Cholesky factorization of a complex Hermitian
 positive definite band matrix A.
 The factorization has the form
    A = U**H * U ,  if UPLO = 'U', or
    A = L  * L**H,  if UPLO = 'L',
 where U is an upper triangular matrix, U**H is the conjugate transpose
 of U, and L is lower triangular.
 This is the unblocked version of the algorithm, calling Level 2 BLAS.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          Specifies whether the upper or lower triangular part of the
          Hermitian matrix A is stored:
          = 'U':  Upper triangular
          = 'L':  Lower triangular
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>KD</i> </p>
<pre>
          KD is INTEGER
          The number of super-diagonals of the matrix A if UPLO = 'U',
          or the number of sub-diagonals if UPLO = 'L'.  KD &gt;= 0.
</pre>
<p> <i>AB</i> </p>
<pre><code>
          AB is COMPLEX array, dimension (LDAB,N)
          On entry, the upper or lower triangle of the Hermitian band
          matrix A, stored in the first KD+1 rows of the array.  The
          j-th column of A is stored in the j-th column of the array AB
          as follows:
          if UPLO = 'U', AB(kd+1+i-j,j) = A(i,j) for max(1,j-kd)&lt;=i&lt;=j;
          if UPLO = 'L', AB(1+i-j,j)    = A(i,j) for j&lt;=i&lt;=min(n,j+kd).
          On exit, if INFO = 0, the triangular factor U or L from the
          Cholesky factorization A = U**H *U or A = L*L**H of the band
          matrix A, in the same storage format as A.
</code></pre>
<p> <i>LDAB</i> </p>
<pre>
          LDAB is INTEGER
          The leading dimension of the array AB.  LDAB &gt;= KD+1.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -k, the k-th argument had an illegal value
          &gt; 0: if INFO = k, the leading minor of order k is not
               positive definite, and the factorization could not be
               completed.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
<dd> September 2012</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  The band storage scheme is illustrated by the following example, when
  N = 6, KD = 2, and UPLO = 'U':
  On entry:                       On exit:
      *    *   a13  a24  a35  a46      *    *   u13  u24  u35  u46
      *   a12  a23  a34  a45  a56      *   u12  u23  u34  u45  u56
     a11  a22  a33  a44  a55  a66     u11  u22  u33  u44  u55  u66
  Similarly, if UPLO = 'L' the format of A is as follows:
  On entry:                       On exit:
     a11  a22  a33  a44  a55  a66     l11  l22  l33  l44  l55  l66
     a21  a32  a43  a54  a65   *      l21  l32  l43  l54  l65   *
     a31  a42  a53  a64   *    *      l31  l42  l53  l64   *    *
  Array elements marked * are not used by the routine.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 143 of file cpbtf2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
