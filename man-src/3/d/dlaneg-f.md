---
title: "dlaneg-f(3)"
name: "dlaneg-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlaneg-f/"
description: "dlaneg.f –"
---

<p>dlaneg.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>INTEGER function <code>dlaneg</code> (N, D, LLD, SIGMA, PIVMIN, R)<br />
 <i></i><code>DLANEG</code> computes the Sturm count.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>INTEGER function dlaneg (integerN, double precision, dimension( * )D, double precision, dimension( * )LLD, double precisionSIGMA, double precisionPIVMIN, integerR)</h3>
<p><code>DLANEG</code> computes the Sturm count. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLANEG computes the Sturm count, the number of negative pivots
 encountered while factoring tridiagonal T - sigma I = L D L^T.
 This implementation works directly on the factors without forming
 the tridiagonal matrix T. The Sturm count is also the number of
 eigenvalues of T less than sigma.
 This routine is called from DLARRB.
 The current routine does not use the PIVMIN parameter but rather
 requires IEEE-754 propagation of Infinities and NaNs. This
 routine also has no input range restrictions but does require
 default exception handling such that x/0 produces Inf when x is
 non-zero, and Inf/Inf produces NaN. For more information, see:
 Marques, Riedy, and Voemel, &quot;Benefits of IEEE-754 Features in
 Modern Symmetric Tridiagonal Eigensolvers,&quot; SIAM Journal on
 Scientific Computing, v28, n5, 2006. DOI 10.1137/050641624
 (Tech report version in LAWN 172 with the same title.)</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 The N diagonal elements of the diagonal matrix D.</pre>
<p><i>LLD</i> </p>
<pre> LLD is DOUBLE PRECISION array, dimension (N-1)
 The (N-1) elements L(i)*L(i)*D(i).</pre>
<p><i>SIGMA</i> </p>
<pre> SIGMA is DOUBLE PRECISION
 Shift amount in T - sigma I = L D L^T.</pre>
<p><i>PIVMIN</i> </p>
<pre> PIVMIN is DOUBLE PRECISION
 The minimum pivot in the Sturm sequence. May be used
 when zero pivots are encountered on non-IEEE-754
 architectures.</pre>
<p><i>R</i> </p>
<pre> R is INTEGER
 The twist index for the twisted factorization that is used
 for the negcount.</pre>
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
<dd>Osni Marques, LBNL/NERSC, USA </p>
<p>&nbsp;<wbr>Christof Voemel, University of California, Berkeley, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Jason Riedy, University of California, Berkeley, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr></dl>
<p> Definition at line 119 of file dlaneg.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
