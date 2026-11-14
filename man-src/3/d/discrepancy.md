---
title: "discrepancy(3)"
name: "discrepancy"
section: "3"
letter: "d"
url: "/docs/linux/man/3-discrepancy/"
description: "QuantLib::DiscrepancyStatistics – Statistic tool for sequences with discrepancy calculation."
---

<h2 class="name">NAME</h2>
<p> QuantLib::DiscrepancyStatistics &#8211; Statistic tool for sequences with discrepancy calculation. </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;ql/math/statistics/discrepancystatistics.hpp&gt; </p>
<p> Inherits <code>GenericSequenceStatistics&lt; Statistics &gt;</code>. </p>
<h3>Public Types</h3>
<p> typedef SequenceStatistics::value_type <code>value_type</code> </p>
<h3>Public Member Functions</h3>
<p> <code>DiscrepancyStatistics</code> (Size dimension) </p>
<p> template&lt;class Sequence &gt; void <code>add</code> (const Sequence &amp;sample, Real weight=1.0) </p>
<p> template&lt;class Iterator &gt; void <code>add</code> (Iterator begin, Iterator end, Real weight=1.0) </p>
<p> void <code>reset</code> (Size dimension=0) </p>
<p> <code>1-dimensional inspectors</code> </p>
<p> Real <code>discrepancy</code> () const </p>
<h2>Detailed Description</h2>
<p> Statistic tool for sequences with discrepancy calculation. </p>
<p> It inherit from SequenceStatistics&lt;Statistics&gt; and adds $ L^2 $ discrepancy calculation </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for QuantLib from the source code. </p>
<h2>Index</h2>
