---
title: "dlasq1(3)"
name: "dlasq1"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlasq1/"
description: "dlasq1.f –"
---

<h2 class="name">NAME</h2>
<p> dlasq1.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlasq1</code> (N, D, E, WORK, INFO)<br />
 <i></i><code>DLASQ1</code> computes the singular values of a real square bidiagonal matrix. Used by sbdsqr.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlasq1 (integerN, double precision, dimension( * )D, double precision, dimension( * )E, double precision, dimension( * )WORK, integerINFO)</h3>
<p> <code>DLASQ1</code> computes the singular values of a real square bidiagonal matrix. Used by sbdsqr. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLASQ1 computes the singular values of a real N-by-N bidiagonal
 matrix with diagonal D and off-diagonal E. The singular values
 are computed to high relative accuracy, in the absence of
 denormalization, underflow and overflow. The algorithm was first
 presented in
 &quot;Accurate singular values and differential qd algorithms&quot; by K. V.
 Fernando and B. N. Parlett, Numer. Math., Vol-67, No. 2, pp. 191-230,
 1994,
 and the present implementation is described in &quot;An implementation of
 the dqds Algorithm (Positive Case)&quot;, LAPACK Working Note.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
        The number of rows and columns in the matrix. N &gt;= 0.
</pre>
<p> <i>D</i> </p>
<pre>
          D is DOUBLE PRECISION array, dimension (N)
        On entry, D contains the diagonal elements of the
        bidiagonal matrix whose SVD is desired. On normal exit,
        D contains the singular values in decreasing order.
</pre>
<p> <i>E</i> </p>
<pre>
          E is DOUBLE PRECISION array, dimension (N)
        On entry, elements E(1:N-1) contain the off-diagonal elements
        of the bidiagonal matrix whose SVD is desired.
        On exit, E is overwritten.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (4*N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
        = 0: successful exit
        &lt; 0: if INFO = -i, the i-th argument had an illegal value
        &gt; 0: the algorithm failed
             = 1, a split was marked by a positive value in E
             = 2, current block of Z not diagonalized after 100*N
                  iterations (in inner while loop)  On exit D and E
                  represent a matrix with the same singular values
                  which the calling subroutine could use to finish the
                  computation, or even feed back into DLASQ1
             = 3, termination criterion of outer while loop not met 
                  (program created more than N unreduced blocks)
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
<p> Definition at line 109 of file dlasq1.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
