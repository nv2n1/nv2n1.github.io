---
title: "dlarnv(3)"
name: "dlarnv"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlarnv/"
description: "dlarnv.f –"
---

<h2 class="name">NAME</h2>
<p> dlarnv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlarnv</code> (IDIST, ISEED, N, X)<br />
 <i></i><code>DLARNV</code> returns a vector of random numbers from a uniform or normal distribution.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlarnv (integerIDIST, integer, dimension( 4 )ISEED, integerN, double precision, dimension( * )X)</h3>
<p> <code>DLARNV</code> returns a vector of random numbers from a uniform or normal distribution. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLARNV returns a vector of n random real numbers from a uniform or
 normal distribution.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>IDIST</i> </p>
<pre>
          IDIST is INTEGER
          Specifies the distribution of the random numbers:
          = 1:  uniform (0,1)
          = 2:  uniform (-1,1)
          = 3:  normal (0,1)
</pre>
<p> <i>ISEED</i> </p>
<pre>
          ISEED is INTEGER array, dimension (4)
          On entry, the seed of the random number generator; the array
          elements must be between 0 and 4095, and <a href="//www.systutorials.com/docs/linux/man/4-ISEED/">ISEED</a>(4) must be
          odd.
          On exit, the seed is updated.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of random numbers to be generated.
</pre>
<p> <i>X</i> </p>
<pre>
          X is DOUBLE PRECISION array, dimension (N)
          The generated random numbers.
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
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  This routine calls the auxiliary routine DLARUV to generate random
  real numbers from a uniform (0,1) distribution, in batches of up to
  128 using vectorisable code. The Box-Muller method is used to
  transform numbers from a uniform to a normal distribution.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 98 of file dlarnv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
