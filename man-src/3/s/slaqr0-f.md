---
title: "slaqr0-f(3)"
name: "slaqr0-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slaqr0-f/"
description: "slaqr0.f –"
---

<p>slaqr0.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slaqr0</code> (WANTT, WANTZ, N, ILO, IHI, H, LDH, WR, WI, ILOZ, IHIZ, Z, LDZ, WORK, LWORK, INFO)<br />
 <i></i><code>SLAQR0</code> computes the eigenvalues of a Hessenberg matrix, and optionally the matrices from the Schur decomposition.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slaqr0 (logicalWANTT, logicalWANTZ, integerN, integerILO, integerIHI, real, dimension( ldh, * )H, integerLDH, real, dimension( * )WR, real, dimension( * )WI, integerILOZ, integerIHIZ, real, dimension( ldz, * )Z, integerLDZ, real, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code>SLAQR0</code> computes the eigenvalues of a Hessenberg matrix, and optionally the matrices from the Schur decomposition. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLAQR0 computes the eigenvalues of a Hessenberg matrix H
 and, optionally, the matrices T and Z from the Schur decomposition
 H = Z T Z**T, where T is an upper quasi-triangular matrix (the
 Schur form), and Z is the orthogonal matrix of Schur vectors.
 Optionally Z may be postmultiplied into an input orthogonal
 matrix Q so that this routine can give the Schur factorization
 of a matrix A which has been reduced to the Hessenberg form H
 by the orthogonal matrix Q: A = Q*H*Q**T = (QZ)*T*(QZ)**T.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>WANTT</i> </p>
<pre> WANTT is LOGICAL
 = .TRUE. : the full Schur form T is required;
 = .FALSE.: only eigenvalues are required.</pre>
<p><i>WANTZ</i> </p>
<pre> WANTZ is LOGICAL
 = .TRUE. : the matrix of Schur vectors Z is required;
 = .FALSE.: Schur vectors are not required.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix H. N .GE. 0.</pre>
<p><i>ILO</i> </p>
<pre> ILO is INTEGER</pre>
<p><i>IHI</i> </p>
<pre> IHI is INTEGER
 It is assumed that H is already upper triangular in rows
 and columns 1:ILO-1 and IHI+1:N and, if ILO.GT.1,
 H(ILO,ILO-1) is zero. ILO and IHI are normally set by a
 previous call to SGEBAL, and then passed to SGEHRD when the
 matrix output by SGEBAL is reduced to Hessenberg form.
 Otherwise, ILO and IHI should be set to 1 and N,
 respectively. If N.GT.0, then 1.LE.ILO.LE.IHI.LE.N.
 If N = 0, then ILO = 1 and IHI = 0.</pre>
<p><i>H</i> </p>
<pre> H is REAL array, dimension (LDH,N)
 On entry, the upper Hessenberg matrix H.
 On exit, if INFO = 0 and WANTT is .TRUE., then H contains
 the upper quasi-triangular matrix T from the Schur
 decomposition (the Schur form); 2-by-2 diagonal blocks
 (corresponding to complex conjugate pairs of eigenvalues)
 are returned in standard form, with H(i,i) = H(i+1,i+1)
 and H(i+1,i)*H(i,i+1).LT.0. If INFO = 0 and WANTT is
 .FALSE., then the contents of H are unspecified on exit.
 (The output value of H when INFO.GT.0 is given under the
 description of INFO below.)
 This subroutine may explicitly set H(i,j) = 0 for i.GT.j and
 j = 1, 2, ... ILO-1 or j = IHI+1, IHI+2, ... N.</pre>
<p><i>LDH</i> </p>
<pre> LDH is INTEGER
 The leading dimension of the array H. LDH .GE. max(1,N).</pre>
<p><i>WR</i> </p>
<pre> WR is REAL array, dimension (IHI)</pre>
<p><i>WI</i> </p>
<pre> WI is REAL array, dimension (IHI)
 The real and imaginary parts, respectively, of the computed
 eigenvalues of H(ILO:IHI,ILO:IHI) are stored in WR(ILO:IHI)
 and WI(ILO:IHI). If two eigenvalues are computed as a
 complex conjugate pair, they are stored in consecutive
 elements of WR and WI, say the i-th and (i+1)th, with
 WI(i) .GT. 0 and WI(i+1) .LT. 0. If WANTT is .TRUE., then
 the eigenvalues are stored in the same order as on the
 diagonal of the Schur form returned in H, with
 WR(i) = H(i,i) and, if H(i:i+1,i:i+1) is a 2-by-2 diagonal
 block, WI(i) = sqrt(-H(i+1,i)*H(i,i+1)) and
 WI(i+1) = -WI(i).</pre>
<p><i>ILOZ</i> </p>
<pre> ILOZ is INTEGER</pre>
<p><i>IHIZ</i> </p>
<pre> IHIZ is INTEGER
 Specify the rows of Z to which transformations must be
 applied if WANTZ is .TRUE..
 1 .LE. ILOZ .LE. ILO; IHI .LE. IHIZ .LE. N.</pre>
<p><i>Z</i> </p>
<pre> Z is REAL array, dimension (LDZ,IHI)
 If WANTZ is .FALSE., then Z is not referenced.
 If WANTZ is .TRUE., then Z(ILO:IHI,ILOZ:IHIZ) is
 replaced by Z(ILO:IHI,ILOZ:IHIZ)*U where U is the
 orthogonal Schur factor of H(ILO:IHI,ILO:IHI).
 (The output value of Z when INFO.GT.0 is given under
 the description of INFO below.)</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. if WANTZ is .TRUE.
 then LDZ.GE.MAX(1,IHIZ). Otherwize, LDZ.GE.1.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension LWORK
 On exit, if LWORK = -1, WORK(1) returns an estimate of
 the optimal value for LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK .GE. max(1,N)
 is sufficient, but LWORK typically as large as 6*N may
 be required for optimal performance. A workspace query
 to determine the optimal workspace size is recommended.
 If LWORK = -1, then SLAQR0 does a workspace query.
 In this case, SLAQR0 checks the input parameters and
 estimates the optimal workspace size for the given
 values of N, ILO and IHI. The estimate is returned
 in WORK(1). No error message related to LWORK is
 issued by XERBLA. Neither H nor Z are accessed.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 .GT. 0: if INFO = i, SLAQR0 failed to compute all of
 the eigenvalues. Elements 1:ilo-1 and i+1:n of WR
 and WI contain those eigenvalues which have been
 successfully computed. (Failures are rare.)
 If INFO .GT. 0 and WANT is .FALSE., then on exit,
 the remaining unconverged eigenvalues are the eigen-
 values of the upper Hessenberg matrix rows and
 columns ILO through INFO of the final, output
 value of H.
 If INFO .GT. 0 and WANTT is .TRUE., then on exit
 (*) (initial value of H)*U = U*(final value of H)
 where U is an orthogonal matrix. The final
 value of H is upper Hessenberg and quasi-triangular
 in rows and columns INFO+1 through IHI.
 If INFO .GT. 0 and WANTZ is .TRUE., then on exit
 (final value of Z(ILO:IHI,ILOZ:IHIZ)
 = (initial value of Z(ILO:IHI,ILOZ:IHIZ)*U
 where U is the orthogonal matrix in (*) (regard-
 less of the value of WANTT.)
 If INFO .GT. 0 and WANTZ is .FALSE., then Z is not
 accessed.</pre>
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
<dd>K. Braman, R. Byers and R. Mathias, The Multi-Shift QR Algorithm Part I: Maintaining Well Focused Shifts, and Level 3 Performance, SIAM Journal of Matrix Analysis, volume 23, pages 929&#8211;947, 2002. </p>
<p>&nbsp;<wbr>K. Braman, R. Byers and R. Mathias, The Multi-Shift QR Algorithm Part II: Aggressive Early Deflation, SIAM Journal of Matrix Analysis, volume 23, pages 948&#8211;973, 2002.&nbsp;<wbr></dl>
<p> Definition at line 256 of file slaqr0.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
