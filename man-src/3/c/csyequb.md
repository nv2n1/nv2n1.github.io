---
title: "csyequb(3)"
name: "csyequb"
section: "3"
letter: "c"
url: "/docs/linux/man/3-csyequb/"
description: "csyequb.f –"
---

<h2 class="name">NAME</h2>
<p> csyequb.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>csyequb</code> (UPLO, N, A, LDA, S, SCOND, AMAX, WORK, INFO)<br />
 <i></i><code>CSYEQUB</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine csyequb (characterUPLO, integerN, complex, dimension( lda, * )A, integerLDA, real, dimension( * )S, realSCOND, realAMAX, complex, dimension( * )WORK, integerINFO)</h3>
<p> <code>CSYEQUB</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CSYEQUB computes row and column scalings intended to equilibrate a
 symmetric matrix A and reduce its condition number
 (with respect to the two-norm).  S contains the scale factors,
 S(i) = 1/sqrt(A(i,i)), chosen so that the scaled matrix B with
 elements B(i,j) = S(i)*A(i,j)*S(j) has ones on the diagonal.  This
 choice of S puts the condition number of B within a factor N of the
 smallest possible condition number over all possible diagonal
 scalings.
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
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
          The N-by-N symmetric matrix whose scaling
          factors are to be computed.  Only the diagonal elements of A
          are referenced.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
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
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (3*N)
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
<p> <code>References: </code></p>
<dl>
<dt>
<dd> Livne, O.E. and Golub, G.H., &#8216;Scaling by Binormalization&#8217;, </p>
<p>&nbsp;<wbr>Numerical Algorithms, vol. 35, no. 1, pp. 97-120, January 2004.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>DOI 10.1023/B:NUMA.0000016606.32820.69&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Tech report version:&nbsp;<wbr><a rel="nofollow" href="http://ruready.utah.edu/archive/papers/bin.pdf">http://ruready.utah.edu/archive/papers/bin.pdf</a>&nbsp;<wbr></dl>
<p> Definition at line 137 of file csyequb.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
