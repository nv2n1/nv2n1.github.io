---
title: "stdcopystdcopy_if(3)"
name: "stdcopystdcopy_if"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcopystdcopy_if/"
---

std::copy,std::copy_if - std::copy,std::copy_if

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class InputIt, class OutputIt &gt;                                                                   (until C++20)

OutputIt copy( InputIt first, InputIt last, OutputIt d_first );

template&lt; class InputIt, class OutputIt &gt;                                                                   (since C++20)

constexpr OutputIt copy( InputIt first, InputIt last, OutputIt d_first );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2 &gt;                                   (2) (since C++17)

ForwardIt2 copy( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first, ForwardIt1 last, ForwardIt2 d_first );

template&lt; class InputIt, class OutputIt, class UnaryPredicate &gt;

OutputIt copy_if( InputIt first, InputIt last,                                                                            (since C++11)

OutputIt d_first,                                                                                   (1)                   (until C++20)

UnaryPredicate pred );

template&lt; class InputIt, class OutputIt, class UnaryPredicate &gt;

constexpr OutputIt copy_if( InputIt first, InputIt last,                                                (3)               (since C++20)

OutputIt d_first,

UnaryPredicate pred );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2, class UnaryPredicate &gt;

ForwardIt2 copy_if( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first, ForwardIt1 last,                            (4)           (since C++17)

ForwardIt2 d_first,

UnaryPredicate pred );</code></pre> 
Copies the elements in the range, defined by [first, last), to another range beginning at d_first. 
1) Copies all elements in the range [first, last) starting from first and proceeding to last - 1. The behavior is undefined if d_first is within the range [first, last). In this case, std::copy_backward may be used instead. 
3) Only copies the elements for which the predicate pred returns true. The relative order of the elements that are copied is preserved. The behavior is undefined if the source and the destination ranges overlap. 
2,4) Same as (1,3), but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first, last - the range of elements to copy 
d_first - the beginning of the destination range. 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unary predicate which returns true for the required elements. 
pred - The expression pred(v) must be convertible to bool for every argument v of type (possibly const) VT, where VT is the value type of InputIt, regardless of value_category, and must not modify v. Thus, a parameter type of VT&amp;is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is VT unless for VT a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>.

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
OutputIt must meet the requirements of LegacyOutputIterator. 
- 
ForwardIt1, ForwardIt2 must meet the requirements of LegacyForwardIterator. 
- 
UnaryPredicate must meet the requirements of Predicate.

<h2>Return value</h2>

Output iterator to the element in the destination range, one past the last element copied. 

<h2>Complexity</h2>

* 1-2) Exactly (last - first) assignments 

 

 
* 3-4) Exactly (last - first) applications of the predicate, between 0 and (last - first) assignments (assignment for every element for which predicate is equal to true, dependent on predicate and input data) 

 
For the overloads with an ExecutionPolicy, there may be a performance cost if ForwardIt1's value_type is not MoveConstructible.

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Notes</h2>

In practice, implementations of std::copy avoid multiple assignments and use bulk copy functions such as std::memmove if the value type is TriviallyCopyable 
When copying overlapping ranges, std::copy is appropriate when copying to the left (beginning of the destination range is outside the source range) while std::copy_backward is appropriate when copying to the right (end of the destination range is outside the source range). 

<h2>Possible implementation</h2>

<h2>First version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt, class OutputIt&gt; 
&nbsp;<wbr>&nbsp;OutputIt copy(InputIt first, InputIt last, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;OutputIt d_first) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first != last) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*d_first++ = *first++; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return d_first; 
&nbsp;<wbr>&nbsp;}

<h2>Second version</h2>

&nbsp;<wbr>&nbsp;template&lt;class InputIt, class OutputIt, class UnaryPredicate&gt; 
&nbsp;<wbr>&nbsp;OutputIt copy_if(InputIt first, InputIt last, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;OutputIt d_first, UnaryPredicate pred) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while (first != last) { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if (pred(*first)) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*d_first++ = *first; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;first++; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return d_first; 
&nbsp;<wbr>&nbsp;}

<h2>Example</h2>

The following code uses copy to both copy the contents of one vector to another and to display the resulting vector: 
 // Run this code <pre><code>#include &lt;algorithm&gt;

#include &lt;iostream&gt;

#include &lt;vector&gt;

#include &lt;iterator&gt;

#include &lt;numeric&gt;
int main()

{
    std::vector&lt;int&gt; from_vector(10);
    std::iota(from_vector.begin(), from_vector.end(), 0);
    std::vector&lt;int&gt; to_vector;
    std::copy(from_vector.begin(), from_vector.end(),
              std::back_inserter(to_vector));

    // or, alternatively,

    //  std::vector&lt;int&gt; to_vector(from_vector.size());

    //  std::copy(from_vector.begin(), from_vector.end(), to_vector.begin());

    // either way is equivalent to

    //  std::vector&lt;int&gt; to_vector = from_vector;
    std::cout &lt;&lt; &quot;to_vector contains: &quot;;
    std::copy(to_vector.begin(), to_vector.end(),
              std::ostream_iterator&lt;int&gt;(std::cout, &quot; &quot;));
    std::cout &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;to_vector contains: 0 1 2 3 4 5 6 7 8 9

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a range of elements in backwards order 
copy_backward <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a copy of a range that is reversed 
reverse_copy <i>(function template)</i> 
copy_n copies a number of elements to a new location 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copy-assigns the given value to every element in a range 
fill <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;copies a range of elements omitting those that satisfy specific criteria 
remove_copy <i>(function template)</i> 
remove_copy_if 
