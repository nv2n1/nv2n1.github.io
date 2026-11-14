---
title: "dlar1v(3)"
name: "dlar1v"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlar1v/"
description: "dlar1v.f –"
---

<h2 class="name">NAME</h2>
<p> dlar1v.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlar1v</code> (N, B1, BN, LAMBDA, D, L, LD, LLD, PIVMIN, GAPTOL, Z, WANTNC, NEGCNT, ZTZ, MINGMA, R, ISUPPZ, NRMINV, RESID, RQCORR, WORK)<br />
 <i></i><code>DLAR1V</code> computes the (scaled) r-th column of the inverse of the submatrix in rows b1 through bn of the tridiagonal matrix LDLT &#8211; λI.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlar1v (integerN, integerB1, integerBN, double precisionLAMBDA, double precision, dimension( * )D, double precision, dimension( * )L, double precision, dimension( * )LD, double precision, dimension( * )LLD, double precisionPIVMIN, double precisionGAPTOL, double precision, dimension( * )Z, logicalWANTNC, integerNEGCNT, double precisionZTZ, double precisionMINGMA, integerR, integer, dimension( * )ISUPPZ, double precisionNRMINV, double precisionRESID, double precisionRQCORR, double precision, dimension( * )WORK)</h3>
<p> <code>DLAR1V</code> computes the (scaled) r-th column of the inverse of the submatrix in rows b1 through bn of the tridiagonal matrix LDLT &#8211; λI. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DLAR1V computes the (scaled) r-th column of the inverse of
 the sumbmatrix in rows B1 through BN of the tridiagonal matrix
 L D L**T - sigma I. When sigma is close to an eigenvalue, the
 computed vector is an accurate eigenvector. Usually, r corresponds
 to the index where the eigenvector is largest in magnitude.
 The following steps accomplish this computation :
 (a) Stationary qd transform,  L D L**T - sigma I = L(+) D(+) L(+)**T,
 (b) Progressive qd transform, L D L**T - sigma I = U(-) D(-) U(-)**T,
 (c) Computation of the diagonal elements of the inverse of
     L D L**T - sigma I by combining the above transforms, and choosing
     r as the index where the diagonal of the inverse is (one of the)
     largest in magnitude.
 (d) Computation of the (scaled) r-th column of the inverse using the
     twisted factorization obtained by combining the top part of the
     the stationary and the bottom part of the progressive transform.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
           The order of the matrix L D L**T.
</pre>
<p> <i>B1</i> </p>
<pre>
          B1 is INTEGER
           First index of the submatrix of L D L**T.
</pre>
<p> <i>BN</i> </p>
<pre>
          BN is INTEGER
           Last index of the submatrix of L D L**T.
</pre>
<p> <i>LAMBDA</i> </p>
<pre>
          LAMBDA is DOUBLE PRECISION
           The shift. In order to compute an accurate eigenvector,
           LAMBDA should be a good approximation to an eigenvalue
           of L D L**T.
</pre>
<p> <i>L</i> </p>
<pre>
          L is DOUBLE PRECISION array, dimension (N-1)
           The (n-1) subdiagonal elements of the unit bidiagonal matrix
           L, in elements 1 to N-1.
</pre>
<p> <i>D</i> </p>
<pre>
          D is DOUBLE PRECISION array, dimension (N)
           The n diagonal elements of the diagonal matrix D.
</pre>
<p> <i>LD</i> </p>
<pre>
          LD is DOUBLE PRECISION array, dimension (N-1)
           The n-1 elements L(i)*D(i).
</pre>
<p> <i>LLD</i> </p>
<pre>
          LLD is DOUBLE PRECISION array, dimension (N-1)
           The n-1 elements L(i)*L(i)*D(i).
</pre>
<p> <i>PIVMIN</i> </p>
<pre>
          PIVMIN is DOUBLE PRECISION
           The minimum pivot in the Sturm sequence.
</pre>
<p> <i>GAPTOL</i> </p>
<pre>
          GAPTOL is DOUBLE PRECISION
           Tolerance that indicates when eigenvector entries are negligible
           w.r.t. their contribution to the residual.
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is DOUBLE PRECISION array, dimension (N)
           On input, all entries of Z must be set to 0.
           On output, Z contains the (scaled) r-th column of the
           inverse. The scaling is such that Z(R) equals 1.
</pre>
<p> <i>WANTNC</i> </p>
<pre>
          WANTNC is LOGICAL
           Specifies whether NEGCNT has to be computed.
</pre>
<p> <i>NEGCNT</i> </p>
<pre>
          NEGCNT is INTEGER
           If WANTNC is .TRUE. then NEGCNT = the number of pivots &lt; pivmin
           in the  matrix factorization L D L**T, and NEGCNT = -1 otherwise.
</pre>
<p> <i>ZTZ</i> </p>
<pre>
          ZTZ is DOUBLE PRECISION
           The square of the 2-norm of Z.
</pre>
<p> <i>MINGMA</i> </p>
<pre>
          MINGMA is DOUBLE PRECISION
           The reciprocal of the largest (in magnitude) diagonal
           element of the inverse of L D L**T - sigma I.
</pre>
<p> <i>R</i> </p>
<pre><code>
          R is INTEGER
           The twist index for the twisted factorization used to
           compute Z.
           On input, 0 &lt;= R &lt;= N. If R is input as 0, R is set to
           the index where (L D L**T - sigma I)^{
    -1} is largest
           in magnitude. If 1 &lt;= R &lt;= N, R is unchanged.
           On output, R contains the twist index used to compute Z.
           Ideally, R designates the position of the maximum entry in the
           eigenvector.
</code></pre>
<p> <i>ISUPPZ</i> </p>
<pre>
          ISUPPZ is INTEGER array, dimension (2)
           The support of the vector in Z, i.e., the vector Z is
           nonzero only in elements <a href="//www.systutorials.com/docs/linux/man/1-ISUPPZ/">ISUPPZ</a>(1) through ISUPPZ( 2 ).
</pre>
<p> <i>NRMINV</i> </p>
<pre>
          NRMINV is DOUBLE PRECISION
           NRMINV = 1/SQRT( ZTZ )
</pre>
<p> <i>RESID</i> </p>
<pre>
          RESID is DOUBLE PRECISION
           The residual of the FP vector.
           RESID = ABS( MINGMA )/SQRT( ZTZ )
</pre>
<p> <i>RQCORR</i> </p>
<pre>
          RQCORR is DOUBLE PRECISION
           The Rayleigh Quotient correction to LAMBDA.
           RQCORR = MINGMA*TMP
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (4*N)
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
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Beresford Parlett, University of California, Berkeley, USA </p>
<p>&nbsp;<wbr>Jim Demmel, University of California, Berkeley, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Inderjit Dhillon, University of Texas, Austin, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Osni Marques, LBNL/NERSC, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Christof Voemel, University of California, Berkeley, USA&nbsp;<wbr></dl>
<p> Definition at line 229 of file dlar1v.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
