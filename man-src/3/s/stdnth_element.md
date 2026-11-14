---
title: "stdnth_element(3)"
name: "stdnth_element"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnth_element/"
---

std::nth_element - std::nth_element

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class RandomIt&gt;
    (until C++ 20)

        void nth_element(RandomIt first, RandomIt nth, RandomIt last);

template &lt;class RandomIt&gt;
(since C++ 20)

    constexpr void nth_element(RandomIt first, RandomIt nth, RandomIt last);

template &lt;class ExecutionPolicy, class RandomIt&gt;

void nth_element(ExecutionPolicy &amp;&amp;policy, (2)(since C++ 17)

                                               RandomIt first,
                 RandomIt nth, RandomIt last);

template &lt;class RandomIt, class Compare&gt;

void nth_element(RandomIt first, RandomIt nth, RandomIt last, (1)(until C++ 20)

                                                                  Compare comp);

template &lt;class RandomIt, class Compare&gt;

constexpr void nth_element(RandomIt first, RandomIt nth, RandomIt last, (3)(since C++ 20)

                                                                            Compare comp);

template &lt;class ExecutionPolicy, class RandomIt, class Compare&gt;

void nth_element(ExecutionPolicy &amp;&amp;policy, (4)(since C++ 17)

                                               RandomIt first,
                 RandomIt nth, RandomIt last,

                 Compare comp);</code></pre> 
nth_element is a partial sorting algorithm that rearranges elements in [first, last) such that: 
* The element pointed at by nth is changed to whatever element would occur in that position if [first, last) were sorted. 
* All of the elements before this new nth element are less than or equal to the elements after the new nth element. 
More formally, nth_element partially sorts the range [first, last) in ascending order so that the condition !(*j &lt; *i) (for (1-2), or comp(*j, *i) == false for (3-4)) is met for any i in the range [first, nth) and for any j in the range [nth, last). The element placed in the nth position is exactly the element that would occur in this position if the range was fully sorted. 
nth may be the end iterator, in this case the function has no effect. 
1) Elements are compared using operator&lt;. 
3) Elements are compared using the given binary comparison function comp. 
2,4) Same as (1,3), but executed according to policy. These overloads do not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first, last - random access iterators defining the range sort 
nth - random access iterator defining the sort partition point 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comparison function object (i.e. an object that satisfies the requirements of Compare) which returns true if the first argument is less than (i.e. is ordered before) the second. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the comparison function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool cmp(const Type1 &amp;a, const Type2 &amp;b); 
comp - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type RandomIt can be dereferenced and then implicitly converted to both of them.

<h2>Type requirements</h2>

- 
RandomIt must meet the requirements of ValueSwappable and LegacyRandomAccessIterator. 
- 
The type of dereferenced RandomIt must meet the requirements of MoveAssignable and MoveConstructible.

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

1,3) Linear in std::distance(first, last) on average. 
2,4) O(N) applications of the predicate, and O(N log N) swaps, where N = last - first.

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Notes</h2>

The algorithm used is typically introselect although other selection_algorithms with suitable average-case complexity are allowed. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;algorithm&gt;

#include &lt;functional&gt;
int main()

{
    std::vector&lt;int&gt; v{5, 6, 4, 3, 2, 6, 7, 9, 3};
    std::nth_element(v.begin(), v.begin() + v.size() / 2, v.end());
    std::cout &lt;&lt; &quot;The median is &quot; &lt;&lt; v[v.size() / 2] &lt;&lt; '\n';
    std::nth_element(v.begin(), v.begin() + 1, v.end(), std::greater&lt;int&gt;());
    std::cout &lt;&lt; &quot;The second largest element is &quot; &lt;&lt; v[1] &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;The median is 5 
&nbsp;<wbr>&nbsp;The second largest element is 7

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies and partially sorts a range of elements 
partial_sort_copy <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sorts a range of elements while preserving order between equal elements 
stable_sort <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sorts a range into ascending order 
sort <i>(function template)</i> 
