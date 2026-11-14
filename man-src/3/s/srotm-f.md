---
title: "srotm-f(3)"
name: "srotm-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-srotm-f/"
description: "srotm.f –"
---

<p>srotm.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>srotm</code> (N, SX, INCX, SY, INCY, SPARAM)<br />
 <i></i><code>SROTM</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine srotm (integerN, real, dimension(*)SX, integerINCX, real, dimension(*)SY, integerINCY, real, <a href="/docs/linux/man/5-dimension/">dimension</a>(5)SPARAM)</h3>
<p><code>SROTM</code> <code>Purpose: </code></p>
<dl>
<dd>
<pre> APPLY THE MODIFIED GIVENS TRANSFORMATION, H, TO THE 2 BY N MATRIX
 (SX**T) , WHERE **T INDICATES TRANSPOSE. THE ELEMENTS OF SX ARE IN
 (SX**T)
 SX(LX+I*INCX), I = 0 TO N-1, WHERE LX = 1 IF INCX .GE. 0, ELSE
 LX = (-INCX)*N, AND SIMILARLY FOR SY USING USING LY AND INCY.
 WITH <a href="//www.systutorials.com/docs/linux/man/1-SPARAM/">SPARAM</a>(1)=SFLAG, H HAS ONE OF THE FOLLOWING FORMS..
 SFLAG=-1.E0 SFLAG=0.E0 SFLAG=1.E0 SFLAG=-2.E0
 (SH11 SH12) (1.E0 SH12) (SH11 1.E0) (1.E0 0.E0)
 H=( ) ( ) ( ) ( )
 (SH21 SH22), (SH21 1.E0), (-1.E0 SH22), (0.E0 1.E0).
 SEE SROTMG FOR A DESCRIPTION OF DATA STORAGE IN SPARAM.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 number of elements in input vector(s)</pre>
<p><i>SX</i> </p>
<pre> SX is REAL array, dimension N
 double precision vector with N elements</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 storage spacing between elements of SX</pre>
<p><i>SY</i> </p>
<pre> SY is REAL array, dimension N
 double precision vector with N elements</pre>
<p><i>INCY</i> </p>
<pre> INCY is INTEGER
 storage spacing between elements of SY</pre>
<p><i>SPARAM</i> </p>
<pre> SPARAM is REAL array, dimension 5
 <a href="//www.systutorials.com/docs/linux/man/1-SPARAM/">SPARAM</a>(1)=SFLAG
 <a href="//www.systutorials.com/docs/linux/man/2-SPARAM/">SPARAM</a>(2)=SH11
 <a href="//www.systutorials.com/docs/linux/man/3-SPARAM/">SPARAM</a>(3)=SH21
 <a href="//www.systutorials.com/docs/linux/man/4-SPARAM/">SPARAM</a>(4)=SH12
 <a href="//www.systutorials.com/docs/linux/man/5-SPARAM/">SPARAM</a>(5)=SH22</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> Definition at line 100 of file srotm.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
