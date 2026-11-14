---
title: "stdpartial_sort(3)"
name: "stdpartial_sort"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpartial_sort/"
---

std::partial_sort - std::partial_sort

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class RandomIt&gt;
    (until C++ 20)

        void partial_sort(RandomIt first, RandomIt middle, RandomIt last);

template &lt;class RandomIt&gt;
(since C++ 20)

    constexpr void partial_sort(RandomIt first, RandomIt middle, RandomIt last);

template &lt;class ExecutionPolicy, class RandomIt&gt;

void partial_sort(ExecutionPolicy &amp;&amp;policy, (2)(since C++ 17)

                                                RandomIt first,
                  RandomIt middle, RandomIt last);

template &lt;class RandomIt, class Compare&gt;

void partial_sort(RandomIt first, RandomIt middle, RandomIt last, (1)(until C++ 20)

                                                                      Compare comp);

template &lt;class RandomIt, class Compare&gt;

constexpr void partial_sort(RandomIt first, RandomIt middle, RandomIt last, (3)(since C++ 20)

                                                                                Compare comp);

template &lt;class ExecutionPolicy, class RandomIt, class Compare&gt;

void partial_sort(ExecutionPolicy &amp;&amp;policy, (4)(since C++ 17)

                                                RandomIt first,
                  RandomIt middle, RandomIt last,

                  Compare comp);</code></pre> 
Rearranges elements such that the range [first, middle) contains the sorted middle - first smallest elements in the range [first, last). 
The order of equal elements is not guaranteed to be preserved. The order of the remaining elements in the range [middle, last) is unspecified. 
1) Elements are compared using operator&lt;. 
3) Elements are compared using the given binary comparison function comp. 
2,4) Same as (1,3), but executed according to policy. These overloads do not participate in overload resolution unless std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first, last - the range of elements to sort 
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

Approximately (last-first)log(middle-first) applications of cmp

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;functional&gt;

#include &lt;array&gt;

#include &lt;iostream&gt;
int main()

{
    std::array&lt;int, 10&gt; s{5, 7, 4, 2, 8, 6, 1, 9, 0, 3};
    std::partial_sort(s.begin(), s.begin() + 3, s.end());
    for (int a : s) {
        std::cout &lt;&lt; a &lt;&lt; &quot; &quot;;
    }
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;0 1 2 7 8 6 5 9 4 3

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;partially sorts the given range making sure that it is partitioned by the given element 
nth_element <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies and partially sorts a range of elements 
partial_sort_copy <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sorts a range of elements while preserving order between equal elements 
stable_sort <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sorts a range into ascending order 
sort <i>(function template)</i> 
