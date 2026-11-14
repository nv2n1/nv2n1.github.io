---
title: "stdcountstdcount_if(3)"
name: "stdcountstdcount_if"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcountstdcount_if/"
---

std::count,std::count_if - std::count,std::count_if

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class InputIt, class T&gt;

    typename iterator_traits&lt;InputIt&gt;::difference_type(until C++ 20)

        count(InputIt first, InputIt last, const T &amp;value);

template &lt;class InputIt, class T&gt;

constexpr typename iterator_traits&lt;InputIt&gt;::difference_type(since C++ 20)

    count(InputIt first, InputIt last, const T &amp;value);

template &lt;class ExecutionPolicy, class ForwardIt, class T&gt;

typename iterator_traits&lt;ForwardIt&gt;::difference_type(2)(since C++ 17)

    count(ExecutionPolicy &amp;&amp;policy, ForwardIt first, ForwardIt last, const T &amp;value);
(1)

    template &lt;class InputIt, class UnaryPredicate&gt;

    typename iterator_traits&lt;InputIt&gt;::difference_type(until C++ 20)

        count_if(InputIt first, InputIt last, UnaryPredicate p);

template &lt;class InputIt, class UnaryPredicate&gt;

constexpr typename iterator_traits&lt;InputIt&gt;::difference_type(3)(since C++ 20)

    count_if(InputIt first, InputIt last, UnaryPredicate p);

template &lt;class ExecutionPolicy, class ForwardIt, class UnaryPredicate&gt;

typename iterator_traits&lt;ForwardIt&gt;::difference_type(4)(since C++ 17)

    count_if(ExecutionPolicy &amp;&amp;policy, ForwardIt first, ForwardIt last, UnaryPredicate p);</code></pre> 
Returns the number of elements in the range [first, last) satisfying specific criteria. 
1) counts the elements that are equal to value. 
3) counts elements for which predicate p returns true. 
2,4) Same as (1,3), but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first, last - the range of elements to examine 
value - the value to search for 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unary predicate which returns true for the required elements. 
p - The expression p(v) must be convertible to bool for every argument v of type (possibly const) VT, where VT is the value type of InputIt, regardless of value_category, and must not modify v. Thus, a parameter type of VT&amp;is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is VT unless for VT a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>.

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
ForwardIt must meet the requirements of LegacyForwardIterator.

<h2>Return value</h2>

number of elements satisfying the condition. 

<h2>Complexity</h2>

exactly last - first comparisons / applications of the predicate

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Notes</h2>

For the number of elements in the range [first, last) without any additional criteria, see std::distance. 

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt, class T&gt; 
&nbsp;<wbr>&nbsp;typename iterator_traits&lt;InputIt&gt;::difference_type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;count(InputIt first, InputIt last, const T&amp; value) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename iterator_traits&lt;InputIt&gt;::difference_type ret = 0; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (*first == value) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret++; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ret; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt, class UnaryPredicate&gt; 
&nbsp;<wbr>&nbsp;typename iterator_traits&lt;InputIt&gt;::difference_type 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;count_if(InputIt first, InputIt last, UnaryPredicate p) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;typename iterator_traits&lt;InputIt&gt;::difference_type ret = 0; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (p(*first)) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret++; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return ret; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

// Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;vector&gt;
int main()

{
    std::vector&lt;int&gt; v{1, 2, 3, 4, 4, 3, 7, 8, 9, 10};
    // determine how many integers in a std::vector match a target value.
    int target1 = 3;
    int target2 = 5;
    int num_items1 = std::count(v.begin(), v.end(), target1);
    int num_items2 = std::count(v.begin(), v.end(), target2);
    std::cout &lt;&lt; &quot;number: &quot; &lt;&lt; target1 &lt;&lt; &quot; count: &quot; &lt;&lt; num_items1 &lt;&lt; '\n';
    std::cout &lt;&lt; &quot;number: &quot; &lt;&lt; target2 &lt;&lt; &quot; count: &quot; &lt;&lt; num_items2 &lt;&lt; '\n';
    // use a lambda expression to count elements divisible by 3.
    int num_items3 = std::count_if(v.begin(), v.end(), [](int i) { return i % 3 == 0; });
    std::cout &lt;&lt; &quot;number divisible by three: &quot; &lt;&lt; num_items3 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;number: 3 count: 2 
&nbsp;<wbr>&nbsp;number: 5 count: 0 
&nbsp;<wbr>&nbsp;number divisible by three: 3

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the distance between two iterators 
distance <i>(function template)</i> 
