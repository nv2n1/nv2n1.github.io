---
title: "slaqr1-f(3)"
name: "slaqr1-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slaqr1-f/"
description: "slaqr1.f –"
---

<p>slaqr1.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slaqr1</code> (N, H, LDH, SR1, SI1, SR2, SI2, V)<br />
 <i></i><code>SLAQR1</code> sets a scalar multiple of the first column of the product of 2-by-2 or 3-by-3 matrix H and specified shifts.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slaqr1 (integerN, real, dimension( ldh, * )H, integerLDH, realSR1, realSI1, realSR2, realSI2, real, dimension( * )V)</h3>
<p><code>SLAQR1</code> sets a scalar multiple of the first column of the product of 2-by-2 or 3-by-3 matrix H and specified shifts. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> Given a 2-by-2 or 3-by-3 matrix H, SLAQR1 sets v to a
 scalar multiple of the first column of the product
 (*) K = (H - (sr1 + i*si1)*I)*(H - (sr2 + i*si2)*I)
 scaling to avoid overflows and most underflows. It
 is assumed that either
 1) sr1 = sr2 and si1 = -si2
 or
 2) si1 = si2 = 0.
 This is useful for starting double implicit shift bulges
 in the QR algorithm.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is integer
 Order of the matrix H. N must be either 2 or 3.</pre>
<p><i>H</i> </p>
<pre> H is REAL array of dimension (LDH,N)
 The 2-by-2 or 3-by-3 matrix H in (*).</pre>
<p><i>LDH</i> </p>
<pre> LDH is integer
 The leading dimension of H as declared in
 the calling procedure. LDH.GE.N</pre>
<p><i>SR1</i> </p>
<pre> SR1 is REAL</pre>
<p><i>SI1</i> </p>
<pre> SI1 is REAL</pre>
<p><i>SR2</i> </p>
<pre> SR2 is REAL</pre>
<p><i>SI2</i> </p>
<pre> SI2 is REAL
 The shifts in (*).</pre>
<p><i>V</i> </p>
<pre> V is REAL array of dimension N
 A scalar multiple of the first column of the
 matrix K in (*).</pre>
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
<dd>Karen Braman and Ralph Byers, Department of Mathematics, University of Kansas, USA</dl>
<p> Definition at line 122 of file slaqr1.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
