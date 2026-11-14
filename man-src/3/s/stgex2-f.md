---
title: "stgex2-f(3)"
name: "stgex2-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stgex2-f/"
description: "stgex2.f –"
---

<p>stgex2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>stgex2</code> (WANTQ, WANTZ, N, A, LDA, B, LDB, Q, LDQ, Z, LDZ, J1, N1, N2, WORK, LWORK, INFO)<br />
 <i></i><code>STGEX2</code> swaps adjacent diagonal blocks in an upper (quasi) triangular matrix pair by an orthogonal equivalence transformation.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine stgex2 (logicalWANTQ, logicalWANTZ, integerN, real, dimension( lda, * )A, integerLDA, real, dimension( ldb, * )B, integerLDB, real, dimension( ldq, * )Q, integerLDQ, real, dimension( ldz, * )Z, integerLDZ, integerJ1, integerN1, integerN2, real, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code>STGEX2</code> swaps adjacent diagonal blocks in an upper (quasi) triangular matrix pair by an orthogonal equivalence transformation. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> STGEX2 swaps adjacent diagonal blocks (A11, B11) and (A22, B22)
 of size 1-by-1 or 2-by-2 in an upper (quasi) triangular matrix pair
 (A, B) by an orthogonal equivalence transformation.
 (A, B) must be in generalized real Schur canonical form (as returned
 by SGGES), i.e. A is block upper triangular with 1-by-1 and 2-by-2
 diagonal blocks. B is upper triangular.
 Optionally, the matrices Q and Z of generalized Schur vectors are
 updated.
 Q(in) * A(in) * Z(in)**T = Q(out) * A(out) * Z(out)**T
 Q(in) * B(in) * Z(in)**T = Q(out) * B(out) * Z(out)**T</pre>
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
<pre> A is REAL arrays, dimensions (LDA,N)
 On entry, the matrix A in the pair (A, B).
 On exit, the updated matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>B</i> </p>
<pre> B is REAL arrays, dimensions (LDB,N)
 On entry, the matrix B in the pair (A, B).
 On exit, the updated matrix B.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>Q</i> </p>
<pre> Q is REAL array, dimension (LDZ,N)
 On entry, if WANTQ = .TRUE., the orthogonal matrix Q.
 On exit, the updated matrix Q.
 Not referenced if WANTQ = .FALSE..</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q. LDQ &gt;= 1.
 If WANTQ = .TRUE., LDQ &gt;= N.</pre>
<p><i>Z</i> </p>
<pre> Z is REAL array, dimension (LDZ,N)
 On entry, if WANTZ =.TRUE., the orthogonal matrix Z.
 On exit, the updated matrix Z.
 Not referenced if WANTZ = .FALSE..</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1.
 If WANTZ = .TRUE., LDZ &gt;= N.</pre>
<p><i>J1</i> </p>
<pre> J1 is INTEGER
 The index to the first block (A11, B11). 1 &lt;= J1 &lt;= N.</pre>
<p><i>N1</i> </p>
<pre> N1 is INTEGER
 The order of the first block (A11, B11). N1 = 0, 1 or 2.</pre>
<p><i>N2</i> </p>
<pre> N2 is INTEGER
 The order of the second block (A22, B22). N2 = 0, 1 or 2.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (MAX(1,LWORK)).</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK.
 LWORK &gt;= MAX( N*(N2+N1), (N2+N1)*(N2+N1)*2 )</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 =0: Successful exit
 &gt;0: If INFO = 1, the transformed matrix (A, B) would be
 too far from generalized Schur form; the blocks are
 not swapped and (A, B) and (Q, Z) are unchanged.
 The problem of swapping is too ill-conditioned.
 &lt;0: If INFO = -16: LWORK is too small. Appropriate value
 for LWORK is returned in WORK(1).</pre>
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
<dd>
<pre> [1] B. Kagstrom; A Direct Method for Reordering Eigenvalues in the
 Generalized Real Schur Form of a Regular Matrix Pair (A, B), in
 M.S. Moonen et al (eds), Linear Algebra for Large Scale and
 Real-Time Applications, Kluwer Academic Publ. 1993, pp 195-218.
 [2] B. Kagstrom and P. Poromaa; Computing Eigenspaces with Specified
 Eigenvalues of a Regular Matrix Pair (A, B) and Condition
 Estimation: Theory, Algorithms and Software,
 Report UMINF - 94.04, Department of Computing Science, Umea
 University, S-901 87 Umea, Sweden, 1994. Also as LAPACK Working
 Note 87. To appear in Numerical Algorithms, 1996.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 221 of file stgex2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
