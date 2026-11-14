---
title: "clacon(3)"
name: "clacon"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clacon/"
description: "clacon.f –"
---

<h2 class="name">NAME</h2>
<p> clacon.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>clacon</code> (N, V, X, EST, KASE)<br />
 <i></i><code>CLACON</code> estimates the 1-norm of a square matrix, using reverse communication for evaluating matrix-vector products.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clacon (integerN, complex, dimension( n )V, complex, dimension( n )X, realEST, integerKASE)</h3>
<p> <code>CLACON</code> estimates the 1-norm of a square matrix, using reverse communication for evaluating matrix-vector products. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLACON estimates the 1-norm of a square, complex matrix A.
 Reverse communication is used for evaluating matrix-vector products.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
         The order of the matrix.  N &gt;= 1.
</pre>
<p> <i>V</i> </p>
<pre>
          V is COMPLEX array, dimension (N)
         On the final return, V = A*W,  where  EST = norm(V)/norm(W)
         (W is not returned).
</pre>
<p> <i>X</i> </p>
<pre>
          X is COMPLEX array, dimension (N)
         On an intermediate return, X should be overwritten by
               A * X,   if KASE=1,
               A**H * X,  if KASE=2,
         where A**H is the conjugate transpose of A, and CLACON must be
         re-called with all the other parameters unchanged.
</pre>
<p> <i>EST</i> </p>
<pre>
          EST is REAL
         On entry with KASE = 1 or 2 and JUMP = 3, EST should be
         unchanged from the previous call to CLACON.
         On exit, EST is an estimate (a lower bound) for norm(A). 
</pre>
<p> <i>KASE</i> </p>
<pre>
          KASE is INTEGER
         On the initial call to CLACON, KASE should be 0.
         On an intermediate return, KASE will be 1 or 2, indicating
         whether X should be overwritten by A * X  or A**H * X.
         On the final return from CLACON, KASE will again be 0.
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
<dd> Originally named CONEST, dated March 16, 1988. </p>
<p>&nbsp;<wbr>Last modified: April, 1999&nbsp;<wbr></dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Nick Higham, University of Manchester</dl>
<p> <code>References: </code></p>
<dl>
<dt>
<dd> N.J. Higham, &#8216;FORTRAN codes for estimating the one-norm of<br />
&nbsp;<wbr>&nbsp;<wbr>a real or complex matrix, with applications to condition estimation&#8217;, ACM Trans. Math. Soft., vol. 14, no. 4, pp. 381-396, December 1988.&nbsp;<wbr></dl>
<p> Definition at line 115 of file clacon.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
