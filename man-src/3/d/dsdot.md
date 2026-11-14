---
title: "dsdot(3)"
name: "dsdot"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dsdot/"
description: "dsdot.f –"
---

<h2 class="name">NAME</h2>
<p> dsdot.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> DOUBLE PRECISION function <code>dsdot</code> (N, SX, INCX, SY, INCY)<br />
 <i></i><code>DSDOT</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function dsdot (integerN, real, dimension(*)SX, integerINCX, real, dimension(*)SY, integerINCY)</h3>
<p> <code>DSDOT</code> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
 Compute the inner product of two vectors with extended
 precision accumulation and result.
 Returns D.P. dot product accumulated in D.P., for S.P. SX and SY
 DSDOT = sum for I = 0 to N-1 of  SX(LX+I*INCX) * SY(LY+I*INCY),
 where LX = 1 if INCX .GE. 0, else LX = 1+(1-N)*INCX, and LY is
 defined in a similar way using INCY.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
         number of elements in input vector(s)
</pre>
<p> <i>SX</i> </p>
<pre>
          SX is REAL array, dimension(N)
         single precision vector with N elements
</pre>
<p> <i>INCX</i> </p>
<pre>
          INCX is INTEGER
          storage spacing between elements of SX
</pre>
<p> <i>SY</i> </p>
<pre>
          SY is REAL array, dimension(N)
         single precision vector with N elements
</pre>
<p> <i>INCY</i> </p>
<pre>
          INCY is INTEGER
         storage spacing between elements of SY
</pre>
</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> DSDOT </p>
<pre>
          DSDOT is DOUBLE PRECISION
         DSDOT  double precision dot product (zero if N.LE.0)
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
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<p>&nbsp;<wbr></dl>
<p> <code>References: </code></p>
<dl>
<dt>
<dd>
<pre>
  C. L. Lawson, R. J. Hanson, D. R. Kincaid and F. T.
  Krogh, Basic linear algebra subprograms for Fortran
  usage, Algorithm No. 539, Transactions on Mathematical
  Software 5, 3 (September 1979), pp. 308-323.
  REVISION HISTORY  (YYMMDD)
  791001  DATE WRITTEN
  890831  Modified array declarations.  (WRB)
  890831  REVISION DATE from Version 3.2
  891214  Prologue converted to Version 4.0 format.  (BAB)
  920310  Corrected definition of LX in DESCRIPTION.  (WRB)
  920501  Reformatted the REFERENCES section.  (WRB)
  070118  Reformat to LAPACK style (JL)
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 120 of file dsdot.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
