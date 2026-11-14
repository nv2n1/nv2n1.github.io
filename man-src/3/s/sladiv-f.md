---
title: "sladiv-f(3)"
name: "sladiv-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sladiv-f/"
description: "sladiv.f –"
---

<p>sladiv.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sladiv</code> (A, B, C, D, P, Q)<br />
 <i></i><code>SLADIV</code> performs complex division in real arithmetic, avoiding unnecessary overflow.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sladiv (realA, realB, realC, realD, realP, realQ)</h3>
<p><code>SLADIV</code> performs complex division in real arithmetic, avoiding unnecessary overflow. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLADIV performs complex division in real arithmetic
 a + i*b
 p + i*q = ---------
 c + i*d
 The algorithm is due to Robert L. Smith and can be found
 in D. Knuth, The art of Computer Programming, Vol.2, p.195</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>A</i> </p>
<pre> A is REAL</pre>
<p><i>B</i> </p>
<pre> B is REAL</pre>
<p><i>C</i> </p>
<pre> C is REAL</pre>
<p><i>D</i> </p>
<pre> D is REAL
 The scalars a, b, c, and d in the above expression.</pre>
<p><i>P</i> </p>
<pre> P is REAL</pre>
<p><i>Q</i> </p>
<pre> Q is REAL
 The scalars p and q in the above expression.</pre>
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
<p> Definition at line 91 of file sladiv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
