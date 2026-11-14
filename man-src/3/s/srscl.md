---
title: "srscl(3)"
name: "srscl"
section: "3"
letter: "s"
url: "/docs/linux/man/3-srscl/"
description: "srscl.f –"
---

<h2 class="name">NAME</h2>
<p> srscl.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>srscl</code> (N, SA, SX, INCX)<br />
 <i></i><code>SRSCL</code> multiplies a vector by the reciprocal of a real scalar.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine srscl (integerN, realSA, real, dimension( * )SX, integerINCX)</h3>
<p> <code>SRSCL</code> multiplies a vector by the reciprocal of a real scalar. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SRSCL multiplies an n-element real vector x by the real scalar 1/a.
 This is done without overflow or underflow as long as
 the final result x/a does not overflow or underflow.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of components of the vector x.
</pre>
<p> <i>SA</i> </p>
<pre>
          SA is REAL
          The scalar a which is used to divide each component of x.
          SA must be &gt;= 0, or the subroutine will divide by zero.
</pre>
<p> <i>SX</i> </p>
<pre>
          SX is REAL array, dimension
                         (1+(N-1)*abs(INCX))
          The n-element vector x.
</pre>
<p> <i>INCX</i> </p>
<pre>
          INCX is INTEGER
          The increment between successive values of the vector SX.
          &gt; 0:  <a href="//www.systutorials.com/docs/linux/man/1-SX/">SX</a>(1) = <a href="//www.systutorials.com/docs/linux/man/1-X/">X</a>(1) and SX(1+(i-1)*INCX) = x(i),     1&lt; i&lt;= n
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
<p> Definition at line 85 of file srscl.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
