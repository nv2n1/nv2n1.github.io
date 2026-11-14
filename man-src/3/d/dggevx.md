---
title: "dggevx(3)"
name: "dggevx"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dggevx/"
description: "dggevx.f –"
---

<h2 class="name">NAME</h2>
<p> dggevx.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dggevx</code> (BALANC, JOBVL, JOBVR, SENSE, N, A, LDA, B, LDB, ALPHAR, ALPHAI, BETA, VL, LDVL, VR, LDVR, ILO, IHI, LSCALE, RSCALE, ABNRM, BBNRM, RCONDE, RCONDV, WORK, LWORK, IWORK, BWORK, INFO)<br />
 <i></i><code> DGGEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dggevx (characterBALANC, characterJOBVL, characterJOBVR, characterSENSE, integerN, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldb, * )B, integerLDB, double precision, dimension( * )ALPHAR, double precision, dimension( * )ALPHAI, double precision, dimension( * )BETA, double precision, dimension( ldvl, * )VL, integerLDVL, double precision, dimension( ldvr, * )VR, integerLDVR, integerILO, integerIHI, double precision, dimension( * )LSCALE, double precision, dimension( * )RSCALE, double precisionABNRM, double precisionBBNRM, double precision, dimension( * )RCONDE, double precision, dimension( * )RCONDV, double precision, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, logical, dimension( * )BWORK, integerINFO)</h3>
<p> <code> DGGEVX computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
 DGGEVX computes for a pair of N-by-N real nonsymmetric matrices (A,B)
 the generalized eigenvalues, and optionally, the left and/or right
 generalized eigenvectors.
 Optionally also, it computes a balancing transformation to improve
 the conditioning of the eigenvalues and eigenvectors (ILO, IHI,
 LSCALE, RSCALE, ABNRM, and BBNRM), reciprocal condition numbers for
 the eigenvalues (RCONDE), and reciprocal condition numbers for the
 right eigenvectors (RCONDV).
 A generalized eigenvalue for a pair of matrices (A,B) is a scalar
 lambda or a ratio alpha/beta = lambda, such that A - lambda*B is
 singular. It is usually represented as the pair (alpha,beta), as
 there is a reasonable interpretation for beta=0, and even for both
 being zero.
 The right eigenvector v(j)
 corresponding to the eigenvalue lambda(j)
     of(A, B) satisfies
     A *v(j) = lambda(j) * B * v(j).The left eigenvector u(j)
 corresponding to the eigenvalue lambda(j)
     of(A, B) satisfies
     u(j) **H *A = lambda(j) * u(j) * *H * B.where u(j) * *H is the conjugate - transpose of u(j).
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>BALANC</i> </p>
<p>BALANC is CHARACTER * 1 Specifies the balance option to be performed.= &#8216;N&#8217; : do not diagonally scale or permute;<br />
= &#8216;P&#8217; : permute only;<br />
= &#8216;S&#8217; : scale only;<br />
          = &#8216;B&#8217;:  both permute and scale.<br />
          Computed reciprocal condition numbers will be for the<br />
          matrices after permuting and/or balancing. Permuting does<br />
          not change condition numbers (in exact arithmetic), but<br />
          balancing does.</p>
<p> <i>JOBVL</i> </p>
<pre>
          JOBVL is CHARACTER*1
          = 'N':  do not compute the left generalized eigenvectors;
          = 'V':  compute the left generalized eigenvectors.
</pre>
<p> <i>JOBVR</i> </p>
<pre>
          JOBVR is CHARACTER*1
          = 'N':  do not compute the right generalized eigenvectors;
          = 'V':  compute the right generalized eigenvectors.
</pre>
<p> <i>SENSE</i> </p>
<p>SENSE is CHARACTER * 1 Determines which reciprocal condition numbers are computed.= &#8216;N&#8217; : none are computed;<br />
          = &#8216;E&#8217;: computed for eigenvalues only;<br />
          = &#8216;V&#8217;: computed for eigenvectors only;<br />
          = &#8216;B&#8217;: computed for eigenvalues and eigenvectors.</p>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrices A, B, VL, and VR.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA, N)
          On entry, the matrix A in the pair (A,B).
          On exit, A has been overwritten. If JOBVL='V' or JOBVR='V'
          or both, then A contains the first part of the real Schur
          form of the &quot;balanced&quot; versions of the input A and B.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of A.  LDA &gt;= max(1,N).
</pre>
<p> <i>B</i> </p>
<pre>
          B is DOUBLE PRECISION array, dimension (LDB, N)
          On entry, the matrix B in the pair (A,B).
          On exit, B has been overwritten. If JOBVL='V' or JOBVR='V'
          or both, then B contains the second part of the real Schur
          form of the &quot;balanced&quot; versions of the input A and B.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of B.  LDB &gt;= max(1,N).
</pre>
<p> <i>ALPHAR</i> </p>
<pre>
          ALPHAR is DOUBLE PRECISION array, dimension (N)
</pre>
<p> <i>ALPHAI</i> </p>
<pre>
          ALPHAI is DOUBLE PRECISION array, dimension (N)
</pre>
<p> <i>BETA</i> </p>
<pre>
          BETA is DOUBLE PRECISION array, dimension (N)
          On exit, (ALPHAR(j) + ALPHAI(j)*i)/BETA(j), j=1,...,N, will
          be the generalized eigenvalues.  If ALPHAI(j) is zero, then
          the j-th eigenvalue is real; if positive, then the j-th and
          (j+1)-st eigenvalues are a complex conjugate pair, with
          ALPHAI(j+1) negative.
          Note: the quotients ALPHAR(j)/BETA(j) and ALPHAI(j)/BETA(j)
          may easily over- or underflow, and BETA(j) may even be zero.
          Thus, the user should avoid naively computing the ratio
          ALPHA/BETA. However, ALPHAR and ALPHAI will be always less
          than and usually comparable with norm(A) in magnitude, and
          BETA always less than and usually comparable with norm(B).
</pre>
<p> <i>VL</i> </p>
<pre>
          VL is DOUBLE PRECISION array, dimension (LDVL,N)
          If JOBVL = 'V', the left eigenvectors u(j) are stored one
          after another in the columns of VL, in the same order as
          their eigenvalues. If the j-th eigenvalue is real, then
          u(j) = VL(:,j), the j-th column of VL. If the j-th and
          (j+1)-th eigenvalues form a complex conjugate pair, then
          u(j) = VL(:,j)+i*VL(:,j+1) and u(j+1) = VL(:,j)-i*VL(:,j+1).
          Each eigenvector will be scaled so the largest component have
          abs(real part) + abs(imag. part) = 1.
          Not referenced if JOBVL = 'N'.
</pre>
<p> <i>LDVL</i> </p>
<pre>
          LDVL is INTEGER
          The leading dimension of the matrix VL. LDVL &gt;= 1, and
          if JOBVL = 'V', LDVL &gt;= N.
</pre>
<p> <i>VR</i> </p>
<pre>
          VR is DOUBLE PRECISION array, dimension (LDVR,N)
          If JOBVR = 'V', the right eigenvectors v(j) are stored one
          after another in the columns of VR, in the same order as
          their eigenvalues. If the j-th eigenvalue is real, then
          v(j) = VR(:,j), the j-th column of VR. If the j-th and
          (j+1)-th eigenvalues form a complex conjugate pair, then
          v(j) = VR(:,j)+i*VR(:,j+1) and v(j+1) = VR(:,j)-i*VR(:,j+1).
          Each eigenvector will be scaled so the largest component have
          abs(real part) + abs(imag. part) = 1.
          Not referenced if JOBVR = 'N'.
</pre>
<p> <i>LDVR</i> </p>
<pre>
          LDVR is INTEGER
          The leading dimension of the matrix VR. LDVR &gt;= 1, and
          if JOBVR = 'V', LDVR &gt;= N.
</pre>
<p> <i>ILO</i> </p>
<pre>
          ILO is INTEGER
</pre>
<p> <i>IHI</i> </p>
<pre>
          IHI is INTEGER
          ILO and IHI are integer values such that on exit
          A(i,j) = 0 and B(i,j) = 0 if i &gt; j and
          j = 1,...,ILO-1 or i = IHI+1,...,N.
          If BALANC = 'N' or 'S', ILO = 1 and IHI = N.
</pre>
<p> <i>LSCALE</i> </p>
<pre>
          LSCALE is DOUBLE PRECISION array, dimension (N)
          Details of the permutations and scaling factors applied
          to the left side of A and B.  If PL(j) is the index of the
          row interchanged with row j, and DL(j) is the scaling
          factor applied to row j, then
            LSCALE(j) = PL(j)  for j = 1,...,ILO-1
                      = DL(j)  for j = ILO,...,IHI
                      = PL(j)  for j = IHI+1,...,N.
          The order in which the interchanges are made is N to IHI+1,
          then 1 to ILO-1.
</pre>
<p> <i>RSCALE</i> </p>
<pre>
          RSCALE is DOUBLE PRECISION array, dimension (N)
          Details of the permutations and scaling factors applied
          to the right side of A and B.  If PR(j) is the index of the
          column interchanged with column j, and DR(j) is the scaling
          factor applied to column j, then
            RSCALE(j) = PR(j)  for j = 1,...,ILO-1
                      = DR(j)  for j = ILO,...,IHI
                      = PR(j)  for j = IHI+1,...,N
          The order in which the interchanges are made is N to IHI+1,
          then 1 to ILO-1.
</pre>
<p> <i>ABNRM</i> </p>
<pre>
          ABNRM is DOUBLE PRECISION
          The one-norm of the balanced matrix A.
</pre>
<p> <i>BBNRM</i> </p>
<pre>
          BBNRM is DOUBLE PRECISION
          The one-norm of the balanced matrix B.
</pre>
<p> <i>RCONDE</i> </p>
<pre>
          RCONDE is DOUBLE PRECISION array, dimension (N)
          If SENSE = 'E' or 'B', the reciprocal condition numbers of
          the eigenvalues, stored in consecutive elements of the array.
          For a complex conjugate pair of eigenvalues two consecutive
          elements of RCONDE are set to the same value. Thus RCONDE(j),
          RCONDV(j), and the j-th columns of VL and VR all correspond
          to the j-th eigenpair.
          If SENSE = 'N or 'V', RCONDE is not referenced.
</pre>
<p> <i>RCONDV</i> </p>
<pre>
          RCONDV is DOUBLE PRECISION array, dimension (N)
          If SENSE = 'V' or 'B', the estimated reciprocal condition
          numbers of the eigenvectors, stored in consecutive elements
          of the array. For a complex eigenvector two consecutive
          elements of RCONDV are set to the same value. If the
          eigenvalues cannot be reordered to compute RCONDV(j),
          RCONDV(j) is set to 0; this can only occur when the true
          value would be very small anyway.
          If SENSE = 'N' or 'E', RCONDV is not referenced.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre><code>
LWORK is INTEGER
        The dimension of the array WORK.LWORK &gt;= max(1, 2 * N).If BALANC = 'S' or 'B',
                                                                  or JOBVL = 'V', or JOBVR = 'V',
                                                                  LWORK &gt;= max(1, 6 * N).If SENSE = 'E' or 'B', LWORK &gt;= max(1, 10 * N).If SENSE = 'V' or 'B', LWORK &gt;= 2 *N *N + 8 *N + 16. If LWORK = -1, then a workspace query is assumed;
the routine
    only calculates the optimal size of the WORK array,
    returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.
</code></pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (N+6)
          If SENSE = 'E', IWORK is not referenced.
</pre>
<p> <i>BWORK</i> </p>
<pre>
          BWORK is LOGICAL array, dimension (N)
          If SENSE = 'N', BWORK is not referenced.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
          = 1,...,N:
                The QZ iteration failed.  No eigenvectors have been
                calculated, but ALPHAR(j), ALPHAI(j), and BETA(j)
                should be correct for j=INFO+1,...,N.
          &gt; N:  =N+1: other than QZ iteration failed in DHGEQZ.
                =N+2: error return from DTGEVC.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
<dd> April 2012</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  Balancing a matrix pair (A,B) includes, first, permuting rows and
  columns to isolate eigenvalues, second, applying diagonal similarity
  transformation to the rows and columns to make the rows and columns
  as close in norm as possible. The computed reciprocal condition
  numbers correspond to the balanced matrix. Permuting rows and columns
  will not change the condition numbers (in exact arithmetic) but
  diagonal scaling will.  For further explanation of balancing, see
  section 4.11.1.2 of LAPACK Users' Guide.
  An approximate error bound on the chordal distance between the i-th
  computed generalized eigenvalue w and the corresponding exact
  eigenvalue lambda is
       chord(w, lambda) &lt;= EPS * norm(ABNRM, BBNRM) / RCONDE(I)
  An approximate error bound for the angle between the i-th computed
  eigenvector VL(i) or VR(i) is given by
       EPS * norm(ABNRM, BBNRM) / DIF(i).
  For further explanation of the reciprocal condition numbers RCONDE
  and RCONDV, see section 4.11 of LAPACK User's Guide.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 389 of file dggevx.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
