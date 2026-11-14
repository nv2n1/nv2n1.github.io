---
title: "dlahqr-f(3)"
name: "dlahqr-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlahqr-f/"
description: "dlahqr.f –"
---

<p>dlahqr.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlahqr</code> (WANTT, WANTZ, N, ILO, IHI, H, LDH, WR, WI, ILOZ, IHIZ, Z, LDZ, INFO)<br />
 <i></i><code>DLAHQR</code> computes the eigenvalues and Schur factorization of an upper Hessenberg matrix, using the double-shift/single-shift QR algorithm.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlahqr (logicalWANTT, logicalWANTZ, integerN, integerILO, integerIHI, double precision, dimension( ldh, * )H, integerLDH, double precision, dimension( * )WR, double precision, dimension( * )WI, integerILOZ, integerIHIZ, double precision, dimension( ldz, * )Z, integerLDZ, integerINFO)</h3>
<p><code>DLAHQR</code> computes the eigenvalues and Schur factorization of an upper Hessenberg matrix, using the double-shift/single-shift QR algorithm. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLAHQR is an auxiliary routine called by DHSEQR to update the
 eigenvalues and Schur decomposition already computed by DHSEQR, by
 dealing with the Hessenberg submatrix in rows and columns ILO to
 IHI.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
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
 The order of the matrix H. N &gt;= 0.</pre>
<p><i>ILO</i> </p>
<pre> ILO is INTEGER</pre>
<p><i>IHI</i> </p>
<pre> IHI is INTEGER
 It is assumed that H is already upper quasi-triangular in
 rows and columns IHI+1:N, and that H(ILO,ILO-1) = 0 (unless
 ILO = 1). DLAHQR works primarily with the Hessenberg
 submatrix in rows and columns ILO to IHI, but applies
 transformations to all of H if WANTT is .TRUE..
 1 &lt;= ILO &lt;= max(1,IHI); IHI &lt;= N.</pre>
<p><i>H</i> </p>
<pre> H is DOUBLE PRECISION array, dimension (LDH,N)
 On entry, the upper Hessenberg matrix H.
 On exit, if INFO is zero and if WANTT is .TRUE., H is upper
 quasi-triangular in rows and columns ILO:IHI, with any
 2-by-2 diagonal blocks in standard form. If INFO is zero
 and WANTT is .FALSE., the contents of H are unspecified on
 exit. The output state of H if INFO is nonzero is given
 below under the description of INFO.</pre>
<p><i>LDH</i> </p>
<pre> LDH is INTEGER
 The leading dimension of the array H. LDH &gt;= max(1,N).</pre>
<p><i>WR</i> </p>
<pre> WR is DOUBLE PRECISION array, dimension (N)</pre>
<p><i>WI</i> </p>
<pre> WI is DOUBLE PRECISION array, dimension (N)
 The real and imaginary parts, respectively, of the computed
 eigenvalues ILO to IHI are stored in the corresponding
 elements of WR and WI. If two eigenvalues are computed as a
 complex conjugate pair, they are stored in consecutive
 elements of WR and WI, say the i-th and (i+1)th, with
 WI(i) &gt; 0 and WI(i+1) &lt; 0. If WANTT is .TRUE., the
 eigenvalues are stored in the same order as on the diagonal
 of the Schur form returned in H, with WR(i) = H(i,i), and, if
 H(i:i+1,i:i+1) is a 2-by-2 diagonal block,
 WI(i) = sqrt(H(i+1,i)*H(i,i+1)) and WI(i+1) = -WI(i).</pre>
<p><i>ILOZ</i> </p>
<pre> ILOZ is INTEGER</pre>
<p><i>IHIZ</i> </p>
<pre> IHIZ is INTEGER
 Specify the rows of Z to which transformations must be
 applied if WANTZ is .TRUE..
 1 &lt;= ILOZ &lt;= ILO; IHI &lt;= IHIZ &lt;= N.</pre>
<p><i>Z</i> </p>
<pre> Z is DOUBLE PRECISION array, dimension (LDZ,N)
 If WANTZ is .TRUE., on entry Z must contain the current
 matrix Z of transformations accumulated by DHSEQR, and on
 exit Z has been updated; transformations are applied only to
 the submatrix Z(ILOZ:IHIZ,ILO:IHI).
 If WANTZ is .FALSE., Z is not referenced.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= max(1,N).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 .GT. 0: If INFO = i, DLAHQR failed to compute all the
 eigenvalues ILO to IHI in a total of 30 iterations
 per eigenvalue; elements i+1:ihi of WR and WI
 contain those eigenvalues which have been
 successfully computed.
 If INFO .GT. 0 and WANTT is .FALSE., then on exit,
 the remaining unconverged eigenvalues are the
 eigenvalues of the upper Hessenberg matrix rows
 and columns ILO thorugh INFO of the final, output
 value of H.
 If INFO .GT. 0 and WANTT is .TRUE., then on exit
 (*) (initial value of H)*U = U*(final value of H)
 where U is an orthognal matrix. The final
 value of H is upper Hessenberg and triangular in
 rows and columns INFO+1 through IHI.
 If INFO .GT. 0 and WANTZ is .TRUE., then on exit
 (final value of Z) = (initial value of Z)*U
 where U is the orthogonal matrix in (*)
 (regardless of the value of WANTT.)</pre>
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
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> 02-96 Based on modifications by
 David Day, Sandia National Laboratory, USA
 12-04 Further modifications by
 Ralph Byers, University of Kansas, USA
 This is a modified version of DLAHQR from LAPACK version 3.0.
 It is (1) more robust against overflow and underflow and
 (2) adopts the more conservative Ahues &amp; Tisseur stopping
 criterion (LAWN 122, 1997).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 207 of file dlahqr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
