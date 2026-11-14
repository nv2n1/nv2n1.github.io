---
title: "slasr(3)"
name: "slasr"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slasr/"
description: "slasr.f –"
---

<h2 class="name">NAME</h2>
<p> slasr.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slasr</code> (SIDE, PIVOT, DIRECT, M, N, C, S, A, LDA)<br />
 <i></i><code>SLASR</code> applies a sequence of plane rotations to a general rectangular matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slasr (characterSIDE, characterPIVOT, characterDIRECT, integerM, integerN, real, dimension( * )C, real, dimension( * )S, real, dimension( lda, * )A, integerLDA)</h3>
<p> <code>SLASR</code> applies a sequence of plane rotations to a general rectangular matrix. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLASR applies a sequence of plane rotations to a real matrix A,
 from either the left or the right.
 
 When SIDE = 'L', the transformation takes the form
 
    A := P*A
 
 and when SIDE = 'R', the transformation takes the form
 
    A := A*P**T
 
 where P is an orthogonal matrix consisting of a sequence of z plane
 rotations, with z = M when SIDE = 'L' and z = N when SIDE = 'R',
 and P**T is the transpose of P.
 
 When DIRECT = 'F' (Forward sequence), then
 
    P = P(z-1) * ... * <a href="//www.systutorials.com/docs/linux/man/2-P/">P</a>(2) * <a href="//www.systutorials.com/docs/linux/man/1-P/">P</a>(1)
 
 and when DIRECT = 'B' (Backward sequence), then
 
    P = <a href="//www.systutorials.com/docs/linux/man/1-P/">P</a>(1) * <a href="//www.systutorials.com/docs/linux/man/2-P/">P</a>(2) * ... * P(z-1)
 
 where P(k) is a plane rotation matrix defined by the 2-by-2 rotation
 
    R(k) = (  c(k)  s(k) )
         = ( -s(k)  c(k) ).
 
 When PIVOT = 'V' (Variable pivot), the rotation is performed
 for the plane (k,k+1), i.e., P(k) has the form
 
    P(k) = (  1                                            )
           (       ...                                     )
           (              1                                )
           (                   c(k)  s(k)                  )
           (                  -s(k)  c(k)                  )
           (                                1              )
           (                                     ...       )
           (                                            1  )
 
 where R(k) appears as a rank-2 modification to the identity matrix in
 rows and columns k and k+1.
 
 When PIVOT = 'T' (Top pivot), the rotation is performed for the
 plane (1,k+1), so P(k) has the form
 
    P(k) = (  c(k)                    s(k)                 )
           (         1                                     )
           (              ...                              )
           (                     1                         )
           ( -s(k)                    c(k)                 )
           (                                 1             )
           (                                      ...      )
           (                                             1 )
 
 where R(k) appears in rows and columns 1 and k+1.
 
 Similarly, when PIVOT = 'B' (Bottom pivot), the rotation is
 performed for the plane (k,z), giving P(k) the form
 
    P(k) = ( 1                                             )
           (      ...                                      )
           (             1                                 )
           (                  c(k)                    s(k) )
           (                         1                     )
           (                              ...              )
           (                                     1         )
           (                 -s(k)                    c(k) )
 
 where R(k) appears in rows and columns k and z.  The rotations are
 performed without ever forming P(k) explicitly.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>SIDE</i> </p>
<pre>
          SIDE is CHARACTER*1
          Specifies whether the plane rotation matrix P is applied to
          A on the left or the right.
          = 'L':  Left, compute A := P*A
          = 'R':  Right, compute A:= A*P**T
</pre>
<p> <i>PIVOT</i> </p>
<pre>
          PIVOT is CHARACTER*1
          Specifies the plane for which P(k) is a plane rotation
          matrix.
          = 'V':  Variable pivot, the plane (k,k+1)
          = 'T':  Top pivot, the plane (1,k+1)
          = 'B':  Bottom pivot, the plane (k,z)
</pre>
<p> <i>DIRECT</i> </p>
<pre>
          DIRECT is CHARACTER*1
          Specifies whether P is a forward or backward sequence of
          plane rotations.
          = 'F':  Forward, P = P(z-1)*...*<a href="//www.systutorials.com/docs/linux/man/2-P/">P</a>(2)*<a href="//www.systutorials.com/docs/linux/man/1-P/">P</a>(1)
          = 'B':  Backward, P = <a href="//www.systutorials.com/docs/linux/man/1-P/">P</a>(1)*<a href="//www.systutorials.com/docs/linux/man/2-P/">P</a>(2)*...*P(z-1)
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the matrix A.  If m &lt;= 1, an immediate
          return is effected.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrix A.  If n &lt;= 1, an
          immediate return is effected.
</pre>
<p> <i>C</i> </p>
<pre>
          C is REAL array, dimension
                  (M-1) if SIDE = 'L'
                  (N-1) if SIDE = 'R'
          The cosines c(k) of the plane rotations.
</pre>
<p> <i>S</i> </p>
<pre>
          S is REAL array, dimension
                  (M-1) if SIDE = 'L'
                  (N-1) if SIDE = 'R'
          The sines s(k) of the plane rotations.  The 2-by-2 plane
          rotation part of the matrix P(k), R(k), has the form
          R(k) = (  c(k)  s(k) )
                 ( -s(k)  c(k) ).
</pre>
<p> <i>A</i> </p>
<pre>
          A is REAL array, dimension (LDA,N)
          The M-by-N matrix A.  On exit, A is overwritten by P*A if
          SIDE = 'R' or by A*P**T if SIDE = 'L'.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,M).
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
<p> Definition at line 200 of file slasr.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
