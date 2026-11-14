---
title: "drotm-f(3)"
name: "drotm-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drotm-f/"
description: "drotm.f –"
---

<p>drotm.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>drotm</code> (N, DX, INCX, DY, INCY, DPARAM)<br />
 <i></i><code>DROTM</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine drotm (integerN, double precision, dimension(*)DX, integerINCX, double precision, dimension(*)DY, integerINCY, double precision, <a href="/docs/linux/man/5-dimension/">dimension</a>(5)DPARAM)</h3>
<p><code>DROTM</code> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> APPLY THE MODIFIED GIVENS TRANSFORMATION, H, TO THE 2 BY N MATRIX
 (DX**T) , WHERE **T INDICATES TRANSPOSE. THE ELEMENTS OF DX ARE IN
 (DY**T)
 DX(LX+I*INCX), I = 0 TO N-1, WHERE LX = 1 IF INCX .GE. 0, ELSE
 LX = (-INCX)*N, AND SIMILARLY FOR SY USING LY AND INCY.
 WITH <a href="//www.systutorials.com/docs/linux/man/1-DPARAM/">DPARAM</a>(1)=DFLAG, H HAS ONE OF THE FOLLOWING FORMS..
 DFLAG=-1.D0 DFLAG=0.D0 DFLAG=1.D0 DFLAG=-2.D0
 (DH11 DH12) (1.D0 DH12) (DH11 1.D0) (1.D0 0.D0)
 H=( ) ( ) ( ) ( )
 (DH21 DH22), (DH21 1.D0), (-1.D0 DH22), (0.D0 1.D0).
 SEE DROTMG FOR A DESCRIPTION OF DATA STORAGE IN DPARAM.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 number of elements in input vector(s)</pre>
<p><i>DX</i> </p>
<pre> DX is DOUBLE PRECISION array, dimension N
 double precision vector with N elements</pre>
<p><i>INCX</i> </p>
<pre> INCX is INTEGER
 storage spacing between elements of DX</pre>
<p><i>DY</i> </p>
<pre> DY is DOUBLE PRECISION array, dimension N
 double precision vector with N elements</pre>
<p><i>INCY</i> </p>
<pre> INCY is INTEGER
 storage spacing between elements of DY</pre>
<p><i>DPARAM</i> </p>
<pre> DPARAM is DOUBLE PRECISION array, dimension 5
 <a href="//www.systutorials.com/docs/linux/man/1-DPARAM/">DPARAM</a>(1)=DFLAG
 <a href="//www.systutorials.com/docs/linux/man/2-DPARAM/">DPARAM</a>(2)=DH11
 <a href="//www.systutorials.com/docs/linux/man/3-DPARAM/">DPARAM</a>(3)=DH21
 <a href="//www.systutorials.com/docs/linux/man/4-DPARAM/">DPARAM</a>(4)=DH12
 <a href="//www.systutorials.com/docs/linux/man/5-DPARAM/">DPARAM</a>(5)=DH22</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> Definition at line 99 of file drotm.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
