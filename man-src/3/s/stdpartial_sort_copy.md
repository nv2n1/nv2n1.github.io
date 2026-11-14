---
title: "stdpartial_sort_copy(3)"
name: "stdpartial_sort_copy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdpartial_sort_copy/"
---

std::partial_sort_copy - std::partial_sort_copy

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class InputIt, class RandomIt&gt;

    RandomIt partial_sort_copy(InputIt first, InputIt last, (until C++ 20)

                                                                RandomIt d_first,
                               RandomIt d_last);

template &lt;class InputIt, class RandomIt&gt;

constexpr RandomIt partial_sort_copy(InputIt first, InputIt last, (since C++ 20)

                                                                      RandomIt d_first,
                                     RandomIt d_last);

template &lt;class ExecutionPolicy, class ForwardIt, class RandomIt&gt;

RandomIt partial_sort_copy(ExecutionPolicy &amp;&amp;policy, ForwardIt first, ForwardIt last, (2)(since C++ 17)

                                                                                          RandomIt d_first,
                           RandomIt d_last);

template &lt;class InputIt, class RandomIt, class Compare&gt;

RandomIt partial_sort_copy(InputIt first, InputIt last, (1)(until C++ 20)

                                                            RandomIt d_first,
                           RandomIt d_last,

                           Compare comp);

template &lt;class InputIt, class RandomIt, class Compare&gt;

constexpr RandomIt partial_sort_copy(InputIt first, InputIt last, (3)(since C++ 20)

                                                                      RandomIt d_first,
                                     RandomIt d_last,

                                     Compare comp);

template &lt;class ExecutionPolicy, class ForwardIt, class RandomIt, class Compare&gt;

RandomIt partial_sort_copy(ExecutionPolicy &amp;&amp;policy, ForwardIt first, ForwardIt last, (4)(since C++ 17)

                                                                                          RandomIt d_first,
                           RandomIt d_last,

                           Compare comp);
Sorts some of the elements in the range [first, last) in ascending order, storing the result in the range [d_first, d_last).

At most d_last - d_first of the elements are placed sorted to the range [d_first, d_first + n). n is the number of elements to sort (n = min(last - first, d_last - d_first)). The order of equal elements is not guaranteed to be preserved.

1) Elements are compared using operator&lt;.

3) Elements are compared using the given binary comparison function comp.

2,4) Same as (1,3), but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true
</code></pre>

<h2>Parameters</h2>

first, last - the range of elements to sort 
d_first, d_last - random access iterators defining the destination range 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;comparison function object (i.e. an object that satisfies the requirements of Compare) which returns true if the first argument is less than (i.e. is ordered before) the second. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the comparison function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool cmp(const Type1 &amp;a, const Type2 &amp;b); 
comp - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type RandomIt can be dereferenced and then implicitly converted to both of them.

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
ForwardIt must meet the requirements of LegacyForwardIterator. 
- 
RandomIt must meet the requirements of ValueSwappable and LegacyRandomAccessIterator. 
- 
The type of dereferenced RandomIt must meet the requirements of MoveAssignable and MoveConstructible.

<h2>Return value</h2>

an iterator to the element defining the upper boundary of the sorted range, i.e. d_first + min(last - first, d_last - d_first). 

<h2>Complexity</h2>

O(N·log(min(D,N)), where N = std::distance(first, last), D = std::distance(d_first, d_last) applications of cmp.

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Example</h2>

The following code sorts a vector of integers and copies them into a smaller and a larger vector. 
 // Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;vector&gt;

#include &lt;functional&gt;

#include &lt;iostream&gt;
int main()

{
    std::vector&lt;int&gt; v0{4, 2, 5, 1, 3};
    std::vector&lt;int&gt; v1{10, 11, 12};
    std::vector&lt;int&gt; v2{10, 11, 12, 13, 14, 15, 16};
    std::vector&lt;int&gt;::iterator it;
    it = std::partial_sort_copy(v0.begin(), v0.end(), v1.begin(), v1.end());
    std::cout &lt;&lt; &quot;Writing to the smaller vector in ascending order gives: &quot;;
    for (int a : v1) {
        std::cout &lt;&lt; a &lt;&lt; &quot; &quot;;
    }
    std::cout &lt;&lt; '\n';
    if (it == v1.end())
        std::cout &lt;&lt; &quot;The return value is the end iterator\n&quot;;
    it = std::partial_sort_copy(v0.begin(), v0.end(), v2.begin(), v2.end(),
                                std::greater&lt;int&gt;());
    std::cout &lt;&lt; &quot;Writing to the larger vector in descending order gives: &quot;;
    for (int a : v2) {
        std::cout &lt;&lt; a &lt;&lt; &quot; &quot;;
    }
    std::cout &lt;&lt; '\n'
              &lt;&lt; &quot;The return value is the iterator to &quot; &lt;&lt; *it &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Writing to the smaller vector in ascending order gives: 1 2 3 
&nbsp;<wbr>&nbsp;The return value is the end iterator 
&nbsp;<wbr>&nbsp;Writing to the larger vector in descending order gives: 5 4 3 2 1 15 16 
&nbsp;<wbr>&nbsp;The return value is the iterator to 15

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sorts the first N elements of a range 
partial_sort <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sorts a range into ascending order 
sort <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sorts a range of elements while preserving order between equal elements 
stable_sort <i>(function template)</i> 
