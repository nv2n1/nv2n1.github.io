---
title: "scsum1(3)"
name: "scsum1"
section: "3"
letter: "s"
url: "/docs/linux/man/3-scsum1/"
description: "scsum1.f –"
---

<h2 class="name">NAME</h2>
<p> scsum1.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> REAL function <code>scsum1</code> (N, CX, INCX)<br />
 <i></i><code>SCSUM1</code> forms the 1-norm of the complex vector using the true absolute value.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function scsum1 (integerN, complex, dimension( * )CX, integerINCX)</h3>
<p> <code>SCSUM1</code> forms the 1-norm of the complex vector using the true absolute value. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SCSUM1 takes the sum of the absolute values of a complex
 vector and returns a single precision result.
 Based on SCASUM from the Level 1 BLAS.
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
          CX is COMPLEX array, dimension (N)
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
<dd> Nick Higham for use with CLACON.</dl>
<p> Definition at line 82 of file scsum1.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
