---
title: "dladiv1(3)"
name: "dladiv1"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dladiv1/"
description: "dladiv.f –"
---

<h2 class="name">NAME</h2>
<p> dladiv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dladiv</code> (A, B, C, D, P, Q)<br />
 <i></i><code>DLADIV</code> performs complex division in real arithmetic, avoiding unnecessary overflow.<br />
 subroutine <code>dladiv1</code> (A, B, C, D, P, Q) </p>
<p> DOUBLE PRECISION function <code>dladiv2</code> (A, B, C, D, R, T) </p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dladiv (double precisionA, double precisionB, double precisionC, double precisionD, double precisionP, double precisionQ)</h3>
<p> <code>DLADIV</code> performs complex division in real arithmetic, avoiding unnecessary overflow. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
DLADIV performs complex division in real arithmetic
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
          A is DOUBLE PRECISION
</pre>
<p> <i>B</i> </p>
<pre>
          B is DOUBLE PRECISION
</pre>
<p> <i>C</i> </p>
<pre>
          C is DOUBLE PRECISION
</pre>
<p> <i>D</i> </p>
<pre>
          D is DOUBLE PRECISION
          The scalars a, b, c, and d in the above expression.
</pre>
<p> <i>P</i> </p>
<pre>
          P is DOUBLE PRECISION
</pre>
<p> <i>Q</i> </p>
<pre>
          Q is DOUBLE PRECISION
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
<p> Definition at line 92 of file dladiv.f.</p>
<h3>subroutine dladiv1 (double precisionA, double precisionB, double precisionC, double precisionD, double precisionP, double precisionQ)</h3>
<p> Definition at line 178 of file dladiv.f.</p>
<h3>DOUBLE PRECISION function dladiv2 (double precisionA, double precisionB, double precisionC, double precisionD, double precisionR, double precisionT)</h3>
<p> Definition at line 216 of file dladiv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
