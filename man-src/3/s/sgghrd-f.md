---
title: "sgghrd-f(3)"
name: "sgghrd-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgghrd-f/"
description: "sgghrd.f –"
---

<p>sgghrd.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sgghrd</code> (COMPQ, COMPZ, N, ILO, IHI, A, LDA, B, LDB, Q, LDQ, Z, LDZ, INFO)<br />
 <i></i><code>SGGHRD</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sgghrd (characterCOMPQ, characterCOMPZ, integerN, integerILO, integerIHI, real, dimension( lda, * )A, integerLDA, real, dimension( ldb, * )B, integerLDB, real, dimension( ldq, * )Q, integerLDQ, real, dimension( ldz, * )Z, integerLDZ, integerINFO)</h3>
<p><code>SGGHRD</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SGGHRD reduces a pair of real matrices (A,B) to generalized upper
 Hessenberg form using orthogonal transformations, where A is a
 general matrix and B is upper triangular. The form of the
 generalized eigenvalue problem is
 A*x = lambda*B*x,
 and B is typically made upper triangular by computing its QR
 factorization and moving the orthogonal matrix Q to the left side
 of the equation.
 This subroutine simultaneously reduces A to a Hessenberg matrix H:
 Q**T*A*Z = H
 and transforms B to another upper triangular matrix T:
 Q**T*B*Z = T
 in order to reduce the problem to its standard form
 H*y = lambda*T*y
 where y = Z**T*x.
 The orthogonal matrices Q and Z are determined as products of Givens
 rotations. They may either be formed explicitly, or they may be
 postmultiplied into input matrices Q1 and Z1, so that
 Q1 * A * Z1**T = (Q1*Q) * H * (Z1*Z)**T
 Q1 * B * Z1**T = (Q1*Q) * T * (Z1*Z)**T
 If Q1 is the orthogonal matrix from the QR factorization of B in the
 original equation A*x = lambda*B*x, then SGGHRD reduces the original
 problem to generalized Hessenberg form.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>COMPQ</i> </p>
<pre> COMPQ is CHARACTER*1
 = 'N': do not compute Q;
 = 'I': Q is initialized to the unit matrix, and the
 orthogonal matrix Q is returned;
 = 'V': Q must contain an orthogonal matrix Q1 on entry,
 and the product Q1*Q is returned.</pre>
<p><i>COMPZ</i> </p>
<pre> COMPZ is CHARACTER*1
 = 'N': do not compute Z;
 = 'I': Z is initialized to the unit matrix, and the
 orthogonal matrix Z is returned;
 = 'V': Z must contain an orthogonal matrix Z1 on entry,
 and the product Z1*Z is returned.</pre>
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
 normally set by a previous call to SGGBAL; otherwise they
 should be set to 1 and N respectively.
 1 &lt;= ILO &lt;= IHI &lt;= N, if N &gt; 0; ILO=1 and IHI=0, if N=0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA, N)
 On entry, the N-by-N general matrix to be reduced.
 On exit, the upper triangle and the first subdiagonal of A
 are overwritten with the upper Hessenberg matrix H, and the
 rest is set to zero.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>B</i> </p>
<pre> B is REAL array, dimension (LDB, N)
 On entry, the N-by-N upper triangular matrix B.
 On exit, the upper triangular matrix T = Q**T B Z. The
 elements below the diagonal are set to zero.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>Q</i> </p>
<pre> Q is REAL array, dimension (LDQ, N)
 On entry, if COMPQ = 'V', the orthogonal matrix Q1,
 typically from the QR factorization of B.
 On exit, if COMPQ='I', the orthogonal matrix Q, and if
 COMPQ = 'V', the product Q1*Q.
 Not referenced if COMPQ='N'.</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q.
 LDQ &gt;= N if COMPQ='V' or 'I'; LDQ &gt;= 1 otherwise.</pre>
<p><i>Z</i> </p>
<pre> Z is REAL array, dimension (LDZ, N)
 On entry, if COMPZ = 'V', the orthogonal matrix Z1.
 On exit, if COMPZ='I', the orthogonal matrix Z, and if
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
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> This routine reduces A to Hessenberg and B to triangular form by
 an unblocked reduction, as described in &lt;em&gt;Matrix_Computations&lt;/em&gt;,
 by Golub and Van Loan (Johns Hopkins Press.)</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 207 of file sgghrd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
