---
title: "clarfx-f(3)"
name: "clarfx-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clarfx-f/"
description: "clarfx.f –"
---

<p>clarfx.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>clarfx</code> (SIDE, M, N, V, TAU, C, LDC, WORK)<br />
 <i></i><code>CLARFX</code> applies an elementary reflector to a general rectangular matrix, with loop unrolling when the reflector has order ≤ 10.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clarfx (characterSIDE, integerM, integerN, complex, dimension( * )V, complexTAU, complex, dimension( ldc, * )C, integerLDC, complex, dimension( * )WORK)</h3>
<p><code>CLARFX</code> applies an elementary reflector to a general rectangular matrix, with loop unrolling when the reflector has order ≤ 10. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CLARFX applies a complex elementary reflector H to a complex m by n
 matrix C, from either the left or the right. H is represented in the
 form
 H = I - tau * v * v**H
 where tau is a complex scalar and v is a complex vector.
 If tau = 0, then H is taken to be the unit matrix
 This version uses inline code if H has order &lt; 11.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
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
<pre> V is COMPLEX array, dimension (M) if SIDE = 'L'
 or (N) if SIDE = 'R'
 The vector v in the representation of H.</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX
 The value tau in the representation of H.</pre>
<p><i>C</i> </p>
<pre> C is COMPLEX array, dimension (LDC,N)
 On entry, the m by n matrix C.
 On exit, C is overwritten by the matrix H * C if SIDE = 'L',
 or C * H if SIDE = 'R'.</pre>
<p><i>LDC</i> </p>
<pre> LDC is INTEGER
 The leading dimension of the array C. LDA &gt;= max(1,M).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (N) if SIDE = 'L'
 or (M) if SIDE = 'R'
 WORK is not referenced if H has order &lt; 11.</pre>
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
<p> Definition at line 120 of file clarfx.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
