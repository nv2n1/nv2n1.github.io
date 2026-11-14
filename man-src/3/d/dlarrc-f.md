---
title: "dlarrc-f(3)"
name: "dlarrc-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlarrc-f/"
description: "dlarrc.f –"
---

<p>dlarrc.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlarrc</code> (JOBT, N, VL, VU, D, E, PIVMIN, EIGCNT, LCNT, RCNT, INFO)<br />
 <i></i><code>DLARRC</code> computes the number of eigenvalues of the symmetric tridiagonal matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlarrc (characterJOBT, integerN, double precisionVL, double precisionVU, double precision, dimension( * )D, double precision, dimension( * )E, double precisionPIVMIN, integerEIGCNT, integerLCNT, integerRCNT, integerINFO)</h3>
<p><code>DLARRC</code> computes the number of eigenvalues of the symmetric tridiagonal matrix. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> Find the number of eigenvalues of the symmetric tridiagonal matrix T
 that are in the interval (VL,VU] if JOBT = 'T', and of L D L^T
 if JOBT = 'L'.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>JOBT</i> </p>
<pre> JOBT is CHARACTER*1
 = 'T': Compute Sturm count for matrix T.
 = 'L': Compute Sturm count for matrix L D L^T.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix. N &gt; 0.</pre>
<p><i>VL</i> </p>
<pre> VL is DOUBLE PRECISION</pre>
<p><i>VU</i> </p>
<pre> VU is DOUBLE PRECISION
 The lower and upper bounds for the eigenvalues.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 JOBT = 'T': The N diagonal elements of the tridiagonal matrix T.
 JOBT = 'L': The N diagonal elements of the diagonal matrix D.</pre>
<p><i>E</i> </p>
<pre> E is DOUBLE PRECISION array, dimension (N)
 JOBT = 'T': The N-1 offdiagonal elements of the matrix T.
 JOBT = 'L': The N-1 offdiagonal elements of the matrix L.</pre>
<p><i>PIVMIN</i> </p>
<pre> PIVMIN is DOUBLE PRECISION
 The minimum pivot in the Sturm sequence for T.</pre>
<p><i>EIGCNT</i> </p>
<pre> EIGCNT is INTEGER
 The number of eigenvalues of the symmetric tridiagonal matrix T
 that are in the interval (VL,VU]</pre>
<p><i>LCNT</i> </p>
<pre> LCNT is INTEGER</pre>
<p><i>RCNT</i> </p>
<pre> RCNT is INTEGER
 The left and right negcounts of the interval.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER</pre>
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
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>Beresford Parlett, University of California, Berkeley, USA </p>
<p>&nbsp;<wbr>Jim Demmel, University of California, Berkeley, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Inderjit Dhillon, University of Texas, Austin, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Osni Marques, LBNL/NERSC, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Christof Voemel, University of California, Berkeley, USA&nbsp;<wbr></dl>
<p> Definition at line 136 of file dlarrc.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
