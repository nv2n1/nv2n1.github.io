---
title: "stdfind(3)"
name: "stdfind"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfind/"
---

std::find,std::find_if,std::find_if_not - std::find,std::find_if,std::find_if_not

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;algorithm&gt;

    template &lt;class InputIt, class T&gt;
    (until C++ 20)

        InputIt find(InputIt first, InputIt last, const T &amp;value);

template &lt;class InputIt, class T&gt;
(since C++ 20)

    constexpr InputIt find(InputIt first, InputIt last, const T &amp;value);

template &lt;class ExecutionPolicy, class ForwardIt, class T&gt;
(2)(since C++ 17)

    ForwardIt find(ExecutionPolicy &amp;&amp;policy, ForwardIt first, ForwardIt last, const T &amp;value);

template &lt;class InputIt, class UnaryPredicate&gt;

InputIt find_if(InputIt first, InputIt last, (until C++ 20)

                                                 UnaryPredicate p);

template &lt;class InputIt, class UnaryPredicate&gt;

constexpr InputIt find_if(InputIt first, InputIt last, (since C++ 20)

                                                           UnaryPredicate p);
(1)

    template &lt;class ExecutionPolicy, class ForwardIt, class UnaryPredicate&gt;

    ForwardIt find_if(ExecutionPolicy &amp;&amp;policy, ForwardIt first, ForwardIt last, (4)(since C++ 17)

                                                                                     UnaryPredicate p);
(3)

    template &lt;class InputIt, class UnaryPredicate&gt;
    (since C++ 11)

        InputIt find_if_not(InputIt first, InputIt last, (until C++ 20)

                                                             UnaryPredicate q);

template &lt;class InputIt, class UnaryPredicate&gt;

constexpr InputIt find_if_not(InputIt first, InputIt last, (5)(since C++ 20)

                                                               UnaryPredicate q);

template &lt;class ExecutionPolicy, class ForwardIt, class UnaryPredicate&gt;

ForwardIt find_if_not(ExecutionPolicy &amp;&amp;policy, ForwardIt first, ForwardIt last, (6)(since C++ 17)

                                                                                     UnaryPredicate q);</code></pre> 
Returns the first element in the range [first, last) that satisfies specific criteria: 
1) find searches for an element equal to value 
3) find_if searches for an element for which predicate p returns true 
5) find_if_not searches for an element for which predicate q returns false 
2,4,6) Same as (1,3,5), but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first, last - the range of elements to examine 
value - value to compare the elements to 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unary predicate which returns true for the required element. 
p - The expression p(v) must be convertible to bool for every argument v of type (possibly const) VT, where VT is the value type of InputIt, regardless of value_category, and must not modify v. Thus, a parameter type of VT&amp;is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is VT unless for VT a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unary predicate which returns false for the required element. 
q - The expression q(v) must be convertible to bool for every argument v of type (possibly const) VT, where VT is the value type of InputIt, regardless of value_category, and must not modify v. Thus, a parameter type of VT&amp;is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is VT unless for VT a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>.

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
ForwardIt must meet the requirements of LegacyForwardIterator. 
- 
UnaryPredicate must meet the requirements of Predicate.

<h2>Return value</h2>

Iterator to the first element satisfying the condition or last if no such element is found. 

<h2>Complexity</h2>

At most last - first applications of the predicate

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt, class T&gt; 
&nbsp;<wbr>&nbsp;constexpr InputIt find(InputIt first, InputIt last, const T&amp; value) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (*first == value) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return last; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt, class UnaryPredicate&gt; 
&nbsp;<wbr>&nbsp;constexpr InputIt find_if(InputIt first, InputIt last, UnaryPredicate p) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (p(*first)) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return last; 
&nbsp;<wbr>&nbsp;} 

 
Third version 

 
&nbsp;<wbr>&nbsp;template&lt;class InputIt, class UnaryPredicate&gt; 
&nbsp;<wbr>&nbsp;constexpr InputIt find_if_not(InputIt first, InputIt last, UnaryPredicate q) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (; first != last; ++first) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (!q(*first)) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return last; 
&nbsp;<wbr>&nbsp;}

<h2>Notes</h2>

If you do not have C++11, an equivalent to std::find_if_not is to use std::find_if with the negated predicate. template &lt;class InputIt, class UnaryPredicate&gt;

InputIt find_if_not(InputIt first, InputIt last, UnaryPredicate q)

{
    return std::find_if(first, last, std::not1(q));
}


<h2>Example</h2>

The following example finds an integer in a vector of integers. 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;algorithm&gt;

#include &lt;vector&gt;

#include &lt;iterator&gt;
int main()

{
    int n1 = 3;
    int n2 = 5;
    std::vector&lt;int&gt; v{0, 1, 2, 3, 4};
    auto result1 = std::find(std::begin(v), std::end(v), n1);
    auto result2 = std::find(std::begin(v), std::end(v), n2);
    if (result1 != std::end(v)) {
        std::cout &lt;&lt; &quot;v contains: &quot; &lt;&lt; n1 &lt;&lt; '\n';
    } else {
        std::cout &lt;&lt; &quot;v does not contain: &quot; &lt;&lt; n1 &lt;&lt; '\n';
    }
    if (result2 != std::end(v)) {
        std::cout &lt;&lt; &quot;v contains: &quot; &lt;&lt; n2 &lt;&lt; '\n';
    } else {
        std::cout &lt;&lt; &quot;v does not contain: &quot; &lt;&lt; n2 &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;v contains: 3 
&nbsp;<wbr>&nbsp;v does not contain: 5

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first two adjacent items that are equal (or satisfy a given predicate) 
adjacent_find <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the last sequence of elements in a certain range 
find_end <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;searches for any one of a set of elements 
find_first_of <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first position where two ranges differ 
mismatch <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;searches for a range of elements 
search <i>(function template)</i> 
