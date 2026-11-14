---
title: "table_type(3)"
name: "table_type"
section: "3"
letter: "t"
url: "/docs/linux/man/3-table_type/"
description: "QuantLib::ConvergenceStatistics – statistics class with convergence table"
---

<p>QuantLib::ConvergenceStatistics &#8211; statistics class with convergence table </p>
<h2>Synopsis</h2>
<pre><code>ConvergenceStatistics (const T &amp;stats, const U &amp;rule=U())



ConvergenceStatistics (const U &amp;rule=U())



void add (const value_type &amp;value, Real weight=1.0)



template&lt;class DataIterator &gt; void addSequence (DataIterator begin, DataIterator end)



template&lt;class DataIterator , class WeightIterator &gt; void addSequence (DataIterator begin, DataIterator end, WeightIterator wbegin)



void reset ()



const std::vector&lt; std::pair&lt; Size, value_type &gt; &gt; &amp; convergenceTable () const</code></pre>
<p> Inherits T.</p>
<h3>Public Types</h3>
<p>typedef T::value_type <code>value_type</code> </p>
<p> typedef std::vector&lt; std::pair&lt; Size, value_type &gt; &gt; <code>table_type</code></p>
<h3>Public Member Functions</h3>
<pre><code>ConvergenceStatistics (const T &amp;stats, const U &amp;rule=U())



ConvergenceStatistics (const U &amp;rule=U())



void add (const value_type &amp;value, Real weight=1.0)



template&lt;class DataIterator &gt; void addSequence (DataIterator begin, DataIterator end)



template&lt;class DataIterator , class WeightIterator &gt; void addSequence (DataIterator begin, DataIterator end, WeightIterator wbegin)



void reset ()



const std::vector&lt; std::pair&lt; Size, value_type &gt; &gt; &amp; convergenceTable () const</code></pre>
<h2>Detailed Description</h2>
<h3>template&lt;class T, class U = DoublingConvergenceSteps&gt; class QuantLib::ConvergenceStatistics&lt; T, U &gt;</h3>
<p>statistics class with convergence table </p>
<p> This class decorates another statistics class adding a convergence table calculation. The table tracks the convergence of the mean. </p>
<p> It is possible to specify the number of samples at which the mean should be stored by mean of the second template parameter; the default is to store $ 2^{n-1} $ samples at the $ n $-th step. Any passed class must implement the following interface: </p>
<pre> Size initialSamples() const;
 Size nextSamples(Size currentSamples) const;</pre>
<p>&nbsp;<wbr>as well as a copy constructor. </p>
<p> <code>Tests</code></p>
<dl>
<dd>results are tested against known good values.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
