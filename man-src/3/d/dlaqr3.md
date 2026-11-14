---
title: "dlaqr3(3)"
name: "dlaqr3"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlaqr3/"
description: "dlaqr3.f –"
---

<h2 class="name">NAME</h2>
<p> dlaqr3.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlaqr3</code> (WANTT, WANTZ, N, KTOP, KBOT, NW, H, LDH, ILOZ, IHIZ, Z, LDZ, NS, ND, SR, SI, V, LDV, NH, T, LDT, NV, WV, LDWV, WORK, LWORK)<br />
 <i></i><code>DLAQR3</code> performs the orthogonal similarity transformation of a Hessenberg matrix to detect and deflate fully converged eigenvalues from a trailing principal submatrix (aggressive early deflation).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlaqr3 (logicalWANTT, logicalWANTZ, integerN, integerKTOP, integerKBOT, integerNW, double precision, dimension( ldh, * )H, integerLDH, integerILOZ, integerIHIZ, double precision, dimension( ldz, * )Z, integerLDZ, integerNS, integerND, double precision, dimension( * )SR, double precision, dimension( * )SI, double precision, dimension( ldv, * )V, integerLDV, integerNH, double precision, dimension( ldt, * )T, integerLDT, integerNV, double precision, dimension( ldwv, * )WV, integerLDWV, double precision, dimension( * )WORK, integerLWORK)</h3>
<p> <code>DLAQR3</code> performs the orthogonal similarity transformation of a Hessenberg matrix to detect and deflate fully converged eigenvalues from a trailing principal submatrix (aggressive early deflation). </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
    Aggressive early deflation:
    DLAQR3 accepts as input an upper Hessenberg matrix
    H and performs an orthogonal similarity transformation
    designed to detect and deflate fully converged eigenvalues from
    a trailing principal submatrix.  On output H has been over-
    written by a new Hessenberg matrix that is a perturbation of
    an orthogonal similarity transformation of H.  It is to be
    hoped that the final version of H has many zero subdiagonal
    entries.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>WANTT</i> </p>
<pre>
          WANTT is LOGICAL
          If .TRUE., then the Hessenberg matrix H is fully updated
          so that the quasi-triangular Schur factor may be
          computed (in cooperation with the calling subroutine).
          If .FALSE., then only enough of H is updated to preserve
          the eigenvalues.
</pre>
<p> <i>WANTZ</i> </p>
<pre>
          WANTZ is LOGICAL
          If .TRUE., then the orthogonal matrix Z is updated so
          so that the orthogonal Schur factor may be computed
          (in cooperation with the calling subroutine).
          If .FALSE., then Z is not referenced.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix H and (if WANTZ is .TRUE.) the
          order of the orthogonal matrix Z.
</pre>
<p> <i>KTOP</i> </p>
<pre>
          KTOP is INTEGER
          It is assumed that either KTOP = 1 or H(KTOP,KTOP-1)=0.
          KBOT and KTOP together determine an isolated block
          along the diagonal of the Hessenberg matrix.
</pre>
<p> <i>KBOT</i> </p>
<pre>
          KBOT is INTEGER
          It is assumed without a check that either
          KBOT = N or H(KBOT+1,KBOT)=0.  KBOT and KTOP together
          determine an isolated block along the diagonal of the
          Hessenberg matrix.
</pre>
<p> <i>NW</i> </p>
<pre>
          NW is INTEGER
          Deflation window size.  1 .LE. NW .LE. (KBOT-KTOP+1).
</pre>
<p> <i>H</i> </p>
<pre>
          H is DOUBLE PRECISION array, dimension (LDH,N)
          On input the initial N-by-N section of H stores the
          Hessenberg matrix undergoing aggressive early deflation.
          On output H has been transformed by an orthogonal
          similarity transformation, perturbed, and the returned
          to Hessenberg form that (it is to be hoped) has some
          zero subdiagonal entries.
</pre>
<p> <i>LDH</i> </p>
<pre>
          LDH is integer
          Leading dimension of H just as declared in the calling
          subroutine.  N .LE. LDH
</pre>
<p> <i>ILOZ</i> </p>
<pre>
          ILOZ is INTEGER
</pre>
<p> <i>IHIZ</i> </p>
<pre>
          IHIZ is INTEGER
          Specify the rows of Z to which transformations must be
          applied if WANTZ is .TRUE.. 1 .LE. ILOZ .LE. IHIZ .LE. N.
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is DOUBLE PRECISION array, dimension (LDZ,N)
          IF WANTZ is .TRUE., then on output, the orthogonal
          similarity transformation mentioned above has been
          accumulated into Z(ILOZ:IHIZ,ILO:IHI) from the right.
          If WANTZ is .FALSE., then Z is unreferenced.
</pre>
<p> <i>LDZ</i> </p>
<pre>
          LDZ is integer
          The leading dimension of Z just as declared in the
          calling subroutine.  1 .LE. LDZ.
</pre>
<p> <i>NS</i> </p>
<pre>
          NS is integer
          The number of unconverged (ie approximate) eigenvalues
          returned in SR and SI that may be used as shifts by the
          calling subroutine.
</pre>
<p> <i>ND</i> </p>
<pre>
          ND is integer
          The number of converged eigenvalues uncovered by this
          subroutine.
</pre>
<p> <i>SR</i> </p>
<pre>
          SR is DOUBLE PRECISION array, dimension (KBOT)
</pre>
<p> <i>SI</i> </p>
<pre>
          SI is DOUBLE PRECISION array, dimension (KBOT)
          On output, the real and imaginary parts of approximate
          eigenvalues that may be used for shifts are stored in
          SR(KBOT-ND-NS+1) through SR(KBOT-ND) and
          SI(KBOT-ND-NS+1) through SI(KBOT-ND), respectively.
          The real and imaginary parts of converged eigenvalues
          are stored in SR(KBOT-ND+1) through SR(KBOT) and
          SI(KBOT-ND+1) through SI(KBOT), respectively.
</pre>
<p> <i>V</i> </p>
<pre>
          V is DOUBLE PRECISION array, dimension (LDV,NW)
          An NW-by-NW work array.
</pre>
<p> <i>LDV</i> </p>
<pre>
          LDV is integer scalar
          The leading dimension of V just as declared in the
          calling subroutine.  NW .LE. LDV
</pre>
<p> <i>NH</i> </p>
<pre>
          NH is integer scalar
          The number of columns of T.  NH.GE.NW.
</pre>
<p> <i>T</i> </p>
<pre>
          T is DOUBLE PRECISION array, dimension (LDT,NW)
</pre>
<p> <i>LDT</i> </p>
<pre>
          LDT is integer
          The leading dimension of T just as declared in the
          calling subroutine.  NW .LE. LDT
</pre>
<p> <i>NV</i> </p>
<pre>
          NV is integer
          The number of rows of work array WV available for
          workspace.  NV.GE.NW.
</pre>
<p> <i>WV</i> </p>
<pre>
          WV is DOUBLE PRECISION array, dimension (LDWV,NW)
</pre>
<p> <i>LDWV</i> </p>
<pre>
          LDWV is integer
          The leading dimension of W just as declared in the
          calling subroutine.  NW .LE. LDV
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (LWORK)
          On exit, WORK(1) is set to an estimate of the optimal value
          of LWORK for the given values of N, NW, KTOP and KBOT.
</pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is integer
          The dimension of the work array WORK.  LWORK = 2*NW
          suffices, but greater efficiency may result from larger
          values of LWORK.
          If LWORK = -1, then a workspace query is assumed; DLAQR3
          only estimates the optimal workspace size for the given
          values of N, NW, KTOP and KBOT.  The estimate is returned
          in WORK(1).  No error message related to LWORK is issued
          by XERBLA.  Neither H nor Z are accessed.
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
<p> Definition at line 274 of file dlaqr3.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
