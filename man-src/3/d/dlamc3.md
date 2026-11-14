---
title: "dlamc3(3)"
name: "dlamc3"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlamc3/"
description: "dlamch.f –"
---

<h2 class="name">NAME</h2>
<p> dlamch.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> DOUBLE PRECISION function <code>dlamch</code> (CMACH)<br />
 <i></i><code>DLAMCH</code><br />
 DOUBLE PRECISION function <code>dlamc3</code> (A, B)<br />
 <i></i><code>DLAMC3</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function dlamc3 (double precisionA, double precisionB)</h3>
<p> <code>DLAMC3</code> <code>Purpose:</code> </p>
<pre>
 DLAMC3  is intended to force  A  and  B  to be stored prior to doing
 the addition of  A  and  B ,  for use in situations where optimizers
 might hold one of these in a register.
</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Author:</code></p>
<dl>
<dt>
<dd> LAPACK is a software package provided by Univ. of Tennessee, Univ. of California Berkeley, Univ. of Colorado Denver and NAG Ltd..</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
<dd> November 2011</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>A</i> </p>
<pre>
          A is a DOUBLE PRECISION
</pre>
<p> <i>B</i> </p>
<pre>
          B is a DOUBLE PRECISION
          The values A and B.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 172 of file dlamch.f.</p>
<h3>DOUBLE PRECISION function dlamch (characterCMACH)</h3>
<p> <code>DLAMCH</code> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLAMCH determines double precision machine parameters.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>CMACH</i> </p>
<pre>
          Specifies the value to be returned by DLAMCH:
          = 'E' or 'e',   DLAMCH := eps
          = 'S' or 's ,   DLAMCH := sfmin
          = 'B' or 'b',   DLAMCH := base
          = 'P' or 'p',   DLAMCH := eps*base
          = 'N' or 'n',   DLAMCH := t
          = 'R' or 'r',   DLAMCH := rnd
          = 'M' or 'm',   DLAMCH := emin
          = 'U' or 'u',   DLAMCH := rmin
          = 'L' or 'l',   DLAMCH := emax
          = 'O' or 'o',   DLAMCH := rmax
          where
          eps   = relative machine precision
          sfmin = safe minimum, such that 1/sfmin does not overflow
          base  = base of the machine
          prec  = eps*base
          t     = number of (base) digits in the mantissa
          rnd   = 1.0 when rounding occurs in addition, 0.0 otherwise
          emin  = minimum exponent before (gradual) underflow
          rmin  = underflow threshold - base**(emin-1)
          emax  = largest exponent before overflow
          rmax  = overflow threshold  - (base**emax)*(1-eps)
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
<dd> November 2011</dl>
<p> Definition at line 64 of file dlamch.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
