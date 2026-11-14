---
title: "convergencestatistics(3)"
name: "convergencestatistics"
section: "3"
letter: "c"
url: "/docs/linux/man/3-convergencestatistics/"
description: "QuantLib::ConvergenceStatistics – statistics class with convergence table"
---

<p>QuantLib::ConvergenceStatistics &#8211; statistics class with convergence table </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/statistics/convergencestatistics.hpp&gt; </p>
<p> Inherits T. </p>
<h3>Public Types</h3>
<p>typedef T::value_type <code>value_type</code> </p>
<p> typedef std::vector&lt; std::pair&lt; Size, value_type &gt; &gt; <code>table_type</code> </p>
<h3>Public Member Functions</h3>
<p><code>ConvergenceStatistics</code> (const T &amp;stats, const U &amp;rule=U()) </p>
<p> <code>ConvergenceStatistics</code> (const U &amp;rule=U()) </p>
<p> void <code>add</code> (const value_type &amp;value, <code>Real</code> weight=1.0) </p>
<p> template&lt;class DataIterator &gt; void <code>addSequence</code> (DataIterator begin, DataIterator end) </p>
<p> template&lt;class DataIterator , class WeightIterator &gt; void <code>addSequence</code> (DataIterator begin, DataIterator end, WeightIterator wbegin) </p>
<p> void <code>reset</code> () </p>
<p> const std::vector&lt; std::pair&lt; Size, value_type &gt; &gt; &amp; <code>convergenceTable</code> () const </p>
<h2>Detailed Description</h2>
<h3>template&lt;class T, class U = DoublingConvergenceSteps&gt; class QuantLib::ConvergenceStatistics&lt; T, U &gt;</h3>
<p>statistics class with convergence table </p>
<p> This class decorates another statistics class adding a convergence table calculation. The table tracks the convergence of the mean. </p>
<p> It is possible to specify the number of samples at which the mean should be stored by mean of the second template parameter; the default is to store $ 2^{n-1} $ samples at the $ n $-th step. Any passed class must implement the following interface: </p>
<pre> Size initialSamples() const;
 Size nextSamples(Size currentSamples) const;</pre>
<p>&nbsp;<wbr>as well as a copy constructor. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>results are tested against known good values.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
