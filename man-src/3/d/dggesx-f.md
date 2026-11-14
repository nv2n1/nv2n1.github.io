---
title: "dggesx-f(3)"
name: "dggesx-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dggesx-f/"
description: "dggesx.f –"
---

<p>dggesx.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dggesx</code> (JOBVSL, JOBVSR, SORT, SELCTG, SENSE, N, A, LDA, B, LDB, SDIM, ALPHAR, ALPHAI, BETA, VSL, LDVSL, VSR, LDVSR, RCONDE, RCONDV, WORK, LWORK, IWORK, LIWORK, BWORK, INFO)<br />
 <i></i><code> DGGESX computes the eigenvalues, the Schur form, and, optionally, the matrix of Schur vectors for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dggesx (characterJOBVSL, characterJOBVSR, characterSORT, logical, externalSELCTG, characterSENSE, integerN, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldb, * )B, integerLDB, integerSDIM, double precision, dimension( * )ALPHAR, double precision, dimension( * )ALPHAI, double precision, dimension( * )BETA, double precision, dimension( ldvsl, * )VSL, integerLDVSL, double precision, dimension( ldvsr, * )VSR, integerLDVSR, double precision, dimension( 2 )RCONDE, double precision, dimension( 2 )RCONDV, double precision, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integerLIWORK, logical, dimension( * )BWORK, integerINFO)</h3>
<p> <code> DGGESX computes the eigenvalues, the Schur form, and, optionally, the matrix of Schur vectors for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dt>
<dd>
<pre>
 DGGESX computes for a pair of N-by-N real nonsymmetric matrices
 (A,B), the generalized eigenvalues, the real Schur form (S,T), and,
 optionally, the left and/or right matrices of Schur vectors (VSL and
 VSR).  This gives the generalized Schur factorization
      (A,B) = ( (VSL) S (VSR)**T, (VSL) T (VSR)**T )
 Optionally, it also orders the eigenvalues so that a selected cluster
 of eigenvalues appears in the leading diagonal blocks of the upper
 quasi-triangular matrix S and the upper triangular matrix T; computes
 a reciprocal condition number for the average of the selected
 eigenvalues (RCONDE); and computes a reciprocal condition number for
 the right and left deflating subspaces corresponding to the selected
 eigenvalues (RCONDV). The leading columns of VSL and VSR then form
 an orthonormal basis for the corresponding left and right eigenspaces
 (deflating subspaces).
 A generalized eigenvalue for a pair of matrices (A,B) is a scalar w
 or a ratio alpha/beta = w, such that  A - w*B is singular.  It is
 usually represented as the pair (alpha,beta), as there is a
 reasonable interpretation for beta=0 or for both being zero.
 A pair of matrices (S,T) is in generalized real Schur form if T is
 upper triangular with non-negative diagonal and S is block upper
 triangular with 1-by-1 and 2-by-2 blocks.  1-by-1 blocks correspond
 to real generalized eigenvalues, while 2-by-2 blocks of S will be
 &quot;standardized&quot; by making the corresponding elements of T have the
 form:
         [  a  0  ]
         [  0  b  ]
 and the pair of corresponding 2-by-2 blocks in S and T will have a
 complex conjugate pair of generalized eigenvalues.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>JOBVSL</i> </p>
<pre>
          JOBVSL is CHARACTER*1
          = 'N':  do not compute the left Schur vectors;
          = 'V':  compute the left Schur vectors.
</pre>
<p> <i>JOBVSR</i> </p>
<pre>
          JOBVSR is CHARACTER*1
          = 'N':  do not compute the right Schur vectors;
          = 'V':  compute the right Schur vectors.
</pre>
<p> <i>SORT</i> </p>
<pre>
          SORT is CHARACTER*1
          Specifies whether or not to order the eigenvalues on the
          diagonal of the generalized Schur form.
          = 'N':  Eigenvalues are not ordered;
          = 'S':  Eigenvalues are ordered (see SELCTG).
</pre>
<p> <i>SELCTG</i> </p>
<pre>
          SELCTG is procedure) LOGICAL FUNCTION of three DOUBLE PRECISION arguments
          SELCTG must be declared EXTERNAL in the calling subroutine.
          If SORT = 'N', SELCTG is not referenced.
          If SORT = 'S', SELCTG is used to select eigenvalues to sort
          to the top left of the Schur form.
          An eigenvalue (ALPHAR(j)+ALPHAI(j))/BETA(j) is selected if
          SELCTG(ALPHAR(j),ALPHAI(j),BETA(j)) is true; i.e. if either
          one of a complex conjugate pair of eigenvalues is selected,
          then both complex eigenvalues are selected.
          Note that a selected complex eigenvalue may no longer satisfy
          SELCTG(ALPHAR(j),ALPHAI(j),BETA(j)) = .TRUE. after ordering,
          since ordering may change the value of complex eigenvalues
          (especially if the eigenvalue is ill-conditioned), in this
          case INFO is set to N+3.
</pre>
<p> <i>SENSE</i> </p>
<pre>
          SENSE is CHARACTER*1
          Determines which reciprocal condition numbers are computed.
          = 'N' : None are computed;
          = 'E' : Computed for average of selected eigenvalues only;
          = 'V' : Computed for selected deflating subspaces only;
          = 'B' : Computed for both.
          If SENSE = 'E', 'V', or 'B', SORT must equal 'S'.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrices A, B, VSL, and VSR.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA, N)
          On entry, the first of the pair of matrices.
          On exit, A has been overwritten by its generalized Schur
          form S.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of A.  LDA &gt;= max(1,N).
</pre>
<p> <i>B</i> </p>
<pre>
          B is DOUBLE PRECISION array, dimension (LDB, N)
          On entry, the second of the pair of matrices.
          On exit, B has been overwritten by its generalized Schur
          form T.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of B.  LDB &gt;= max(1,N).
</pre>
<p> <i>SDIM</i> </p>
<pre>
          SDIM is INTEGER
          If SORT = 'N', SDIM = 0.
          If SORT = 'S', SDIM = number of eigenvalues (after sorting)
          for which SELCTG is true.  (Complex conjugate pairs for which
          SELCTG is true for either eigenvalue count as 2.)
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
          be the generalized eigenvalues.  ALPHAR(j) + ALPHAI(j)*i
          and BETA(j),j=1,...,N  are the diagonals of the complex Schur
          form (S,T) that would result if the 2-by-2 diagonal blocks of
          the real Schur form of (A,B) were further reduced to
          triangular form using 2-by-2 complex unitary transformations.
          If ALPHAI(j) is zero, then the j-th eigenvalue is real; if
          positive, then the j-th and (j+1)-st eigenvalues are a
          complex conjugate pair, with ALPHAI(j+1) negative.
          Note: the quotients ALPHAR(j)/BETA(j) and ALPHAI(j)/BETA(j)
          may easily over- or underflow, and BETA(j) may even be zero.
          Thus, the user should avoid naively computing the ratio.
          However, ALPHAR and ALPHAI will be always less than and
          usually comparable with norm(A) in magnitude, and BETA always
          less than and usually comparable with norm(B).
</pre>
<p> <i>VSL</i> </p>
<pre>
          VSL is DOUBLE PRECISION array, dimension (LDVSL,N)
          If JOBVSL = 'V', VSL will contain the left Schur vectors.
          Not referenced if JOBVSL = 'N'.
</pre>
<p> <i>LDVSL</i> </p>
<pre>
          LDVSL is INTEGER
          The leading dimension of the matrix VSL. LDVSL &gt;=1, and
          if JOBVSL = 'V', LDVSL &gt;= N.
</pre>
<p> <i>VSR</i> </p>
<pre>
          VSR is DOUBLE PRECISION array, dimension (LDVSR,N)
          If JOBVSR = 'V', VSR will contain the right Schur vectors.
          Not referenced if JOBVSR = 'N'.
</pre>
<p> <i>LDVSR</i> </p>
<pre>
          LDVSR is INTEGER
          The leading dimension of the matrix VSR. LDVSR &gt;= 1, and
          if JOBVSR = 'V', LDVSR &gt;= N.
</pre>
<p> <i>RCONDE</i> </p>
<pre>
          RCONDE is DOUBLE PRECISION array, dimension ( 2 )
          If SENSE = 'E' or 'B', <a href="//www.systutorials.com/docs/linux/man/1-RCONDE/">RCONDE</a>(1) and <a href="//www.systutorials.com/docs/linux/man/2-RCONDE/">RCONDE</a>(2) contain the
          reciprocal condition numbers for the average of the selected
          eigenvalues.
          Not referenced if SENSE = 'N' or 'V'.
</pre>
<p> <i>RCONDV</i> </p>
<pre>
          RCONDV is DOUBLE PRECISION array, dimension ( 2 )
          If SENSE = 'V' or 'B', <a href="//www.systutorials.com/docs/linux/man/1-RCONDV/">RCONDV</a>(1) and <a href="//www.systutorials.com/docs/linux/man/2-RCONDV/">RCONDV</a>(2) contain the
          reciprocal condition numbers for the selected deflating
          subspaces.
          Not referenced if SENSE = 'N' or 'E'.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is INTEGER
          The dimension of the array WORK.
          If N = 0, LWORK &gt;= 1, else if SENSE = 'E', 'V', or 'B',
          LWORK &gt;= max( 8*N, 6*N+16, 2*SDIM*(N-SDIM) ), else
          LWORK &gt;= max( 8*N, 6*N+16 ).
          Note that 2*SDIM*(N-SDIM) &lt;= N*N/2.
          Note also that an error is only returned if
          LWORK &lt; max( 8*N, 6*N+16), but if SENSE = 'E' or 'V' or 'B'
          this may not be large enough.
          If LWORK = -1, then a workspace query is assumed; the routine
          only calculates the bound on the optimal size of the WORK
          array and the minimum size of the IWORK array, returns these
          values as the first entries of the WORK and IWORK arrays, and
          no error message related to LWORK or LIWORK is issued by
          XERBLA.
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (MAX(1,LIWORK))
          On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the minimum LIWORK.
</pre>
<p> <i>LIWORK</i> </p>
<pre>
          LIWORK is INTEGER
          The dimension of the array IWORK.
          If SENSE = 'N' or N = 0, LIWORK &gt;= 1, otherwise
          LIWORK &gt;= N+6.
          If LIWORK = -1, then a workspace query is assumed; the
          routine only calculates the bound on the optimal size of the
          WORK array and the minimum size of the IWORK array, returns
          these values as the first entries of the WORK and IWORK
          arrays, and no error message related to LWORK or LIWORK is
          issued by XERBLA.
</pre>
<p> <i>BWORK</i> </p>
<pre>
          BWORK is LOGICAL array, dimension (N)
          Not referenced if SORT = 'N'.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
          = 1,...,N:
                The QZ iteration failed.  (A,B) are not in Schur
                form, but ALPHAR(j), ALPHAI(j), and BETA(j) should
                be correct for j=INFO+1,...,N.
          &gt; N:  =N+1: other than QZ iteration failed in DHGEQZ
                =N+2: after reordering, roundoff changed values of
                      some complex eigenvalues so that leading
                      eigenvalues in the Generalized Schur form no
                      longer satisfy SELCTG=.TRUE.  This could also
                      be caused due to scaling.
                =N+3: reordering failed in DTGSEN.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dt>
<dd> November 2011</dl>
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dt>
<dd>
<pre>
  An approximate (asymptotic) bound on the average absolute error of
  the selected eigenvalues is
       EPS * norm((A, B)) / RCONDE( 1 ).
  An approximate (asymptotic) bound on the maximum angular error in
  the computed deflating subspaces is
       EPS * norm((A, B)) / RCONDV( 2 ).
  See LAPACK User's Guide, section 4.11 for more information.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 363 of file dggesx.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code.</p>
