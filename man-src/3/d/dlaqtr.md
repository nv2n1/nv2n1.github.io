---
title: "dlaqtr(3)"
name: "dlaqtr"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlaqtr/"
description: "dlaqtr.f –"
---

<h2 class="name">NAME</h2>
<p> dlaqtr.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dlaqtr</code> (LTRAN, LREAL, N, T, LDT, B, W, SCALE, X, WORK, INFO)<br />
 <i></i><code>DLAQTR</code> solves a real quasi-triangular system of equations, or a complex quasi-triangular system of special form, in real arithmetic.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlaqtr (logicalLTRAN, logicalLREAL, integerN, double precision, dimension( ldt, * )T, integerLDT, double precision, dimension( * )B, double precisionW, double precisionSCALE, double precision, dimension( * )X, double precision, dimension( * )WORK, integerINFO)</h3>
<p> <code>DLAQTR</code> solves a real quasi-triangular system of equations, or a complex quasi-triangular system of special form, in real arithmetic. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
 DLAQTR solves the real quasi-triangular system
              op(T)*p = scale*c,               if LREAL = .TRUE.
 or the complex quasi-triangular systems
            op(T + iB)*(p+iq) = scale*(c+id),  if LREAL = .FALSE.
 in real arithmetic, where T is upper quasi-triangular.
 If LREAL = .FALSE., then the first diagonal block of T must be
 1 by 1, B is the specially structured matrix
                B = [ b(1) b(2) ... b(n) ]
                    [       w            ]
                    [           w        ]
                    [              .     ]
                    [                 w  ]
 op(A) = A or A**T, A**T denotes the transpose of
 matrix A.
 On input, X = [ c ].  On output, X = [ p ].
               [ d ]                  [ q ]
 This subroutine is designed for the condition number estimation
 in routine DTRSNA.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>LTRAN</i> </p>
<pre>
          LTRAN is LOGICAL
          On entry, LTRAN specifies the option of conjugate transpose:
             = .FALSE.,    op(T+i*B) = T+i*B,
             = .TRUE.,     op(T+i*B) = (T+i*B)**T.
</pre>
<p> <i>LREAL</i> </p>
<pre>
          LREAL is LOGICAL
          On entry, LREAL specifies the input matrix structure:
             = .FALSE.,    the input is complex
             = .TRUE.,     the input is real
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          On entry, N specifies the order of T+i*B. N &gt;= 0.
</pre>
<p> <i>T</i> </p>
<pre>
          T is DOUBLE PRECISION array, dimension (LDT,N)
          On entry, T contains a matrix in Schur canonical form.
          If LREAL = .FALSE., then the first diagonal block of T mu
          be 1 by 1.
</pre>
<p> <i>LDT</i> </p>
<pre>
          LDT is INTEGER
          The leading dimension of the matrix T. LDT &gt;= max(1,N).
</pre>
<p> <i>B</i> </p>
<pre>
          B is DOUBLE PRECISION array, dimension (N)
          On entry, B contains the elements to form the matrix
          B as described above.
          If LREAL = .TRUE., B is not referenced.
</pre>
<p> <i>W</i> </p>
<pre>
          W is DOUBLE PRECISION
          On entry, W is the diagonal element of the matrix B.
          If LREAL = .TRUE., W is not referenced.
</pre>
<p> <i>SCALE</i> </p>
<pre>
          SCALE is DOUBLE PRECISION
          On exit, SCALE is the scale factor.
</pre>
<p> <i>X</i> </p>
<pre>
          X is DOUBLE PRECISION array, dimension (2*N)
          On entry, X contains the right hand side of the system.
          On exit, X is overwritten by the solution.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          On exit, INFO is set to
             0: successful exit.
               1: the some diagonal 1 by 1 block has been perturbed by
                  a small number SMIN to keep nonsingularity.
               2: the some diagonal 2 by 2 block has been perturbed by
                  a small number in DLALN2 to keep nonsingularity.
          NOTE: In the interests of speed, this routine does not
                check the inputs for errors.
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
<p> Definition at line 165 of file dlaqtr.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
