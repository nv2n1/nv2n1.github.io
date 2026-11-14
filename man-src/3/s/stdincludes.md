---
title: "stdincludes(3)"
name: "stdincludes"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdincludes/"
---

std::includes - std::includes

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class InputIt1, class InputIt2 &gt;

bool includes( InputIt1 first1, InputIt1 last1,                                              (until C++20)

InputIt2 first2, InputIt2 last2 );

template&lt; class InputIt1, class InputIt2 &gt;

constexpr bool includes( InputIt1 first1, InputIt1 last1,                                    (since C++20)

InputIt2 first2, InputIt2 last2 );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2 &gt;

bool includes( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first1, ForwardIt1 last1,            (2) (since C++17)

ForwardIt2 first2, ForwardIt2 last2 );                                               (1)

template&lt; class InputIt1, class InputIt2, class Compare &gt;

bool includes( InputIt1 first1, InputIt1 last1,                                                            (until C++20)

InputIt2 first2, InputIt2 last2, Compare comp );

template&lt; class InputIt1, class InputIt2, class Compare &gt;

constexpr bool includes( InputIt1 first1, InputIt1 last1,                                (3)               (since C++20)

InputIt2 first2, InputIt2 last2, Compare comp );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2, class Compare &gt;

bool includes( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first1, ForwardIt1 last1,                (4)           (since C++17)

ForwardIt2 first2, ForwardIt2 last2, Compare comp );</code></pre> 
Returns true if the sorted range [first2, last2) is a subsequence of the sorted range [first1, last1). (A subsequence need not be contiguous.) 
1) Both ranges must be sorted with operator&lt;. 
3) Both ranges must be sorted with the given comparison function comp. 
2,4) Same as (1,3), but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first1, last1 - the sorted range of elements to examine 
first2, last2 - the sorted range of elements to search for 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comparison function object (i.e. an object that satisfies the requirements of Compare) which returns true if the first argument is less than (i.e. is ordered before) the second. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the comparison function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool cmp(const Type1 &amp;a, const Type2 &amp;b); 
comp - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type InputIt can be dereferenced and then implicitly converted to both of them.

<h2>Type requirements</h2>

- 
InputIt1, InputIt2 must meet the requirements of LegacyInputIterator. 
- 
ForwardIt1, ForwardIt2 must meet the requirements of LegacyForwardIterator.

<h2>Return value</h2>

true if [first2, last2) is a subsequence of [first1, last1); otherwise false. 

<h2>Complexity</h2>

At most 2·(N1+N2-1) comparisons, where N1 = std::distance(first1, last1) and N2 = std::distance(first2, last2).

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt1, class InputIt2&gt; 
&nbsp;<wbr>&nbsp;bool includes(InputIt1 first1, InputIt1 last1, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;InputIt2 first2, InputIt2 last2) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first2 != last2; ++first1) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (first1 == last1 || *first2 &lt; *first1) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return false; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if ( !(*first1 &lt; *first2) ) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++first2; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return true; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt1, class InputIt2, class Compare&gt; 
&nbsp;<wbr>&nbsp;bool includes(InputIt1 first1, InputIt1 last1, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;InputIt2 first2, InputIt2 last2, Compare comp) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first2 != last2; ++first1) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (first1 == last1 || comp(*first2, *first1)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return false; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (!comp(*first1, *first2)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;++first2; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return true; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;algorithm&gt;

#include &lt;cctype&gt;

#include &lt;vector&gt;
int main()

{
    std::vector&lt;char&gt; v1{'a', 'b', 'c', 'f', 'h', 'x'};
    std::vector&lt;char&gt; v2{'a', 'b', 'c'};
    std::vector&lt;char&gt; v3{'a', 'c'};
    std::vector&lt;char&gt; v4{'g'};
    std::vector&lt;char&gt; v5{'a', 'c', 'g'};
    for (auto i : v1)
        std::cout &lt;&lt; i &lt;&lt; ' ';
    std::cout &lt;&lt; &quot;\nincludes:\n&quot;
              &lt;&lt; std::boolalpha;
    for (auto i : v2)
        std::cout &lt;&lt; i &lt;&lt; ' ';
    std::cout &lt;&lt; &quot;: &quot; &lt;&lt; std::includes(v1.begin(), v1.end(), v2.begin(), v2.end()) &lt;&lt; '\n';
    for (auto i : v3)
        std::cout &lt;&lt; i &lt;&lt; ' ';
    std::cout &lt;&lt; &quot;: &quot; &lt;&lt; std::includes(v1.begin(), v1.end(), v3.begin(), v3.end()) &lt;&lt; '\n';
    for (auto i : v4)
        std::cout &lt;&lt; i &lt;&lt; ' ';
    std::cout &lt;&lt; &quot;: &quot; &lt;&lt; std::includes(v1.begin(), v1.end(), v4.begin(), v4.end()) &lt;&lt; '\n';
    for (auto i : v5)
        std::cout &lt;&lt; i &lt;&lt; ' ';
    std::cout &lt;&lt; &quot;: &quot; &lt;&lt; std::includes(v1.begin(), v1.end(), v5.begin(), v5.end()) &lt;&lt; '\n';
    auto cmp_nocase = [](char a, char b) {
        return std::tolower(a) &lt; std::tolower(b);
    };
    std::vector&lt;char&gt; v6{'A', 'B', 'C'};
    for (auto i : v6)
        std::cout &lt;&lt; i &lt;&lt; ' ';
    std::cout &lt;&lt; &quot;: (case-insensitive) &quot;
              &lt;&lt; std::includes(v1.begin(), v1.end(), v6.begin(), v6.end(), cmp_nocase)
              &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;a b c f h x 
&nbsp;<wbr>&nbsp;includes: 
&nbsp;<wbr>&nbsp;a b c : true 
&nbsp;<wbr>&nbsp;a c : true 
&nbsp;<wbr>&nbsp;g : false 
&nbsp;<wbr>&nbsp;a c g : false 
&nbsp;<wbr>&nbsp;A B C : (case-insensitive) true

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;computes the difference between two sets 
set_difference <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;searches for a range of elements 
search <i>(function template)</i> 
