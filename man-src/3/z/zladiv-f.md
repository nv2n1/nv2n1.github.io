---
title: "zladiv-f(3)"
name: "zladiv-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zladiv-f/"
description: "zladiv.f –"
---

<p>zladiv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>COMPLEX *16 function <code>zladiv</code> (X, Y)<br />
 <i></i><code>ZLADIV</code> performs complex division in real arithmetic, avoiding unnecessary overflow.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>COMPLEX*16 function zladiv (complex*16X, complex*16Y)</h3>
<p><code>ZLADIV</code> performs complex division in real arithmetic, avoiding unnecessary overflow. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLADIV := X / Y, where X and Y are complex. The computation of X / Y
 will not overflow on an intermediary step unless the results
 overflows.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>X</i> </p>
<pre> X is COMPLEX*16</pre>
<p><i>Y</i> </p>
<pre> Y is COMPLEX*16
 The complex scalars X and Y.</pre>
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
<p> Definition at line 65 of file zladiv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
