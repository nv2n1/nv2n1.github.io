---
title: "stgexc-f(3)"
name: "stgexc-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stgexc-f/"
description: "stgexc.f –"
---

<p>stgexc.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>stgexc</code> (WANTQ, WANTZ, N, A, LDA, B, LDB, Q, LDQ, Z, LDZ, IFST, ILST, WORK, LWORK, INFO)<br />
 <i></i><code>STGEXC</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine stgexc (logicalWANTQ, logicalWANTZ, integerN, real, dimension( lda, * )A, integerLDA, real, dimension( ldb, * )B, integerLDB, real, dimension( ldq, * )Q, integerLDQ, real, dimension( ldz, * )Z, integerLDZ, integerIFST, integerILST, real, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code>STGEXC</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> STGEXC reorders the generalized real Schur decomposition of a real
 matrix pair (A,B) using an orthogonal equivalence transformation
 (A, B) = Q * (A, B) * Z**T,
 so that the diagonal block of (A, B) with row index IFST is moved
 to row ILST.
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
<pre> A is REAL array, dimension (LDA,N)
 On entry, the matrix A in generalized real Schur canonical
 form.
 On exit, the updated matrix A, again in generalized
 real Schur canonical form.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>B</i> </p>
<pre> B is REAL array, dimension (LDB,N)
 On entry, the matrix B in generalized real Schur canonical
 form (A,B).
 On exit, the updated matrix B, again in generalized
 real Schur canonical form (A,B).</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>Q</i> </p>
<pre> Q is REAL array, dimension (LDZ,N)
 On entry, if WANTQ = .TRUE., the orthogonal matrix Q.
 On exit, the updated matrix Q.
 If WANTQ = .FALSE., Q is not referenced.</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q. LDQ &gt;= 1.
 If WANTQ = .TRUE., LDQ &gt;= N.</pre>
<p><i>Z</i> </p>
<pre> Z is REAL array, dimension (LDZ,N)
 On entry, if WANTZ = .TRUE., the orthogonal matrix Z.
 On exit, the updated matrix Z.
 If WANTZ = .FALSE., Z is not referenced.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1.
 If WANTZ = .TRUE., LDZ &gt;= N.</pre>
<p><i>IFST</i> </p>
<pre> IFST is INTEGER</pre>
<p><i>ILST</i> </p>
<pre> ILST is INTEGER
 Specify the reordering of the diagonal blocks of (A, B).
 The block with row index IFST is moved to row ILST, by a
 sequence of swapping between adjacent blocks.
 On exit, if IFST pointed on entry to the second row of
 a 2-by-2 block, it is changed to point to the first row;
 ILST always points to the first row of the block in its
 final position (which may differ from its input value by
 +1 or -1). 1 &lt;= IFST, ILST &lt;= N.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK.
 LWORK &gt;= 1 when N &lt;= 1, otherwise LWORK &gt;= 4*N + 16.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 =0: successful exit.
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
<dd>
<pre> [1] B. Kagstrom; A Direct Method for Reordering Eigenvalues in the
 Generalized Real Schur Form of a Regular Matrix Pair (A, B), in
 M.S. Moonen et al (eds), Linear Algebra for Large Scale and
 Real-Time Applications, Kluwer Academic Publ. 1993, pp 195-218.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 220 of file stgexc.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
