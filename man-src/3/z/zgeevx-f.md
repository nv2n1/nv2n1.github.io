---
title: "zgeevx-f(3)"
name: "zgeevx-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zgeevx-f/"
description: "zgeevx.f –"
---

<p>zgeevx.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zgeevx</code> (BALANC, JOBVL, JOBVR, SENSE, N, A, LDA, W, VL, LDVL, VR, LDVR, ILO, IHI, SCALE, ABNRM, RCONDE, RCONDV, WORK, LWORK, RWORK, INFO)<br />
 <i></i><code> ZGEEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zgeevx (characterBALANC, characterJOBVL, characterJOBVR, characterSENSE, integerN, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( * )W, complex*16, dimension( ldvl, * )VL, integerLDVL, complex*16, dimension( ldvr, * )VR, integerLDVR, integerILO, integerIHI, double precision, dimension( * )SCALE, double precisionABNRM, double precision, dimension( * )RCONDE, double precision, dimension( * )RCONDV, complex*16, dimension( * )WORK, integerLWORK, double precision, dimension( * )RWORK, integerINFO)</h3>
<p><code> ZGEEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZGEEVX computes for an N-by-N complex nonsymmetric matrix A, the
 eigenvalues and, optionally, the left and/or right eigenvectors.
 Optionally also, it computes a balancing transformation to improve
 the conditioning of the eigenvalues and eigenvectors (ILO, IHI,
 SCALE, and ABNRM), reciprocal condition numbers for the eigenvalues
 (RCONDE), and reciprocal condition numbers for the right
 eigenvectors (RCONDV).
 The right eigenvector v(j) of A satisfies
 A * v(j) = lambda(j) * v(j)
 where lambda(j) is its eigenvalue.
 The left eigenvector u(j) of A satisfies
 u(j)**H * A = lambda(j) * u(j)**H
 where u(j)**H denotes the conjugate transpose of u(j).
 The computed eigenvectors are normalized to have Euclidean norm
 equal to 1 and largest component real.
 Balancing a matrix means permuting the rows and columns to make it
 more nearly upper triangular, and applying a diagonal similarity
 transformation D * A * D**(-1), where D is a diagonal matrix, to
 make its rows and columns closer in norm and the condition numbers
 of its eigenvalues and eigenvectors smaller. The computed
 reciprocal condition numbers correspond to the balanced matrix.
 Permuting rows and columns will not change the condition numbers
 (in exact arithmetic) but diagonal scaling will. For further
 explanation of balancing, see section 4.10.2 of the LAPACK
 Users' Guide.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>BALANC</i> </p>
<pre> BALANC is CHARACTER*1
 Indicates how the input matrix should be diagonally scaled
 and/or permuted to improve the conditioning of its
 eigenvalues.
 = 'N': Do not diagonally scale or permute;
 = 'P': Perform permutations to make the matrix more nearly
 upper triangular. Do not diagonally scale;
 = 'S': Diagonally scale the matrix, ie. replace A by
 D*A*D**(-1), where D is a diagonal matrix chosen
 to make the rows and columns of A more equal in
 norm. Do not permute;
 = 'B': Both diagonally scale and permute A.
 Computed reciprocal condition numbers will be for the matrix
 after balancing and/or permuting. Permuting does not change
 condition numbers (in exact arithmetic), but balancing does.</pre>
<p><i>JOBVL</i> </p>
<pre> JOBVL is CHARACTER*1
 = 'N': left eigenvectors of A are not computed;
 = 'V': left eigenvectors of A are computed.
 If SENSE = 'E' or 'B', JOBVL must = 'V'.</pre>
<p><i>JOBVR</i> </p>
<pre> JOBVR is CHARACTER*1
 = 'N': right eigenvectors of A are not computed;
 = 'V': right eigenvectors of A are computed.
 If SENSE = 'E' or 'B', JOBVR must = 'V'.</pre>
<p><i>SENSE</i> </p>
<pre> SENSE is CHARACTER*1
 Determines which reciprocal condition numbers are computed.
 = 'N': None are computed;
 = 'E': Computed for eigenvalues only;
 = 'V': Computed for right eigenvectors only;
 = 'B': Computed for eigenvalues and right eigenvectors.
 If SENSE = 'E' or 'B', both left and right eigenvectors
 must also be computed (JOBVL = 'V' and JOBVR = 'V').</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the N-by-N matrix A.
 On exit, A has been overwritten. If JOBVL = 'V' or
 JOBVR = 'V', A contains the Schur form of the balanced
 version of the matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>W</i> </p>
<pre> W is COMPLEX*16 array, dimension (N)
 W contains the computed eigenvalues.</pre>
<p><i>VL</i> </p>
<pre> VL is COMPLEX*16 array, dimension (LDVL,N)
 If JOBVL = 'V', the left eigenvectors u(j) are stored one
 after another in the columns of VL, in the same order
 as their eigenvalues.
 If JOBVL = 'N', VL is not referenced.
 u(j) = VL(:,j), the j-th column of VL.</pre>
<p><i>LDVL</i> </p>
<pre> LDVL is INTEGER
 The leading dimension of the array VL. LDVL &gt;= 1; if
 JOBVL = 'V', LDVL &gt;= N.</pre>
<p><i>VR</i> </p>
<pre> VR is COMPLEX*16 array, dimension (LDVR,N)
 If JOBVR = 'V', the right eigenvectors v(j) are stored one
 after another in the columns of VR, in the same order
 as their eigenvalues.
 If JOBVR = 'N', VR is not referenced.
 v(j) = VR(:,j), the j-th column of VR.</pre>
<p><i>LDVR</i> </p>
<pre> LDVR is INTEGER
 The leading dimension of the array VR. LDVR &gt;= 1; if
 JOBVR = 'V', LDVR &gt;= N.</pre>
<p><i>ILO</i> </p>
<pre> ILO is INTEGER</pre>
<p><i>IHI</i> </p>
<pre> IHI is INTEGER
 ILO and IHI are integer values determined when A was
 balanced. The balanced A(i,j) = 0 if I &gt; J and
 J = 1,...,ILO-1 or I = IHI+1,...,N.</pre>
<p><i>SCALE</i> </p>
<pre> SCALE is DOUBLE PRECISION array, dimension (N)
 Details of the permutations and scaling factors applied
 when balancing A. If P(j) is the index of the row and column
 interchanged with row and column j, and D(j) is the scaling
 factor applied to row and column j, then
 SCALE(J) = P(J), for J = 1,...,ILO-1
 = D(J), for J = ILO,...,IHI
 = P(J) for J = IHI+1,...,N.
 The order in which the interchanges are made is N to IHI+1,
 then 1 to ILO-1.</pre>
<p><i>ABNRM</i> </p>
<pre> ABNRM is DOUBLE PRECISION
 The one-norm of the balanced matrix (the maximum
 of the sum of absolute values of elements of any column).</pre>
<p><i>RCONDE</i> </p>
<pre> RCONDE is DOUBLE PRECISION array, dimension (N)
 RCONDE(j) is the reciprocal condition number of the j-th
 eigenvalue.</pre>
<p><i>RCONDV</i> </p>
<pre> RCONDV is DOUBLE PRECISION array, dimension (N)
 RCONDV(j) is the reciprocal condition number of the j-th
 right eigenvector.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. If SENSE = 'N' or 'E',
 LWORK &gt;= max(1,2*N), and if SENSE = 'V' or 'B',
 LWORK &gt;= N*N+2*N.
 For good performance, LWORK must generally be larger.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (2*N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: if INFO = i, the QR algorithm failed to compute all the
 eigenvalues, and no eigenvectors or condition numbers
 have been computed; elements 1:ILO-1 and i+1:N of W
 contain eigenvalues which have converged.</pre>
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
<p> Definition at line 284 of file zgeevx.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
