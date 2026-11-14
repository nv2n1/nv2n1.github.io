---
title: "x_iterator(3)"
name: "x_iterator"
section: "3"
letter: "x"
url: "/docs/linux/man/3-x_iterator/"
description: "QuantLib::LexicographicalView – Lexicographical 2-D view of a contiguous set of data."
---

<p>QuantLib::LexicographicalView &#8211; Lexicographical 2-D view of a contiguous set of data. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/math/lexicographicalview.hpp&gt;</code></pre>
<h3>Public Types</h3>
<p>typedef RandomAccessIterator <code>x_iterator</code><br />
 <i>iterates over $ v_{ij} $ with $ j $ fixed. </i><br />
 typedef boost::reverse_iterator&lt; RandomAccessIterator &gt; <code>reverse_x_iterator</code><br />
 <i>iterates backwards over $ v_{ij} $ with $ j $ fixed. </i><br />
 typedef <code>step_iterator</code>&lt; RandomAccessIterator &gt; <code>y_iterator</code><br />
 <i>iterates over $ v_{ij} $ with $ i $ fixed. </i><br />
 typedef boost::reverse_iterator&lt; <code>y_iterator</code> &gt; <code>reverse_y_iterator</code><br />
 <i>iterates backwards over $ v_{ij} $ with $ i $ fixed. </i></p>
<h3>Public Member Functions</h3>
<p><code>LexicographicalView</code> (const RandomAccessIterator &amp;begin, const RandomAccessIterator &amp;end, Size xSize)<br />
 <i>attaches the view with the given dimension to a sequence </i> <code>Element access</code> </p>
<p> <code>y_iterator</code> <code>operator[]</code> (Size i)<br />
 <code>Iterator access</code> </p>
<p> <code>x_iterator</code> <code>xbegin</code> (Size j) </p>
<p> <code>x_iterator</code> <code>xend</code> (Size j) </p>
<p> <code>reverse_x_iterator</code> <code>rxbegin</code> (Size j) </p>
<p> <code>reverse_x_iterator</code> <code>rxend</code> (Size j) </p>
<p> <code>y_iterator</code> <code>ybegin</code> (Size i) </p>
<p> <code>y_iterator</code> <code>yend</code> (Size i) </p>
<p> <code>reverse_y_iterator</code> <code>rybegin</code> (Size i) </p>
<p> <code>reverse_y_iterator</code> <code>ryend</code> (Size i)<br />
 <code>Inspectors</code> </p>
<p> Size <code>xSize</code> () const<br />
 <i>dimension of the array along x </i><br />
 Size <code>ySize</code> () const<br />
 <i>dimension of the array along y </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;class RandomAccessIterator&gt; class QuantLib::LexicographicalView&lt; RandomAccessIterator &gt;</h3>
<p>Lexicographical 2-D view of a contiguous set of data. </p>
<p> This view can be used to easily store a discretized 2-D function in an array to be used in a finite differences calculation.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
