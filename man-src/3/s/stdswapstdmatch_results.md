---
title: "stdswapstdmatch_results(3)"
name: "stdswapstdmatch_results"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdswapstdmatch_results/"
---

std::swap(std::match_results) - std::swap(std::match_results)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;regex&gt;

    template &lt;class BidirIt, class Alloc&gt;

    void swap(match_results&lt;BidirIt, Alloc&gt; &amp;x1, (since C++ 11)

                                                     match_results&lt;BidirIt, Alloc&gt; &amp;x2) noexcept;</code></pre> 
Specializes the std::swap algorithm for std::match_results. Exchanges the contents of x1 with those of x2. Effectively calls x1.swap(x2). 

<h2>Parameters</h2>

x1, x2 - the match_results objects whose contents will be swapped

<h2>Type requirements</h2>

- 
BidirIt must meet the requirements of LegacyBidirectionalIterator. 
- 
Alloc must meet the requirements of Allocator.

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swaps the contents 
swap <i>(public member function)</i> 
