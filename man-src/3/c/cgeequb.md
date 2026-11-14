---
title: "cgeequb(3)"
name: "cgeequb"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgeequb/"
description: "cgeequb.f –"
---

<h2 class="name">NAME</h2>
<p> cgeequb.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cgeequb</code> (M, N, A, LDA, R, C, ROWCND, COLCND, AMAX, INFO)<br />
 <i></i><code>CGEEQUB</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgeequb (integerM, integerN, complex, dimension( lda, * )A, integerLDA, real, dimension( * )R, real, dimension( * )C, realROWCND, realCOLCND, realAMAX, integerINFO)</h3>
<p> <code>CGEEQUB</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CGEEQUB computes row and column scalings intended to equilibrate an
 M-by-N matrix A and reduce its condition number.  R returns the row
 scale factors and C the column scale factors, chosen to try to make
 the largest element in each row and column of the matrix B with
 elements B(i,j)=R(i)*A(i,j)*C(j) have an absolute value of at most
 the radix.
 R(i) and C(j) are restricted to be a power of the radix between
 SMLNUM = smallest safe number and BIGNUM = largest safe number.  Use
 of these scaling factors is not guaranteed to reduce the condition
 number of A but works well in practice.
 This routine differs from CGEEQU by restricting the scaling factors
 to a power of the radix.  Baring over- and underflow, scaling by
 these factors introduces no additional rounding errors.  However, the
 scaled entries' magnitured are no longer approximately 1 but lie
 between sqrt(radix) and 1/sqrt(radix).
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the matrix A.  M &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrix A.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
          The M-by-N matrix whose equilibration factors are
          to be computed.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,M).
</pre>
<p> <i>R</i> </p>
<pre>
          R is REAL array, dimension (M)
          If INFO = 0 or INFO &gt; M, R contains the row scale factors
          for A.
</pre>
<p> <i>C</i> </p>
<pre>
          C is REAL array, dimension (N)
          If INFO = 0,  C contains the column scale factors for A.
</pre>
<p> <i>ROWCND</i> </p>
<pre>
          ROWCND is REAL
          If INFO = 0 or INFO &gt; M, ROWCND contains the ratio of the
          smallest R(i) to the largest R(i).  If ROWCND &gt;= 0.1 and
          AMAX is neither too large nor too small, it is not worth
          scaling by R.
</pre>
<p> <i>COLCND</i> </p>
<pre>
          COLCND is REAL
          If INFO = 0, COLCND contains the ratio of the smallest
          C(i) to the largest C(i).  If COLCND &gt;= 0.1, it is not
          worth scaling by C.
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
          &gt; 0:  if INFO = i,  and i is
                &lt;= M:  the i-th row of A is exactly zero
                &gt;  M:  the (i-M)-th column of A is exactly zero
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
<p> Definition at line 147 of file cgeequb.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
