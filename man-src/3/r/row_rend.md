---
title: "row_rend(3)"
name: "row_rend"
section: "3"
letter: "r"
url: "/docs/linux/man/3-row_rend/"
description: "QuantLib::Matrix – Matrix used in linear algebra."
---

<p>QuantLib::Matrix &#8211; Matrix used in linear algebra. </p>
<h2>Synopsis</h2>
<pre><code>const Matrix &amp; operator+= (const Matrix &amp;)



const Matrix &amp; operator-= (const Matrix &amp;)



const Matrix &amp; operator*= (Real)



const Matrix &amp; operator/= (Real)</code></pre>
<p> Inherited by <code>Disposable&lt; Matrix &gt;</code>.</p>
<h3>Public Types</h3>
<p>typedef Real * <code>iterator</code> </p>
<p> typedef const Real * <code>const_iterator</code> </p>
<p> typedef boost::reverse_iterator&lt; iterator &gt; <code>reverse_iterator</code> </p>
<p> typedef boost::reverse_iterator&lt; const_iterator &gt; <code>const_reverse_iterator</code> </p>
<p> typedef Real * <code>row_iterator</code> </p>
<p> typedef const Real * <code>const_row_iterator</code> </p>
<p> typedef boost::reverse_iterator&lt; row_iterator &gt; <code>reverse_row_iterator</code> </p>
<p> typedef boost::reverse_iterator&lt; const_row_iterator &gt; <code>const_reverse_row_iterator</code> </p>
<p> typedef <code>step_iterator</code>&lt; iterator &gt; <code>column_iterator</code> </p>
<p> typedef <code>step_iterator</code>&lt; const_iterator &gt; <code>const_column_iterator</code> </p>
<p> typedef boost::reverse_iterator&lt; <code>column_iterator</code> &gt; <code>reverse_column_iterator</code> </p>
<p> typedef boost::reverse_iterator&lt; <code>const_column_iterator</code> &gt; <code>const_reverse_column_iterator</code></p>
<h3>Public Member Functions</h3>
<p><code>Constructors, destructor, and assignment</code><br />
 const Matrix &amp; operator+= (const Matrix &amp;)</p>
<p>const Matrix &amp; operator-= (const Matrix &amp;)</p>
<p>const Matrix &amp; operator*= (Real)</p>
<p>const Matrix &amp; operator/= (Real) <code>Algebraic operators</code> </p>
<pre><code>const Matrix &amp; operator+= (const Matrix &amp;)



const Matrix &amp; operator-= (const Matrix &amp;)



const Matrix &amp; operator*= (Real)



const Matrix &amp; operator/= (Real)</code></pre>
<p> <code>Iterator access</code> </p>
<p> const_iterator <code>begin</code> () const </p>
<p> iterator <code>begin</code> () </p>
<p> const_iterator <code>end</code> () const </p>
<p> iterator <code>end</code> () </p>
<p> const_reverse_iterator <code>rbegin</code> () const </p>
<p> reverse_iterator <code>rbegin</code> () </p>
<p> const_reverse_iterator <code>rend</code> () const </p>
<p> reverse_iterator <code>rend</code> () </p>
<p> const_row_iterator <code>row_begin</code> (Size i) const </p>
<p> row_iterator <code>row_begin</code> (Size i) </p>
<p> const_row_iterator <code>row_end</code> (Size i) const </p>
<p> row_iterator <code>row_end</code> (Size i) </p>
<p> const_reverse_row_iterator <code>row_rbegin</code> (Size i) const </p>
<p> reverse_row_iterator <code>row_rbegin</code> (Size i) </p>
<p> const_reverse_row_iterator <code>row_rend</code> (Size i) const </p>
<p> reverse_row_iterator <code>row_rend</code> (Size i) </p>
<p> <code>const_column_iterator</code> <code>column_begin</code> (Size i) const </p>
<p> <code>column_iterator</code> <code>column_begin</code> (Size i) </p>
<p> <code>const_column_iterator</code> <code>column_end</code> (Size i) const </p>
<p> <code>column_iterator</code> <code>column_end</code> (Size i) </p>
<p> const_reverse_column_iterator <code>column_rbegin</code> (Size i) const </p>
<p> reverse_column_iterator <code>column_rbegin</code> (Size i) </p>
<p> const_reverse_column_iterator <code>column_rend</code> (Size i) const </p>
<p> reverse_column_iterator <code>column_rend</code> (Size i)<br />
 <code>Element access</code> </p>
<p> const_row_iterator <code>operator[]</code> (Size) const </p>
<p> const_row_iterator <code>at</code> (Size) const </p>
<p> row_iterator <code>operator[]</code> (Size) </p>
<p> row_iterator <code>at</code> (Size) </p>
<p> <code>Disposable</code>&lt; <code>Array</code> &gt; <code>diagonal</code> (void) const<br />
 <code>Inspectors</code> </p>
<p> Size <code>rows</code> () const </p>
<p> Size <code>columns</code> () const </p>
<p> bool <code>empty</code> () const<br />
 <code>Utilities</code> </p>
<p> void <code>swap</code> (<code>Matrix</code> &amp;)</p>
<h3>Related Functions</h3>
<p>(Note that these are not member functions.)<br />
 const <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>operator+</code> (const <code>Matrix</code> &amp;, const <code>Matrix</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>operator-</code> (const <code>Matrix</code> &amp;, const <code>Matrix</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>operator*</code> (const <code>Matrix</code> &amp;, Real) </p>
<p> const <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>operator*</code> (Real, const <code>Matrix</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>operator/</code> (const <code>Matrix</code> &amp;, Real) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>operator*</code> (const <code>Array</code> &amp;, const <code>Matrix</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Array</code> &gt; <code>operator*</code> (const <code>Matrix</code> &amp;, const <code>Array</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>operator*</code> (const <code>Matrix</code> &amp;, const <code>Matrix</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>transpose</code> (const <code>Matrix</code> &amp;) </p>
<p> const <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>outerProduct</code> (const <code>Array</code> &amp;v1, const <code>Array</code> &amp;v2) </p>
<p> template&lt;class Iterator1 , class Iterator2 &gt; const <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>outerProduct</code> (Iterator1 v1begin, Iterator1 v1end, Iterator2 v2begin, Iterator2 v2end) </p>
<p> void <code>swap</code> (<code>Matrix</code> &amp;, <code>Matrix</code> &amp;) </p>
<p> std::ostream &amp; <code>operator&lt;&lt;</code> (std::ostream &amp;, const <code>Matrix</code> &amp;) </p>
<p> <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>inverse</code> (const <code>Matrix</code> &amp;m) </p>
<p> Real <code>determinant</code> (const <code>Matrix</code> &amp;m) </p>
<p> const <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>CholeskyDecomposition</code> (const <code>Matrix</code> &amp;m, bool flexible=false) </p>
<p> const <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>pseudoSqrt</code> (const <code>Matrix</code> &amp;, SalvagingAlgorithm::Type=SalvagingAlgorithm::None)<br />
 <i>Returns the pseudo square root of a real symmetric matrix. </i><br />
 const <code>Disposable</code>&lt; <code>Matrix</code> &gt; <code>rankReducedSqrt</code> (const <code>Matrix</code> &amp;, Size maxRank, Real componentRetainedPercentage, SalvagingAlgorithm::Type)<br />
 <i>Returns the rank-reduced pseudo square root of a real symmetric matrix. </i></p>
<h2>Detailed Description</h2>
<p>Matrix used in linear algebra. </p>
<p> This class implements the concept of <code>Matrix</code> as used in linear algebra. As such, it is <code>not</code> meant to be used as a container.</p>
<h2>Member Function Documentation</h2>
<h3>const <code>Matrix</code> &amp; operator+= (const <code>Matrix</code> &amp; m)</h3>
<p><code>Precondition:</code></p>
<dl>
<dd>all matrices involved in an algebraic expression must have the same size.</dl>
<h2>Friends And Related Function Documentation</h2>
<h3>const <code>Disposable</code>&lt; <code>Matrix</code> &gt; operator+ (const <code>Matrix</code> &amp;, const <code>Matrix</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Matrix</code> &gt; operator- (const <code>Matrix</code> &amp;, const <code>Matrix</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Matrix</code> &gt; operator* (const <code>Matrix</code> &amp;, Real) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Matrix</code> &gt; operator* (Real, const <code>Matrix</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Matrix</code> &gt; operator/ (const <code>Matrix</code> &amp;, Real) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; operator* (const <code>Array</code> &amp;, const <code>Matrix</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Array</code> &gt; operator* (const <code>Matrix</code> &amp;, const <code>Array</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Matrix</code> &gt; operator* (const <code>Matrix</code> &amp;, const <code>Matrix</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Matrix</code> &gt; transpose (const <code>Matrix</code> &amp;) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Matrix</code> &gt; outerProduct (const <code>Array</code> &amp; v1, const <code>Array</code> &amp; v2) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Matrix</code> &gt; outerProduct (Iterator1 v1begin, Iterator1 v1end, Iterator2 v2begin, Iterator2 v2end) [related]</h3>
<h3>void swap (<code>Matrix</code> &amp;, <code>Matrix</code> &amp;) [related]</h3>
<h3>std::ostream &amp; operator&lt;&lt; (std::ostream &amp;, const <code>Matrix</code> &amp;) [related]</h3>
<h3><code>Disposable</code>&lt; <code>Matrix</code> &gt; inverse (const <code>Matrix</code> &amp; m) [related]</h3>
<h3>Real determinant (const <code>Matrix</code> &amp; m) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Matrix</code> &gt; CholeskyDecomposition (const <code>Matrix</code> &amp; m, bool flexible = false) [related]</h3>
<h3>const <code>Disposable</code>&lt; <code>Matrix</code> &gt; pseudoSqrt (const <code>Matrix</code> &amp;, SalvagingAlgorithm::Type = SalvagingAlgorithm::None) [related]</h3>
<p>Returns the pseudo square root of a real symmetric matrix. </p>
<p> Given a matrix $ M $, the result $ S $ is defined as the matrix such that $ S S^T = M. $ If the matrix is not positive semi definite, it can return an approximation of the pseudo square root using a (user selected) salvaging algorithm. </p>
<p> For more information see: &#8216;The most general methodology to create a valid correlation matrix for risk management and option pricing purposes&#8217;, by R. Rebonato and P. J�ckel. The Journal of Risk, <a href="/docs/linux/man/2-2/">2</a>(2), Winter 1999/2000 <a rel="nofollow" href="http://www.rebonato.com/correlationmatrix.pdf">http://www.rebonato.com/correlationmatrix.pdf</a> </p>
<p> Revised and extended in &#8216;Monte Carlo Methods in Finance&#8217;, by Peter J�ckel, Chapter 6. </p>
<p> <code>Precondition:</code></p>
<dl>
<dd>the given matrix must be symmetric.</dl>
<p> <code>Warning</code></p>
<dl>
<dd>Higham algorithm only works for correlation matrices.</dl>
<p> <code>Tests</code></p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>the correctness of the results is tested by reproducing known good data.</p>
<dt>*</p>
<dd>the correctness of the results is tested by checking returned values against numerical calculations.</dl>
</dl>
<h3>const <code>Disposable</code>&lt; <code>Matrix</code> &gt; rankReducedSqrt (const <code>Matrix</code> &amp;, Size maxRank, Real componentRetainedPercentage, SalvagingAlgorithm::Type) [related]</h3>
<p>Returns the rank-reduced pseudo square root of a real symmetric matrix. </p>
<p> The result matrix has rank&lt;=maxRank. If maxRank&gt;=size, then the specified percentage of eigenvalues out of the eigenvalues&#8217; sum is retained. </p>
<p> If the input matrix is not positive semi definite, it can return an approximation of the pseudo square root using a (user selected) salvaging algorithm. </p>
<p> <code>Precondition:</code></p>
<dl>
<dd>the given matrix must be symmetric.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
