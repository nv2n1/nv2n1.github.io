---
title: "zlarz-f(3)"
name: "zlarz-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlarz-f/"
description: "zlarz.f –"
---

<p>zlarz.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlarz</code> (SIDE, M, N, L, V, INCV, TAU, C, LDC, WORK)<br />
 <i></i><code>ZLARZ</code> applies an elementary reflector (as returned by stzrzf) to a general matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlarz (characterSIDE, integerM, integerN, integerL, complex*16, dimension( * )V, integerINCV, complex*16TAU, complex*16, dimension( ldc, * )C, integerLDC, complex*16, dimension( * )WORK)</h3>
<p><code>ZLARZ</code> applies an elementary reflector (as returned by stzrzf) to a general matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLARZ applies a complex elementary reflector H to a complex
 M-by-N matrix C, from either the left or the right. H is represented
 in the form
 H = I - tau * v * v**H
 where tau is a complex scalar and v is a complex vector.
 If tau = 0, then H is taken to be the unit matrix.
 To apply H**H (the conjugate transpose of H), supply conjg(tau) instead
 tau.
 H is a product of k elementary reflectors as returned by ZTZRZF.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>SIDE</i> </p>
<pre> SIDE is CHARACTER*1
 = 'L': form H * C
 = 'R': form C * H</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix C.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix C.</pre>
<p><i>L</i> </p>
<pre> L is INTEGER
 The number of entries of the vector V containing
 the meaningful part of the Householder vectors.
 If SIDE = 'L', M &gt;= L &gt;= 0, if SIDE = 'R', N &gt;= L &gt;= 0.</pre>
<p><i>V</i> </p>
<pre> V is COMPLEX*16 array, dimension (1+(L-1)*abs(INCV))
 The vector v in the representation of H as returned by
 ZTZRZF. V is not used if TAU = 0.</pre>
<p><i>INCV</i> </p>
<pre> INCV is INTEGER
 The increment between elements of v. INCV &lt;&gt; 0.</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX*16
 The value tau in the representation of H.</pre>
<p><i>C</i> </p>
<pre> C is COMPLEX*16 array, dimension (LDC,N)
 On entry, the M-by-N matrix C.
 On exit, C is overwritten by the matrix H * C if SIDE = 'L',
 or C * H if SIDE = 'R'.</pre>
<p><i>LDC</i> </p>
<pre> LDC is INTEGER
 The leading dimension of the array C. LDC &gt;= max(1,M).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension
 (N) if SIDE = 'L'
 or (M) if SIDE = 'R'</pre>
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
<p> <code>Contributors: </code></p>
<dl>
<dd>A. Petitet, Computer Science Dept., Univ. of Tenn., Knoxville, USA</dl>
<p> <code>Further Details: </code></p>
<dl>
<dd>&nbsp;<wbr></dl>
<p> Definition at line 148 of file zlarz.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
