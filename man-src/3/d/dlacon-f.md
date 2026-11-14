---
title: "dlacon-f(3)"
name: "dlacon-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlacon-f/"
description: "dlacon.f –"
---

<p>dlacon.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlacon</code> (N, V, X, ISGN, EST, KASE)<br />
 <i></i><code>DLACON</code> estimates the 1-norm of a square matrix, using reverse communication for evaluating matrix-vector products.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlacon (integerN, double precision, dimension( * )V, double precision, dimension( * )X, integer, dimension( * )ISGN, double precisionEST, integerKASE)</h3>
<p><code>DLACON</code> estimates the 1-norm of a square matrix, using reverse communication for evaluating matrix-vector products. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLACON estimates the 1-norm of a square, real matrix A.
 Reverse communication is used for evaluating matrix-vector products.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix. N &gt;= 1.</pre>
<p><i>V</i> </p>
<pre> V is DOUBLE PRECISION array, dimension (N)
 On the final return, V = A*W, where EST = norm(V)/norm(W)
 (W is not returned).</pre>
<p><i>X</i> </p>
<pre> X is DOUBLE PRECISION array, dimension (N)
 On an intermediate return, X should be overwritten by
 A * X, if KASE=1,
 A**T * X, if KASE=2,
 and DLACON must be re-called with all the other parameters
 unchanged.</pre>
<p><i>ISGN</i> </p>
<pre> ISGN is INTEGER array, dimension (N)</pre>
<p><i>EST</i> </p>
<pre> EST is DOUBLE PRECISION
 On entry with KASE = 1 or 2 and JUMP = 3, EST should be
 unchanged from the previous call to DLACON.
 On exit, EST is an estimate (a lower bound) for norm(A). </pre>
<p><i>KASE</i> </p>
<pre> KASE is INTEGER
 On the initial call to DLACON, KASE should be 0.
 On an intermediate return, KASE will be 1 or 2, indicating
 whether X should be overwritten by A * X or A**T * X.
 On the final return from DLACON, KASE will again be 0.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>Nick Higham, University of Manchester. </p>
<p>&nbsp;<wbr>Originally named SONEST, dated March 16, 1988.&nbsp;<wbr></dl>
<p> <code>References: </code></p>
<dl COMPACT>
<dd>N.J. Higham, &#8216;FORTRAN codes for estimating the one-norm of<br />
&nbsp;<wbr>&nbsp;<wbr>a real or complex matrix, with applications to condition estimation&#8217;, ACM Trans. Math. Soft., vol. 14, no. 4, pp. 381-396, December 1988.&nbsp;<wbr></dl>
<p> Definition at line 116 of file dlacon.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
