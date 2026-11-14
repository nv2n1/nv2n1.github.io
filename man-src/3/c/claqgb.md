---
title: "claqgb(3)"
name: "claqgb"
section: "3"
letter: "c"
url: "/docs/linux/man/3-claqgb/"
description: "claqgb.f –"
---

<h2 class="name">NAME</h2>
<p> claqgb.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>claqgb</code> (M, N, KL, KU, AB, LDAB, R, C, ROWCND, COLCND, AMAX, EQUED)<br />
 <i></i><code>CLAQGB</code> scales a general band matrix, using row and column scaling factors computed by sgbequ.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine claqgb (integerM, integerN, integerKL, integerKU, complex, dimension( ldab, * )AB, integerLDAB, real, dimension( * )R, real, dimension( * )C, realROWCND, realCOLCND, realAMAX, characterEQUED)</h3>
<p> <code>CLAQGB</code> scales a general band matrix, using row and column scaling factors computed by sgbequ. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLAQGB equilibrates a general M by N band matrix A with KL
 subdiagonals and KU superdiagonals using the row and scaling factors
 in the vectors R and C.
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
<p> <i>KL</i> </p>
<pre>
          KL is INTEGER
          The number of subdiagonals within the band of A.  KL &gt;= 0.
</pre>
<p> <i>KU</i> </p>
<pre>
          KU is INTEGER
          The number of superdiagonals within the band of A.  KU &gt;= 0.
</pre>
<p> <i>AB</i> </p>
<pre><code>
          AB is COMPLEX array, dimension (LDAB,N)
          On entry, the matrix A in band storage, in rows 1 to KL+KU+1.
          The j-th column of A is stored in the j-th column of the
          array AB as follows:
          AB(ku+1+i-j,j) = A(i,j) for max(1,j-ku)&lt;=i&lt;=min(m,j+kl)
          On exit, the equilibrated matrix, in the same storage format
          as A.  See EQUED for the form of the equilibrated matrix.
</code></pre>
<p> <i>LDAB</i> </p>
<pre>
          LDAB is INTEGER
          The leading dimension of the array AB.  LDA &gt;= KL+KU+1.
</pre>
<p> <i>R</i> </p>
<pre>
          R is REAL array, dimension (M)
          The row scale factors for A.
</pre>
<p> <i>C</i> </p>
<pre>
          C is REAL array, dimension (N)
          The column scale factors for A.
</pre>
<p> <i>ROWCND</i> </p>
<pre>
          ROWCND is REAL
          Ratio of the smallest R(i) to the largest R(i).
</pre>
<p> <i>COLCND</i> </p>
<pre>
          COLCND is REAL
          Ratio of the smallest C(i) to the largest C(i).
</pre>
<p> <i>AMAX</i> </p>
<pre>
          AMAX is REAL
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
<p> Definition at line 160 of file claqgb.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
