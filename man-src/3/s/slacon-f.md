---
title: "slacon-f(3)"
name: "slacon-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slacon-f/"
description: "slacon.f –"
---

<p>slacon.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slacon</code> (N, V, X, ISGN, EST, KASE)<br />
 <i></i><code>SLACON</code> estimates the 1-norm of a square matrix, using reverse communication for evaluating matrix-vector products.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slacon (integerN, real, dimension( * )V, real, dimension( * )X, integer, dimension( * )ISGN, realEST, integerKASE)</h3>
<p><code>SLACON</code> estimates the 1-norm of a square matrix, using reverse communication for evaluating matrix-vector products. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLACON estimates the 1-norm of a square, real matrix A.
 Reverse communication is used for evaluating matrix-vector products.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix. N &gt;= 1.</pre>
<p><i>V</i> </p>
<pre> V is REAL array, dimension (N)
 On the final return, V = A*W, where EST = norm(V)/norm(W)
 (W is not returned).</pre>
<p><i>X</i> </p>
<pre> X is REAL array, dimension (N)
 On an intermediate return, X should be overwritten by
 A * X, if KASE=1,
 A**T * X, if KASE=2,
 and SLACON must be re-called with all the other parameters
 unchanged.</pre>
<p><i>ISGN</i> </p>
<pre> ISGN is INTEGER array, dimension (N)</pre>
<p><i>EST</i> </p>
<pre> EST is REAL
 On entry with KASE = 1 or 2 and JUMP = 3, EST should be
 unchanged from the previous call to SLACON.
 On exit, EST is an estimate (a lower bound) for norm(A). </pre>
<p><i>KASE</i> </p>
<pre> KASE is INTEGER
 On the initial call to SLACON, KASE should be 0.
 On an intermediate return, KASE will be 1 or 2, indicating
 whether X should be overwritten by A * X or A**T * X.
 On the final return from SLACON, KASE will again be 0.</pre>
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
<p> <code>Contributors: </code></p>
<dl>
<dd>Nick Higham, University of Manchester. </p>
<p>&nbsp;<wbr>Originally named SONEST, dated March 16, 1988.&nbsp;<wbr></dl>
<p> <code>References: </code></p>
<dl>
<dd>N.J. Higham, &#8216;FORTRAN codes for estimating the one-norm of<br />
&nbsp;<wbr>&nbsp;<wbr>a real or complex matrix, with applications to condition estimation&#8217;, ACM Trans. Math. Soft., vol. 14, no. 4, pp. 381-396, December 1988.&nbsp;<wbr></dl>
<p> Definition at line 116 of file slacon.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
