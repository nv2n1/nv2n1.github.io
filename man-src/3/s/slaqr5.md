---
title: "slaqr5(3)"
name: "slaqr5"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slaqr5/"
description: "slaqr5.f –"
---

<h2 class="name">NAME</h2>
<p> slaqr5.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slaqr5</code> (WANTT, WANTZ, KACC22, N, KTOP, KBOT, NSHFTS, SR, SI, H, LDH, ILOZ, IHIZ, Z, LDZ, V, LDV, U, LDU, NV, WV, LDWV, NH, WH, LDWH)<br />
 <i></i><code>SLAQR5</code> performs a single small-bulge multi-shift QR sweep.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slaqr5 (logicalWANTT, logicalWANTZ, integerKACC22, integerN, integerKTOP, integerKBOT, integerNSHFTS, real, dimension( * )SR, real, dimension( * )SI, real, dimension( ldh, * )H, integerLDH, integerILOZ, integerIHIZ, real, dimension( ldz, * )Z, integerLDZ, real, dimension( ldv, * )V, integerLDV, real, dimension( ldu, * )U, integerLDU, integerNV, real, dimension( ldwv, * )WV, integerLDWV, integerNH, real, dimension( ldwh, * )WH, integerLDWH)</h3>
<p> <code>SLAQR5</code> performs a single small-bulge multi-shift QR sweep. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
    SLAQR5, called by SLAQR0, performs a
    single small-bulge multi-shift QR sweep.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>WANTT</i> </p>
<pre>
          WANTT is logical scalar
             WANTT = .true. if the quasi-triangular Schur factor
             is being computed.  WANTT is set to .false. otherwise.
</pre>
<p> <i>WANTZ</i> </p>
<pre>
          WANTZ is logical scalar
             WANTZ = .true. if the orthogonal Schur factor is being
             computed.  WANTZ is set to .false. otherwise.
</pre>
<p> <i>KACC22</i> </p>
<pre>
          KACC22 is integer with value 0, 1, or 2.
             Specifies the computation mode of far-from-diagonal
             orthogonal updates.
        = 0: SLAQR5 does not accumulate reflections and does not
             use matrix-matrix multiply to update far-from-diagonal
             matrix entries.
        = 1: SLAQR5 accumulates reflections and uses matrix-matrix
             multiply to update the far-from-diagonal matrix entries.
        = 2: SLAQR5 accumulates reflections, uses matrix-matrix
             multiply to update the far-from-diagonal matrix entries,
             and takes advantage of 2-by-2 block structure during
             matrix multiplies.
</pre>
<p> <i>N</i> </p>
<pre>
          N is integer scalar
             N is the order of the Hessenberg matrix H upon which this
             subroutine operates.
</pre>
<p> <i>KTOP</i> </p>
<pre>
          KTOP is integer scalar
</pre>
<p> <i>KBOT</i> </p>
<pre>
          KBOT is integer scalar
             These are the first and last rows and columns of an
             isolated diagonal block upon which the QR sweep is to be
             applied. It is assumed without a check that
                       either KTOP = 1  or   H(KTOP,KTOP-1) = 0
             and
                       either KBOT = N  or   H(KBOT+1,KBOT) = 0.
</pre>
<p> <i>NSHFTS</i> </p>
<pre>
          NSHFTS is integer scalar
             NSHFTS gives the number of simultaneous shifts.  NSHFTS
             must be positive and even.
</pre>
<p> <i>SR</i> </p>
<pre>
          SR is REAL array of size (NSHFTS)
</pre>
<p> <i>SI</i> </p>
<pre>
          SI is REAL array of size (NSHFTS)
             SR contains the real parts and SI contains the imaginary
             parts of the NSHFTS shifts of origin that define the
             multi-shift QR sweep.  On output SR and SI may be
             reordered.
</pre>
<p> <i>H</i> </p>
<pre>
          H is REAL array of size (LDH,N)
             On input H contains a Hessenberg matrix.  On output a
             multi-shift QR sweep with shifts SR(J)+i*SI(J) is applied
             to the isolated diagonal block in rows and columns KTOP
             through KBOT.
</pre>
<p> <i>LDH</i> </p>
<pre>
          LDH is integer scalar
             LDH is the leading dimension of H just as declared in the
             calling procedure.  LDH.GE.MAX(1,N).
</pre>
<p> <i>ILOZ</i> </p>
<pre>
          ILOZ is INTEGER
</pre>
<p> <i>IHIZ</i> </p>
<pre>
          IHIZ is INTEGER
             Specify the rows of Z to which transformations must be
             applied if WANTZ is .TRUE.. 1 .LE. ILOZ .LE. IHIZ .LE. N
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is REAL array of size (LDZ,IHI)
             If WANTZ = .TRUE., then the QR Sweep orthogonal
             similarity transformation is accumulated into
             Z(ILOZ:IHIZ,ILO:IHI) from the right.
             If WANTZ = .FALSE., then Z is unreferenced.
</pre>
<p> <i>LDZ</i> </p>
<pre>
          LDZ is integer scalar
             LDA is the leading dimension of Z just as declared in
             the calling procedure. LDZ.GE.N.
</pre>
<p> <i>V</i> </p>
<pre>
          V is REAL array of size (LDV,NSHFTS/2)
</pre>
<p> <i>LDV</i> </p>
<pre>
          LDV is integer scalar
             LDV is the leading dimension of V as declared in the
             calling procedure.  LDV.GE.3.
</pre>
<p> <i>U</i> </p>
<pre>
          U is REAL array of size
             (LDU,3*NSHFTS-3)
</pre>
<p> <i>LDU</i> </p>
<pre>
          LDU is integer scalar
             LDU is the leading dimension of U just as declared in the
             in the calling subroutine.  LDU.GE.3*NSHFTS-3.
</pre>
<p> <i>NH</i> </p>
<pre>
          NH is integer scalar
             NH is the number of columns in array WH available for
             workspace. NH.GE.1.
</pre>
<p> <i>WH</i> </p>
<pre>
          WH is REAL array of size (LDWH,NH)
</pre>
<p> <i>LDWH</i> </p>
<pre>
          LDWH is integer scalar
             Leading dimension of WH just as declared in the
             calling procedure.  LDWH.GE.3*NSHFTS-3.
</pre>
<p> <i>NV</i> </p>
<pre>
          NV is integer scalar
             NV is the number of rows in WV agailable for workspace.
             NV.GE.1.
</pre>
<p> <i>WV</i> </p>
<pre>
          WV is REAL array of size
             (LDWV,3*NSHFTS-3)
</pre>
<p> <i>LDWV</i> </p>
<pre>
          LDWV is integer scalar
             LDWV is the leading dimension of WV as declared in the
             in the calling subroutine.  LDWV.GE.NV.
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
<dd> Karen Braman and Ralph Byers, Department of Mathematics, University of Kansas, USA</dl>
<p> <code>References: </code></p>
<dl>
<dt>
<dd> K. Braman, R. Byers and R. Mathias, The Multi-Shift QR Algorithm Part I: Maintaining Well Focused Shifts, and Level 3 Performance, SIAM Journal of Matrix Analysis, volume 23, pages 929&#8211;947, 2002.</dl>
<p> Definition at line 258 of file slaqr5.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
