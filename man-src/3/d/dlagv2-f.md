---
title: "dlagv2-f(3)"
name: "dlagv2-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlagv2-f/"
description: "dlagv2.f –"
---

<p>dlagv2.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlagv2</code> (A, LDA, B, LDB, ALPHAR, ALPHAI, BETA, CSL, SNL, CSR, SNR)<br />
 <i></i><code>DLAGV2</code> computes the Generalized Schur factorization of a real 2-by-2 matrix pencil (A,B) where B is upper triangular.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlagv2 (double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldb, * )B, integerLDB, double precision, dimension( 2 )ALPHAR, double precision, dimension( 2 )ALPHAI, double precision, dimension( 2 )BETA, double precisionCSL, double precisionSNL, double precisionCSR, double precisionSNR)</h3>
<p><code>DLAGV2</code> computes the Generalized Schur factorization of a real 2-by-2 matrix pencil (A,B) where B is upper triangular. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLAGV2 computes the Generalized Schur factorization of a real 2-by-2
 matrix pencil (A,B) where B is upper triangular. This routine
 computes orthogonal (rotation) matrices given by CSL, SNL and CSR,
 SNR such that
 1) if the pencil (A,B) has two real eigenvalues (include 0/0 or 1/0
 types), then
 [ a11 a12 ] := [ CSL SNL ] [ a11 a12 ] [ CSR -SNR ]
 [ 0 a22 ] [ -SNL CSL ] [ a21 a22 ] [ SNR CSR ]
 [ b11 b12 ] := [ CSL SNL ] [ b11 b12 ] [ CSR -SNR ]
 [ 0 b22 ] [ -SNL CSL ] [ 0 b22 ] [ SNR CSR ],
 2) if the pencil (A,B) has a pair of complex conjugate eigenvalues,
 then
 [ a11 a12 ] := [ CSL SNL ] [ a11 a12 ] [ CSR -SNR ]
 [ a21 a22 ] [ -SNL CSL ] [ a21 a22 ] [ SNR CSR ]
 [ b11 0 ] := [ CSL SNL ] [ b11 b12 ] [ CSR -SNR ]
 [ 0 b22 ] [ -SNL CSL ] [ 0 b22 ] [ SNR CSR ]
 where b11 &gt;= b22 &gt; 0.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA, 2)
 On entry, the 2 x 2 matrix A.
 On exit, A is overwritten by the ``A-part'' of the
 generalized Schur form.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 THe leading dimension of the array A. LDA &gt;= 2.</pre>
<p><i>B</i> </p>
<pre> B is DOUBLE PRECISION array, dimension (LDB, 2)
 On entry, the upper triangular 2 x 2 matrix B.
 On exit, B is overwritten by the ``B-part'' of the
 generalized Schur form.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 THe leading dimension of the array B. LDB &gt;= 2.</pre>
<p><i>ALPHAR</i> </p>
<pre> ALPHAR is DOUBLE PRECISION array, dimension (2)</pre>
<p><i>ALPHAI</i> </p>
<pre> ALPHAI is DOUBLE PRECISION array, dimension (2)</pre>
<p><i>BETA</i> </p>
<pre> BETA is DOUBLE PRECISION array, dimension (2)
 (ALPHAR(k)+i*ALPHAI(k))/BETA(k) are the eigenvalues of the
 pencil (A,B), k=1,2, i = sqrt(-1). Note that BETA(k) may
 be zero.</pre>
<p><i>CSL</i> </p>
<pre> CSL is DOUBLE PRECISION
 The cosine of the left rotation matrix.</pre>
<p><i>SNL</i> </p>
<pre> SNL is DOUBLE PRECISION
 The sine of the left rotation matrix.</pre>
<p><i>CSR</i> </p>
<pre> CSR is DOUBLE PRECISION
 The cosine of the right rotation matrix.</pre>
<p><i>SNR</i> </p>
<pre> SNR is DOUBLE PRECISION
 The sine of the right rotation matrix.</pre>
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
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>Mark Fahey, Department of Mathematics, Univ. of Kentucky, USA</dl>
<p> Definition at line 157 of file dlagv2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
