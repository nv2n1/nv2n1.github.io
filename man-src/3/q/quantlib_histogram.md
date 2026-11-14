---
title: "quantlib_histogram(3)"
name: "quantlib_histogram"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_histogram/"
description: "QuantLib::Histogram – Histogram class."
---

<p>QuantLib::Histogram &#8211; <code>Histogram</code> class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/statistics/histogram.hpp&gt; </p>
<h3>Public Types</h3>
<p>enum <code>Algorithm</code> { <code>None</code>, <code>Sturges</code>, <code>FD</code>, <code>Scott</code> } </p>
<h3>Public Member Functions</h3>
<p><code>constructors</code> </p>
<p> <code>Histogram</code> () </p>
<p> template&lt;class T &gt; <code>Histogram</code> (T data_begin, T data_end, Size breaks) </p>
<p> template&lt;class T &gt; <code>Histogram</code> (T data_begin, T data_end, Algorithm algorithm) </p>
<p> template&lt;class T , class U &gt; <code>Histogram</code> (T data_begin, T data_end, U breaks_begin, U breaks_end) </p>
<p> <code>inspectors</code> </p>
<p> Size <code>bins</code> () const </p>
<p> const std::vector&lt; <code>Real</code> &gt; &amp; <code>breaks</code> () const </p>
<p> Algorithm <code>algorithm</code> () const </p>
<p> bool <code>empty</code> () const </p>
<p> <code>results</code> </p>
<p> Size <code>counts</code> (Size i) const </p>
<p> <code>Real</code> <code>frequency</code> (Size i) const </p>
<h2>Detailed Description</h2>
<p><code>Histogram</code> class. </p>
<p> This class computes the histogram of a given data set. The caller can specify the number of bins, the breaks, or the algorithm for determining these quantities in computing the histogram. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
