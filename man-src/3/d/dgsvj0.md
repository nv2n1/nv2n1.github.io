---
title: "dgsvj0(3)"
name: "dgsvj0"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgsvj0/"
description: "dgsvj0.f –"
---

<h2 class="name">NAME</h2>
<p> dgsvj0.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dgsvj0</code> (JOBV, M, N, A, LDA, D, SVA, MV, V, LDV, EPS, SFMIN, TOL, NSWEEP, WORK, LWORK, INFO)<br />
 <i></i><code>DGSVJ0</code> pre-processor for the routine sgesvj.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgsvj0 (character*1JOBV, integerM, integerN, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( n )D, double precision, dimension( n )SVA, integerMV, double precision, dimension( ldv, * )V, integerLDV, double precisionEPS, double precisionSFMIN, double precisionTOL, integerNSWEEP, double precision, dimension( lwork )WORK, integerLWORK, integerINFO)</h3>
<p> <code>DGSVJ0</code> pre-processor for the routine sgesvj. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DGSVJ0 is called from DGESVJ as a pre-processor and that is its main
 purpose. It applies Jacobi rotations in the same way as DGESVJ does, but
 it does not check convergence (stopping criterion). Few tuning
 parameters (marked by [TP]) are available for the implementer.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>JOBV</i> </p>
<pre>
          JOBV is CHARACTER*1
          Specifies whether the output from this procedure is used
          to compute the matrix V:
          = 'V': the product of the Jacobi rotations is accumulated
                 by postmulyiplying the N-by-N array V.
                (See the description of V.)
          = 'A': the product of the Jacobi rotations is accumulated
                 by postmulyiplying the MV-by-N array V.
                (See the descriptions of MV and V.)
          = 'N': the Jacobi rotations are not accumulated.
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the input matrix A.  M &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the input matrix A.
          M &gt;= N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
          On entry, M-by-N matrix A, such that A*diag(D) represents
          the input matrix.
          On exit,
          A_onexit * D_onexit represents the input matrix A*diag(D)
          post-multiplied by a sequence of Jacobi rotations, where the
          rotation threshold and the total number of sweeps are given in
          TOL and NSWEEP, respectively.
          (See the descriptions of D, TOL and NSWEEP.)
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,M).
</pre>
<p> <i>D</i> </p>
<pre>
          D is DOUBLE PRECISION array, dimension (N)
          The array D accumulates the scaling factors from the fast scaled
          Jacobi rotations.
          On entry, A*diag(D) represents the input matrix.
          On exit, A_onexit*diag(D_onexit) represents the input matrix
          post-multiplied by a sequence of Jacobi rotations, where the
          rotation threshold and the total number of sweeps are given in
          TOL and NSWEEP, respectively.
          (See the descriptions of A, TOL and NSWEEP.)
</pre>
<p> <i>SVA</i> </p>
<pre>
          SVA is DOUBLE PRECISION array, dimension (N)
          On entry, SVA contains the Euclidean norms of the columns of
          the matrix A*diag(D).
          On exit, SVA contains the Euclidean norms of the columns of
          the matrix onexit*diag(D_onexit).
</pre>
<p> <i>MV</i> </p>
<pre>
          MV is INTEGER
          If JOBV .EQ. 'A', then MV rows of V are post-multipled by a
                           sequence of Jacobi rotations.
          If JOBV = 'N',   then MV is not referenced.
</pre>
<p> <i>V</i> </p>
<pre>
          V is DOUBLE PRECISION array, dimension (LDV,N)
          If JOBV .EQ. 'V' then N rows of V are post-multipled by a
                           sequence of Jacobi rotations.
          If JOBV .EQ. 'A' then MV rows of V are post-multipled by a
                           sequence of Jacobi rotations.
          If JOBV = 'N',   then V is not referenced.
</pre>
<p> <i>LDV</i> </p>
<pre>
          LDV is INTEGER
          The leading dimension of the array V,  LDV &gt;= 1.
          If JOBV = 'V', LDV .GE. N.
          If JOBV = 'A', LDV .GE. MV.
</pre>
<p> <i>EPS</i> </p>
<pre>
          EPS is DOUBLE PRECISION
          EPS = DLAMCH('Epsilon')
</pre>
<p> <i>SFMIN</i> </p>
<pre>
          SFMIN is DOUBLE PRECISION
          SFMIN = DLAMCH('Safe Minimum')
</pre>
<p> <i>TOL</i> </p>
<pre>
          TOL is DOUBLE PRECISION
          TOL is the threshold for Jacobi rotations. For a pair
          A(:,p), A(:,q) of pivot columns, the Jacobi rotation is
          applied only if DABS(COS(angle(A(:,p),A(:,q)))) .GT. TOL.
</pre>
<p> <i>NSWEEP</i> </p>
<pre>
          NSWEEP is INTEGER
          NSWEEP is the number of sweeps of Jacobi rotations to be
          performed.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (LWORK)
</pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is INTEGER
          LWORK is the dimension of WORK. LWORK .GE. M.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0 : successful exit.
          &lt; 0 : if INFO = -i, then the i-th argument had an illegal value
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
<dd> September 2012</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd> DGSVJ0 is used just to enable DGESVJ to call a simplified version of itself to work on a submatrix of the original matrix.</dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Zlatko Drmac (Zagreb, Croatia) and Kresimir Veselic (Hagen, Germany)</dl>
<p> <code>Bugs, Examples and Comments: </code></p>
<dl>
<dt>
<dd> Please report all bugs and send interesting test examples and comments to drmac [at] math.hr. Thank you.</dl>
<p> Definition at line 218 of file dgsvj0.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
