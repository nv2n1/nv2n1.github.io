---
title: "dlasq3-f(3)"
name: "dlasq3-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlasq3-f/"
description: "dlasq3.f –"
---

<p>dlasq3.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlasq3</code> (I0, N0, Z, PP, DMIN, SIGMA, DESIG, QMAX, NFAIL, ITER, NDIV, IEEE, TTYPE, DMIN1, DMIN2, DN, DN1, DN2, G, TAU)<br />
 <i></i><code>DLASQ3</code> checks for deflation, computes a shift and calls dqds. Used by sbdsqr.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlasq3 (integerI0, integerN0, double precision, dimension( * )Z, integerPP, double precisionDMIN, double precisionSIGMA, double precisionDESIG, double precisionQMAX, integerNFAIL, integerITER, integerNDIV, logicalIEEE, integerTTYPE, double precisionDMIN1, double precisionDMIN2, double precisionDN, double precisionDN1, double precisionDN2, double precisionG, double precisionTAU)</h3>
<p><code>DLASQ3</code> checks for deflation, computes a shift and calls dqds. Used by sbdsqr. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLASQ3 checks for deflation, computes a shift (TAU) and calls dqds.
 In case of failure it changes shifts, and tries again until output
 is positive.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>I0</i> </p>
<pre> I0 is INTEGER
 First index.</pre>
<p><i>N0</i> </p>
<pre> N0 is INTEGER
 Last index.</pre>
<p><i>Z</i> </p>
<pre> Z is DOUBLE PRECISION array, dimension ( 4*N )
 Z holds the qd array.</pre>
<p><i>PP</i> </p>
<pre> PP is INTEGER
 PP=0 for ping, PP=1 for pong.
 PP=2 indicates that flipping was applied to the Z array 
 and that the initial tests for deflation should not be 
 performed.</pre>
<p><i>DMIN</i> </p>
<pre> DMIN is DOUBLE PRECISION
 Minimum value of d.</pre>
<p><i>SIGMA</i> </p>
<pre> SIGMA is DOUBLE PRECISION
 Sum of shifts used in current segment.</pre>
<p><i>DESIG</i> </p>
<pre> DESIG is DOUBLE PRECISION
 Lower order part of SIGMA</pre>
<p><i>QMAX</i> </p>
<pre> QMAX is DOUBLE PRECISION
 Maximum value of q.</pre>
<p><i>NFAIL</i> </p>
<pre> NFAIL is INTEGER
 Number of times shift was too big.</pre>
<p><i>ITER</i> </p>
<pre> ITER is INTEGER
 Number of iterations.</pre>
<p><i>NDIV</i> </p>
<pre> NDIV is INTEGER
 Number of divisions.</pre>
<p><i>IEEE</i> </p>
<pre> IEEE is LOGICAL
 Flag for IEEE or non IEEE arithmetic (passed to DLASQ5).</pre>
<p><i>TTYPE</i> </p>
<pre> TTYPE is INTEGER
 Shift type.</pre>
<p><i>DMIN1</i> </p>
<pre> DMIN1 is DOUBLE PRECISION</pre>
<p><i>DMIN2</i> </p>
<pre> DMIN2 is DOUBLE PRECISION</pre>
<p><i>DN</i> </p>
<pre> DN is DOUBLE PRECISION</pre>
<p><i>DN1</i> </p>
<pre> DN1 is DOUBLE PRECISION</pre>
<p><i>DN2</i> </p>
<pre> DN2 is DOUBLE PRECISION</pre>
<p><i>G</i> </p>
<pre> G is DOUBLE PRECISION</pre>
<p><i>TAU</i> </p>
<pre> TAU is DOUBLE PRECISION
 These are passed as arguments in order to save their values
 between calls to DLASQ3.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> Definition at line 181 of file dlasq3.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
