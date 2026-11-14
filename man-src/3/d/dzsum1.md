---
title: "dzsum1(3)"
name: "dzsum1"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dzsum1/"
description: "dzsum1.f –"
---

<h2 class="name">NAME</h2>
<p> dzsum1.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> DOUBLE PRECISION function <code>dzsum1</code> (N, CX, INCX)<br />
 <i></i><code>DZSUM1</code> forms the 1-norm of the complex vector using the true absolute value.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function dzsum1 (integerN, complex*16, dimension( * )CX, integerINCX)</h3>
<p> <code>DZSUM1</code> forms the 1-norm of the complex vector using the true absolute value. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DZSUM1 takes the sum of the absolute values of a complex
 vector and returns a double precision result.
 Based on DZASUM from the Level 1 BLAS.
 The change is to use the 'genuine' absolute value.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of elements in the vector CX.
</pre>
<p> <i>CX</i> </p>
<pre>
          CX is COMPLEX*16 array, dimension (N)
          The vector whose elements will be summed.
</pre>
<p> <i>INCX</i> </p>
<pre>
          INCX is INTEGER
          The spacing between successive values of CX.  INCX &gt; 0.
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
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Nick Higham for use with ZLACON.</dl>
<p> Definition at line 82 of file dzsum1.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
