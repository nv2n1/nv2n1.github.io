---
title: "cggrqf(3)"
name: "cggrqf"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cggrqf/"
description: "cggrqf.f –"
---

<h2 class="name">NAME</h2>
<p> cggrqf.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cggrqf</code> (M, P, N, A, LDA, TAUA, B, LDB, TAUB, WORK, LWORK, INFO)<br />
 <i></i><code>CGGRQF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cggrqf (integerM, integerP, integerN, complex, dimension( lda, * )A, integerLDA, complex, dimension( * )TAUA, complex, dimension( ldb, * )B, integerLDB, complex, dimension( * )TAUB, complex, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p> <code>CGGRQF</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
CGGRQF computes a generalized RQ factorization of an M - by - N matrix A and a P - by - N matrix B : A = R * Q, B = Z * T * Q,
                                                                                                     where Q is an N - by - N unitary matrix, Z is a P - by - P unitary matrix, and R and T assume one of the forms : if M &lt;= N, R = (0 R12)M, or if M &gt; N, R = (R11)M - N,
                                                                                                     N - M M(R21)
N
        N
            where R12 or
    R21 is upper triangular,
    and if P &gt;= N, T = (T11)N, or if P &lt; N, T = (T11 T12)P,
                   (0)P - N P N - P N where T11 is upper triangular.In particular, if B is square and nonsingular, the GRQ factorization of A and B implicitly gives the RQ factorization of A *inv(B)
    : A * inv(B) = (R * inv(T)) * Z * *H where inv(B)
denotes the inverse of the matrix B, and Z **H denotes the
                                             conjugate transpose of the matrix Z.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the matrix A.  M &gt;= 0.
</pre>
<p> <i>P</i> </p>
<pre>
          P is INTEGER
          The number of rows of the matrix B.  P &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrices A and B. N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<p>A is COMPLEX array, dimension(LDA, N) On entry, the M &#8211; by &#8211; N matrix A.On exit, if M &lt;= N, the upper triangle of the subarray A(1<br />
                                                                                                                                 : M, N &#8211; M + 1<br />
                                                                                                                                 : N) contains the M<br />
                                                                                                &#8211; by &#8211; M upper triangular matrix R;<br />
if M<br />
    &gt; N, the elements on and above the(M &#8211; N) &#8211; th subdiagonal contain the M &#8211; by &#8211; N upper trapezoidal matrix R;<br />
the remaining<br />
    elements,<br />
    with the array TAUA, represent the unitary matrix Q as a product of elementary reflectors(see Further Details).</p>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A. LDA &gt;= max(1,M).
</pre>
<p> <i>TAUA</i> </p>
<pre>
          TAUA is COMPLEX array, dimension (min(M,N))
          The scalar factors of the elementary reflectors which
          represent the unitary matrix Q (see Further Details).
</pre>
<p> <i>B</i> </p>
<pre>
          B is COMPLEX array, dimension (LDB,N)
          On entry, the P-by-N matrix B.
          On exit, the elements on and above the diagonal of the array
          contain the min(P,N)-by-N upper trapezoidal matrix T (T is
          upper triangular if P &gt;= N); the elements below the diagonal,
          with the array TAUB, represent the unitary matrix Z as a
          product of elementary reflectors (see Further Details).
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B. LDB &gt;= max(1,P).
</pre>
<p> <i>TAUB</i> </p>
<pre>
          TAUB is COMPLEX array, dimension (min(P,N))
          The scalar factors of the elementary reflectors which
          represent the unitary matrix Z (see Further Details).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<p>          LWORK is INTEGER<br />
          The dimension of the array WORK. LWORK &gt;= max(1,N,M,P).<br />
          For optimum performance LWORK &gt;= max(N,M,P)*max(NB1,NB2,NB3),<br />
          where NB1 is the optimal blocksize for the RQ factorization<br />
          of an M-by-N matrix, NB2 is the optimal blocksize for the<br />
          QR factorization of a P-by-N matrix, and NB3 is the optimal<br />
          blocksize for a call of CUNMRQ.<br />
          If LWORK = -1, then a workspace query is assumed;<br />
          the routine<br />
              only calculates the optimal size of the WORK array,<br />
              returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.</p>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO=-i, the i-th argument had an illegal value.
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
<pre><code>
The matrix Q is represented as a product of elementary reflectors
    Q = H(1) H(2)...H(k),
    where k = min(m, n).Each H(i)
has the form
    H(i) = I - taua * v * v * *H where taua is a complex scalar,
    and v is a complex vector with
    v(n - k + i + 1
      : n) = 0 and v(n - k + i) = 1;
v(1
  : n - k + i - 1) is stored on exit in
    A(m - k + i, 1
      : n - k + i - 1),
    and taua in TAUA(i).To form Q explicitly, use LAPACK subroutine CUNGRQ.To use Q to update another matrix, use LAPACK subroutine CUNMRQ.The matrix Z is represented as a product of elementary reflectors Z = H(1) H(2)...H(k), where k = min(p, n).Each H(i)
has the form
    H(i) = I - taub * v * v * *H where taub is a complex scalar,
    and v is a complex vector with
    v(1
      : i - 1) = 0 and v(i) = 1;
v(i + 1
  : p) is stored on exit in B(i + 1
                              : p, i),
    and taub in TAUB(i).To form Z explicitly, use LAPACK subroutine CUNGQR.To use Z to update another matrix, use LAPACK subroutine CUNMQR.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 214 of file cggrqf.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
