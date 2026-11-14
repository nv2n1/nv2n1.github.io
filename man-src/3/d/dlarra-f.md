---
title: "dlarra-f(3)"
name: "dlarra-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlarra-f/"
description: "dlarra.f –"
---

<p>dlarra.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlarra</code> (N, D, E, E2, SPLTOL, TNRM, NSPLIT, ISPLIT, INFO)<br />
 <i></i><code>DLARRA</code> computes the splitting points with the specified threshold.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlarra (integerN, double precision, dimension( * )D, double precision, dimension( * )E, double precision, dimension( * )E2, double precisionSPLTOL, double precisionTNRM, integerNSPLIT, integer, dimension( * )ISPLIT, integerINFO)</h3>
<p><code>DLARRA</code> computes the splitting points with the specified threshold. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> Compute the splitting points with threshold SPLTOL.
 DLARRA sets any &quot;small&quot; off-diagonal elements to zero.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix. N &gt; 0.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 On entry, the N diagonal elements of the tridiagonal
 matrix T.</pre>
<p><i>E</i> </p>
<pre> E is DOUBLE PRECISION array, dimension (N)
 On entry, the first (N-1) entries contain the subdiagonal
 elements of the tridiagonal matrix T; E(N) need not be set.
 On exit, the entries E( ISPLIT( I ) ), 1 &lt;= I &lt;= NSPLIT,
 are set to zero, the other entries of E are untouched.</pre>
<p><i>E2</i> </p>
<pre> E2 is DOUBLE PRECISION array, dimension (N)
 On entry, the first (N-1) entries contain the SQUARES of the
 subdiagonal elements of the tridiagonal matrix T;
 E2(N) need not be set.
 On exit, the entries E2( ISPLIT( I ) ),
 1 &lt;= I &lt;= NSPLIT, have been set to zero</pre>
<p><i>SPLTOL</i> </p>
<pre> SPLTOL is DOUBLE PRECISION
 The threshold for splitting. Two criteria can be used:
 SPLTOL&lt;0 : criterion based on absolute off-diagonal value
 SPLTOL&gt;0 : criterion that preserves relative accuracy</pre>
<p><i>TNRM</i> </p>
<pre> TNRM is DOUBLE PRECISION
 The norm of the matrix.</pre>
<p><i>NSPLIT</i> </p>
<pre> NSPLIT is INTEGER
 The number of blocks T splits into. 1 &lt;= NSPLIT &lt;= N.</pre>
<p><i>ISPLIT</i> </p>
<pre> ISPLIT is INTEGER array, dimension (N)
 The splitting points, at which T breaks up into blocks.
 The first block consists of rows/columns 1 to <a href="//www.systutorials.com/docs/linux/man/1-ISPLIT/">ISPLIT</a>(1),
 the second of rows/columns <a href="//www.systutorials.com/docs/linux/man/1-ISPLIT/">ISPLIT</a>(1)+1 through <a href="//www.systutorials.com/docs/linux/man/2-ISPLIT/">ISPLIT</a>(2),
 etc., and the NSPLIT-th consists of rows/columns
 ISPLIT(NSPLIT-1)+1 through ISPLIT(NSPLIT)=N.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit</pre>
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
<p> Definition at line 136 of file dlarra.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
