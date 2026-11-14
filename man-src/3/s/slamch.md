---
title: "slamch(3)"
name: "slamch"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slamch/"
description: "slamch.f –"
---

<h2 class="name">NAME</h2>
<p> slamch.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> REAL function <code>slamch</code> (CMACH)<br />
 <i></i><code>SLAMCH</code><br />
 REAL function <code>slamc3</code> (A, B)<br />
 <i></i><code>SLAMC3</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>REAL function slamc3 (realA, realB)</h3>
<p> <code>SLAMC3</code> <code>Purpose:</code> </p>
<pre>
 SLAMC3  is intended to force  A  and  B  to be stored prior to doing
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
<p> <i>B</i> </p>
<pre>
          The values A and B.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 171 of file slamch.f.</p>
<h3>REAL function slamch (characterCMACH)</h3>
<p> <code>SLAMCH</code> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLAMCH determines single precision machine parameters.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>CMACH</i> </p>
<pre>
          Specifies the value to be returned by SLAMCH:
          = 'E' or 'e',   SLAMCH := eps
          = 'S' or 's ,   SLAMCH := sfmin
          = 'B' or 'b',   SLAMCH := base
          = 'P' or 'p',   SLAMCH := eps*base
          = 'N' or 'n',   SLAMCH := t
          = 'R' or 'r',   SLAMCH := rnd
          = 'M' or 'm',   SLAMCH := emin
          = 'U' or 'u',   SLAMCH := rmin
          = 'L' or 'l',   SLAMCH := emax
          = 'O' or 'o',   SLAMCH := rmax
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
<p> Definition at line 68 of file slamch.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
