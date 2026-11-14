---
title: "dlae2-f(3)"
name: "dlae2-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlae2-f/"
description: "dlae2.f –"
---

<p>dlae2.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlae2</code> (A, B, C, RT1, RT2)<br />
 <i></i><code>DLAE2</code> computes the eigenvalues of a 2-by-2 symmetric matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlae2 (double precisionA, double precisionB, double precisionC, double precisionRT1, double precisionRT2)</h3>
<p><code>DLAE2</code> computes the eigenvalues of a 2-by-2 symmetric matrix. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLAE2 computes the eigenvalues of a 2-by-2 symmetric matrix
 [ A B ]
 [ B C ].
 On return, RT1 is the eigenvalue of larger absolute value, and RT2
 is the eigenvalue of smaller absolute value.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>A</i> </p>
<pre> A is DOUBLE PRECISION
 The (1,1) element of the 2-by-2 matrix.</pre>
<p><i>B</i> </p>
<pre> B is DOUBLE PRECISION
 The (1,2) and (2,1) elements of the 2-by-2 matrix.</pre>
<p><i>C</i> </p>
<pre> C is DOUBLE PRECISION
 The (2,2) element of the 2-by-2 matrix.</pre>
<p><i>RT1</i> </p>
<pre> RT1 is DOUBLE PRECISION
 The eigenvalue of larger absolute value.</pre>
<p><i>RT2</i> </p>
<pre> RT2 is DOUBLE PRECISION
 The eigenvalue of smaller absolute value.</pre>
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
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> RT1 is accurate to a few ulps barring over/underflow.
 RT2 may be inaccurate if there is massive cancellation in the
 determinant A*C-B*B; higher precision or correctly rounded or
 correctly truncated arithmetic would be needed to compute RT2
 accurately in all cases.
 Overflow is possible only if RT1 is within a factor of 5 of overflow.
 Underflow is harmless if the input data is 0 or exceeds
 underflow_threshold / macheps.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 103 of file dlae2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
