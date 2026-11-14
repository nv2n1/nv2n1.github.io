---
title: "zlarf-f(3)"
name: "zlarf-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlarf-f/"
description: "zlarf.f –"
---

<p>zlarf.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlarf</code> (SIDE, M, N, V, INCV, TAU, C, LDC, WORK)<br />
 <i></i><code>ZLARF</code> applies an elementary reflector to a general rectangular matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlarf (characterSIDE, integerM, integerN, complex*16, dimension( * )V, integerINCV, complex*16TAU, complex*16, dimension( ldc, * )C, integerLDC, complex*16, dimension( * )WORK)</h3>
<p><code>ZLARF</code> applies an elementary reflector to a general rectangular matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLARF applies a complex elementary reflector H to a complex M-by-N
 matrix C, from either the left or the right. H is represented in the
 form
 H = I - tau * v * v**H
 where tau is a complex scalar and v is a complex vector.
 If tau = 0, then H is taken to be the unit matrix.
 To apply H**H, supply conjg(tau) instead
 tau.</pre>
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
<p><i>V</i> </p>
<pre> V is COMPLEX*16 array, dimension
 (1 + (M-1)*abs(INCV)) if SIDE = 'L'
 or (1 + (N-1)*abs(INCV)) if SIDE = 'R'
 The vector v in the representation of H. V is not used if
 TAU = 0.</pre>
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
<p> Definition at line 129 of file zlarf.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
