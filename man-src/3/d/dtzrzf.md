---
title: "dtzrzf(3)"
name: "dtzrzf"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dtzrzf/"
description: "dtzrzf.f –"
---

<h2 class="name">NAME</h2>
<p> dtzrzf.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dtzrzf</code> (M, N, A, LDA, TAU, WORK, LWORK, INFO)<br />
 <i></i><code>DTZRZF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dtzrzf (integerM, integerN, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )TAU, double precision, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p> <code>DTZRZF</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DTZRZF reduces the M-by-N ( M&lt;=N ) real upper trapezoidal matrix A
 to upper triangular form by means of orthogonal transformations.
 The upper trapezoidal matrix A is factored as
    A = ( R  0 ) * Z,
 where Z is an N-by-N orthogonal matrix and R is an M-by-M upper
 triangular matrix.
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
          The number of columns of the matrix A.  N &gt;= M.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
          On entry, the leading M-by-N upper trapezoidal part of the
          array A must contain the matrix to be factorized.
          On exit, the leading M-by-M upper triangular part of A
          contains the upper triangular matrix R, and elements M+1 to
          N of the first M rows of A, with the array TAU, represent the
          orthogonal matrix Z as a product of M elementary reflectors.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,M).
</pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is DOUBLE PRECISION array, dimension (M)
          The scalar factors of the elementary reflectors.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is INTEGER
          The dimension of the array WORK.  LWORK &gt;= max(1,M).
          For optimum performance LWORK &gt;= M*NB, where NB is
          the optimal blocksize.
          If LWORK = -1, then a workspace query is assumed; the routine
          only calculates the optimal size of the WORK array, returns
          this value as the first entry of the WORK array, and no error
          message related to LWORK is issued by XERBLA.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
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
<dd> April 2012</dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> A. Petitet, Computer Science Dept., Univ. of Tenn., Knoxville, USA</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  The N-by-N matrix Z can be computed by
     Z =  <a href="//www.systutorials.com/docs/linux/man/1-Z/">Z</a>(1)*<a href="//www.systutorials.com/docs/linux/man/2-Z/">Z</a>(2)* ... *Z(M)
  where each N-by-N Z(k) is given by
     Z(k) = I - tau(k)*v(k)*v(k)**T
  with v(k) is the kth row vector of the M-by-N matrix
     V = ( I   A(:,M+1:N) )
  I is the M-by-M identity matrix, A(:,M+1:N) 
  is the output stored in A on exit from DTZRZF,
  and tau(k) is the kth element of the array TAU.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 152 of file dtzrzf.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
