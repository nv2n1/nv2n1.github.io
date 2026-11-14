---
title: "sladiv(3)"
name: "sladiv"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sladiv/"
description: "sladiv.f –"
---

<h2 class="name">NAME</h2>
<p> sladiv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sladiv</code> (A, B, C, D, P, Q)<br />
 <i></i><code>SLADIV</code> performs complex division in real arithmetic, avoiding unnecessary overflow.<br />
 subroutine <code>sladiv1</code> (A, B, C, D, P, Q) </p>
<p> REAL function <code>sladiv2</code> (A, B, C, D, R, T) </p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sladiv (realA, realB, realC, realD, realP, realQ)</h3>
<p> <code>SLADIV</code> performs complex division in real arithmetic, avoiding unnecessary overflow. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
SLADIV performs complex division in real arithmetic
        a +
    i *b
        p +
    i *q = -- -- -- -- -c + i * d
                                    The algorithm is due to Michael Baudin and
           Robert L.Smith and can be found in the paper "A Robust Complex Division in Scilab"
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>A</i> </p>
<pre>
          A is REAL
</pre>
<p> <i>B</i> </p>
<pre>
          B is REAL
</pre>
<p> <i>C</i> </p>
<pre>
          C is REAL
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL
          The scalars a, b, c, and d in the above expression.
</pre>
<p> <i>P</i> </p>
<pre>
          P is REAL
</pre>
<p> <i>Q</i> </p>
<pre>
          Q is REAL
          The scalars p and q in the above expression.
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
<dd> January 2013</dl>
<p> Definition at line 92 of file sladiv.f.</p>
<h3>subroutine sladiv1 (realA, realB, realC, realD, realP, realQ)</h3>
<p> Definition at line 178 of file sladiv.f.</p>
<h3>REAL function sladiv2 (realA, realB, realC, realD, realR, realT)</h3>
<p> Definition at line 216 of file sladiv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
