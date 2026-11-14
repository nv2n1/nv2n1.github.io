---
title: "zlaqr5-f(3)"
name: "zlaqr5-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlaqr5-f/"
description: "zlaqr5.f –"
---

<p>zlaqr5.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlaqr5</code> (WANTT, WANTZ, KACC22, N, KTOP, KBOT, NSHFTS, S, H, LDH, ILOZ, IHIZ, Z, LDZ, V, LDV, U, LDU, NV, WV, LDWV, NH, WH, LDWH)<br />
 <i></i><code>ZLAQR5</code> performs a single small-bulge multi-shift QR sweep.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlaqr5 (logicalWANTT, logicalWANTZ, integerKACC22, integerN, integerKTOP, integerKBOT, integerNSHFTS, complex*16, dimension( * )S, complex*16, dimension( ldh, * )H, integerLDH, integerILOZ, integerIHIZ, complex*16, dimension( ldz, * )Z, integerLDZ, complex*16, dimension( ldv, * )V, integerLDV, complex*16, dimension( ldu, * )U, integerLDU, integerNV, complex*16, dimension( ldwv, * )WV, integerLDWV, integerNH, complex*16, dimension( ldwh, * )WH, integerLDWH)</h3>
<p><code>ZLAQR5</code> performs a single small-bulge multi-shift QR sweep. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLAQR5, called by ZLAQR0, performs a
 single small-bulge multi-shift QR sweep.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>WANTT</i> </p>
<pre> WANTT is logical scalar
 WANTT = .true. if the triangular Schur factor
 is being computed. WANTT is set to .false. otherwise.</pre>
<p><i>WANTZ</i> </p>
<pre> WANTZ is logical scalar
 WANTZ = .true. if the unitary Schur factor is being
 computed. WANTZ is set to .false. otherwise.</pre>
<p><i>KACC22</i> </p>
<pre> KACC22 is integer with value 0, 1, or 2.
 Specifies the computation mode of far-from-diagonal
 orthogonal updates.
 = 0: ZLAQR5 does not accumulate reflections and does not
 use matrix-matrix multiply to update far-from-diagonal
 matrix entries.
 = 1: ZLAQR5 accumulates reflections and uses matrix-matrix
 multiply to update the far-from-diagonal matrix entries.
 = 2: ZLAQR5 accumulates reflections, uses matrix-matrix
 multiply to update the far-from-diagonal matrix entries,
 and takes advantage of 2-by-2 block structure during
 matrix multiplies.</pre>
<p><i>N</i> </p>
<pre> N is integer scalar
 N is the order of the Hessenberg matrix H upon which this
 subroutine operates.</pre>
<p><i>KTOP</i> </p>
<pre> KTOP is integer scalar</pre>
<p><i>KBOT</i> </p>
<pre> KBOT is integer scalar
 These are the first and last rows and columns of an
 isolated diagonal block upon which the QR sweep is to be
 applied. It is assumed without a check that
 either KTOP = 1 or H(KTOP,KTOP-1) = 0
 and
 either KBOT = N or H(KBOT+1,KBOT) = 0.</pre>
<p><i>NSHFTS</i> </p>
<pre> NSHFTS is integer scalar
 NSHFTS gives the number of simultaneous shifts. NSHFTS
 must be positive and even.</pre>
<p><i>S</i> </p>
<pre> S is COMPLEX*16 array of size (NSHFTS)
 S contains the shifts of origin that define the multi-
 shift QR sweep. On output S may be reordered.</pre>
<p><i>H</i> </p>
<pre> H is COMPLEX*16 array of size (LDH,N)
 On input H contains a Hessenberg matrix. On output a
 multi-shift QR sweep with shifts SR(J)+i*SI(J) is applied
 to the isolated diagonal block in rows and columns KTOP
 through KBOT.</pre>
<p><i>LDH</i> </p>
<pre> LDH is integer scalar
 LDH is the leading dimension of H just as declared in the
 calling procedure. LDH.GE.MAX(1,N).</pre>
<p><i>ILOZ</i> </p>
<pre> ILOZ is INTEGER</pre>
<p><i>IHIZ</i> </p>
<pre> IHIZ is INTEGER
 Specify the rows of Z to which transformations must be
 applied if WANTZ is .TRUE.. 1 .LE. ILOZ .LE. IHIZ .LE. N</pre>
<p><i>Z</i> </p>
<pre> Z is COMPLEX*16 array of size (LDZ,IHI)
 If WANTZ = .TRUE., then the QR Sweep unitary
 similarity transformation is accumulated into
 Z(ILOZ:IHIZ,ILO:IHI) from the right.
 If WANTZ = .FALSE., then Z is unreferenced.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is integer scalar
 LDA is the leading dimension of Z just as declared in
 the calling procedure. LDZ.GE.N.</pre>
<p><i>V</i> </p>
<pre> V is COMPLEX*16 array of size (LDV,NSHFTS/2)</pre>
<p><i>LDV</i> </p>
<pre> LDV is integer scalar
 LDV is the leading dimension of V as declared in the
 calling procedure. LDV.GE.3.</pre>
<p><i>U</i> </p>
<pre> U is COMPLEX*16 array of size
 (LDU,3*NSHFTS-3)</pre>
<p><i>LDU</i> </p>
<pre> LDU is integer scalar
 LDU is the leading dimension of U just as declared in the
 in the calling subroutine. LDU.GE.3*NSHFTS-3.</pre>
<p><i>NH</i> </p>
<pre> NH is integer scalar
 NH is the number of columns in array WH available for
 workspace. NH.GE.1.</pre>
<p><i>WH</i> </p>
<pre> WH is COMPLEX*16 array of size (LDWH,NH)</pre>
<p><i>LDWH</i> </p>
<pre> LDWH is integer scalar
 Leading dimension of WH just as declared in the
 calling procedure. LDWH.GE.3*NSHFTS-3.</pre>
<p><i>NV</i> </p>
<pre> NV is integer scalar
 NV is the number of rows in WV agailable for workspace.
 NV.GE.1.</pre>
<p><i>WV</i> </p>
<pre> WV is COMPLEX*16 array of size
 (LDWV,3*NSHFTS-3)</pre>
<p><i>LDWV</i> </p>
<pre> LDWV is integer scalar
 LDWV is the leading dimension of WV as declared in the
 in the calling subroutine. LDWV.GE.NV.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> <code>Contributors: </code></p>
<dl>
<dd>Karen Braman and Ralph Byers, Department of Mathematics, University of Kansas, USA</dl>
<p> <code>References: </code></p>
<dl>
<dd>K. Braman, R. Byers and R. Mathias, The Multi-Shift QR Algorithm Part I: Maintaining Well Focused Shifts, and Level 3 Performance, SIAM Journal of Matrix Analysis, volume 23, pages 929&#8211;947, 2002.</dl>
<p> Definition at line 250 of file zlaqr5.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
