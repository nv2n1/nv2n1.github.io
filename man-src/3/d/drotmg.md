---

title: "drotmg(3)"
name: "drotmg"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drotmg/"
description: "drotmg.f –"
---

<p> drotmg.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>drotmg</code> (DD1, DD2, DX1, DY1, DPARAM)<br />
 <i></i><code>DROTMG</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine drotmg (double precisionDD1, double precisionDD2, double precisionDX1, double precisionDY1, double precision, dimension(5)DPARAM)</h3>
<p> <code>DROTMG</code> <code>Purpose: </code></p>
<dl>
<dt>
</dt><dd>
<pre>
    CONSTRUCT THE MODIFIED GIVENS TRANSFORMATION MATRIX H WHICH ZEROS
    THE SECOND COMPONENT OF THE 2-VECTOR  (DSQRT(DD1)*DX1,DSQRT(DD2)*&gt;    DY2)**T.
    WITH DPARAM(1)=DFLAG, H HAS ONE OF THE FOLLOWING FORMS..
    DFLAG=-1.D0     DFLAG=0.D0        DFLAG=1.D0     DFLAG=-2.D0
      (DH11  DH12)    (1.D0  DH12)    (DH11  1.D0)    (1.D0  0.D0)
    H=(          )    (          )    (          )    (          )
      (DH21  DH22),   (DH21  1.D0),   (-1.D0 DH22),   (0.D0  1.D0).
    LOCATIONS 2-4 OF DPARAM CONTAIN DH11, DH21, DH12, AND DH22
    RESPECTIVELY. (VALUES OF 1.D0, -1.D0, OR 0.D0 IMPLIED BY THE
    VALUE OF DPARAM(1) ARE NOT STORED IN DPARAM.)
    THE VALUES OF GAMSQ AND RGAMSQ SET IN THE DATA STATEMENT MAY BE
    INEXACT.  THIS IS OK AS THEY ARE ONLY USED FOR TESTING THE SIZE
    OF DD1 AND DD2.  ALL ACTUAL SCALING OF DATA IS DONE USING GAM.
</pre>
<p>&nbsp;<wbr></dd></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
</dt><dd> <i>DD1</i> </dd>
<pre>
          DD1 is DOUBLE PRECISION
</pre>
<p> <i>DD2</i> </p>
<pre>
          DD2 is DOUBLE PRECISION
</pre>
<p> <i>DX1</i> </p>
<pre>
          DX1 is DOUBLE PRECISION
</pre>
<p> <i>DY1</i> </p>
<pre>
          DY1 is DOUBLE PRECISION
</pre>
<p> <i>DPARAM</i> </p>
<pre>
          DPARAM is DOUBLE PRECISION array, dimension 5
     DPARAM(1)=DFLAG
     DPARAM(2)=DH11
     DPARAM(3)=DH21
     DPARAM(4)=DH12
     DPARAM(5)=DH22
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dt>
</dt><dd> Univ. of Tennessee </dd>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
</dt><dd> November 2011</dd></dl>
<p> Definition at line 91 of file drotmg.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
