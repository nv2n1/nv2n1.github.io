---
title: "stdsort(3)"
name: "stdsort"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsort/"
---

std::sort - std::sort

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class RandomIt&gt;
    (until C++ 20)

        void sort(RandomIt first, RandomIt last);

template &lt;class RandomIt&gt;
(since C++ 20)

    constexpr void sort(RandomIt first, RandomIt last);

template &lt;class ExecutionPolicy, class RandomIt&gt;
(2)(since C++ 17)

    void sort(ExecutionPolicy &amp;&amp;policy, RandomIt first, RandomIt last);
(1)

    template &lt;class RandomIt, class Compare&gt;
    (until C++ 20)

        void sort(RandomIt first, RandomIt last, Compare comp);

template &lt;class RandomIt, class Compare&gt;
(3)(since C++ 20)

    constexpr void sort(RandomIt first, RandomIt last, Compare comp);

template &lt;class ExecutionPolicy, class RandomIt, class Compare&gt;
(4)(since C++ 17)

    void sort(ExecutionPolicy &amp;&amp;policy, RandomIt first, RandomIt last, Compare comp);</code></pre> 
Sorts the elements in the range [first, last) in ascending order. The order of equal elements is not guaranteed to be preserved. 
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
- 
Compare must meet the requirements of Compare.

<h2>Return value</h2>

<i>(none)</i> 

<h2>Complexity</h2>

O(N·log(N)), where N = std::distance(first, last) comparisons on average.<i>(until C++11)</i> 
O(N·log(N)), where N = std::distance(first, last) comparisons. <i>(since C++11)</i>

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
    std::array&lt;int, 10&gt; s = {5, 7, 4, 2, 8, 6, 1, 9, 0, 3};
    // sort using the default operator&lt;
    std::sort(s.begin(), s.end());
    for (auto a : s) {
        std::cout &lt;&lt; a &lt;&lt; &quot; &quot;;
    }
    std::cout &lt;&lt; '\n';
    // sort using a standard library compare function object
    std::sort(s.begin(), s.end(), std::greater&lt;int&gt;());
    for (auto a : s) {
        std::cout &lt;&lt; a &lt;&lt; &quot; &quot;;
    }
    std::cout &lt;&lt; '\n';
    // sort using a custom function object
    struct {
        bool operator()(int a, int b) const
        {
            return a &lt; b;
        }
    } customLess;
    std::sort(s.begin(), s.end(), customLess);
    for (auto a : s) {
        std::cout &lt;&lt; a &lt;&lt; &quot; &quot;;
    }
    std::cout &lt;&lt; '\n';
    // sort using a lambda expression
    std::sort(s.begin(), s.end(), [](int a, int b) {
        return a &gt; b;
    });
    for (auto a : s) {
        std::cout &lt;&lt; a &lt;&lt; &quot; &quot;;
    }
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;0 1 2 3 4 5 6 7 8 9 
&nbsp;<wbr>&nbsp;9 8 7 6 5 4 3 2 1 0 
&nbsp;<wbr>&nbsp;0 1 2 3 4 5 6 7 8 9 
&nbsp;<wbr>&nbsp;9 8 7 6 5 4 3 2 1 0

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sorts the first N elements of a range 
partial_sort <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sorts a range of elements while preserving order between equal elements 
stable_sort <i>(function template)</i> 
