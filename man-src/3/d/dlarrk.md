---
title: "dlarrk(3)"
name: "dlarrk"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlarrk/"
description: "dlarrk.f –"
---

<h2 class="name">NAME</h2>
<p> dlarrk.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlarrk</code> (N, IW, GL, GU, D, E2, PIVMIN, RELTOL, W, WERR, INFO)<br />
 <i></i><code>DLARRK</code> computes one eigenvalue of a symmetric tridiagonal matrix T to suitable accuracy.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlarrk (integerN, integerIW, double precisionGL, double precisionGU, double precision, dimension( * )D, double precision, dimension( * )E2, double precisionPIVMIN, double precisionRELTOL, double precisionW, double precisionWERR, integerINFO)</h3>
<p> <code>DLARRK</code> computes one eigenvalue of a symmetric tridiagonal matrix T to suitable accuracy. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLARRK computes one eigenvalue of a symmetric tridiagonal
 matrix T to suitable accuracy. This is an auxiliary code to be
 called from DSTEMR.
 To avoid overflow, the matrix must be scaled so that its
 largest element is no greater than overflow**(1/2) * underflow**(1/4) in absolute value, and for greatest
 accuracy, it should not be much smaller than that.
 See W. Kahan &quot;Accurate Eigenvalues of a Symmetric Tridiagonal
 Matrix&quot;, Report CS41, Computer Science Dept., Stanford
 University, July 21, 1966.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the tridiagonal matrix T.  N &gt;= 0.
</pre>
<p> <i>IW</i> </p>
<pre>
          IW is INTEGER
          The index of the eigenvalues to be returned.
</pre>
<p> <i>GL</i> </p>
<pre>
          GL is DOUBLE PRECISION
</pre>
<p> <i>GU</i> </p>
<pre>
          GU is DOUBLE PRECISION
          An upper and a lower bound on the eigenvalue.
</pre>
<p> <i>D</i> </p>
<pre>
          D is DOUBLE PRECISION array, dimension (N)
          The n diagonal elements of the tridiagonal matrix T.
</pre>
<p> <i>E2</i> </p>
<pre>
          E2 is DOUBLE PRECISION array, dimension (N-1)
          The (n-1) squared off-diagonal elements of the tridiagonal matrix T.
</pre>
<p> <i>PIVMIN</i> </p>
<pre>
          PIVMIN is DOUBLE PRECISION
          The minimum pivot allowed in the Sturm sequence for T.
</pre>
<p> <i>RELTOL</i> </p>
<pre>
          RELTOL is DOUBLE PRECISION
          The minimum relative width of an interval.  When an interval
          is narrower than RELTOL times the larger (in
          magnitude) endpoint, then it is considered to be
          sufficiently small, i.e., converged.  Note: this should
          always be at least radix*machine epsilon.
</pre>
<p> <i>W</i> </p>
<pre>
          W is DOUBLE PRECISION
</pre>
<p> <i>WERR</i> </p>
<pre>
          WERR is DOUBLE PRECISION
          The error bound on the corresponding eigenvalue approximation
          in W.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:       Eigenvalue converged
          = -1:      Eigenvalue did NOT converge
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Internal Parameters: </code></p>
<dl>
<dt>
<dd>
<pre>
  FUDGE   DOUBLE PRECISION, default = 2
          A &quot;fudge factor&quot; to widen the Gershgorin intervals.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
<dd> September 2012</dl>
<p> Definition at line 145 of file dlarrk.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
