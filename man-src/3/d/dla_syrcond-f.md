---
title: "dla_syrcond-f(3)"
name: "dla_syrcond-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dla_syrcond-f/"
description: "dla_syrcond.f –"
---

<p>dla_syrcond.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>DOUBLE PRECISION function <code>dla_syrcond</code> (UPLO, N, A, LDA, AF, LDAF, IPIV, CMODE, C, INFO, WORK, IWORK)<br />
 <i></i><code>DLA_SYRCOND</code> estimates the Skeel condition number for a symmetric indefinite matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>DOUBLE PRECISION function dla_syrcond (characterUPLO, integerN, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldaf, * )AF, integerLDAF, integer, dimension( * )IPIV, integerCMODE, double precision, dimension( * )C, integerINFO, double precision, dimension( * )WORK, integer, dimension( * )IWORK)</h3>
<p><code>DLA_SYRCOND</code> estimates the Skeel condition number for a symmetric indefinite matrix. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLA_SYRCOND estimates the Skeel condition number of op(A) * op2(C)
 where op2 is determined by CMODE as follows
 CMODE = 1 op2(C) = C
 CMODE = 0 op2(C) = I
 CMODE = -1 op2(C) = inv(C)
 The Skeel condition number cond(A) = norminf( |inv(A)||A| )
 is computed by computing scaling factors R such that
 diag(R)*A*op2(C) is row equilibrated and computing the standard
 infinity-norm condition number.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of linear equations, i.e., the order of the
 matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA,N)
 On entry, the N-by-N matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>AF</i> </p>
<pre> AF is DOUBLE PRECISION array, dimension (LDAF,N)
 The block diagonal matrix D and the multipliers used to
 obtain the factor U or L as computed by DSYTRF.</pre>
<p><i>LDAF</i> </p>
<pre> LDAF is INTEGER
 The leading dimension of the array AF. LDAF &gt;= max(1,N).</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 Details of the interchanges and the block structure of D
 as determined by DSYTRF.</pre>
<p><i>CMODE</i> </p>
<pre> CMODE is INTEGER
 Determines op2(C) in the formula op(A) * op2(C) as follows:
 CMODE = 1 op2(C) = C
 CMODE = 0 op2(C) = I
 CMODE = -1 op2(C) = inv(C)</pre>
<p><i>C</i> </p>
<pre> C is DOUBLE PRECISION array, dimension (N)
 The vector C in the formula op(A) * op2(C).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: Successful exit.
 i &gt; 0: The ith argument is invalid.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (3*N).
 Workspace.</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (N).
 Workspace.</pre>
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
<p> Definition at line 147 of file dla_syrcond.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
