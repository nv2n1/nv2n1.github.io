---
title: "stdsample(3)"
name: "stdsample"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsample/"
---

std::sample - std::sample

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class PopulationIterator, class SampleIterator,

class Distance, class URBG &gt;

SampleIterator sample( PopulationIterator first, PopulationIterator last,  (since C++17)

SampleIterator out, Distance n,

URBG&amp;&amp; g);</code></pre> 
Selects n elements from the sequence [first; last) such that each possible sample has equal probability of appearance, and writes those selected elements into the output iterator out. Random numbers are generated using the random number generator g. 
If n is greater than the number of elements in the sequence, selects last-first elements. 
The algorithm is stable (preserves the relative order of the selected elements) only if PopulationIterator meets the requirements of LegacyForwardIterator 

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
std::remove_reference_t&lt;URBG&gt; must meet the requirements of UniformRandomBitGenerator and its return type must be convertible to Distance

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

#include &lt;algorithm&gt;
int main()

{
    std::string in = &quot;abcdefgh&quot;, out;
    std::sample(in.begin(), in.end(), std::back_inserter(out),
                5, std::mt19937{std::random_device{}()});
    std::cout &lt;&lt; &quot;five random letters out of &quot; &lt;&lt; in &lt;&lt; &quot; : &quot; &lt;&lt; out &lt;&lt; '\n';
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;five random letters out of abcdefgh : adfgh

<h2>See also</h2>

random_shuffle 
shuffle randomly re-orders elements in a range 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(until C++17)</i> 
<i>(C++11)</i> 
