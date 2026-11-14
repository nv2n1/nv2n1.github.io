---
title: "stdexperimentalsample(3)"
name: "stdexperimentalsample"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalsample/"
---

std::experimental::sample - std::experimental::sample

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/algorithm&gt;

template&lt; class PopulationIterator, class SampleIterator,

class Distance, class URBG &gt;

SampleIterator sample( PopulationIterator first, PopulationIterator last,  (1) (library fundamentals TS)

SampleIterator out, Distance n,

URBG&amp;&amp; g);

template&lt; class PopulationIterator, class SampleIterator, class Distance &gt;

SampleIterator sample( PopulationIterator first, PopulationIterator last,  (2) (library fundamentals TS v2)

SampleIterator out, Distance n);</code></pre> 
Selects n elements from the sequence [first; last) such that each possible sample has equal probability of appearance, and writes those selected elements into the output iterator out 
If n is greater than the number of elements in the sequence, selects last-first elements. 
The algorithm is stable only if PopulationIterator meets the requirements of LegacyForwardIterator 
1) Random numbers are generated using the random number generator g. 
2) Random numbers are generated using the per-thread_engine. 

<h2>Parameters</h2>

first, last - pair of iterators forming the range from which to make the sampling (the population) 
out - the output iterator where the samples are written. Must not be in the [first;last) range 
n - number of samples to make 
g - the random number generator used as the source of randomness 
- 
PopulationIterator must meet the requirements of LegacyInputIterator. 
- 
SampleIterator must meet the requirements of LegacyOutputIterator. 
- 
SampleIterator must also meet the requirements of LegacyRandomAccessIterator if PopulationIterator doesn't meet LegacyForwardIterator 
- 
PopulationIterator's value type must be writeable to out 
- 
Distance must be an integer type 
- 
URBG must meet the requirements of UniformRandomBitGenerator and its return type must be convertible to Distance

<h2>Return value</h2>

Returns a copy of out after the last sample that was output, that is, end of the sample range. 

<h2>Complexity</h2>

Linear in std::distance(first,last)

<h2>Notes</h2>

This function may implement selection sampling or reservoir sampling. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;random&gt;

#include &lt;string&gt;

#include &lt;iterator&gt;

#include &lt;experimental/algorithm&gt;
int main()

{
    std::string in = &quot;abcdefgh&quot;, out;
    std::experimental::sample(in.begin(), in.end(), std::back_inserter(out),
                              5, std::mt19937{std::random_device{}()});
    std::cout &lt;&lt; &quot;five random letters out of &quot; &lt;&lt; in &lt;&lt; &quot; : &quot; &lt;&lt; out &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;five random letters out of abcdefgh : cdefg

<h2>See also</h2>

random_shuffle 
shuffle randomly re-orders elements in a range 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(until C++17)</i> 
<i>(C++11)</i> 
