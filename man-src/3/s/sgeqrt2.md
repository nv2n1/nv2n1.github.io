---
title: "sgeqrt2(3)"
name: "sgeqrt2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgeqrt2/"
description: "sgeqrt2.f –"
---

<h2 class="name">NAME</h2>
<p> sgeqrt2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sgeqrt2</code> (M, N, A, LDA, T, LDT, INFO)<br />
 <i></i><code>SGEQRT2</code> computes a QR factorization of a general real or complex matrix using the compact WY representation of Q.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sgeqrt2 (integerM, integerN, real, dimension( lda, * )A, integerLDA, real, dimension( ldt, * )T, integerLDT, integerINFO)</h3>
<p> <code>SGEQRT2</code> computes a QR factorization of a general real or complex matrix using the compact WY representation of Q. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SGEQRT2 computes a QR factorization of a real M-by-N matrix A, 
 using the compact WY representation of Q. 
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the matrix A.  M &gt;= N.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrix A.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is REAL array, dimension (LDA,N)
          On entry, the real M-by-N matrix A.  On exit, the elements on and
          above the diagonal contain the N-by-N upper triangular matrix R; the
          elements below the diagonal are the columns of V.  See below for
          further details.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,M).
</pre>
<p> <i>T</i> </p>
<pre>
          T is REAL array, dimension (LDT,N)
          The N-by-N upper triangular factor of the block reflector.
          The elements on and above the diagonal contain the block
          reflector T; the elements below the diagonal are not used.
          See below for further details.
</pre>
<p> <i>LDT</i> </p>
<pre>
          LDT is INTEGER
          The leading dimension of the array T.  LDT &gt;= max(1,N).
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -i, the i-th argument had an illegal value
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
  The matrix V stores the elementary reflectors H(i) in the i-th column
  below the diagonal. For example, if M=5 and N=3, the matrix V is
               V = (  1       )
                   ( v1  1    )
                   ( v1 v2  1 )
                   ( v1 v2 v3 )
                   ( v1 v2 v3 )
  where the vi's represent the vectors which define H(i), which are returned
  in the matrix A.  The 1's along the diagonal of V are not stored in A.  The
  block reflector H is then given by
               H = I - V * T * V**T
  where V**T is the transpose of V.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 128 of file sgeqrt2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
