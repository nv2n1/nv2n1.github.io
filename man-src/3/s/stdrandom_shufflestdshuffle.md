---
title: "stdrandom_shufflestdshuffle(3)"
name: "stdrandom_shufflestdshuffle"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrandom_shufflestdshuffle/"
---

std::random_shuffle,std::shuffle - std::random_shuffle,std::shuffle

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class RandomIt&gt;
    (1)(deprecated in C++ 14)

        void random_shuffle(RandomIt first, RandomIt last);
(removed in C++ 17)

    template &lt;class RandomIt, class RandomFunc&gt;
    (until C++ 11)

        void random_shuffle(RandomIt first, RandomIt last, RandomFunc &amp;r);

template &lt;class RandomIt, class RandomFunc&gt;
(since C++ 11)

    void random_shuffle(RandomIt first, RandomIt last, RandomFunc &amp;&amp;r);
(2)(deprecated in C++ 14)(removed in C++ 17)

    template &lt;class RandomIt, class URBG&gt;
    (3)(since C++ 11)

        void shuffle(RandomIt first, RandomIt last, URBG &amp;&amp;g);</code></pre> 
Reorders the elements in the given range [first, last) such that each possible permutation of those elements has equal probability of appearance. 
1) The random number generator is implementation-defined, but the function std::rand is often used. 
2) The random number generator is the function object r. 
3) The random number generator is the function object g. 

<h2>Parameters</h2>

first, last - the range of elements to shuffle randomly 
r - function object returning a randomly chosen value of type convertible to std::iterator_traits&lt;RandomIt&gt;::difference_type in the interval [0,n) if invoked as <a HREF="/docs/linux/man/n-r/">r</a>(n) 
g - a UniformRandomBitGenerator whose result type is convertible to std::iterator_traits&lt;RandomIt&gt;::difference_type

<h2>Type requirements</h2>

- 
RandomIt must meet the requirements of ValueSwappable and LegacyRandomAccessIterator. 
- 
std::remove_reference_t&lt;URBG&gt; must meet the requirements of UniformRandomBitGenerator.

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

Linear in the distance between first and last

<h2>Notes</h2>

Note that the implementation is not dictated by the standard, so even if you use exactly the same RandomFunc or URBG you may get different results with different standard library implementations. 

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt; class RandomIt &gt; 
&nbsp;<wbr>&nbsp;void random_shuffle( RandomIt first, RandomIt last ) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::iterator_traits&lt;RandomIt&gt;::difference_type i, n; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n = last - first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (i = n-1; i &gt; 0; --i) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using std::swap; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swap(first[i], first[std::rand() % (i+1)]); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// rand() % (i+1) isn't actually correct, because the generated number 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// is not uniformly distributed for most values of i. A correct implementation 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// will need to essentially reimplement C++11 std::uniform_int_distribution, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;// which is beyond the scope of this example. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class RandomIt, class RandomFunc&gt; 
&nbsp;<wbr>&nbsp;void random_shuffle(RandomIt first, RandomIt last, RandomFunc&amp;&amp; r) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename std::iterator_traits&lt;RandomIt&gt;::difference_type i, n; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n = last - first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (i = n-1; i &gt; 0; --i) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using std::swap; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swap(first[i], first[r(i+1)]); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;} 

 
Third version 

 
&nbsp;<wbr>&nbsp;template&lt;class RandomIt, class URBG&gt; 
&nbsp;<wbr>&nbsp;void shuffle(RandomIt first, RandomIt last, URBG&amp;&amp; g) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef typename std::iterator_traits&lt;RandomIt&gt;::difference_type diff_t; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef std::uniform_int_distribution&lt;diff_t&gt; distr_t; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typedef typename distr_t::param_type param_t; 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;distr_t D; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;diff_t n = last - first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (diff_t i = n-1; i &gt; 0; --i) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using std::swap; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;swap(first[i], first[D(g, param_t(0, i))]); 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

The following code randomly shuffles the integers 1..10: 
 // Run this code <pre><code>#include &lt;random&gt;

#include &lt;algorithm&gt;

#include &lt;iterator&gt;

#include &lt;iostream&gt;
int main()

{
    std::vector&lt;int&gt; v = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::random_device rd;
    std::mt19937 g(rd());
    std::shuffle(v.begin(), v.end(), g);
    std::copy(v.begin(), v.end(), std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;));
    std::cout &lt;&lt; &quot;\n&quot;;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;8 6 10 4 2 3 7 1 9 5

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;generates the next greater lexicographic permutation of a range of elements 
next_permutation <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;generates the next smaller lexicographic permutation of a range of elements 
prev_permutation <i>(function template)</i> 
