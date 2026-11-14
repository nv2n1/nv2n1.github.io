---
title: "dlarf-f(3)"
name: "dlarf-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlarf-f/"
description: "dlarf.f –"
---

<p>dlarf.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlarf</code> (SIDE, M, N, V, INCV, TAU, C, LDC, WORK)<br />
 <i></i><code>DLARF</code> applies an elementary reflector to a general rectangular matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlarf (characterSIDE, integerM, integerN, double precision, dimension( * )V, integerINCV, double precisionTAU, double precision, dimension( ldc, * )C, integerLDC, double precision, dimension( * )WORK)</h3>
<p><code>DLARF</code> applies an elementary reflector to a general rectangular matrix. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLARF applies a real elementary reflector H to a real m by n matrix
 C, from either the left or the right. H is represented in the form
 H = I - tau * v * v**T
 where tau is a real scalar and v is a real vector.
 If tau = 0, then H is taken to be the unit matrix.</pre>
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
<pre> V is DOUBLE PRECISION array, dimension
 (1 + (M-1)*abs(INCV)) if SIDE = 'L'
 or (1 + (N-1)*abs(INCV)) if SIDE = 'R'
 The vector v in the representation of H. V is not used if
 TAU = 0.</pre>
<p><i>INCV</i> </p>
<pre> INCV is INTEGER
 The increment between elements of v. INCV &lt;&gt; 0.</pre>
<p><i>TAU</i> </p>
<pre> TAU is DOUBLE PRECISION
 The value tau in the representation of H.</pre>
<p><i>C</i> </p>
<pre> C is DOUBLE PRECISION array, dimension (LDC,N)
 On entry, the m by n matrix C.
 On exit, C is overwritten by the matrix H * C if SIDE = 'L',
 or C * H if SIDE = 'R'.</pre>
<p><i>LDC</i> </p>
<pre> LDC is INTEGER
 The leading dimension of the array C. LDC &gt;= max(1,M).</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension
 (N) if SIDE = 'L'
 or (M) if SIDE = 'R'</pre>
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
<p> Definition at line 125 of file dlarf.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
