---
title: "claev2-f(3)"
name: "claev2-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-claev2-f/"
description: "claev2.f –"
---

<p>claev2.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>claev2</code> (A, B, C, RT1, RT2, CS1, SN1)<br />
 <i></i><code>CLAEV2</code> computes the eigenvalues and eigenvectors of a 2-by-2 symmetric/Hermitian matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine claev2 (complexA, complexB, complexC, realRT1, realRT2, realCS1, complexSN1)</h3>
<p><code>CLAEV2</code> computes the eigenvalues and eigenvectors of a 2-by-2 symmetric/Hermitian matrix. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CLAEV2 computes the eigendecomposition of a 2-by-2 Hermitian matrix
 [ A B ]
 [ CONJG(B) C ].
 On return, RT1 is the eigenvalue of larger absolute value, RT2 is the
 eigenvalue of smaller absolute value, and (CS1,SN1) is the unit right
 eigenvector for RT1, giving the decomposition
 [ CS1 CONJG(SN1) ] [ A B ] [ CS1 -CONJG(SN1) ] = [ RT1 0 ]
 [-SN1 CS1 ] [ CONJG(B) C ] [ SN1 CS1 ] [ 0 RT2 ].</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>A</i> </p>
<pre> A is COMPLEX
 The (1,1) element of the 2-by-2 matrix.</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX
 The (1,2) element and the conjugate of the (2,1) element of
 the 2-by-2 matrix.</pre>
<p><i>C</i> </p>
<pre> C is COMPLEX
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
<pre> SN1 is COMPLEX
 The vector (CS1, SN1) is a unit right eigenvector for RT1.</pre>
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
 CS1 and SN1 are accurate to a few ulps barring over/underflow.
 Overflow is possible only if RT1 is within a factor of 5 of overflow.
 Underflow is harmless if the input data is 0 or exceeds
 underflow_threshold / macheps.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 122 of file claev2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
