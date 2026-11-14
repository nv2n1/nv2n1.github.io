---
title: "ztrsna(3)"
name: "ztrsna"
section: "3"
letter: "z"
url: "/docs/linux/man/3-ztrsna/"
description: "ztrsna.f –"
---

<p>ztrsna.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>ztrsna</code> (JOB, HOWMNY, SELECT, N, T, LDT, VL, LDVL, VR, LDVR, S, SEP, MM, M, WORK, LDWORK, RWORK, INFO)<br />
 <i></i><code>ZTRSNA</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ztrsna (characterJOB, characterHOWMNY, logical, dimension( * )SELECT, integerN, complex*16, dimension( ldt, * )T, integerLDT, complex*16, dimension( ldvl, * )VL, integerLDVL, complex*16, dimension( ldvr, * )VR, integerLDVR, double precision, dimension( * )S, double precision, dimension( * )SEP, integerMM, integerM, complex*16, dimension( ldwork, * )WORK, integerLDWORK, double precision, dimension( * )RWORK, integerINFO)</h3>
<p><code>ZTRSNA</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZTRSNA estimates reciprocal condition numbers for specified
 eigenvalues and/or right eigenvectors of a complex upper triangular
 matrix T (or of any matrix Q*T*Q**H with Q unitary).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>JOB</i> </p>
<pre> JOB is CHARACTER*1
 Specifies whether condition numbers are required for
 eigenvalues (S) or eigenvectors (SEP):
 = 'E': for eigenvalues only (S);
 = 'V': for eigenvectors only (SEP);
 = 'B': for both eigenvalues and eigenvectors (S and SEP).</pre>
<p><i>HOWMNY</i> </p>
<pre> HOWMNY is CHARACTER*1
 = 'A': compute condition numbers for all eigenpairs;
 = 'S': compute condition numbers for selected eigenpairs
 specified by the array SELECT.</pre>
<p><i>SELECT</i> </p>
<pre> SELECT is LOGICAL array, dimension (N)
 If HOWMNY = 'S', SELECT specifies the eigenpairs for which
 condition numbers are required. To select condition numbers
 for the j-th eigenpair, SELECT(j) must be set to .TRUE..
 If HOWMNY = 'A', SELECT is not referenced.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix T. N &gt;= 0.</pre>
<p><i>T</i> </p>
<pre> T is COMPLEX*16 array, dimension (LDT,N)
 The upper triangular matrix T.</pre>
<p><i>LDT</i> </p>
<pre> LDT is INTEGER
 The leading dimension of the array T. LDT &gt;= max(1,N).</pre>
<p><i>VL</i> </p>
<pre> VL is COMPLEX*16 array, dimension (LDVL,M)
 If JOB = 'E' or 'B', VL must contain left eigenvectors of T
 (or of any Q*T*Q**H with Q unitary), corresponding to the
 eigenpairs specified by HOWMNY and SELECT. The eigenvectors
 must be stored in consecutive columns of VL, as returned by
 ZHSEIN or ZTREVC.
 If JOB = 'V', VL is not referenced.</pre>
<p><i>LDVL</i> </p>
<pre> LDVL is INTEGER
 The leading dimension of the array VL.
 LDVL &gt;= 1; and if JOB = 'E' or 'B', LDVL &gt;= N.</pre>
<p><i>VR</i> </p>
<pre> VR is COMPLEX*16 array, dimension (LDVR,M)
 If JOB = 'E' or 'B', VR must contain right eigenvectors of T
 (or of any Q*T*Q**H with Q unitary), corresponding to the
 eigenpairs specified by HOWMNY and SELECT. The eigenvectors
 must be stored in consecutive columns of VR, as returned by
 ZHSEIN or ZTREVC.
 If JOB = 'V', VR is not referenced.</pre>
<p><i>LDVR</i> </p>
<pre> LDVR is INTEGER
 The leading dimension of the array VR.
 LDVR &gt;= 1; and if JOB = 'E' or 'B', LDVR &gt;= N.</pre>
<p><i>S</i> </p>
<pre> S is DOUBLE PRECISION array, dimension (MM)
 If JOB = 'E' or 'B', the reciprocal condition numbers of the
 selected eigenvalues, stored in consecutive elements of the
 array. Thus S(j), SEP(j), and the j-th columns of VL and VR
 all correspond to the same eigenpair (but not in general the
 j-th eigenpair, unless all eigenpairs are selected).
 If JOB = 'V', S is not referenced.</pre>
<p><i>SEP</i> </p>
<pre> SEP is DOUBLE PRECISION array, dimension (MM)
 If JOB = 'V' or 'B', the estimated reciprocal condition
 numbers of the selected eigenvectors, stored in consecutive
 elements of the array.
 If JOB = 'E', SEP is not referenced.</pre>
<p><i>MM</i> </p>
<pre> MM is INTEGER
 The number of elements in the arrays S (if JOB = 'E' or 'B')
 and/or SEP (if JOB = 'V' or 'B'). MM &gt;= M.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of elements of the arrays S and/or SEP actually
 used to store the estimated condition numbers.
 If HOWMNY = 'A', M is set to N.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (LDWORK,N+6)
 If JOB = 'E', WORK is not referenced.</pre>
<p><i>LDWORK</i> </p>
<pre> LDWORK is INTEGER
 The leading dimension of the array WORK.
 LDWORK &gt;= 1; and if JOB = 'V' or 'B', LDWORK &gt;= N.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (N)
 If JOB = 'E', RWORK is not referenced.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
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
<pre> The reciprocal of the condition number of an eigenvalue lambda is
 defined as
 S(lambda) = |v**H*u| / (norm(u)*norm(v))
 where u and v are the right and left eigenvectors of T corresponding
 to lambda; v**H denotes the conjugate transpose of v, and norm(u)
 denotes the Euclidean norm. These reciprocal condition numbers always
 lie between zero (very badly conditioned) and one (very well
 conditioned). If n = 1, S(lambda) is defined to be 1.
 An approximate error bound for a computed eigenvalue W(i) is given by
 EPS * norm(T) / S(i)
 where EPS is the machine precision.
 The reciprocal of the condition number of the right eigenvector u
 corresponding to lambda is defined as follows. Suppose
 T = ( lambda c )
 ( 0 T22 )
 Then the reciprocal condition number is
 SEP( lambda, T22 ) = sigma-min( T22 - lambda*I )
 where sigma-min denotes the smallest singular value. We approximate
 the smallest singular value by the reciprocal of an estimate of the
 one-norm of the inverse of T22 - lambda*I. If n = 1, <a href="//www.systutorials.com/docs/linux/man/1-SEP/">SEP</a>(1) is
 defined to be abs(T(1,1)).
 An approximate error bound for a computed right eigenvector VR(i)
 is given by
 EPS * norm(T) / SEP(i)</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 248 of file ztrsna.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
