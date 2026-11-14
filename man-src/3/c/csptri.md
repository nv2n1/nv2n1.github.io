---
title: "csptri(3)"
name: "csptri"
section: "3"
letter: "c"
url: "/docs/linux/man/3-csptri/"
description: "csptri.f –"
---

<h2 class="name">NAME</h2>
<p> csptri.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>csptri</code> (UPLO, N, AP, IPIV, WORK, INFO)<br />
 <i></i><code>CSPTRI</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine csptri (characterUPLO, integerN, complex, dimension( * )AP, integer, dimension( * )IPIV, complex, dimension( * )WORK, integerINFO)</h3>
<p> <code>CSPTRI</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CSPTRI computes the inverse of a complex symmetric indefinite matrix
 A in packed storage using the factorization A = U*D*U**T or
 A = L*D*L**T computed by CSPTRF.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          Specifies whether the details of the factorization are stored
          as an upper or lower triangular matrix.
          = 'U':  Upper triangular, form is A = U*D*U**T;
          = 'L':  Lower triangular, form is A = L*D*L**T.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>AP</i> </p>
<pre><code>
AP is COMPLEX array, dimension(N *(N + 1) / 2) On entry, the block diagonal matrix D and the multipliers used to obtain the factor U or L as computed by CSPTRF,
    stored as a packed triangular matrix.On exit, if INFO = 0, the(symmetric) inverse of the original matrix, stored as a packed triangular matrix.The j - th column of inv(A) is stored in the array AP as follows:
          if UPLO = 'U', AP(i + (j-1)*j/2) = inv(A)(i,j) for 1&lt;=i&lt;=j;
if UPLO = 'L',
             AP(i + (j-1)*(2n-j)/2) = inv(A)(i,j) for j&lt;=i&lt;=n.
</code></pre>
<p> <i>IPIV</i> </p>
<pre>
          IPIV is INTEGER array, dimension (N)
          Details of the interchanges and the block structure of D
          as determined by CSPTRF.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (N)
</pre>
<p> <i>INFO</i> </p>
<pre><code>
INFO is INTEGER = 0 : successful exit &lt; 0 : if INFO = -i, the i - th argument had an illegal value &gt; 0 : if INFO = i, D(i, i) = 0;
the matrix is singular and its
    inverse could not be computed.
</code></pre>
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
<p> Definition at line 110 of file csptri.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
