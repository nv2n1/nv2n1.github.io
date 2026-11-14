---
title: "clacrt(3)"
name: "clacrt"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clacrt/"
description: "clacrt.f –"
---

<h2 class="name">NAME</h2>
<p> clacrt.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>clacrt</code> (N, CX, INCX, CY, INCY, C, S)<br />
 <i></i><code>CLACRT</code> performs a linear transformation of a pair of complex vectors.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clacrt (integerN, complex, dimension( * )CX, integerINCX, complex, dimension( * )CY, integerINCY, complexC, complexS)</h3>
<p> <code>CLACRT</code> performs a linear transformation of a pair of complex vectors. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLACRT performs the operation
    (  c  s )( x )  ==&gt; ( x )
    ( -s  c )( y )      ( y )
 where c and s are complex and the vectors x and y are complex.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of elements in the vectors CX and CY.
</pre>
<p> <i>CX</i> </p>
<pre>
          CX is COMPLEX array, dimension (N)
          On input, the vector x.
          On output, CX is overwritten with c*x + s*y.
</pre>
<p> <i>INCX</i> </p>
<pre>
          INCX is INTEGER
          The increment between successive values of CX.  INCX &lt;&gt; 0.
</pre>
<p> <i>CY</i> </p>
<pre>
          CY is COMPLEX array, dimension (N)
          On input, the vector y.
          On output, CY is overwritten with -s*x + c*y.
</pre>
<p> <i>INCY</i> </p>
<pre>
          INCY is INTEGER
          The increment between successive values of CY.  INCY &lt;&gt; 0.
</pre>
<p> <i>C</i> </p>
<pre>
          C is COMPLEX
</pre>
<p> <i>S</i> </p>
<pre><code>
S is COMPLEX
    C and S define the matrix
        [C S]
            .
                [-S C]
</code></pre>
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
<p> Definition at line 106 of file clacrt.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
