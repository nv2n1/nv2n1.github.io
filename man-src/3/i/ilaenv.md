---
title: "ilaenv(3)"
name: "ilaenv"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ilaenv/"
description: "ilaenv.f –"
---

<h2 class="name">NAME</h2>
<p> ilaenv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> INTEGER function <code>ilaenv</code> (ISPEC, NAME, OPTS, N1, N2, N3, N4)<br />
 <i></i><code>ILAENV</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>INTEGER function ilaenv (integerISPEC, character*( * )NAME, character*( * )OPTS, integerN1, integerN2, integerN3, integerN4)</h3>
<p> <code>ILAENV</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
 ILAENV is called from the LAPACK routines to choose problem-dependent
 parameters for the local environment.  See ISPEC for a description of
 the parameters.
 ILAENV returns an INTEGER
 if ILAENV &gt;= 0: ILAENV returns the value of the parameter specified by ISPEC
 if ILAENV &lt; 0:  if ILAENV = -k, the k-th argument had an illegal value.
 This version provides a set of parameters which should give good,
 but not optimal, performance on many of the currently available
 computers.  Users are encouraged to modify this subroutine to set
 the tuning parameters for their particular machine using the option
 and problem size information in the arguments.
 This routine will not function correctly if it is converted to all
 lower case.  Converting it to all upper case is allowed.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ISPEC</i> </p>
<pre><code>
ISPEC is INTEGER
    Specifies the parameter to be returned as the value of
        ILAENV.= 1 : the optimal blocksize;
if this value is 1, an unblocked
               algorithm will give the best performance.
          = 2: the minimum block size for which the block routine
               should be used;
if the usable block size is less than
               this value, an unblocked routine should be used.
          = 3: the crossover point (in a block routine, for N less
               than this value, an unblocked routine should be used)
          = 4: the number of shifts, used in the nonsymmetric
               eigenvalue routines (DEPRECATED)
          = 5: the minimum column dimension for blocking to be used;
               rectangular blocks must have dimension at least k by m,
               where k is given by ILAENV(2,...) and m by ILAENV(5,...)
          = 6: the crossover point for the SVD (when reducing an m by n
               matrix to bidiagonal form, if max(m,n)/min(m,n) exceeds
               this value, a QR factorization is used first to reduce
               the matrix to a triangular form.)
          = 7: the number of processors
          = 8: the crossover point for the multishift QR method
               for nonsymmetric eigenvalue problems (DEPRECATED)
          = 9: maximum size of the subproblems at the bottom of the
               computation tree in the divide-and-conquer algorithm
               (used by xGELSD and xGESDD)
          =10: ieee NaN arithmetic can be trusted not to trap
          =11: infinity arithmetic can be trusted not to trap
          12 &lt;= ISPEC &lt;= 16:
               xHSEQR or one of its subroutines,
               see IPARMQ for detailed explanation
</code></pre>
<p> <i>NAME</i> </p>
<pre>
          NAME is CHARACTER*(*)
          The name of the calling subroutine, in either upper case or
          lower case.
</pre>
<p> <i>OPTS</i> </p>
<pre>
          OPTS is CHARACTER*(*)
          The character options to the subroutine NAME, concatenated
          into a single character string.  For example, UPLO = 'U',
          TRANS = 'T', and DIAG = 'N' for a triangular routine would
          be specified as OPTS = 'UTN'.
</pre>
<p> <i>N1</i> </p>
<pre>
          N1 is INTEGER
</pre>
<p> <i>N2</i> </p>
<pre>
          N2 is INTEGER
</pre>
<p> <i>N3</i> </p>
<pre>
          N3 is INTEGER
</pre>
<p> <i>N4</i> </p>
<pre>
          N4 is INTEGER
          Problem dimensions for the subroutine NAME; these may not all
          be required.
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
<dd> November 2011</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  The following conventions have been used when calling ILAENV from the
  LAPACK routines:
  1)  OPTS is a concatenation of all of the character options to
      subroutine NAME, in the same order that they appear in the
      argument list for NAME, even if they are not used in determining
      the value of the parameter specified by ISPEC.
  2)  The problem dimensions N1, N2, N3, N4 are specified in the order
      that they appear in the argument list for NAME.  N1 is used
      first, N2 second, and so on, and unused problem dimensions are
      passed a value of -1.
  3)  The parameter value returned by ILAENV is checked for validity in
      the calling subroutine.  For example, ILAENV is used to retrieve
      the optimal blocksize for STRTRI as follows:
      NB = ILAENV( 1, 'STRTRI', UPLO // DIAG, N, -1, -1, -1 )
      IF( NB.LE.1 ) NB = MAX( 1, N )
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 163 of file ilaenv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
