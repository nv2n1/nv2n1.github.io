---
title: "cgghrd-f(3)"
name: "cgghrd-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgghrd-f/"
description: "cgghrd.f –"
---

<p>cgghrd.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cgghrd</code> (COMPQ, COMPZ, N, ILO, IHI, A, LDA, B, LDB, Q, LDQ, Z, LDZ, INFO)<br />
 <i></i><code>CGGHRD</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgghrd (characterCOMPQ, characterCOMPZ, integerN, integerILO, integerIHI, complex, dimension( lda, * )A, integerLDA, complex, dimension( ldb, * )B, integerLDB, complex, dimension( ldq, * )Q, integerLDQ, complex, dimension( ldz, * )Z, integerLDZ, integerINFO)</h3>
<p><code>CGGHRD</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CGGHRD reduces a pair of complex matrices (A,B) to generalized upper
 Hessenberg form using unitary transformations, where A is a
 general matrix and B is upper triangular. The form of the generalized
 eigenvalue problem is
 A*x = lambda*B*x,
 and B is typically made upper triangular by computing its QR
 factorization and moving the unitary matrix Q to the left side
 of the equation.
 This subroutine simultaneously reduces A to a Hessenberg matrix H:
 Q**H*A*Z = H
 and transforms B to another upper triangular matrix T:
 Q**H*B*Z = T
 in order to reduce the problem to its standard form
 H*y = lambda*T*y
 where y = Z**H*x.
 The unitary matrices Q and Z are determined as products of Givens
 rotations. They may either be formed explicitly, or they may be
 postmultiplied into input matrices Q1 and Z1, so that
 Q1 * A * Z1**H = (Q1*Q) * H * (Z1*Z)**H
 Q1 * B * Z1**H = (Q1*Q) * T * (Z1*Z)**H
 If Q1 is the unitary matrix from the QR factorization of B in the
 original equation A*x = lambda*B*x, then CGGHRD reduces the original
 problem to generalized Hessenberg form.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>COMPQ</i> </p>
<pre> COMPQ is CHARACTER*1
 = 'N': do not compute Q;
 = 'I': Q is initialized to the unit matrix, and the
 unitary matrix Q is returned;
 = 'V': Q must contain a unitary matrix Q1 on entry,
 and the product Q1*Q is returned.</pre>
<p><i>COMPZ</i> </p>
<pre> COMPZ is CHARACTER*1
 = 'N': do not compute Q;
 = 'I': Q is initialized to the unit matrix, and the
 unitary matrix Q is returned;
 = 'V': Q must contain a unitary matrix Q1 on entry,
 and the product Q1*Q is returned.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrices A and B. N &gt;= 0.</pre>
<p><i>ILO</i> </p>
<pre> ILO is INTEGER</pre>
<p><i>IHI</i> </p>
<pre> IHI is INTEGER
 ILO and IHI mark the rows and columns of A which are to be
 reduced. It is assumed that A is already upper triangular
 in rows and columns 1:ILO-1 and IHI+1:N. ILO and IHI are
 normally set by a previous call to CGGBAL; otherwise they
 should be set to 1 and N respectively.
 1 &lt;= ILO &lt;= IHI &lt;= N, if N &gt; 0; ILO=1 and IHI=0, if N=0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX array, dimension (LDA, N)
 On entry, the N-by-N general matrix to be reduced.
 On exit, the upper triangle and the first subdiagonal of A
 are overwritten with the upper Hessenberg matrix H, and the
 rest is set to zero.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX array, dimension (LDB, N)
 On entry, the N-by-N upper triangular matrix B.
 On exit, the upper triangular matrix T = Q**H B Z. The
 elements below the diagonal are set to zero.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>Q</i> </p>
<pre> Q is COMPLEX array, dimension (LDQ, N)
 On entry, if COMPQ = 'V', the unitary matrix Q1, typically
 from the QR factorization of B.
 On exit, if COMPQ='I', the unitary matrix Q, and if
 COMPQ = 'V', the product Q1*Q.
 Not referenced if COMPQ='N'.</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q.
 LDQ &gt;= N if COMPQ='V' or 'I'; LDQ &gt;= 1 otherwise.</pre>
<p><i>Z</i> </p>
<pre> Z is COMPLEX array, dimension (LDZ, N)
 On entry, if COMPZ = 'V', the unitary matrix Z1.
 On exit, if COMPZ='I', the unitary matrix Z, and if
 COMPZ = 'V', the product Z1*Z.
 Not referenced if COMPZ='N'.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z.
 LDZ &gt;= N if COMPZ='V' or 'I'; LDZ &gt;= 1 otherwise.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.</pre>
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
<pre> This routine reduces A to Hessenberg and B to triangular form by
 an unblocked reduction, as described in &lt;em&gt;Matrix_Computations&lt;/em&gt;,
 by Golub and van Loan (Johns Hopkins Press).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 204 of file cgghrd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
