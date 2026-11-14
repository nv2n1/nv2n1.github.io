---
title: "slanv2-f(3)"
name: "slanv2-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slanv2-f/"
description: "slanv2.f –"
---

<p>slanv2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slanv2</code> (A, B, C, D, RT1R, RT1I, RT2R, RT2I, CS, SN)<br />
 <i></i><code>SLANV2</code> computes the Schur factorization of a real 2-by-2 nonsymmetric matrix in standard form.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slanv2 (realA, realB, realC, realD, realRT1R, realRT1I, realRT2R, realRT2I, realCS, realSN)</h3>
<p><code>SLANV2</code> computes the Schur factorization of a real 2-by-2 nonsymmetric matrix in standard form. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLANV2 computes the Schur factorization of a real 2-by-2 nonsymmetric
 matrix in standard form:
 [ A B ] = [ CS -SN ] [ AA BB ] [ CS SN ]
 [ C D ] [ SN CS ] [ CC DD ] [-SN CS ]
 where either
 1) CC = 0 so that AA and DD are real eigenvalues of the matrix, or
 2) AA = DD and BB*CC &lt; 0, so that AA + or - sqrt(BB*CC) are complex
 conjugate eigenvalues.</pre>
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
 On entry, the elements of the input matrix.
 On exit, they are overwritten by the elements of the
 standardised Schur form.</pre>
<p><i>RT1R</i> </p>
<pre> RT1R is REAL</pre>
<p><i>RT1I</i> </p>
<pre> RT1I is REAL</pre>
<p><i>RT2R</i> </p>
<pre> RT2R is REAL</pre>
<p><i>RT2I</i> </p>
<pre> RT2I is REAL
 The real and imaginary parts of the eigenvalues. If the
 eigenvalues are a complex conjugate pair, RT1I &gt; 0.</pre>
<p><i>CS</i> </p>
<pre> CS is REAL</pre>
<p><i>SN</i> </p>
<pre> SN is REAL
 Parameters of the rotation matrix.</pre>
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
<pre> Modified by V. Sima, Research Institute for Informatics, Bucharest,
 Romania, to reduce the risk of cancellation errors,
 when computing real eigenvalues, and to ensure, if possible, that
 abs(RT1R) &gt;= abs(RT2R).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 128 of file slanv2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
