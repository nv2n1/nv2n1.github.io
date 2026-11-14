---
title: "slaev2-f(3)"
name: "slaev2-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slaev2-f/"
description: "slaev2.f –"
---

<p>slaev2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slaev2</code> (A, B, C, RT1, RT2, CS1, SN1)<br />
 <i></i><code>SLAEV2</code> computes the eigenvalues and eigenvectors of a 2-by-2 symmetric/Hermitian matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slaev2 (realA, realB, realC, realRT1, realRT2, realCS1, realSN1)</h3>
<p><code>SLAEV2</code> computes the eigenvalues and eigenvectors of a 2-by-2 symmetric/Hermitian matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLAEV2 computes the eigendecomposition of a 2-by-2 symmetric matrix
 [ A B ]
 [ B C ].
 On return, RT1 is the eigenvalue of larger absolute value, RT2 is the
 eigenvalue of smaller absolute value, and (CS1,SN1) is the unit right
 eigenvector for RT1, giving the decomposition
 [ CS1 SN1 ] [ A B ] [ CS1 -SN1 ] = [ RT1 0 ]
 [-SN1 CS1 ] [ B C ] [ SN1 CS1 ] [ 0 RT2 ].</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>A</i> </p>
<pre> A is REAL
 The (1,1) element of the 2-by-2 matrix.</pre>
<p><i>B</i> </p>
<pre> B is REAL
 The (1,2) element and the conjugate of the (2,1) element of
 the 2-by-2 matrix.</pre>
<p><i>C</i> </p>
<pre> C is REAL
 The (2,2) element of the 2-by-2 matrix.</pre>
<p><i>RT1</i> </p>
<pre> RT1 is REAL
 The eigenvalue of larger absolute value.</pre>
<p><i>RT2</i> </p>
<pre> RT2 is REAL
 The eigenvalue of smaller absolute value.</pre>
<p><i>CS1</i> </p>
<pre> CS1 is REAL</pre>
<p><i>SN1</i> </p>
<pre> SN1 is REAL
 The vector (CS1, SN1) is a unit right eigenvector for RT1.</pre>
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
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> RT1 is accurate to a few ulps barring over/underflow.
 RT2 may be inaccurate if there is massive cancellation in the
 determinant A*C-B*B; higher precision or correctly rounded or
 correctly truncated arithmetic would be needed to compute RT2
 accurately in all cases.
 CS1 and SN1 are accurate to a few ulps barring over/underflow.
 Overflow is possible only if RT1 is within a factor of 5 of overflow.
 Underflow is harmless if the input data is 0 or exceeds
 underflow_threshold / macheps.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 121 of file slaev2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
