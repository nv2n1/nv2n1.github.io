---
title: "ztgexc(3)"
name: "ztgexc"
section: "3"
letter: "z"
url: "/docs/linux/man/3-ztgexc/"
description: "ztgexc.f –"
---

<p>ztgexc.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ztgexc</code> (WANTQ, WANTZ, N, A, LDA, B, LDB, Q, LDQ, Z, LDZ, IFST, ILST, INFO)<br />
 <i></i><code>ZTGEXC</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ztgexc (logicalWANTQ, logicalWANTZ, integerN, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldb, * )B, integerLDB, complex*16, dimension( ldq, * )Q, integerLDQ, complex*16, dimension( ldz, * )Z, integerLDZ, integerIFST, integerILST, integerINFO)</h3>
<p><code>ZTGEXC</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZTGEXC reorders the generalized Schur decomposition of a complex
 matrix pair (A,B), using an unitary equivalence transformation
 (A, B) := Q * (A, B) * Z**H, so that the diagonal block of (A, B) with
 row index IFST is moved to row ILST.
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
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the upper triangular matrix A in the pair (A, B).
 On exit, the updated matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB,N)
 On entry, the upper triangular matrix B in the pair (A, B).
 On exit, the updated matrix B.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>Q</i> </p>
<pre> Q is COMPLEX*16 array, dimension (LDZ,N)
 On entry, if WANTQ = .TRUE., the unitary matrix Q.
 On exit, the updated matrix Q.
 If WANTQ = .FALSE., Q is not referenced.</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q. LDQ &gt;= 1;
 If WANTQ = .TRUE., LDQ &gt;= N.</pre>
<p><i>Z</i> </p>
<pre> Z is COMPLEX*16 array, dimension (LDZ,N)
 On entry, if WANTZ = .TRUE., the unitary matrix Z.
 On exit, the updated matrix Z.
 If WANTZ = .FALSE., Z is not referenced.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1;
 If WANTZ = .TRUE., LDZ &gt;= N.</pre>
<p><i>IFST</i> </p>
<pre> IFST is INTEGER</pre>
<p><i>ILST</i> </p>
<pre> ILST is INTEGER
 Specify the reordering of the diagonal blocks of (A, B).
 The block with row index IFST is moved to row ILST, by a
 sequence of swapping between adjacent blocks.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 =0: Successful exit.
 &lt;0: if INFO = -i, the i-th argument had an illegal value.
 =1: The transformed matrix pair (A, B) would be too far
 from generalized Schur form; the problem is ill-
 conditioned. (A, B) may have been partially reordered,
 and ILST points to the first row of the current
 position of the block being moved.</pre>
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
<p> <code>Contributors: </code></p>
<dl>
<dd>Bo Kagstrom and Peter Poromaa, Department of Computing Science, Umea University, S-901 87 Umea, Sweden.</dl>
<p> <code>References: </code></p>
<dl>
<dd>[1] B. Kagstrom; A Direct Method for Reordering Eigenvalues in the Generalized Real Schur Form of a Regular Matrix Pair (A, B), in M.S. Moonen et al (eds), Linear Algebra for Large Scale and Real-Time Applications, Kluwer Academic Publ. 1993, pp 195-218. </p>
<p>&nbsp;<wbr>[2]&nbsp;<wbr>B. Kagstrom and P. Poromaa;&nbsp;<wbr>Computing Eigenspaces with Specified Eigenvalues of a Regular Matrix Pair&nbsp;<wbr>(A, B)&nbsp;<wbr>and Condition Estimation: Theory, Algorithms and Software, Report UMINF &#8211; 94.04, Department of Computing Science, Umea University, S-901 87 Umea, Sweden, 1994. Also as LAPACK Working Note 87. To appear in Numerical Algorithms, 1996.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>[3]&nbsp;<wbr>B. Kagstrom and P. Poromaa, LAPACK-Style Algorithms and Software for Solving the Generalized Sylvester Equation and Estimating the Separation between Regular Matrix Pairs, Report UMINF &#8211; 93.23, Department of Computing Science, Umea University, S-901 87 Umea, Sweden, December 1993, Revised April 1994, Also as LAPACK working Note 75. To appear in ACM Trans. on Math. Software, Vol 22, No 1, 1996.&nbsp;<wbr></dl>
<p> Definition at line 200 of file ztgexc.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
