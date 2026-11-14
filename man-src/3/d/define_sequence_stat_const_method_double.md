---
title: "define_sequence_stat_const_method_double(3)"
name: "define_sequence_stat_const_method_double"
section: "3"
letter: "d"
url: "/docs/linux/man/3-define_sequence_stat_const_method_double/"
description: "ql/math/statistics/sequencestatistics.hpp – Statistics tools for sequence (vector, list, array) samples."
---

<p>ql/math/statistics/sequencestatistics.hpp &#8211; Statistics tools for sequence (vector, list, array) samples. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/statistics/statistics.hpp&gt;<br />
 #include &lt;ql/math/statistics/incrementalstatistics.hpp&gt;<br />
 #include &lt;ql/math/matrix.hpp&gt; </p>
<h3>Classes</h3>
<p>class <code>GenericSequenceStatistics&lt; StatisticsType &gt;</code><br />
 <i>Statistics analysis of N-dimensional (sequence) data. </i></p>
<h3>Defines</h3>
<p>#define <code>DEFINE_SEQUENCE_STAT_CONST_METHOD_VOID</code>(METHOD) </p>
<p> #define <code>DEFINE_SEQUENCE_STAT_CONST_METHOD_DOUBLE</code>(METHOD) </p>
<h3>Typedefs</h3>
<p>typedef GenericSequenceStatistics&lt; Statistics &gt; <code>SequenceStatistics</code><br />
 <i>default multi-dimensional statistics tool </i><br />
 typedef GenericSequenceStatistics&lt; IncrementalStatistics &gt; <code>SequenceStatisticsInc</code> </p>
<h2>Detailed Description</h2>
<p>Statistics tools for sequence (vector, list, array) samples. </p>
<h2>Define Documentation</h2>
<h3>#define DEFINE_SEQUENCE_STAT_CONST_METHOD_VOID(METHOD)</h3>
<p><code>Value:</code> </p>
<pre>template &lt;class Stat&gt; std::vector&lt;Real&gt; GenericSequenceStatistics&lt;Stat&gt;::METHOD() const { for (Size i=0; i&lt;dimension_; i++) results_[i] = stats_[i].METHOD(); return results_; }</pre>
<h3>#define DEFINE_SEQUENCE_STAT_CONST_METHOD_DOUBLE(METHOD)</h3>
<p><code>Value:</code> </p>
<pre>template &lt;class Stat&gt; std::vector&lt;Real&gt; GenericSequenceStatistics&lt;Stat&gt;::METHOD(Real x) const { for (Size i=0; i&lt;dimension_; i++) results_[i] = stats_[i].METHOD(x); return results_; }</pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
