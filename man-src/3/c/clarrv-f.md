---
title: "clarrv-f(3)"
name: "clarrv-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clarrv-f/"
description: "clarrv.f –"
---

<p>clarrv.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>clarrv</code> (N, VL, VU, D, L, PIVMIN, ISPLIT, M, DOL, DOU, MINRGP, RTOL1, RTOL2, W, WERR, WGAP, IBLOCK, INDEXW, GERS, Z, LDZ, ISUPPZ, WORK, IWORK, INFO)<br />
 <i></i><code>CLARRV</code> computes the eigenvectors of the tridiagonal matrix T = L D LT given L, D and the eigenvalues of L D LT.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clarrv (integerN, realVL, realVU, real, dimension( * )D, real, dimension( * )L, realPIVMIN, integer, dimension( * )ISPLIT, integerM, integerDOL, integerDOU, realMINRGP, realRTOL1, realRTOL2, real, dimension( * )W, real, dimension( * )WERR, real, dimension( * )WGAP, integer, dimension( * )IBLOCK, integer, dimension( * )INDEXW, real, dimension( * )GERS, complex, dimension( ldz, * )Z, integerLDZ, integer, dimension( * )ISUPPZ, real, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p><code>CLARRV</code> computes the eigenvectors of the tridiagonal matrix T = L D LT given L, D and the eigenvalues of L D LT. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CLARRV computes the eigenvectors of the tridiagonal matrix
 T = L D L**T given L, D and APPROXIMATIONS to the eigenvalues of L D L**T.
 The input eigenvalues should have been computed by SLARRE.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix. N &gt;= 0.</pre>
<p><i>VL</i> </p>
<pre> VL is REAL</pre>
<p><i>VU</i> </p>
<pre> VU is REAL
 Lower and upper bounds of the interval that contains the desired
 eigenvalues. VL &lt; VU. Needed to compute gaps on the left or right
 end of the extremal eigenvalues in the desired RANGE.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (N)
 On entry, the N diagonal elements of the diagonal matrix D.
 On exit, D may be overwritten.</pre>
<p><i>L</i> </p>
<pre> L is REAL array, dimension (N)
 On entry, the (N-1) subdiagonal elements of the unit
 bidiagonal matrix L are in elements 1 to N-1 of L
 (if the matrix is not splitted.) At the end of each block
 is stored the corresponding shift as given by SLARRE.
 On exit, L is overwritten.</pre>
<p><i>PIVMIN</i> </p>
<pre> PIVMIN is REAL
 The minimum pivot allowed in the Sturm sequence.</pre>
<p><i>ISPLIT</i> </p>
<pre> ISPLIT is INTEGER array, dimension (N)
 The splitting points, at which T breaks up into blocks.
 The first block consists of rows/columns 1 to
 ISPLIT( 1 ), the second of rows/columns ISPLIT( 1 )+1
 through ISPLIT( 2 ), etc.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The total number of input eigenvalues. 0 &lt;= M &lt;= N.</pre>
<p><i>DOL</i> </p>
<pre> DOL is INTEGER</pre>
<p><i>DOU</i> </p>
<pre> DOU is INTEGER
 If the user wants to compute only selected eigenvectors from all
 the eigenvalues supplied, he can specify an index range DOL:DOU.
 Or else the setting DOL=1, DOU=M should be applied.
 Note that DOL and DOU refer to the order in which the eigenvalues
 are stored in W.
 If the user wants to compute only selected eigenpairs, then
 the columns DOL-1 to DOU+1 of the eigenvector space Z contain the
 computed eigenvectors. All other columns of Z are set to zero.</pre>
<p><i>MINRGP</i> </p>
<pre> MINRGP is REAL</pre>
<p><i>RTOL1</i> </p>
<pre> RTOL1 is REAL</pre>
<p><i>RTOL2</i> </p>
<pre> RTOL2 is REAL
 Parameters for bisection.
 An interval [LEFT,RIGHT] has converged if
 RIGHT-LEFT.LT.MAX( RTOL1*GAP, RTOL2*MAX(|LEFT|,|RIGHT|) )</pre>
<p><i>W</i> </p>
<pre> W is REAL array, dimension (N)
 The first M elements of W contain the APPROXIMATE eigenvalues for
 which eigenvectors are to be computed. The eigenvalues
 should be grouped by split-off block and ordered from
 smallest to largest within the block ( The output array
 W from SLARRE is expected here ). Furthermore, they are with
 respect to the shift of the corresponding root representation
 for their block. On exit, W holds the eigenvalues of the
 UNshifted matrix.</pre>
<p><i>WERR</i> </p>
<pre> WERR is REAL array, dimension (N)
 The first M elements contain the semiwidth of the uncertainty
 interval of the corresponding eigenvalue in W</pre>
<p><i>WGAP</i> </p>
<pre> WGAP is REAL array, dimension (N)
 The separation from the right neighbor eigenvalue in W.</pre>
<p><i>IBLOCK</i> </p>
<pre> IBLOCK is INTEGER array, dimension (N)
 The indices of the blocks (submatrices) associated with the
 corresponding eigenvalues in W; IBLOCK(i)=1 if eigenvalue
 W(i) belongs to the first block from the top, =2 if W(i)
 belongs to the second block, etc.</pre>
<p><i>INDEXW</i> </p>
<pre> INDEXW is INTEGER array, dimension (N)
 The indices of the eigenvalues within each block (submatrix);
 for example, INDEXW(i)= 10 and IBLOCK(i)=2 imply that the
 i-th eigenvalue W(i) is the 10-th eigenvalue in the second block.</pre>
<p><i>GERS</i> </p>
<pre> GERS is REAL array, dimension (2*N)
 The N Gerschgorin intervals (the i-th Gerschgorin interval
 is (GERS(2*i-1), GERS(2*i)). The Gerschgorin intervals should
 be computed from the original UNshifted matrix.</pre>
<p><i>Z</i> </p>
<pre> Z is array, dimension (LDZ, max(1,M) )
 If INFO = 0, the first M columns of Z contain the
 orthonormal eigenvectors of the matrix T
 corresponding to the input eigenvalues, with the i-th
 column of Z holding the eigenvector associated with W(i).
 Note: the user must ensure that at least max(1,M) columns are
 supplied in the array Z.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= 1, and if
 JOBZ = 'V', LDZ &gt;= max(1,N).</pre>
<p><i>ISUPPZ</i> </p>
<pre> ISUPPZ is INTEGER array, dimension ( 2*max(1,M) )
 The support of the eigenvectors in Z, i.e., the indices
 indicating the nonzero elements in Z. The I-th eigenvector
 is nonzero only in elements ISUPPZ( 2*I-1 ) through
 ISUPPZ( 2*I ).</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (12*N)</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (7*N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &gt; 0: A problem occured in CLARRV.
 &lt; 0: One of the called subroutines signaled an internal problem.
 Needs inspection of the corresponding parameter IINFO
 for further information.
 =-1: Problem in SLARRB when refining a child's eigenvalues.
 =-2: Problem in SLARRF when computing the RRR of a child.
 When a child is inside a tight cluster, it can be difficult
 to find an RRR. A partial remedy from the user's point of
 view is to make the parameter MINRGP smaller and recompile.
 However, as the orthogonality of the computed vectors is
 proportional to 1/MINRGP, the user should be aware that
 he might be trading in precision when he decreases MINRGP.
 =-3: Problem in SLARRB when refining a single eigenvalue
 after the Rayleigh correction was rejected.
 = 5: The Rayleigh Quotient Iteration failed to converge to
 full accuracy in MAXITR steps.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>Beresford Parlett, University of California, Berkeley, USA </p>
<p>&nbsp;<wbr>Jim Demmel, University of California, Berkeley, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Inderjit Dhillon, University of Texas, Austin, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Osni Marques, LBNL/NERSC, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr>Christof Voemel, University of California, Berkeley, USA&nbsp;<wbr></dl>
<p> Definition at line 280 of file clarrv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
