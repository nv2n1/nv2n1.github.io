---
title: "srotmg-f(3)"
name: "srotmg-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-srotmg-f/"
description: "srotmg.f –"
---

<p>srotmg.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>srotmg</code> (SD1, SD2, SX1, SY1, SPARAM)<br />
 <i></i><code>SROTMG</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine srotmg (realSD1, realSD2, realSX1, realSY1, real, <a href="/docs/linux/man/5-dimension/">dimension</a>(5)SPARAM)</h3>
<p><code>SROTMG</code> <code>Purpose: </code></p>
<dl>
<dd>
<pre> CONSTRUCT THE MODIFIED GIVENS TRANSFORMATION MATRIX H WHICH ZEROS
 THE SECOND COMPONENT OF THE 2-VECTOR (SQRT(SD1)*SX1,SQRT(SD2)*&gt; SY2)**T.
 WITH <a href="//www.systutorials.com/docs/linux/man/1-SPARAM/">SPARAM</a>(1)=SFLAG, H HAS ONE OF THE FOLLOWING FORMS..
 SFLAG=-1.E0 SFLAG=0.E0 SFLAG=1.E0 SFLAG=-2.E0
 (SH11 SH12) (1.E0 SH12) (SH11 1.E0) (1.E0 0.E0)
 H=( ) ( ) ( ) ( )
 (SH21 SH22), (SH21 1.E0), (-1.E0 SH22), (0.E0 1.E0).
 LOCATIONS 2-4 OF SPARAM CONTAIN SH11,SH21,SH12, AND SH22
 RESPECTIVELY. (VALUES OF 1.E0, -1.E0, OR 0.E0 IMPLIED BY THE
 VALUE OF <a href="//www.systutorials.com/docs/linux/man/1-SPARAM/">SPARAM</a>(1) ARE NOT STORED IN SPARAM.)
 THE VALUES OF GAMSQ AND RGAMSQ SET IN THE DATA STATEMENT MAY BE
 INEXACT. THIS IS OK AS THEY ARE ONLY USED FOR TESTING THE SIZE
 OF SD1 AND SD2. ALL ACTUAL SCALING OF DATA IS DONE USING GAM.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>SD1</i> </p>
<pre> SD1 is REAL</pre>
<p><i>SD2</i> </p>
<pre> SD2 is REAL</pre>
<p><i>SX1</i> </p>
<pre> SX1 is REAL</pre>
<p><i>SY1</i> </p>
<pre> SY1 is REAL</pre>
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
<p> Definition at line 91 of file srotmg.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
