---
title: "iparmq-f(3)"
name: "iparmq-f"
section: "3"
letter: "i"
url: "/docs/linux/man/3-iparmq-f/"
description: "iparmq.f –"
---

<p>iparmq.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>INTEGER function <code>iparmq</code> (ISPEC, NAME, OPTS, N, ILO, IHI, LWORK)<br />
 <i></i><code>IPARMQ</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>INTEGER function iparmq (integerISPEC, character, dimension( * )NAME, character, dimension( * )OPTS, integerN, integerILO, integerIHI, integerLWORK)</h3>
<p><code>IPARMQ</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> This program sets problem and machine dependent parameters
 useful for xHSEQR and its subroutines. It is called whenever 
 ILAENV is called with 12 &lt;= ISPEC &lt;= 16</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ISPEC</i> </p>
<pre> ISPEC is integer scalar
 ISPEC specifies which tunable parameter IPARMQ should
 return.
 ISPEC=12: (INMIN) Matrices of order nmin or less
 are sent directly to xLAHQR, the implicit
 double shift QR algorithm. NMIN must be
 at least 11.
 ISPEC=13: (INWIN) Size of the deflation window.
 This is best set greater than or equal to
 the number of simultaneous shifts NS.
 Larger matrices benefit from larger deflation
 windows.
 ISPEC=14: (INIBL) Determines when to stop nibbling and
 invest in an (expensive) multi-shift QR sweep.
 If the aggressive early deflation subroutine
 finds LD converged eigenvalues from an order
 NW deflation window and LD.GT.(NW*NIBBLE)/100,
 then the next QR sweep is skipped and early
 deflation is applied immediately to the
 remaining active diagonal block. Setting
 IPARMQ(ISPEC=14) = 0 causes TTQRE to skip a
 multi-shift QR sweep whenever early deflation
 finds a converged eigenvalue. Setting
 IPARMQ(ISPEC=14) greater than or equal to 100
 prevents TTQRE from skipping a multi-shift
 QR sweep.
 ISPEC=15: (NSHFTS) The number of simultaneous shifts in
 a multi-shift QR iteration.
 ISPEC=16: (IACC22) IPARMQ is set to 0, 1 or 2 with the
 following meanings.
 0: During the multi-shift QR sweep,
 xLAQR5 does not accumulate reflections and
 does not use matrix-matrix multiply to
 update the far-from-diagonal matrix
 entries.
 1: During the multi-shift QR sweep,
 xLAQR5 and/or xLAQRaccumulates reflections and uses
 matrix-matrix multiply to update the
 far-from-diagonal matrix entries.
 2: During the multi-shift QR sweep.
 xLAQR5 accumulates reflections and takes
 advantage of 2-by-2 block structure during
 matrix-matrix multiplies.
 (If xTRMM is slower than xGEMM, then
 IPARMQ(ISPEC=16)=1 may be more efficient than
 IPARMQ(ISPEC=16)=2 despite the greater level of
 arithmetic work implied by the latter choice.)</pre>
<p><i>NAME</i> </p>
<pre> NAME is character string
 Name of the calling subroutine</pre>
<p><i>OPTS</i> </p>
<pre> OPTS is character string
 This is a concatenation of the string arguments to
 TTQRE.</pre>
<p><i>N</i> </p>
<pre> N is integer scalar
 N is the order of the Hessenberg matrix H.</pre>
<p><i>ILO</i> </p>
<pre> ILO is INTEGER</pre>
<p><i>IHI</i> </p>
<pre> IHI is INTEGER
 It is assumed that H is already upper triangular
 in rows and columns 1:ILO-1 and IHI+1:N.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is integer scalar
 The amount of workspace available.</pre>
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
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> Little is known about how best to choose these parameters.
 It is possible to use different values of the parameters
 for each of CHSEQR, DHSEQR, SHSEQR and ZHSEQR.
 It is probably best to choose different parameters for
 different matrices and different parameters at different
 times during the iteration, but this has not been
 implemented --- yet.
 The best choices of most of the parameters depend
 in an ill-understood way on the relative execution
 rate of xLAQR3 and xLAQR5 and on the nature of each
 particular eigenvalue problem. Experiment may be the
 only practical way to determine which choices are most
 effective.
 Following is a list of default values supplied by IPARMQ.
 These defaults may be adjusted in order to attain better
 performance in any particular computational environment.
 IPARMQ(ISPEC=12) The xLAHQR vs xLAQR0 crossover point.
 Default: 75. (Must be at least 11.)
 IPARMQ(ISPEC=13) Recommended deflation window size.
 This depends on ILO, IHI and NS, the
 number of simultaneous shifts returned
 by IPARMQ(ISPEC=15). The default for
 (IHI-ILO+1).LE.500 is NS. The default
 for (IHI-ILO+1).GT.500 is 3*NS/2.
 IPARMQ(ISPEC=14) Nibble crossover point. Default: 14.
 IPARMQ(ISPEC=15) Number of simultaneous shifts, NS.
 a multi-shift QR iteration.
 If IHI-ILO+1 is ...
 greater than ...but less ... the
 or equal to ... than default is
 0 30 NS = 2+
 30 60 NS = 4+
 60 150 NS = 10
 150 590 NS = **
 590 3000 NS = 64
 3000 6000 NS = 128
 6000 infinity NS = 256
 (+) By default matrices of this order are
 passed to the implicit double shift routine
 xLAHQR. See IPARMQ(ISPEC=12) above. These
 values of NS are used only in case of a rare
 xLAHQR failure.
 (**) The asterisks (**) indicate an ad-hoc
 function increasing from 10 to 64.
 IPARMQ(ISPEC=16) Select structured matrix multiply.
 (See ISPEC=16 above for details.)
 Default: 3.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 215 of file iparmq.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
