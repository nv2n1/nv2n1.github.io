---
title: "dlaebz-f(3)"
name: "dlaebz-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlaebz-f/"
description: "dlaebz.f –"
---

<p>dlaebz.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlaebz</code> (IJOB, NITMAX, N, MMAX, MINP, NBMIN, ABSTOL, RELTOL, PIVMIN, D, E, E2, NVAL, AB, C, MOUT, NAB, WORK, IWORK, INFO)<br />
 <i></i><code>DLAEBZ</code> computes the number of eigenvalues of a real symmetric tridiagonal matrix which are less than or equal to a given value, and performs other tasks required by the routine sstebz.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlaebz (integerIJOB, integerNITMAX, integerN, integerMMAX, integerMINP, integerNBMIN, double precisionABSTOL, double precisionRELTOL, double precisionPIVMIN, double precision, dimension( * )D, double precision, dimension( * )E, double precision, dimension( * )E2, integer, dimension( * )NVAL, double precision, dimension( mmax, * )AB, double precision, dimension( * )C, integerMOUT, integer, dimension( mmax, * )NAB, double precision, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p><code>DLAEBZ</code> computes the number of eigenvalues of a real symmetric tridiagonal matrix which are less than or equal to a given value, and performs other tasks required by the routine sstebz. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLAEBZ contains the iteration loops which compute and use the
 function N(w), which is the count of eigenvalues of a symmetric
 tridiagonal matrix T less than or equal to its argument w. It
 performs a choice of two types of loops:
 IJOB=1, followed by
 IJOB=2: It takes as input a list of intervals and returns a list of
 sufficiently small intervals whose union contains the same
 eigenvalues as the union of the original intervals.
 The input intervals are (AB(j,1),AB(j,2)], j=1,...,MINP.
 The output interval (AB(j,1),AB(j,2)] will contain
 eigenvalues NAB(j,1)+1,...,NAB(j,2), where 1 &lt;= j &lt;= MOUT.
 IJOB=3: It performs a binary search in each input interval
 (AB(j,1),AB(j,2)] for a point w(j) such that
 N(w(j))=NVAL(j), and uses C(j) as the starting point of
 the search. If such a w(j) is found, then on output
 AB(j,1)=AB(j,2)=w. If no such w(j) is found, then on output
 (AB(j,1),AB(j,2)] will be a small interval containing the
 point where N(w) jumps through NVAL(j), unless that point
 lies outside the initial interval.
 Note that the intervals are in all cases half-open intervals,
 i.e., of the form (a,b] , which includes b but not a .
 To avoid underflow, the matrix should be scaled so that its largest
 element is no greater than overflow**(1/2) * underflow**(1/4)
 in absolute value. To assure the most accurate computation
 of small eigenvalues, the matrix should be scaled to be
 not much smaller than that, either.
 See W. Kahan &quot;Accurate Eigenvalues of a Symmetric Tridiagonal
 Matrix&quot;, Report CS41, Computer Science Dept., Stanford
 University, July 21, 1966
 Note: the arguments are, in general, *not* checked for unreasonable
 values.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>IJOB</i> </p>
<pre> IJOB is INTEGER
 Specifies what is to be done:
 = 1: Compute NAB for the initial intervals.
 = 2: Perform bisection iteration to find eigenvalues of T.
 = 3: Perform bisection iteration to invert N(w), i.e.,
 to find a point which has a specified number of
 eigenvalues of T to its left.
 Other values will cause DLAEBZ to return with INFO=-1.</pre>
<p><i>NITMAX</i> </p>
<pre> NITMAX is INTEGER
 The maximum number of &quot;levels&quot; of bisection to be
 performed, i.e., an interval of width W will not be made
 smaller than 2^(-NITMAX) * W. If not all intervals
 have converged after NITMAX iterations, then INFO is set
 to the number of non-converged intervals.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The dimension n of the tridiagonal matrix T. It must be at
 least 1.</pre>
<p><i>MMAX</i> </p>
<pre> MMAX is INTEGER
 The maximum number of intervals. If more than MMAX intervals
 are generated, then DLAEBZ will quit with INFO=MMAX+1.</pre>
<p><i>MINP</i> </p>
<pre> MINP is INTEGER
 The initial number of intervals. It may not be greater than
 MMAX.</pre>
<p><i>NBMIN</i> </p>
<pre> NBMIN is INTEGER
 The smallest number of intervals that should be processed
 using a vector loop. If zero, then only the scalar loop
 will be used.</pre>
<p><i>ABSTOL</i> </p>
<pre> ABSTOL is DOUBLE PRECISION
 The minimum (absolute) width of an interval. When an
 interval is narrower than ABSTOL, or than RELTOL times the
 larger (in magnitude) endpoint, then it is considered to be
 sufficiently small, i.e., converged. This must be at least
 zero.</pre>
<p><i>RELTOL</i> </p>
<pre> RELTOL is DOUBLE PRECISION
 The minimum relative width of an interval. When an interval
 is narrower than ABSTOL, or than RELTOL times the larger (in
 magnitude) endpoint, then it is considered to be
 sufficiently small, i.e., converged. Note: this should
 always be at least radix*machine epsilon.</pre>
<p><i>PIVMIN</i> </p>
<pre> PIVMIN is DOUBLE PRECISION
 The minimum absolute value of a &quot;pivot&quot; in the Sturm
 sequence loop.
 This must be at least max |e(j)**2|*safe_min and at
 least safe_min, where safe_min is at least
 the smallest number that can divide one without overflow.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 The diagonal elements of the tridiagonal matrix T.</pre>
<p><i>E</i> </p>
<pre> E is DOUBLE PRECISION array, dimension (N)
 The offdiagonal elements of the tridiagonal matrix T in
 positions 1 through N-1. E(N) is arbitrary.</pre>
<p><i>E2</i> </p>
<pre> E2 is DOUBLE PRECISION array, dimension (N)
 The squares of the offdiagonal elements of the tridiagonal
 matrix T. E2(N) is ignored.</pre>
<p><i>NVAL</i> </p>
<pre> NVAL is INTEGER array, dimension (MINP)
 If IJOB=1 or 2, not referenced.
 If IJOB=3, the desired values of N(w). The elements of NVAL
 will be reordered to correspond with the intervals in AB.
 Thus, NVAL(j) on output will not, in general be the same as
 NVAL(j) on input, but it will correspond with the interval
 (AB(j,1),AB(j,2)] on output.</pre>
<p><i>AB</i> </p>
<pre> AB is DOUBLE PRECISION array, dimension (MMAX,2)
 The endpoints of the intervals. AB(j,1) is a(j), the left
 endpoint of the j-th interval, and AB(j,2) is b(j), the
 right endpoint of the j-th interval. The input intervals
 will, in general, be modified, split, and reordered by the
 calculation.</pre>
<p><i>C</i> </p>
<pre> C is DOUBLE PRECISION array, dimension (MMAX)
 If IJOB=1, ignored.
 If IJOB=2, workspace.
 If IJOB=3, then on input C(j) should be initialized to the
 first search point in the binary search.</pre>
<p><i>MOUT</i> </p>
<pre> MOUT is INTEGER
 If IJOB=1, the number of eigenvalues in the intervals.
 If IJOB=2 or 3, the number of intervals output.
 If IJOB=3, MOUT will equal MINP.</pre>
<p><i>NAB</i> </p>
<pre> NAB is INTEGER array, dimension (MMAX,2)
 If IJOB=1, then on output NAB(i,j) will be set to N(AB(i,j)).
 If IJOB=2, then on input, NAB(i,j) should be set. It must
 satisfy the condition:
 N(AB(i,1)) &lt;= NAB(i,1) &lt;= NAB(i,2) &lt;= N(AB(i,2)),
 which means that in interval i only eigenvalues
 NAB(i,1)+1,...,NAB(i,2) will be considered. Usually,
 NAB(i,j)=N(AB(i,j)), from a previous call to DLAEBZ with
 IJOB=1.
 On output, NAB(i,j) will contain
 max(na(k),min(nb(k),N(AB(i,j)))), where k is the index of
 the input interval that the output interval
 (AB(j,1),AB(j,2)] came from, and na(k) and nb(k) are the
 the input values of NAB(k,1) and NAB(k,2).
 If IJOB=3, then on output, NAB(i,j) contains N(AB(i,j)),
 unless N(w) &gt; NVAL(i) for all search points w , in which
 case NAB(i,1) will not be modified, i.e., the output
 value will be the same as the input value (modulo
 reorderings -- see NVAL and AB), or unless N(w) &lt; NVAL(i)
 for all search points w , in which case NAB(i,2) will
 not be modified. Normally, NAB should be set to some
 distinctive value(s) before DLAEBZ is called.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (MMAX)
 Workspace.</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (MMAX)
 Workspace.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: All intervals converged.
 = 1--MMAX: The last INFO intervals did not converge.
 = MMAX+1: More than MMAX intervals were generated.</pre>
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
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> This routine is intended to be called only by other LAPACK
 routines, thus the interface is less user-friendly. It is intended
 for two purposes:
 (a) finding eigenvalues. In this case, DLAEBZ should have one or
 more initial intervals set up in AB, and DLAEBZ should be called
 with IJOB=1. This sets up NAB, and also counts the eigenvalues.
 Intervals with no eigenvalues would usually be thrown out at
 this point. Also, if not all the eigenvalues in an interval i
 are desired, NAB(i,1) can be increased or NAB(i,2) decreased.
 For example, set NAB(i,1)=NAB(i,2)-1 to get the largest
 eigenvalue. DLAEBZ is then called with IJOB=2 and MMAX
 no smaller than the value of MOUT returned by the call with
 IJOB=1. After this (IJOB=2) call, eigenvalues NAB(i,1)+1
 through NAB(i,2) are approximately AB(i,1) (or AB(i,2)) to the
 tolerance specified by ABSTOL and RELTOL.
 (b) finding an interval (a',b'] containing eigenvalues w(f),...,<a href="//www.systutorials.com/docs/linux/man/l-w/">w</a>(l).
 In this case, start with a Gershgorin interval (a,b). Set up
 AB to contain 2 search intervals, both initially (a,b). One
 NVAL element should contain f-1 and the other should contain l
 , while C should contain a and b, resp. NAB(i,1) should be -1
 and NAB(i,2) should be N+1, to flag an error if the desired
 interval does not lie in (a,b). DLAEBZ is then called with
 IJOB=3. On exit, if w(f-1) &lt; w(f), then one of the intervals --
 j -- will have AB(j,1)=AB(j,2) and NAB(j,1)=NAB(j,2)=f-1, while
 if, to the specified tolerance, w(f-k)=...=w(f+r), k &gt; 0 and r
 &gt;= 0, then the interval will have N(AB(j,1))=NAB(j,1)=f-k and
 N(AB(j,2))=NAB(j,2)=f+r. The cases <a href="//www.systutorials.com/docs/linux/man/l-w/">w</a>(l) &lt; w(l+1) and
 w(l-r)=...=w(l+k) are handled similarly.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 318 of file dlaebz.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
