---
title: "slarrr-f(3)"
name: "slarrr-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slarrr-f/"
description: "slarrr.f –"
---

<p>slarrr.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slarrr</code> (N, D, E, INFO)<br />
 <i></i><code>SLARRR</code> performs tests to decide whether the symmetric tridiagonal matrix T warrants expensive computations which guarantee high relative accuracy in the eigenvalues.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slarrr (integerN, real, dimension( * )D, real, dimension( * )E, integerINFO)</h3>
<p><code>SLARRR</code> performs tests to decide whether the symmetric tridiagonal matrix T warrants expensive computations which guarantee high relative accuracy in the eigenvalues. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> Perform tests to decide whether the symmetric tridiagonal matrix T
 warrants expensive computations which guarantee high relative accuracy
 in the eigenvalues.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix. N &gt; 0.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (N)
 The N diagonal elements of the tridiagonal matrix T.</pre>
<p><i>E</i> </p>
<pre> E is REAL array, dimension (N)
 On entry, the first (N-1) entries contain the subdiagonal
 elements of the tridiagonal matrix T; E(N) is set to ZERO.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 INFO = 0(default) : the matrix warrants computations preserving
 relative accuracy.
 INFO = 1 : the matrix warrants computations guaranteeing
 only absolute accuracy.</pre>
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
<dd>Beresford Parlett, University of California, Berkeley, USA </p>
<p>&nbsp;<wbr>Jim Demmel, University of California, Berkeley, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Inderjit Dhillon, University of Texas, Austin, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Osni Marques, LBNL/NERSC, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Christof Voemel, University of California, Berkeley, USA&nbsp;<wbr></dl>
<p> Definition at line 95 of file slarrr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
