---
title: "claqp2(3)"
name: "claqp2"
section: "3"
letter: "c"
url: "/docs/linux/man/3-claqp2/"
description: "claqp2.f –"
---

<h2 class="name">NAME</h2>
<p> claqp2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>claqp2</code> (M, N, OFFSET, A, LDA, JPVT, TAU, VN1, VN2, WORK)<br />
 <i></i><code>CLAQP2</code> computes a QR factorization with column pivoting of the matrix block.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine claqp2 (integerM, integerN, integerOFFSET, complex, dimension( lda, * )A, integerLDA, integer, dimension( * )JPVT, complex, dimension( * )TAU, real, dimension( * )VN1, real, dimension( * )VN2, complex, dimension( * )WORK)</h3>
<p> <code>CLAQP2</code> computes a QR factorization with column pivoting of the matrix block. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLAQP2 computes a QR factorization with column pivoting of
 the block A(OFFSET+1:M,1:N).
 The block A(1:OFFSET,1:N) is accordingly pivoted, but not factorized.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the matrix A. M &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrix A. N &gt;= 0.
</pre>
<p> <i>OFFSET</i> </p>
<pre>
          OFFSET is INTEGER
          The number of rows of the matrix A that must be pivoted
          but no factorized. OFFSET &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
          On entry, the M-by-N matrix A.
          On exit, the upper triangle of block A(OFFSET+1:M,1:N) is 
          the triangular factor obtained; the elements in block
          A(OFFSET+1:M,1:N) below the diagonal, together with the
          array TAU, represent the orthogonal matrix Q as a product of
          elementary reflectors. Block A(1:OFFSET,1:N) has been
          accordingly pivoted, but no factorized.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A. LDA &gt;= max(1,M).
</pre>
<p> <i>JPVT</i> </p>
<pre><code>
JPVT is INTEGER array, dimension(N) On entry, if JPVT (i).ne.0, the i - th column of A is permuted to the front of A *P(a leading column);
if JPVT (i)
= 0,
    the i - th column of A is a free column.On exit, if JPVT (i) = k, then the i - th column of A *P was the k - th column of A.
</code></pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is COMPLEX array, dimension (min(M,N))
          The scalar factors of the elementary reflectors.
</pre>
<p> <i>VN1</i> </p>
<pre>
          VN1 is REAL array, dimension (N)
          The vector with the partial column norms.
</pre>
<p> <i>VN2</i> </p>
<pre>
          VN2 is REAL array, dimension (N)
          The vector with the exact column norms.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (N)
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
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> G. Quintana-Orti, Depto. de Informatica, Universidad Jaime I, Spain X. Sun, Computer Science Dept., Duke University, USA </p>
<p>&nbsp;<wbr>Partial column norm updating strategy modified on April 2011 Z. Drmac and Z. Bujanovic, Dept. of Mathematics, University of Zagreb, Croatia.&nbsp;<wbr></dl>
<p> <code>References: </code></p>
<dl>
<dt>
<dd> LAPACK Working Note 176</dl>
<p> Definition at line 149 of file claqp2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
