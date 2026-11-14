---
title: "evolutiontimes(3)"
name: "evolutiontimes"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evolutiontimes/"
description: "QuantLib::EvolutionDescription – Market-model evolution description."
---

<p>QuantLib::EvolutionDescription &#8211; Market-model evolution description. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/marketmodels/evolutiondescription.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>EvolutionDescription</code> (const std::vector&lt; <code>Time</code> &gt; &amp;rateTimes, const std::vector&lt; <code>Time</code> &gt; &amp;evolutionTimes=std::vector&lt; <code>Time</code> &gt;(), const std::vector&lt; std::pair&lt; Size, Size &gt; &gt; &amp;relevanceRates=std::vector&lt; range &gt;()) </p>
<p> const std::vector&lt; <code>Time</code> &gt; &amp; <code>rateTimes</code> () const </p>
<p> const std::vector&lt; <code>Time</code> &gt; &amp; <code>rateTaus</code> () const </p>
<p> const std::vector&lt; <code>Time</code> &gt; &amp; <code>evolutionTimes</code> () const </p>
<p> const std::vector&lt; Size &gt; &amp; <code>firstAliveRate</code> () const </p>
<p> const std::vector&lt; std::pair&lt; Size, Size &gt; &gt; &amp; <code>relevanceRates</code> () const </p>
<p> Size <code>numberOfRates</code> () const </p>
<p> Size <code>numberOfSteps</code> () const </p>
<h2>Detailed Description</h2>
<p>Market-model evolution description. </p>
<p> This class stores:</p>
<dl COMPACT>
<dt>1.</p>
<dd>evolutionTimes = the times defining the rates that are to be evolved,</p>
<dt>2.</p>
<dd>rateTimes = the times at which the rates need to be known,</p>
<dt>3.</p>
<dd>relevanceRates = which rates need to be known at each time.</dl>
<p> This class is really just a tuple of evolution and rate times;</p>
<dl COMPACT>
<dt>*</p>
<dd>there will be n+1 rate times expressing payment and reset times of forward rates.</p>
<dt>*</p>
<dd>there will be any number of evolution times.</p>
<dt>*</p>
<dd>we also store which part of the rates are relevant for pricing via relevance rates. The important part for the i-th step will then range from relevanceRates[i].first to relevanceRates[i].second. Default values for relevance rates will be 0 and n.</p>
<dt>*</p>
<dd>example for n = 5:</dl>
<pre> |-----|-----|-----|-----|-----| (size = 6)
 t0 t1 t2 t3 t4 t5 rateTimes
 f0 f1 f2 f3 f4 forwardRates
 d0 d1 d2 d3 d4 d5 discountBonds
 d0/d0 d1/d0 d2/d0 d3/d0 d4/d0 d5/d0 discountRatios
 sr0 sr1 sr2 sr3 sr4 coterminalSwaps</pre>
<p>&nbsp;<wbr> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
