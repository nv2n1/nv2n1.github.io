---
title: "dlamc1(3)"
name: "dlamc1"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlamc1/"
description: "dlamchf77.f –"
---

<h2 class="name">NAME</h2>
<p> dlamchf77.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> DOUBLE PRECISION function <code>dlamch</code> (CMACH)<br />
 <i></i><code>DLAMCHF77</code> deprecated<br />
 subroutine <code>dlamc1</code> (BETA, T, RND, IEEE1)<br />
 <i></i><code>DLAMC1</code><br />
 subroutine <code>dlamc2</code> (BETA, T, RND, EPS, EMIN, RMIN, EMAX, RMAX)<br />
 <i></i><code>DLAMC2</code><br />
 DOUBLE PRECISION function <code>dlamc3</code> (A, B)<br />
 <i></i><code>DLAMC3</code><br />
 subroutine <code>dlamc4</code> (EMIN, START, BASE)<br />
 <i></i><code>DLAMC4</code><br />
 subroutine <code>dlamc5</code> (BETA, P, EMIN, IEEE, EMAX, RMAX)<br />
 <i></i><code>DLAMC5</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlamc1 (integerBETA, integerT, logicalRND, logicalIEEE1)</h3>
<p> <code>DLAMC1</code> <code>Purpose:</code> </p>
<pre>
 DLAMC1 determines the machine parameters given by BETA, T, RND, and
 IEEE1.
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>BETA</i> </p>
<pre>
          The base of the machine.
</pre>
<p> <i>T</i> </p>
<pre>
          The number of ( BETA ) digits in the mantissa.
</pre>
<p> <i>RND</i> </p>
<pre>
          Specifies whether proper rounding  ( RND = .TRUE. )  or
          chopping  ( RND = .FALSE. )  occurs in addition. This may not
          be a reliable guide to the way in which the machine performs
          its arithmetic.
</pre>
<p> <i>IEEE1</i> </p>
<pre>
          Specifies whether rounding appears to be done in the IEEE
          'round to nearest' style.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dt>
<dd> LAPACK is a software package provided by Univ. of Tennessee, Univ. of California Berkeley, Univ. of Colorado Denver and NAG Ltd..</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
<dd> April 2012</dl>
<p> <code>Further</code> <code>Details</code> </p>
<pre>
  The routine is based on the routine  ENVRON  by Malcolm and
  incorporates suggestions by Gentleman and Marovich. See
     Malcolm M. A. (1972) Algorithms to reveal properties of
        floating-point arithmetic. Comms. of the ACM, 15, 949-951.
     Gentleman W. M. and Marovich S. B. (1974) More on algorithms
        that reveal properties of floating point arithmetic units.
        Comms. of the ACM, 17, 276-277.
</pre>
<p>&nbsp;<wbr> </p>
<p> Definition at line 206 of file dlamchf77.f.</p>
<h3>subroutine dlamc2 (integerBETA, integerT, logicalRND, double precisionEPS, integerEMIN, double precisionRMIN, integerEMAX, double precisionRMAX)</h3>
<p> <code>DLAMC2</code> <code>Purpose:</code> </p>
<pre>
 DLAMC2 determines the machine parameters specified in its argument
 list.
</pre>
<p>&nbsp;<wbr> </p>
<p> <code>Author:</code></p>
<dl>
<dt>
<dd> LAPACK is a software package provided by Univ. of Tennessee, Univ. of California Berkeley, Univ. of Colorado Denver and NAG Ltd..</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
<dd> April 2012</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>BETA</i> </p>
<pre>
          The base of the machine.
</pre>
<p> <i>T</i> </p>
<pre>
          The number of ( BETA ) digits in the mantissa.
</pre>
<p> <i>RND</i> </p>
<pre>
          Specifies whether proper rounding  ( RND = .TRUE. )  or
          chopping  ( RND = .FALSE. )  occurs in addition. This may not
          be a reliable guide to the way in which the machine performs
          its arithmetic.
</pre>
<p> <i>EPS</i> </p>
<pre>
          The smallest positive number such that
             fl( 1.0 - EPS ) .LT. 1.0,
          where fl denotes the computed value.
</pre>
<p> <i>EMIN</i> </p>
<pre>
          The minimum exponent before (gradual) underflow occurs.
</pre>
<p> <i>RMIN</i> </p>
<pre>
          The smallest normalized number for the machine, given by
          BASE**( EMIN - 1 ), where  BASE  is the floating point value
          of BETA.
</pre>
<p> <i>EMAX</i> </p>
<pre>
          The maximum exponent before overflow occurs.
</pre>
<p> <i>RMAX</i> </p>
<pre>
          The largest positive number for the machine, given by
          BASE**EMAX * ( 1 - EPS ), where  BASE  is the floating point
          value of BETA.
</pre>
</dl>
<p> <code>Further</code> <code>Details</code> </p>
<pre>
  The computation of  EPS  is based on a routine PARANOIA by
  W. Kahan of the University of California at Berkeley.
</pre>
<p>&nbsp;<wbr> </p>
<p> Definition at line 419 of file dlamchf77.f.</p>
<h3>DOUBLE PRECISION function dlamc3 (double precisionA, double precisionB)</h3>
<p> <code>DLAMC3</code> <code>Purpose:</code> </p>
<pre>
 DLAMC3  is intended to force  A  and  B  to be stored prior to doing
 the addition of  A  and  B ,  for use in situations where optimizers
 might hold one of these in a register.
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>A</i><br />
 <i>B</i> </p>
<pre>
          The values A and B.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 642 of file dlamchf77.f.</p>
<h3>subroutine dlamc4 (integerEMIN, double precisionSTART, integerBASE)</h3>
<p> <code>DLAMC4</code> <code>Purpose:</code> </p>
<pre>
 DLAMC4 is a service routine for DLAMC2.
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>EMIN</i> </p>
<pre>
          The minimum exponent before (gradual) underflow, computed by
          setting A = START and dividing by BASE until the previous A
          can not be recovered.
</pre>
<p> <i>START</i> </p>
<pre>
          The starting point for determining EMIN.
</pre>
<p> <i>BASE</i> </p>
<pre>
          The base of the machine.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 689 of file dlamchf77.f.</p>
<h3>subroutine dlamc5 (integerBETA, integerP, integerEMIN, logicalIEEE, integerEMAX, double precisionRMAX)</h3>
<p> <code>DLAMC5</code> <code>Purpose:</code> </p>
<pre>
 DLAMC5 attempts to compute RMAX, the largest machine floating-point
 number, without overflow.  It assumes that EMAX + abs(EMIN) sum
 approximately to a power of 2.  It will fail on machines where this
 assumption does not hold, for example, the Cyber 205 (EMIN = -28625,
 EMAX = 28718).  It will also fail if the value supplied for EMIN is
 too large (i.e. too close to zero), probably with overflow.
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>BETA</i> </p>
<pre>
          The base of floating-point arithmetic.
</pre>
<p> <i>P</i> </p>
<pre>
          The number of base BETA digits in the mantissa of a
          floating-point value.
</pre>
<p> <i>EMIN</i> </p>
<pre>
          The minimum exponent before (gradual) underflow.
</pre>
<p> <i>IEEE</i> </p>
<pre>
          A logical flag specifying whether or not the arithmetic
          system is thought to comply with the IEEE standard.
</pre>
<p> <i>EMAX</i> </p>
<pre>
          The largest exponent before overflow
</pre>
<p> <i>RMAX</i> </p>
<pre>
          The largest machine floating-point number.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 796 of file dlamchf77.f.</p>
<h3>DOUBLE PRECISION function dlamch (characterCMACH)</h3>
<p> <code>DLAMCHF77</code> deprecated <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLAMCHF77 determines double precision machine parameters.
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
<dd> April 2012</dl>
<p> Definition at line 64 of file dlamchf77.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
