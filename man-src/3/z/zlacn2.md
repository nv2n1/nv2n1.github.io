---
title: "zlacn2(3)"
name: "zlacn2"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlacn2/"
description: "zlacn2.f –"
---

<p>zlacn2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlacn2</code> (N, V, X, EST, KASE, ISAVE)<br />
 <i></i><code>ZLACN2</code> estimates the 1-norm of a square matrix, using reverse communication for evaluating matrix-vector products.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlacn2 (integerN, complex*16, dimension( * )V, complex*16, dimension( * )X, double precisionEST, integerKASE, integer, dimension( 3 )ISAVE)</h3>
<p><code>ZLACN2</code> estimates the 1-norm of a square matrix, using reverse communication for evaluating matrix-vector products. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLACN2 estimates the 1-norm of a square, complex matrix A.
 Reverse communication is used for evaluating matrix-vector products.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix. N &gt;= 1.</pre>
<p><i>V</i> </p>
<pre> V is COMPLEX*16 array, dimension (N)
 On the final return, V = A*W, where EST = norm(V)/norm(W)
 (W is not returned).</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX*16 array, dimension (N)
 On an intermediate return, X should be overwritten by
 A * X, if KASE=1,
 A**H * X, if KASE=2,
 where A**H is the conjugate transpose of A, and ZLACN2 must be
 re-called with all the other parameters unchanged.</pre>
<p><i>EST</i> </p>
<pre> EST is DOUBLE PRECISION
 On entry with KASE = 1 or 2 and <a href="//www.systutorials.com/docs/linux/man/1-ISAVE/">ISAVE</a>(1) = 3, EST should be
 unchanged from the previous call to ZLACN2.
 On exit, EST is an estimate (a lower bound) for norm(A). </pre>
<p><i>KASE</i> </p>
<pre> KASE is INTEGER
 On the initial call to ZLACN2, KASE should be 0.
 On an intermediate return, KASE will be 1 or 2, indicating
 whether X should be overwritten by A * X or A**H * X.
 On the final return from ZLACN2, KASE will again be 0.</pre>
<p><i>ISAVE</i> </p>
<pre> ISAVE is INTEGER array, dimension (3)
 ISAVE is used to save variables between calls to ZLACN2</pre>
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
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> Originally named CONEST, dated March 16, 1988.
 Last modified: April, 1999
 This is a thread safe version of ZLACON, which uses the array ISAVE
 in place of a SAVE statement, as follows:
 ZLACON ZLACN2
 JUMP <a href="//www.systutorials.com/docs/linux/man/1-ISAVE/">ISAVE</a>(1)
 J <a href="//www.systutorials.com/docs/linux/man/2-ISAVE/">ISAVE</a>(2)
 ITER <a href="//www.systutorials.com/docs/linux/man/3-ISAVE/">ISAVE</a>(3)</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Contributors: </code></p>
<dl>
<dd>Nick Higham, University of Manchester</dl>
<p> <code>References: </code></p>
<dl>
<dd>N.J. Higham, &#8216;FORTRAN codes for estimating the one-norm of<br />
&nbsp;<wbr>&nbsp;<wbr>a real or complex matrix, with applications to condition estimation&#8217;, ACM Trans. Math. Soft., vol. 14, no. 4, pp. 381-396, December 1988.&nbsp;<wbr></dl>
<p> Definition at line 134 of file zlacn2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
