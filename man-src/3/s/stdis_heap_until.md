---
title: "stdis_heap_until(3)"
name: "stdis_heap_until"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdis_heap_until/"
---

std::is_heap_until - std::is_heap_until

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class RandomIt &gt;                                                                               (since C++11)

RandomIt is_heap_until( RandomIt first, RandomIt last );                                                 (until C++20)

template&lt; class RandomIt &gt;                                                                               (since C++20)

constexpr RandomIt is_heap_until( RandomIt first, RandomIt last );

template&lt; class ExecutionPolicy, class RandomIt &gt;                                                    (2) (since C++17)

RandomIt is_heap_until( ExecutionPolicy&amp;&amp; policy, RandomIt first, RandomIt last );               (1)

template&lt; class RandomIt, class Compare &gt;                                                                               (since C++11)

RandomIt is_heap_until( RandomIt first, RandomIt last, Compare comp );                                                  (until C++20)

template&lt; class RandomIt, class Compare &gt;                                                            (3)                (since C++20)

constexpr RandomIt is_heap_until( RandomIt first, RandomIt last, Compare comp );

template&lt; class ExecutionPolicy, class RandomIt, class Compare &gt;                                         (4)            (since C++17)

RandomIt is_heap_until( ExecutionPolicy&amp;&amp; policy, RandomIt first, RandomIt last, Compare comp );</code></pre> 
Examines the range [first, last) and finds the largest range beginning at first which is a max heap. 
1) Elements are compared using operator&lt;. 
3) Elements are compared using the given binary comparison function comp. 
2,4) Same as (1,3), but executed according to policy. These overloads do not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first, last - the range of elements to examine 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comparison function object (i.e. an object that satisfies the requirements of Compare) which returns true if the first argument is less than the second. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the comparison function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool cmp(const Type1 &amp;a, const Type2 &amp;b); 
comp - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type RandomIt can be dereferenced and then implicitly converted to both of them.

<h2>Type requirements</h2>

- 
RandomIt must meet the requirements of LegacyRandomAccessIterator.

<h2>Return value</h2>

The upper bound of the largest range beginning at first which is a max heap. That is, the last iterator it for which range [first, it) is a max heap. 

<h2>Complexity</h2>

Linear in the distance between first and last

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Notes</h2>

A max heap is a range of elements [f,l) that has the following properties: 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;algorithm&gt;

#include &lt;vector&gt;
int main()

{
    std::vector&lt;int&gt; v{3, 1, 4, 1, 5, 9};
    std::make_heap(v.begin(), v.end());
    // probably mess up the heap
    v.push_back(2);
    v.push_back(6);
    auto heap_end = std::is_heap_until(v.begin(), v.end());
    std::cout &lt;&lt; &quot;all of v: &quot;;
    for (auto i : v)
        std::cout &lt;&lt; i &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;only heap: &quot;;
    for (auto i = v.begin(); i != heap_end; ++i)
        std::cout &lt;&lt; *i &lt;&lt; ' ';
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;all of v: 9 5 4 1 1 3 2 6 
&nbsp;<wbr>&nbsp;only heap: 9 5 4 1 1 3 2

<h2>See also</h2>

is_heap checks if the given range is a max heap 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
