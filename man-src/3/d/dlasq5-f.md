---
title: "dlasq5-f(3)"
name: "dlasq5-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlasq5-f/"
---

dlasq5.f - 

<h2>Synopsis</h2><h3>Functions/Subroutines</h3>subroutine <b>dlasq5</b> (I0, N0, Z, PP, TAU, SIGMA, DMIN, DMIN1, DMIN2, DN, DNM1, DNM2, IEEE, EPS) 
 <i></i><b>DLASQ5</b> computes one dqds transform in ping-pong form. Used by sbdsqr and sstegr.
<h2>Function/Subroutine Documentation</h2><h3>subroutine dlasq5 (integerI0, integerN0, double precision, dimension( * )Z, integerPP, double precisionTAU, double precisionSIGMA, double precisionDMIN, double precisionDMIN1, double precisionDMIN2, double precisionDN, double precisionDNM1, double precisionDNM2, logicalIEEE, double precisionEPS)</h3><b>DLASQ5</b> computes one dqds transform in ping-pong form. Used by sbdsqr and sstegr. 

 <b>Purpose: </b>
<dl COMPACT><dd><pre> DLASQ5 computes one dqds transform in ping-pong form, one
 version for IEEE machines another for non IEEE machines.</pre>&nbsp;<wbr></dl>
 

 <b>Parameters:</b>
<dl COMPACT><dd><i>I0</i> 

 <pre> I0 is INTEGER
 First index.</pre><i>N0</i> 

 <pre> N0 is INTEGER
 Last index.</pre><i>Z</i> 

 <pre> Z is DOUBLE PRECISION array, dimension ( 4*N )
 Z holds the qd array. EMIN is stored in Z(4*N0) to avoid
 an extra argument.</pre><i>PP</i> 

 <pre> PP is INTEGER
 PP=0 for ping, PP=1 for pong.</pre><i>TAU</i> 

 <pre> TAU is DOUBLE PRECISION
 This is the shift.</pre><i>SIGMA</i> 

 <pre> SIGMA is DOUBLE PRECISION
 This is the accumulated shift up to this step.</pre><i>DMIN</i> 

 <pre> DMIN is DOUBLE PRECISION
 Minimum value of d.</pre><i>DMIN1</i> 

 <pre> DMIN1 is DOUBLE PRECISION
 Minimum value of d, excluding D( N0 ).</pre><i>DMIN2</i> 

 <pre> DMIN2 is DOUBLE PRECISION
 Minimum value of d, excluding D( N0 ) and D( N0-1 ).</pre><i>DN</i> 

 <pre> DN is DOUBLE PRECISION
 d(N0), the last value of d.</pre><i>DNM1</i> 

 <pre> DNM1 is DOUBLE PRECISION
 d(N0-1).</pre><i>DNM2</i> 

 <pre> DNM2 is DOUBLE PRECISION
 d(N0-2).</pre><i>IEEE</i> 

 <pre> IEEE is LOGICAL
 Flag for IEEE or non IEEE arithmetic.</pre>&nbsp;<wbr> 
 <i>EPS</i> 

 <pre> EPS is DOUBLE PRECISION
 This is the value of epsilon used.</pre>&nbsp;<wbr></dl>
 

 <b>Author:</b>
<dl COMPACT><dd>Univ. of Tennessee 

 Univ. of California Berkeley 

 Univ. of Colorado Denver 

 NAG Ltd.</dl>
 

 <b>Date:</b>
<dl COMPACT><dd>September 2012</dl>
 

 

 

 Definition at line 144 of file dlasq5.f.
<h2>Author</h2>Generated automatically by Doxygen for LAPACK from the source code.
