---
title: "dlaqge(3)"
name: "dlaqge"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlaqge/"
description: "dlaqge.f –"
---

<h2 class="name">NAME</h2>
<p> dlaqge.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlaqge</code> (M, N, A, LDA, R, C, ROWCND, COLCND, AMAX, EQUED)<br />
 <i></i><code>DLAQGE</code> scales a general rectangular matrix, using row and column scaling factors computed by sgeequ.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlaqge (integerM, integerN, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )R, double precision, dimension( * )C, double precisionROWCND, double precisionCOLCND, double precisionAMAX, characterEQUED)</h3>
<p> <code>DLAQGE</code> scales a general rectangular matrix, using row and column scaling factors computed by sgeequ. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLAQGE equilibrates a general M by N matrix A using the row and
 column scaling factors in the vectors R and C.
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
          A is DOUBLE PRECISION array, dimension (LDA,N)
          On entry, the M by N matrix A.
          On exit, the equilibrated matrix.  See EQUED for the form of
          the equilibrated matrix.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(M,1).
</pre>
<p> <i>R</i> </p>
<pre>
          R is DOUBLE PRECISION array, dimension (M)
          The row scale factors for A.
</pre>
<p> <i>C</i> </p>
<pre>
          C is DOUBLE PRECISION array, dimension (N)
          The column scale factors for A.
</pre>
<p> <i>ROWCND</i> </p>
<pre>
          ROWCND is DOUBLE PRECISION
          Ratio of the smallest R(i) to the largest R(i).
</pre>
<p> <i>COLCND</i> </p>
<pre>
          COLCND is DOUBLE PRECISION
          Ratio of the smallest C(i) to the largest C(i).
</pre>
<p> <i>AMAX</i> </p>
<pre>
          AMAX is DOUBLE PRECISION
          Absolute value of largest matrix entry.
</pre>
<p> <i>EQUED</i> </p>
<pre>
          EQUED is CHARACTER*1
          Specifies the form of equilibration that was done.
          = 'N':  No equilibration
          = 'R':  Row equilibration, i.e., A has been premultiplied by
                  diag(R).
          = 'C':  Column equilibration, i.e., A has been postmultiplied
                  by diag(C).
          = 'B':  Both row and column equilibration, i.e., A has been
                  replaced by diag(R) * A * diag(C).
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Internal Parameters: </code></p>
<dl>
<dt>
<dd>
<pre>
  THRESH is a threshold value used to decide if row or column scaling
  should be done based on the ratio of the row or column scaling
  factors.  If ROWCND &lt; THRESH, row scaling is done, and if
  COLCND &lt; THRESH, column scaling is done.
  LARGE and SMALL are threshold values used to decide if row scaling
  should be done based on the absolute size of the largest matrix
  element.  If AMAX &gt; LARGE or AMAX &lt; SMALL, row scaling is done.
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
<p> Definition at line 142 of file dlaqge.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
