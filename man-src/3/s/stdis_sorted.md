---
title: "stdis_sorted(3)"
name: "stdis_sorted"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_sorted/"
---

std::is_sorted - std::is_sorted

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class ForwardIt &gt;                                                                        (since C++11)

bool is_sorted( ForwardIt first, ForwardIt last );                                                 (until C++20)

template&lt; class ForwardIt &gt;                                                                        (since C++20)

constexpr bool is_sorted( ForwardIt first, ForwardIt last );

template&lt; class ExecutionPolicy, class ForwardIt &gt;                                             (2) (since C++17)

bool is_sorted( ExecutionPolicy&amp;&amp; policy, ForwardIt first, ForwardIt last );               (1)

template&lt; class ForwardIt, class Compare &gt;                                                                        (since C++11)

bool is_sorted( ForwardIt first, ForwardIt last, Compare comp );                                                  (until C++20)

template&lt; class ForwardIt, class Compare &gt;                                                     (3)                (since C++20)

constexpr bool is_sorted( ForwardIt first, ForwardIt last, Compare comp );

template&lt; class ExecutionPolicy, class ForwardIt, class Compare &gt;                                  (4)            (since C++17)

bool is_sorted( ExecutionPolicy&amp;&amp; policy, ForwardIt first, ForwardIt last, Compare comp );</code></pre> 
Checks if the elements in range [first, last) are sorted in non-descending order. 
1) Elements are compared using operator&lt;. 
3) Elements are compared using the given binary comparison function comp. 
2,4) Same as (1,3), but executed according to policy. These overloads do not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first, last - the range of elements to examine 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comparison function object (i.e. an object that satisfies the requirements of Compare) which returns true if the first argument is less than (i.e. is ordered before) the second. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the comparison function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool cmp(const Type1 &amp;a, const Type2 &amp;b); 
comp - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type ForwardIt can be dereferenced and then implicitly converted to both of them.

<h2>Type requirements</h2>

- 
ForwardIt must meet the requirements of LegacyForwardIterator.

<h2>Return value</h2>

true if the elements in the range are sorted in ascending order 

<h2>Complexity</h2>

linear in the distance between first and last

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt&gt; 
&nbsp;<wbr>&nbsp;bool is_sorted(ForwardIt first, ForwardIt last) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::is_sorted_until(first, last) == last; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class ForwardIt, class Compare&gt; 
&nbsp;<wbr>&nbsp;bool is_sorted(ForwardIt first, ForwardIt last, Compare comp) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::is_sorted_until(first, last, comp) == last; 
&nbsp;<wbr>&nbsp;}

<h2>Notes</h2>

std::is_sorted and std::is_sorted_until both return true for empty ranges and ranges of length one. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;algorithm&gt;

#include &lt;iterator&gt;

int main()

{
    int digits[] = {3, 1, 4, 1, 5};
    for (auto i : digits)
        std::cout &lt;&lt; i &lt;&lt; ' ';
    std::cout &lt;&lt; &quot;: is_sorted: &quot; &lt;&lt; std::boolalpha
              &lt;&lt; std::is_sorted(std::begin(digits), std::end(digits)) &lt;&lt; '\n';
    std::sort(std::begin(digits), std::end(digits));
    for (auto i : digits)
        std::cout &lt;&lt; i &lt;&lt; ' ';
    std::cout &lt;&lt; &quot;: is_sorted: &quot;
              &lt;&lt; std::is_sorted(std::begin(digits), std::end(digits)) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;3 1 4 1 5 : is_sorted: false 
&nbsp;<wbr>&nbsp;1 1 3 4 5 : is_sorted: true

<h2>See also</h2>

is_sorted_until finds the largest sorted subrange 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
