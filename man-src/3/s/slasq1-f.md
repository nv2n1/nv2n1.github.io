---
title: "slasq1-f(3)"
name: "slasq1-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slasq1-f/"
description: "slasq1.f –"
---

<p>slasq1.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slasq1</code> (N, D, E, WORK, INFO)<br />
 <i></i><code>SLASQ1</code> computes the singular values of a real square bidiagonal matrix. Used by sbdsqr.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slasq1 (integerN, real, dimension( * )D, real, dimension( * )E, real, dimension( * )WORK, integerINFO)</h3>
<p><code>SLASQ1</code> computes the singular values of a real square bidiagonal matrix. Used by sbdsqr. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLASQ1 computes the singular values of a real N-by-N bidiagonal
 matrix with diagonal D and off-diagonal E. The singular values
 are computed to high relative accuracy, in the absence of
 denormalization, underflow and overflow. The algorithm was first
 presented in
 &quot;Accurate singular values and differential qd algorithms&quot; by K. V.
 Fernando and B. N. Parlett, Numer. Math., Vol-67, No. 2, pp. 191-230,
 1994,
 and the present implementation is described in &quot;An implementation of
 the dqds Algorithm (Positive Case)&quot;, LAPACK Working Note.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of rows and columns in the matrix. N &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (N)
 On entry, D contains the diagonal elements of the
 bidiagonal matrix whose SVD is desired. On normal exit,
 D contains the singular values in decreasing order.</pre>
<p><i>E</i> </p>
<pre> E is REAL array, dimension (N)
 On entry, elements E(1:N-1) contain the off-diagonal elements
 of the bidiagonal matrix whose SVD is desired.
 On exit, E is overwritten.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (4*N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: the algorithm failed
 = 1, a split was marked by a positive value in E
 = 2, current block of Z not diagonalized after 100*N
 iterations (in inner while loop) On exit D and E
 represent a matrix with the same singular values
 which the calling subroutine could use to finish the
 computation, or even feed back into SLASQ1
 = 3, termination criterion of outer while loop not met 
 (program created more than N unreduced blocks)</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> Definition at line 109 of file slasq1.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
