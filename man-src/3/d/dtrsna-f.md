---
title: "dtrsna-f(3)"
name: "dtrsna-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dtrsna-f/"
description: "dtrsna.f –"
---

<p>dtrsna.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dtrsna</code> (JOB, HOWMNY, SELECT, N, T, LDT, VL, LDVL, VR, LDVR, S, SEP, MM, M, WORK, LDWORK, IWORK, INFO)<br />
 <i></i><code>DTRSNA</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dtrsna (characterJOB, characterHOWMNY, logical, dimension( * )SELECT, integerN, double precision, dimension( ldt, * )T, integerLDT, double precision, dimension( ldvl, * )VL, integerLDVL, double precision, dimension( ldvr, * )VR, integerLDVR, double precision, dimension( * )S, double precision, dimension( * )SEP, integerMM, integerM, double precision, dimension( ldwork, * )WORK, integerLDWORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p><code>DTRSNA</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DTRSNA estimates reciprocal condition numbers for specified
 eigenvalues and/or right eigenvectors of a real upper
 quasi-triangular matrix T (or of any matrix Q*T*Q**T with Q
 orthogonal).
 T must be in Schur canonical form (as returned by DHSEQR), that is,
 block upper triangular with 1-by-1 and 2-by-2 diagonal blocks; each
 2-by-2 diagonal block has its diagonal elements equal and its
 off-diagonal elements of opposite sign.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
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
 for the eigenpair corresponding to a real eigenvalue w(j),
 SELECT(j) must be set to .TRUE.. To select condition numbers
 corresponding to a complex conjugate pair of eigenvalues w(j)
 and w(j+1), either SELECT(j) or SELECT(j+1) or both, must be
 set to .TRUE..
 If HOWMNY = 'A', SELECT is not referenced.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix T. N &gt;= 0.</pre>
<p><i>T</i> </p>
<pre> T is DOUBLE PRECISION array, dimension (LDT,N)
 The upper quasi-triangular matrix T, in Schur canonical form.</pre>
<p><i>LDT</i> </p>
<pre> LDT is INTEGER
 The leading dimension of the array T. LDT &gt;= max(1,N).</pre>
<p><i>VL</i> </p>
<pre> VL is DOUBLE PRECISION array, dimension (LDVL,M)
 If JOB = 'E' or 'B', VL must contain left eigenvectors of T
 (or of any Q*T*Q**T with Q orthogonal), corresponding to the
 eigenpairs specified by HOWMNY and SELECT. The eigenvectors
 must be stored in consecutive columns of VL, as returned by
 DHSEIN or DTREVC.
 If JOB = 'V', VL is not referenced.</pre>
<p><i>LDVL</i> </p>
<pre> LDVL is INTEGER
 The leading dimension of the array VL.
 LDVL &gt;= 1; and if JOB = 'E' or 'B', LDVL &gt;= N.</pre>
<p><i>VR</i> </p>
<pre> VR is DOUBLE PRECISION array, dimension (LDVR,M)
 If JOB = 'E' or 'B', VR must contain right eigenvectors of T
 (or of any Q*T*Q**T with Q orthogonal), corresponding to the
 eigenpairs specified by HOWMNY and SELECT. The eigenvectors
 must be stored in consecutive columns of VR, as returned by
 DHSEIN or DTREVC.
 If JOB = 'V', VR is not referenced.</pre>
<p><i>LDVR</i> </p>
<pre> LDVR is INTEGER
 The leading dimension of the array VR.
 LDVR &gt;= 1; and if JOB = 'E' or 'B', LDVR &gt;= N.</pre>
<p><i>S</i> </p>
<pre> S is DOUBLE PRECISION array, dimension (MM)
 If JOB = 'E' or 'B', the reciprocal condition numbers of the
 selected eigenvalues, stored in consecutive elements of the
 array. For a complex conjugate pair of eigenvalues two
 consecutive elements of S are set to the same value. Thus
 S(j), SEP(j), and the j-th columns of VL and VR all
 correspond to the same eigenpair (but not in general the
 j-th eigenpair, unless all eigenpairs are selected).
 If JOB = 'V', S is not referenced.</pre>
<p><i>SEP</i> </p>
<pre> SEP is DOUBLE PRECISION array, dimension (MM)
 If JOB = 'V' or 'B', the estimated reciprocal condition
 numbers of the selected eigenvectors, stored in consecutive
 elements of the array. For a complex eigenvector two
 consecutive elements of SEP are set to the same value. If
 the eigenvalues cannot be reordered to compute SEP(j), SEP(j)
 is set to 0; this can only occur when the true value would be
 very small anyway.
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
<pre> WORK is DOUBLE PRECISION array, dimension (LDWORK,N+6)
 If JOB = 'E', WORK is not referenced.</pre>
<p><i>LDWORK</i> </p>
<pre> LDWORK is INTEGER
 The leading dimension of the array WORK.
 LDWORK &gt;= 1; and if JOB = 'V' or 'B', LDWORK &gt;= N.</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (2*(N-1))
 If JOB = 'E', IWORK is not referenced.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
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
<pre> The reciprocal of the condition number of an eigenvalue lambda is
 defined as
 S(lambda) = |v**T*u| / (norm(u)*norm(v))
 where u and v are the right and left eigenvectors of T corresponding
 to lambda; v**T denotes the transpose of v, and norm(u)
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
<p> Definition at line 264 of file dtrsna.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
