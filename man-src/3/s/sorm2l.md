---
title: "sorm2l(3)"
name: "sorm2l"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sorm2l/"
---

<h2 class="name">NAME</h2>
 

 sorm2l.f - 

<h2>SYNOPSIS</h2>

 
 

<h3>Functions/Subroutines</h3>

 

 
 subroutine <b>sorm2l</b> (SIDE, TRANS, M, N, K, A, LDA, TAU, C, LDC, WORK, INFO) 
 <i></i><b>SORM2L</b> multiplies a general matrix by the orthogonal matrix from a QL factorization determined by sgeqlf (unblocked algorithm).

<h2>Function/Subroutine Documentation</h2>

 

<h3>subroutine sorm2l (characterSIDE, characterTRANS, integerM, integerN, integerK, real, dimension( lda, * )A, integerLDA, real, dimension( * )TAU, real, dimension( ldc, * )C, integerLDC, real, dimension( * )WORK, integerINFO)</h3>

 

 

 <b>SORM2L</b> multiplies a general matrix by the orthogonal matrix from a QL factorization determined by sgeqlf (unblocked algorithm). 

 <b>Purpose: </b>
<dl>
<dt>
<dd> 

 

 <pre><code>
SORM2L overwrites the general real m by n matrix C with
    Q *C if SIDE = 'L' and TRANS = 'N',
            or
                Q **T *C if SIDE = 'L' and TRANS = 'T',
            or
                C *Q if SIDE = 'R' and TRANS = 'N',
            or
                C *Q **T if SIDE = 'R' and TRANS = 'T',
            where Q is a real orthogonal matrix defined as the product of k
                elementary reflectors
                    Q = H(k)...H(2) H(1)
                            as returned by SGEQLF.Q is of order m if SIDE = 'L' and of order n if SIDE = 'R'.
</code></pre> 

 
&nbsp;<wbr></dl>
 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>SIDE</i> 

 <pre>
          SIDE is CHARACTER*1
          = 'L': apply Q or Q**T from the Left
          = 'R': apply Q or Q**T from the Right
</pre> 

 
 <i>TRANS</i> 

 <pre>
          TRANS is CHARACTER*1
          = 'N': apply Q  (No transpose)
          = 'T': apply Q**T (Transpose)
</pre> 

 
 <i>M</i> 

 <pre>
          M is INTEGER
          The number of rows of the matrix C. M &gt;= 0.
</pre> 

 
 <i>N</i> 

 <pre>
          N is INTEGER
          The number of columns of the matrix C. N &gt;= 0.
</pre> 

 
 <i>K</i> 

 
K is INTEGER
    The number of elementary reflectors whose product defines
        the matrix Q.If SIDE = 'L',
                        M &gt;= K &gt;= 0;
if SIDE
= 'R', N &gt;= K &gt;= 0.
 

 
 <i>A</i> 

 <pre>
          A is REAL array, dimension (LDA,K)
          The i-th column must contain the vector which defines the
          elementary reflector H(i), for i = 1,2,...,k, as returned by
          SGEQLF in the last k columns of its array argument A.
          A is modified by the routine but restored on exit.
</pre> 

 
 <i>LDA</i> 

 <pre><code>
LDA is INTEGER
    The leading dimension of the array A.If SIDE = 'L',
                                            LDA &gt;= max(1, M);
if SIDE
= 'R', LDA &gt;= max(1, N).
</code></pre> 

 
 <i>TAU</i> 

 <pre>
          TAU is REAL array, dimension (K)
          TAU(i) must contain the scalar factor of the elementary
          reflector H(i), as returned by SGEQLF.
</pre> 

 
 <i>C</i> 

 <pre>
          C is REAL array, dimension (LDC,N)
          On entry, the m by n matrix C.
          On exit, C is overwritten by Q*C or Q**T*C or C*Q**T or C*Q.
</pre> 

 
 <i>LDC</i> 

 <pre>
          LDC is INTEGER
          The leading dimension of the array C. LDC &gt;= max(1,M).
</pre> 

 
 <i>WORK</i> 

 <pre>
          WORK is REAL array, dimension
                                   (N) if SIDE = 'L',
                                   (M) if SIDE = 'R'
</pre> 

 
 <i>INFO</i> 

 <pre>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -i, the i-th argument had an illegal value
</pre> 

 
&nbsp;<wbr></dl>
 

 <b>Author:</b>
<dl>
<dt>
<dd> Univ. of Tennessee 

 Univ. of California Berkeley 

 Univ. of Colorado Denver 

 NAG Ltd.</dl>
 

 <b>Date:</b>
<dl>
<dt>
<dd> September 2012</dl>
 

 

 

 Definition at line 159 of file sorm2l.f.

<h2>Author</h2>

 

 Generated automatically by Doxygen for LAPACK from the source code. 

<h2>Index</h2>


