---
title: "cpptrf(3)"
name: "cpptrf"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpptrf/"
description: "cpptrf.f –"
---

<h2 class="name">NAME</h2>
<p> cpptrf.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cpptrf</code> (UPLO, N, AP, INFO)<br />
 <i></i><code>CPPTRF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cpptrf (characterUPLO, integerN, complex, dimension( * )AP, integerINFO)</h3>
<p> <code>CPPTRF</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CPPTRF computes the Cholesky factorization of a complex Hermitian
 positive definite matrix A stored in packed format.
 The factorization has the form
    A = U**H * U,  if UPLO = 'U', or
    A = L  * L**H,  if UPLO = 'L',
 where U is an upper triangular matrix and L is lower triangular.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  Upper triangle of A is stored;
          = 'L':  Lower triangle of A is stored.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>AP</i> </p>
<pre><code>
          AP is COMPLEX array, dimension (N*(N+1)/2)
          On entry, the upper or lower triangle of the Hermitian matrix
          A, packed columnwise in a linear array.  The j-th column of A
          is stored in the array AP as follows:
          if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
          if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
          See below for further details.
          On exit, if INFO = 0, the triangular factor U or L from the
          Cholesky factorization A = U**H*U or A = L*L**H, in the same
          storage format as A.
</code></pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
          &gt; 0:  if INFO = i, the leading minor of order i is not
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
<dd> November 2011</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  The packed storage scheme is illustrated by the following example
  when N = 4, UPLO = 'U':
  Two-dimensional storage of the Hermitian matrix A:
     a11 a12 a13 a14
         a22 a23 a24
             a33 a34     (aij = conjg(aji))
                 a44
  Packed storage of the upper triangle of A:
  AP = [ a11, a12, a22, a13, a23, a33, a14, a24, a34, a44 ]
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 120 of file cpptrf.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
