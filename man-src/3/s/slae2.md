---
title: "slae2(3)"
name: "slae2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slae2/"
description: "slae2.f –"
---

<h2 class="name">NAME</h2>
<p> slae2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slae2</code> (A, B, C, RT1, RT2)<br />
 <i></i><code>SLAE2</code> computes the eigenvalues of a 2-by-2 symmetric matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slae2 (realA, realB, realC, realRT1, realRT2)</h3>
<p> <code>SLAE2</code> computes the eigenvalues of a 2-by-2 symmetric matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
SLAE2 computes the eigenvalues of a 2 - by - 2 symmetric matrix[A B][B C].On return, RT1 is the eigenvalue of larger absolute value, and RT2 is the eigenvalue of smaller absolute value.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>A</i> </p>
<pre>
          A is REAL
          The (1,1) element of the 2-by-2 matrix.
</pre>
<p> <i>B</i> </p>
<pre>
          B is REAL
          The (1,2) and (2,1) elements of the 2-by-2 matrix.
</pre>
<p> <i>C</i> </p>
<pre>
          C is REAL
          The (2,2) element of the 2-by-2 matrix.
</pre>
<p> <i>RT1</i> </p>
<pre>
          RT1 is REAL
          The eigenvalue of larger absolute value.
</pre>
<p> <i>RT2</i> </p>
<pre>
          RT2 is REAL
          The eigenvalue of smaller absolute value.
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
<dd>
<pre>
  RT1 is accurate to a few ulps barring over/underflow.
  RT2 may be inaccurate if there is massive cancellation in the
  determinant A*C-B*B; higher precision or correctly rounded or
  correctly truncated arithmetic would be needed to compute RT2
  accurately in all cases.
  Overflow is possible only if RT1 is within a factor of 5 of overflow.
  Underflow is harmless if the input data is 0 or exceeds
     underflow_threshold / macheps.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 103 of file slae2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
