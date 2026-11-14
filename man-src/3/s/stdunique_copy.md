---
title: "stdunique_copy(3)"
name: "stdunique_copy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunique_copy/"
---

std::unique_copy - std::unique_copy

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;algorithm&gt;

template&lt; class InputIt, class OutputIt &gt;

OutputIt unique_copy( InputIt first, InputIt last,                                                   (until C++20)

OutputIt d_first );

template&lt; class InputIt, class OutputIt &gt;

constexpr OutputIt unique_copy( InputIt first, InputIt last,                                         (since C++20)

OutputIt d_first );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2 &gt;

ForwardIt2 unique_copy( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first, ForwardIt1 last,             (2) (since C++17)

ForwardIt2 d_first );                                                                        (1)

template&lt; class InputIt, class OutputIt, class BinaryPredicate &gt;

OutputIt unique_copy( InputIt first, InputIt last,                                                                 (until C++20)

OutputIt d_first, BinaryPredicate p );

template&lt; class InputIt, class OutputIt, class BinaryPredicate &gt;

constexpr OutputIt unique_copy( InputIt first, InputIt last,                                     (3)               (since C++20)

OutputIt d_first, BinaryPredicate p );

template&lt; class ExecutionPolicy, class ForwardIt1, class ForwardIt2, class BinaryPredicate &gt;

ForwardIt2 unique_copy( ExecutionPolicy&amp;&amp; policy, ForwardIt1 first, ForwardIt1 last,                 (4)           (since C++17)

ForwardIt2 d_first, BinaryPredicate p );</code></pre> 
Copies the elements from the range [first, last), to another range beginning at d_first in such a way that there are no consecutive equal elements. Only the first element of each group of equal elements is copied. 
1) Elements are compared using operator==. The behavior is undefined if it is not an equivalence_relation. 
3) Elements are compared using the given binary predicate p. The behavior is undefined if it is not an equivalence relation. 
2,4) Same as (1,3), but executed according to policy. This overload only participates in overload resolution if std::is_execution_policy_v&lt;std::decay_t&lt;ExecutionPolicy&gt;&gt; is true 

<h2>Parameters</h2>

first, last - the range of elements to process 
d_first - the beginning of the destination range 
policy - the execution policy to use. See execution_policy for details. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;binary predicate which returns true if the elements should be treated as equal. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The signature of the predicate function should be equivalent to the following: 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool pred(const Type1 &amp;a, const Type2 &amp;b); 
p - While the signature does not need to have const &amp;, the function must not modify the objects passed to it and must be able to accept all values of type (possibly const) Type1 and Type2 regardless of value_category (thus, Type1 &amp; is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is Type1 unless for Type1 a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>). 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The types Type1 and Type2 must be such that an object of type InputIt can be dereferenced and then implicitly converted to both of them.

<h2>Type requirements</h2>

- 
InputIt must meet the requirements of LegacyInputIterator. 
- 
OutputIt must meet the requirements of LegacyOutputIterator. 
- 
ForwardIt1, ForwardIt2 must meet the requirements of LegacyForwardIterator. 
- 
The type of dereferenced InputIt must meet the requirements of CopyAssignable. if InputIt does not satisfy LegacyForwardIterator 
- 
The type of dereferenced InputIt must meet the requirements of CopyConstructible. if neither InputIt nor OutputIt satisfies LegacyForwardIterator, or if InputIt does not satisfy LegacyForwardIterator and the value type of InputIt differs from that of OutputIt

<h2>Return value</h2>

Output iterator to the element past the last written element 

<h2>Complexity</h2>

For nonempty ranges, exactly std::distance(first, last) - 1 applications of the corresponding predicate.

<h2>Exceptions</h2>

The overloads with a template parameter named ExecutionPolicy report errors as follows: 

 
* If execution of a function invoked as part of the algorithm throws an exception and ExecutionPolicy is one of the standard_policies, std::terminate is called. For any other ExecutionPolicy, the behavior is implementation-defined. 
* If the algorithm fails to allocate memory, std::bad_alloc is thrown.

<h2>Notes</h2>

If InputIt satisfies LegacyForwardIterator, this function rereads the input in order to detect duplicates. 
Otherwise, if OutputIt satisfies LegacyForwardIterator, and the value type of InputIt is the same as that of OutputIt, this function compare *d_first to *first. 
Otherwise, this function compares *first to a local element copy. 
For the overloads with an ExecutionPolicy, there may be a performance cost if the value type of ForwardIterator1 is not both CopyConstructible and CopyAssignable 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;string&gt;

#include &lt;iostream&gt;

#include &lt;algorithm&gt;

#include &lt;iterator&gt;
int main()

{
    std::string s1 = &quot;The      string    with many       spaces!&quot;;
    std::cout &lt;&lt; &quot;before: &quot; &lt;&lt; s1 &lt;&lt; '\n';
    std::string s2;
    std::unique_copy(s1.begin(), s1.end(), std::back_inserter(s2),
                     [](char c1, char c2) { return c1 == ' ' &amp;&amp; c2 == ' '; });
    std::cout &lt;&lt; &quot;after:  &quot; &lt;&lt; s2 &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;before: The string with many spaces! 
&nbsp;<wbr>&nbsp;after: The string with many spaces!

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first two adjacent items that are equal (or satisfy a given predicate) 
adjacent_find <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes consecutive duplicate elements in a range 
unique <i>(function template)</i> 
