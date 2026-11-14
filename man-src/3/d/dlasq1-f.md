---
title: "dlasq1-f(3)"
name: "dlasq1-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlasq1-f/"
---

dlasq1.f - 

<h2>Synopsis</h2><h3>Functions/Subroutines</h3>subroutine <b>dlasq1</b> (N, D, E, WORK, INFO) 
 <i></i><b>DLASQ1</b> computes the singular values of a real square bidiagonal matrix. Used by sbdsqr.
<h2>Function/Subroutine Documentation</h2><h3>subroutine dlasq1 (integerN, double precision, dimension( * )D, double precision, dimension( * )E, double precision, dimension( * )WORK, integerINFO)</h3><b>DLASQ1</b> computes the singular values of a real square bidiagonal matrix. Used by sbdsqr. 

 <b>Purpose: </b>
<dl COMPACT><dd><pre> DLASQ1 computes the singular values of a real N-by-N bidiagonal
 matrix with diagonal D and off-diagonal E. The singular values
 are computed to high relative accuracy, in the absence of
 denormalization, underflow and overflow. The algorithm was first
 presented in
 &quot;Accurate singular values and differential qd algorithms&quot; by K. V.
 Fernando and B. N. Parlett, Numer. Math., Vol-67, No. 2, pp. 191-230,
 1994,
 and the present implementation is described in &quot;An implementation of
 the dqds Algorithm (Positive Case)&quot;, LAPACK Working Note.</pre>&nbsp;<wbr></dl>
 

 <b>Parameters:</b>
<dl COMPACT><dd><i>N</i> 

 <pre> N is INTEGER
 The number of rows and columns in the matrix. N &gt;= 0.</pre><i>D</i> 

 <pre> D is DOUBLE PRECISION array, dimension (N)
 On entry, D contains the diagonal elements of the
 bidiagonal matrix whose SVD is desired. On normal exit,
 D contains the singular values in decreasing order.</pre><i>E</i> 

 <pre> E is DOUBLE PRECISION array, dimension (N)
 On entry, elements E(1:N-1) contain the off-diagonal elements
 of the bidiagonal matrix whose SVD is desired.
 On exit, E is overwritten.</pre><i>WORK</i> 

 <pre> WORK is DOUBLE PRECISION array, dimension (4*N)</pre><i>INFO</i> 

 <pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: the algorithm failed
 = 1, a split was marked by a positive value in E
 = 2, current block of Z not diagonalized after 100*N
 iterations (in inner while loop) On exit D and E
 represent a matrix with the same singular values
 which the calling subroutine could use to finish the
 computation, or even feed back into DLASQ1
 = 3, termination criterion of outer while loop not met 
 (program created more than N unreduced blocks)</pre>&nbsp;<wbr></dl>
 

 <b>Author:</b>
<dl COMPACT><dd>Univ. of Tennessee 

 Univ. of California Berkeley 

 Univ. of Colorado Denver 

 NAG Ltd.</dl>
 

 <b>Date:</b>
<dl COMPACT><dd>September 2012</dl>
 

 

 

 Definition at line 109 of file dlasq1.f.
<h2>Author</h2>Generated automatically by Doxygen for LAPACK from the source code.
