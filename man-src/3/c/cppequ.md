---
title: "cppequ(3)"
name: "cppequ"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cppequ/"
description: "cppequ.f –"
---

<h2 class="name">NAME</h2>
<p> cppequ.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cppequ</code> (UPLO, N, AP, S, SCOND, AMAX, INFO)<br />
 <i></i><code>CPPEQU</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cppequ (characterUPLO, integerN, complex, dimension( * )AP, real, dimension( * )S, realSCOND, realAMAX, integerINFO)</h3>
<p> <code>CPPEQU</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CPPEQU computes row and column scalings intended to equilibrate a
 Hermitian positive definite matrix A in packed storage and reduce
 its condition number (with respect to the two-norm).  S contains the
 scale factors, S(i)=1/sqrt(A(i,i)), chosen so that the scaled matrix
 B with elements B(i,j)=S(i)*A(i,j)*S(j) has ones on the diagonal.
 This choice of S puts the condition number of B within a factor N of
 the smallest possible condition number over all possible diagonal
 scalings.
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
          The upper or lower triangle of the Hermitian matrix A, packed
          columnwise in a linear array.  The j-th column of A is stored
          in the array AP as follows:
          if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
          if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
</code></pre>
<p> <i>S</i> </p>
<pre>
          S is REAL array, dimension (N)
          If INFO = 0, S contains the scale factors for A.
</pre>
<p> <i>SCOND</i> </p>
<pre>
          SCOND is REAL
          If INFO = 0, S contains the ratio of the smallest S(i) to
          the largest S(i).  If SCOND &gt;= 0.1 and AMAX is neither too
          large nor too small, it is not worth scaling by S.
</pre>
<p> <i>AMAX</i> </p>
<pre>
          AMAX is REAL
          Absolute value of largest matrix element.  If AMAX is very
          close to overflow or very close to underflow, the matrix
          should be scaled.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
          &gt; 0:  if INFO = i, the i-th diagonal element is nonpositive.
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
<p> Definition at line 118 of file cppequ.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
