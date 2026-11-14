---
title: "cgesdd(3)"
name: "cgesdd"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgesdd/"
description: "cgesdd.f –"
---

<h2 class="name">NAME</h2>
<p> cgesdd.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cgesdd</code> (JOBZ, M, N, A, LDA, S, U, LDU, VT, LDVT, WORK, LWORK, RWORK, IWORK, INFO)<br />
 <i></i><code>CGESDD</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgesdd (characterJOBZ, integerM, integerN, complex, dimension( lda, * )A, integerLDA, real, dimension( * )S, complex, dimension( ldu, * )U, integerLDU, complex, dimension( ldvt, * )VT, integerLDVT, complex, dimension( * )WORK, integerLWORK, real, dimension( * )RWORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>CGESDD</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CGESDD computes the singular value decomposition (SVD) of a complex
 M-by-N matrix A, optionally computing the left and/or right singular
 vectors, by using divide-and-conquer method. The SVD is written
      A = U * SIGMA * conjugate-transpose(V)
 where SIGMA is an M-by-N matrix which is zero except for its
 min(m,n) diagonal elements, U is an M-by-M unitary matrix, and
 V is an N-by-N unitary matrix.  The diagonal elements of SIGMA
 are the singular values of A; they are real and non-negative, and
 are returned in descending order.  The first min(m,n) columns of
 U and V are the left and right singular vectors of A.
 Note that the routine returns VT = V**H, not V.
 The divide and conquer algorithm makes very mild assumptions about
 floating point arithmetic. It will work on machines with a guard
 digit in add/subtract, or on those binary machines without guard
 digits which subtract like the Cray X-MP, Cray Y-MP, Cray C-90, or
 Cray-2. It could conceivably fail on hexadecimal or decimal machines
 without guard digits, but we know of none.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>JOBZ</i> </p>
<pre><code>
          JOBZ is CHARACTER*1
          Specifies options for computing all or part of the matrix U:
          = 'A':  all M columns of U and all N rows of V**H are
                  returned in the arrays U and VT;
          = 'S' : the first min(M, N)
          columns of U and the first
          min(M, N)
          rows of V **H are returned in the arrays U
              and VT;
          = 'O' : If M &gt;= N, the first N columns of U are overwritten
                                 in the array A and all rows of V **H are returned in
                                     the array VT;
          otherwise, all columns of U are returned in the
                         array U and the first M rows of V **H are overwritten
                             in the array A;
          = 'N' : no columns of U or rows of V * *H are computed.
</code></pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the input matrix A.  M &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the input matrix A.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
          On entry, the M-by-N matrix A.
          On exit,
          if JOBZ = 'O',  A is overwritten with the first N columns
                          of U (the left singular vectors, stored
                          columnwise) if M &gt;= N;
                          A is overwritten with the first M rows
                          of V**H (the right singular vectors, stored
                          rowwise) otherwise.
          if JOBZ .ne. 'O', the contents of A are destroyed.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,M).
</pre>
<p> <i>S</i> </p>
<pre>
          S is REAL array, dimension (min(M,N))
          The singular values of A, sorted so that S(i) &gt;= S(i+1).
</pre>
<p> <i>U</i> </p>
<p>U is COMPLEX array, dimension(LDU, UCOL)<br />
                        UCOL = M if JOBZ = &#8216;A&#8217; or JOBZ = &#8216;O&#8217; and M &lt; N;<br />
UCOL = min(M, N) if JOBZ = &#8216;S&#8217;.If JOBZ = &#8216;A&#8217; or JOBZ = &#8216;O&#8217; and M &lt; N, U contains the M &#8211; by &#8211; M unitary matrix U;<br />
if JOBZ<br />
    = &#8216;S&#8217;, U contains the first min(M, N) columns of U(the left singular vectors, stored columnwise);<br />
if JOBZ<br />
= &#8216;O&#8217; and M &gt;= N, or JOBZ = &#8216;N&#8217;, U is not referenced.</p>
<p> <i>LDU</i> </p>
<p>LDU is INTEGER<br />
        The leading dimension of the array U.LDU &gt;= 1;<br />
if JOBZ<br />
= &#8216;S&#8217; or &#8216;A&#8217; or JOBZ = &#8216;O&#8217; and M &lt; N, LDU &gt;= M.</p>
<p> <i>VT</i> </p>
<p>VT is COMPLEX array, dimension(LDVT, N) If JOBZ = &#8216;A&#8217; or JOBZ = &#8216;O&#8217; and M &gt;= N, VT contains the N &#8211; by &#8211; N unitary matrix V **H;<br />
if JOBZ<br />
    = &#8216;S&#8217;, VT contains the first min(M, N) rows of<br />
        V **H(the right singular vectors, stored rowwise);<br />
if JOBZ<br />
= &#8216;O&#8217; and M &lt; N, or JOBZ = &#8216;N&#8217;, VT is not referenced.</p>
<p> <i>LDVT</i> </p>
<p>LDVT is INTEGER<br />
        The leading dimension of the array VT.LDVT &gt;= 1;<br />
if JOBZ<br />
    = &#8216;A&#8217; or JOBZ = &#8216;O&#8217; and M &gt;= N, LDVT &gt;= N;<br />
if JOBZ<br />
= &#8216;S&#8217;, LDVT &gt;= min(M, N).</p>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre><code>
          LWORK is INTEGER
          The dimension of the array WORK. LWORK &gt;= 1.
          if JOBZ = 'N', LWORK &gt;= 2*min(M,N)+max(M,N).
          if JOBZ = 'O',
                LWORK &gt;= 2*min(M,N)*min(M,N)+2*min(M,N)+max(M,N).
          if JOBZ = 'S' or 'A',
                LWORK &gt;= min(M,N)*min(M,N)+2*min(M,N)+max(M,N).
          For good performance, LWORK should generally be larger.
          If LWORK = -1, a workspace query is assumed.  The optimal
          size for the WORK array is calculated and stored in WORK(1),
          and no other work except argument checking is performed.
</code></pre>
<p> <i>RWORK</i> </p>
<pre>
          RWORK is REAL array, dimension (MAX(1,LRWORK))
          If JOBZ = 'N', LRWORK &gt;= 5*min(M,N).
          Otherwise, 
          LRWORK &gt;= min(M,N)*max(5*min(M,N)+7,2*max(M,N)+2*min(M,N)+1)
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (8*min(M,N))
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit.
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
          &gt; 0:  The updating process of SBDSDC did not converge.
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
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Ming Gu and Huan Ren, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 222 of file cgesdd.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
