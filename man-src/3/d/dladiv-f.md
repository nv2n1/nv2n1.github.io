---
title: "dladiv-f(3)"
name: "dladiv-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dladiv-f/"
description: "dladiv.f –"
---

<p>dladiv.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dladiv</code> (A, B, C, D, P, Q)<br />
 <i></i><code>DLADIV</code> performs complex division in real arithmetic, avoiding unnecessary overflow.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dladiv (double precisionA, double precisionB, double precisionC, double precisionD, double precisionP, double precisionQ)</h3>
<p><code>DLADIV</code> performs complex division in real arithmetic, avoiding unnecessary overflow. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLADIV performs complex division in real arithmetic
 a + i*b
 p + i*q = ---------
 c + i*d
 The algorithm is due to Robert L. Smith and can be found
 in D. Knuth, The art of Computer Programming, Vol.2, p.195</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>A</i> </p>
<pre> A is DOUBLE PRECISION</pre>
<p><i>B</i> </p>
<pre> B is DOUBLE PRECISION</pre>
<p><i>C</i> </p>
<pre> C is DOUBLE PRECISION</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION
 The scalars a, b, c, and d in the above expression.</pre>
<p><i>P</i> </p>
<pre> P is DOUBLE PRECISION</pre>
<p><i>Q</i> </p>
<pre> Q is DOUBLE PRECISION
 The scalars p and q in the above expression.</pre>
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
<p> Definition at line 91 of file dladiv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
