---
title: "zlarfx(3)"
name: "zlarfx"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlarfx/"
description: "zlarfx.f –"
---

<p>zlarfx.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlarfx</code> (SIDE, M, N, V, TAU, C, LDC, WORK)<br />
 <i></i><code>ZLARFX</code> applies an elementary reflector to a general rectangular matrix, with loop unrolling when the reflector has order ≤ 10.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlarfx (characterSIDE, integerM, integerN, complex*16, dimension( * )V, complex*16TAU, complex*16, dimension( ldc, * )C, integerLDC, complex*16, dimension( * )WORK)</h3>
<p><code>ZLARFX</code> applies an elementary reflector to a general rectangular matrix, with loop unrolling when the reflector has order ≤ 10. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLARFX applies a complex elementary reflector H to a complex m by n
 matrix C, from either the left or the right. H is represented in the
 form
 H = I - tau * v * v**H
 where tau is a complex scalar and v is a complex vector.
 If tau = 0, then H is taken to be the unit matrix
 This version uses inline code if H has order &lt; 11.</pre>
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
<pre> V is COMPLEX*16 array, dimension (M) if SIDE = 'L'
 or (N) if SIDE = 'R'
 The vector v in the representation of H.</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX*16
 The value tau in the representation of H.</pre>
<p><i>C</i> </p>
<pre> C is COMPLEX*16 array, dimension (LDC,N)
 On entry, the m by n matrix C.
 On exit, C is overwritten by the matrix H * C if SIDE = 'L',
 or C * H if SIDE = 'R'.</pre>
<p><i>LDC</i> </p>
<pre> LDC is INTEGER
 The leading dimension of the array C. LDA &gt;= max(1,M).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (N) if SIDE = 'L'
 or (M) if SIDE = 'R'
 WORK is not referenced if H has order &lt; 11.</pre>
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
<p> Definition at line 120 of file zlarfx.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
