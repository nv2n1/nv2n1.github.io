---
title: "ztgex2-f(3)"
name: "ztgex2-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-ztgex2-f/"
description: "ztgex2.f –"
---

<p>ztgex2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ztgex2</code> (WANTQ, WANTZ, N, A, LDA, B, LDB, Q, LDQ, Z, LDZ, J1, INFO)<br />
 <i></i><code>ZTGEX2</code> swaps adjacent diagonal blocks in an upper (quasi) triangular matrix pair by an unitary equivalence transformation.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ztgex2 (logicalWANTQ, logicalWANTZ, integerN, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldb, * )B, integerLDB, complex*16, dimension( ldq, * )Q, integerLDQ, complex*16, dimension( ldz, * )Z, integerLDZ, integerJ1, integerINFO)</h3>
<p><code>ZTGEX2</code> swaps adjacent diagonal blocks in an upper (quasi) triangular matrix pair by an unitary equivalence transformation. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZTGEX2 swaps adjacent diagonal 1 by 1 blocks (A11,B11) and (A22,B22)
 in an upper triangular matrix pair (A, B) by an unitary equivalence
 transformation.
 (A, B) must be in generalized Schur canonical form, that is, A and
 B are both upper triangular.
 Optionally, the matrices Q and Z of generalized Schur vectors are
 updated.
 Q(in) * A(in) * Z(in)**H = Q(out) * A(out) * Z(out)**H
 Q(in) * B(in) * Z(in)**H = Q(out) * B(out) * Z(out)**H</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>WANTQ</i> </p>
<pre> WANTQ is LOGICAL
 .TRUE. : update the left transformation matrix Q;
 .FALSE.: do not update Q.</pre>
<p><i>WANTZ</i> </p>
<pre> WANTZ is LOGICAL
 .TRUE. : update the right transformation matrix Z;
 .FALSE.: do not update Z.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrices A and B. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 arrays, dimensions (LDA,N)
 On entry, the matrix A in the pair (A, B).
 On exit, the updated matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 arrays, dimensions (LDB,N)
 On entry, the matrix B in the pair (A, B).
 On exit, the updated matrix B.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>Q</i> </p>
<pre> Q is COMPLEX*16 array, dimension (LDZ,N)
 If WANTQ = .TRUE, on entry, the unitary matrix Q. On exit,
 the updated matrix Q.
 Not referenced if WANTQ = .FALSE..</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q. LDQ &gt;= 1;
 If WANTQ = .TRUE., LDQ &gt;= N.</pre>
<p><i>Z</i> </p>
<pre> Z is COMPLEX*16 array, dimension (LDZ,N)
 If WANTZ = .TRUE, on entry, the unitary matrix Z. On exit,
 the updated matrix Z.
 Not referenced if WANTZ = .FALSE..</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1;
 If WANTZ = .TRUE., LDZ &gt;= N.</pre>
<p><i>J1</i> </p>
<pre> J1 is INTEGER
 The index to the first block (A11, B11).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 =0: Successful exit.
 =1: The transformed matrix pair (A, B) would be too far
 from generalized Schur form; the problem is ill-
 conditioned. </pre>
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
<p> <code>Further Details: </code></p>
<dl>
<dd>In the current code both weak and strong stability tests are performed. The user can omit the strong stability test by changing the internal logical parameter WANDS to .FALSE.. See ref. [2] for details.</dl>
<p> <code>Contributors: </code></p>
<dl>
<dd>Bo Kagstrom and Peter Poromaa, Department of Computing Science, Umea University, S-901 87 Umea, Sweden.</dl>
<p> <code>References: </code></p>
<dl>
<dd>[1] B. Kagstrom; A Direct Method for Reordering Eigenvalues in the Generalized Real Schur Form of a Regular Matrix Pair (A, B), in M.S. Moonen et al (eds), Linear Algebra for Large Scale and Real-Time Applications, Kluwer Academic Publ. 1993, pp 195-218. </p>
<p>&nbsp;<wbr>[2]&nbsp;<wbr>B. Kagstrom and P. Poromaa;&nbsp;<wbr>Computing Eigenspaces with Specified Eigenvalues of a Regular Matrix Pair&nbsp;<wbr>(A, B)&nbsp;<wbr>and Condition Estimation: Theory, Algorithms and Software, Report UMINF-94.04, Department of Computing Science, Umea University, S-901 87 Umea, Sweden, 1994. Also as LAPACK Working Note 87. To appear in Numerical Algorithms, 1996.&nbsp;<wbr></dl>
<p> Definition at line 190 of file ztgex2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
