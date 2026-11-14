---
title: "relevancerates(3)"
name: "relevancerates"
section: "3"
letter: "r"
url: "/docs/linux/man/3-relevancerates/"
---

QuantLib::EvolutionDescription - Market-model evolution description. 

<h2>Synopsis</h2>

<pre><code>EvolutionDescription (const std::vector&lt; Time &gt; &amp;rateTimes, const std::vector&lt; Time &gt; &amp;evolutionTimes=std::vector&lt; Time &gt;(), const std::vector&lt; std::pair&lt; Size, Size &gt; &gt; &amp;relevanceRates=std::vector&lt; range &gt;())



const std::vector&lt; Time &gt; &amp; rateTimes () const



const std::vector&lt; Time &gt; &amp; rateTaus () const



const std::vector&lt; Time &gt; &amp; evolutionTimes () const



const std::vector&lt; Size &gt; &amp; firstAliveRate () const



const std::vector&lt; std::pair&lt; Size, Size &gt; &gt; &amp; relevanceRates () const



Size numberOfRates () const



Size numberOfSteps () const</code></pre>

<h3>Public Member Functions</h3>

<pre><code>EvolutionDescription (const std::vector&lt; Time &gt; &amp;rateTimes, const std::vector&lt; Time &gt; &amp;evolutionTimes=std::vector&lt; Time &gt;(), const std::vector&lt; std::pair&lt; Size, Size &gt; &gt; &amp;relevanceRates=std::vector&lt; range &gt;())



const std::vector&lt; Time &gt; &amp; rateTimes () const



const std::vector&lt; Time &gt; &amp; rateTaus () const



const std::vector&lt; Time &gt; &amp; evolutionTimes () const



const std::vector&lt; Size &gt; &amp; firstAliveRate () const



const std::vector&lt; std::pair&lt; Size, Size &gt; &gt; &amp; relevanceRates () const



Size numberOfRates () const



Size numberOfSteps () const</code></pre>

<h2>Detailed Description</h2>

Market-model evolution description. 

 This class stores:
<dl><dt>1.
<dd>evolutionTimes = the times defining the rates that are to be evolved,
<dt>2.
<dd>rateTimes = the times at which the rates need to be known,
<dt>3.
<dd>relevanceRates = which rates need to be known at each time.</dl>
 

 

 This class is really just a tuple of evolution and rate times;
<dl><dt>*
<dd>there will be n+1 rate times expressing payment and reset times of forward rates.
<dt>*
<dd>there will be any number of evolution times.
<dt>*
<dd>we also store which part of the rates are relevant for pricing via relevance rates. The important part for the i-th step will then range from relevanceRates[i].first to relevanceRates[i].second. Default values for relevance rates will be 0 and n.
<dt>*
<dd>example for n = 5:</dl>
 

 <pre> |-----|-----|-----|-----|-----| (size = 6)
 t0 t1 t2 t3 t4 t5 rateTimes
 f0 f1 f2 f3 f4 forwardRates
 d0 d1 d2 d3 d4 d5 discountBonds
 d0/d0 d1/d0 d2/d0 d3/d0 d4/d0 d5/d0 discountRatios
 sr0 sr1 sr2 sr3 sr4 coterminalSwaps</pre>&nbsp;<wbr>

<h2>Author</h2>

Generated automatically by Doxygen for QuantLib from the source code.
